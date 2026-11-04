#!/usr/bin/env python3
"""The eval harness: run a stage's hidden test set and write a run directory with pass counts per exercise.

    python scripts/eval.py 01                   # hidden tests against stages/01-*/exercises/
    python scripts/eval.py 01 --solutions       # ... against stages/01-*/solutions/ (maintainers, CI)
    python scripts/eval.py --solutions --all    # every stage that has an eval/ directory; exit 1 on any failure

Writes stages/NN-*/eval/runs/<timestamp>-<sha>/summary.json (committed) and junit.xml (gitignored), and prints a
table: exercise, passed/total, failing case IDs. The gate threshold for the stage is read from
stages/NN-*/eval/threshold.json ({"pass": N, "total": M}) and the verdict is printed and recorded.

Case IDs are the pytest parametrize ids, e.g. s01-r4e3-b: stage 1, rung 4, exercise 3, case b. They are stable.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASE_RE = re.compile(r"\[(s\d\d-r\w+?e\d+-\w+)\]")


def stage_dir(n: str) -> Path:
    hits = sorted((ROOT / "stages").glob(f"{n}-*/"))
    if not hits:
        sys.exit(f"no stage {n}")
    return hits[0]


def git_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip() or "nogit"
    except OSError:
        return "nogit"


def ensure_fixture() -> None:
    d = ROOT / os.environ.get("LIBRARY_DATA_DIR", "data/library")
    if not (d / "reference.json").exists():
        subprocess.run([sys.executable, str(ROOT / "data" / "build_files.py"), "--out", str(d)], check=True)


def run_stage(n: str, solutions: bool) -> dict:
    sd = stage_dir(n)
    eval_dir = sd / "eval"
    if not eval_dir.exists():
        return {"stage": f"s{n}", "skipped": True}
    if int(n) >= 3:
        ensure_fixture()
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    run_dir = eval_dir / "runs" / f"{ts}-{git_sha()}"
    run_dir.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "COURSE_TARGET": "solutions" if solutions else "exercises"}
    junit = run_dir / "junit.xml"
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", str(eval_dir), "-q", "--tb=no", "-p", "no:cacheprovider",
         "--import-mode=importlib", f"--junitxml={junit}", "-o", "junit_family=xunit2"],
        cwd=ROOT, env=env, capture_output=True, text=True,
    )
    if not junit.exists():
        print(proc.stdout, proc.stderr)
        sys.exit(f"pytest did not produce {junit}")
    per: dict[str, dict] = defaultdict(lambda: {"pass": 0, "total": 0, "failed": []})
    n_pass = n_total = 0
    for tc in ET.parse(junit).getroot().iter("testcase"):
        m = CASE_RE.search(tc.get("name", ""))
        cid = m.group(1) if m else tc.get("name", "?")
        ex = cid.split("-")[1] if m else "other"
        failed = any(child.tag in ("failure", "error") for child in tc)
        per[ex]["total"] += 1
        n_total += 1
        if failed:
            per[ex]["failed"].append(cid)
        else:
            per[ex]["pass"] += 1
            n_pass += 1
    threshold_file = eval_dir / "threshold.json"
    threshold = json.loads(threshold_file.read_text()) if threshold_file.exists() else {"pass": n_total, "total": n_total}
    verdict = "pass" if n_pass >= threshold["pass"] else "not yet"
    summary = {
        "stage": f"s{n}", "target": env["COURSE_TARGET"], "timestamp": ts, "git_sha": git_sha(),
        "python": sys.version.split()[0], "n_total": n_total, "n_pass": n_pass,
        "threshold": threshold, "verdict": verdict,
        "per_exercise": dict(sorted(per.items())),
    }
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"\n== Stage {int(n)} · {env['COURSE_TARGET']} · {n_pass}/{n_total} hidden tests pass "
          f"(gate: ≥ {threshold['pass']} of {threshold['total']}) → {verdict.upper()}")
    print(f"   run directory: {run_dir.relative_to(ROOT)}")
    print(f"   {'exercise':<10} {'passed':>8}  failing case IDs")
    for ex, r in sorted(per.items()):
        print(f"   {ex:<10} {r['pass']:>3}/{r['total']:<4}  {', '.join(r['failed'])}")
    return summary


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", nargs="?", help="two-digit stage number, e.g. 01")
    ap.add_argument("--solutions", action="store_true", help="grade the reference solutions instead of exercises/")
    ap.add_argument("--all", action="store_true", help="every stage with an eval/ directory")
    a = ap.parse_args()
    if a.all:
        stages = sorted(p.name[:2] for p in (ROOT / "stages").iterdir() if (p / "eval").is_dir())
    elif a.stage:
        stages = [a.stage.zfill(2)]
    else:
        ap.error("give a stage number or --all")
    results = [run_stage(s, a.solutions) for s in stages]
    bad = [r for r in results if not r.get("skipped") and r["n_pass"] != r["n_total"]] if a.solutions else []
    if bad:
        sys.exit(f"\n{len(bad)} stage(s) where the reference solutions do not pass every hidden test")


if __name__ == "__main__":
    main()
