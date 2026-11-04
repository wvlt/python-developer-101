#!/usr/bin/env python3
"""Compile the course state into BOARD.md, the README outline block and site/data.json.

Sources (never duplicated by hand):
  status/board.json       stage-level state (locked / in_progress / ...), build state, Now/Next, tiers
  stages/NN-*/README.md   parts and rungs, parsed from `## Part X — …` and `### Rung N — …` headings
  PROGRESS.md             the learner's rung log; a rung is done when Run, See and Say are all ticked

    python scripts/render_board.py           # write BOARD.md, README block, site/data.json
    python scripts/render_board.py --check   # exit 1 if any output is stale (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "status" / "board.json"
PROGRESS = ROOT / "PROGRESS.md"
OUT_BOARD = ROOT / "BOARD.md"
OUT_DATA = ROOT / "site" / "data.json"
README = ROOT / "README.md"
START, END = "<!-- board:start -->", "<!-- board:end -->"

RUNG_RE = re.compile(r"^#{2,3} Rung (\w+) — (.+?)\s*$", re.M)
PART_RE = re.compile(r"^#{2,3} Part ([A-Z]) — (.+?)\s*$", re.M)
MIN_RE = re.compile(r"\*~(\d+) min")
TICKED = {"☑", "✓", "✔", "x", "X", "[x]", "[X]", "yes", "✅"}

LEARNER_LABEL = {"locked": "Locked", "ready": "Ready", "in_progress": "In progress",
                 "feedback": "Feedback filed", "revising": "Revising", "passed": "Passed"}
LEARNER_ICON = {"locked": "🔒", "ready": "🟢", "in_progress": "▶", "feedback": "📝", "revising": "🛠", "passed": "✅"}
BUILD_LABEL = {"outline": "outline", "rung_numbered": "rung-numbered", "verified": "verified", "ready": "ready"}


def gh_slug(text: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s", "-", s.strip())


def bar(frac: float, width: int = 10) -> str:
    n = round(frac * width)
    return "▰" * n + "▱" * (width - n)


def stage_dir(stage_id: str) -> Path | None:
    n = stage_id[1:]
    hits = sorted((ROOT / "stages").glob(f"{n}-*/README.md"))
    return hits[0] if hits else None


def parse_brief(path: Path, stage_id: str) -> dict:
    text = path.read_text()
    parts: list[dict] = []
    # Walk headings in order to attach rungs to parts.
    events = []
    for m in PART_RE.finditer(text):
        events.append((m.start(), "part", m.group(1), m.group(2)))
    for m in RUNG_RE.finditer(text):
        events.append((m.start(), "rung", m.group(1), m.group(2), m.end()))
    events.sort()
    cur: dict | None = None
    for ev in events:
        if ev[1] == "part":
            cur = {"id": ev[2], "title": ev[3], "rungs": []}
            parts.append(cur)
        else:
            if cur is None:
                cur = {"id": "", "title": "Build", "rungs": []}
                parts.append(cur)
            tail = text[ev[4]: ev[4] + 400]
            mm = MIN_RE.search(tail)
            section_end = min([e[0] for e in events if e[0] > ev[0]] + [len(text)])
            section = text[ev[0]:section_end]
            cur["rungs"].append({
                "id": f"{stage_id}-r{ev[2]}",
                "n": ev[2],
                "title": ev[3],
                "minutes": int(mm.group(1)) if mm else None,
                "has_check": "**Check**" in section,
                "anchor": gh_slug(f"Rung {ev[2]} — {ev[3]}"),
            })
    return {"path": str(path.relative_to(ROOT)), "parts": parts}


def parse_progress() -> dict[str, dict]:
    """rung id -> {run, see, say, minutes, started, note}"""
    if not PROGRESS.exists():
        return {}
    out = {}
    for line in PROGRESS.read_text().splitlines():
        if not line.startswith("| s"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        rid = cells[0]
        if not re.fullmatch(r"s\d\d-r\w+", rid):
            continue
        run, see, say = (c in TICKED for c in cells[3:6])
        out[rid] = {"run": run, "see": see, "say": say, "done": run and see and say,
                    "started": cells[1], "minutes": cells[2], "note": cells[7] if len(cells) > 7 else ""}
    return out


def compile_state(b: dict) -> dict:
    prog = parse_progress()
    stages = []
    current = None
    for s in b["stages"]:
        d = stage_dir(s["id"])
        brief = parse_brief(d, s["id"]) if d else {"path": None, "parts": []}
        rungs = [r for p in brief["parts"] for r in p["rungs"]]
        for r in rungs:
            pr = prog.get(r["id"], {})
            r["done"] = bool(pr.get("done"))
            r["run"], r["see"], r["say"] = bool(pr.get("run")), bool(pr.get("see")), bool(pr.get("say"))
            r["minutes_spent"] = pr.get("minutes", "")
            r["current"] = False
        done = sum(1 for r in rungs if r["done"])
        total = len(rungs)
        frac = (1.0 if s["learner"] == "passed" else (done / total if total else 0.0))
        st = {**s, "brief": brief["path"], "parts": brief["parts"], "rungs_total": total, "rungs_done": done,
              "fraction": frac, "learner_label": LEARNER_LABEL[s["learner"]], "build_label": BUILD_LABEL[s["build"]],
              "tier_name": b["tiers"].get(s["tier"], "")}
        if s["learner"] == "in_progress" and current is None:
            nxt = next((r for r in rungs if not r["done"]), None)
            if nxt:
                nxt["current"] = True
                current = {"stage": s["id"], "stage_name": s["name"], "rung": nxt}
            else:
                current = {"stage": s["id"], "stage_name": s["name"], "rung": None}
        stages.append(st)
    hours_total = sum(s["hours"] for s in stages)
    hours_done = sum(s["hours"] for s in stages if s["learner"] == "passed")
    return {
        "updated": b["updated"], "curriculum_version": b["curriculum_version"], "learner": b["learner"],
        "course": b.get("course", {}),
        "now": b["now"], "tiers": b["tiers"], "stages": stages, "current": current,
        "hours_total": hours_total, "hours_done": hours_done,
        "stages_passed": sum(1 for s in stages if s["learner"] == "passed"),
        "maintainer_queue": b["maintainer_queue"], "activity": b["activity"],
        "progress_file": PROGRESS.exists(),
    }


# ---------- Markdown outputs ----------

def continue_line(st: dict) -> str:
    c = st["current"]
    if not c:
        return "_No stage in progress._"
    if c["rung"] is None:
        return f"**Stage {int(c['stage'][1:])} — {c['stage_name']}**: all rungs done. File `STAGE_FEEDBACK.md`."
    r = c["rung"]
    mins = f" · ~{r['minutes']} min" if r["minutes"] else ""
    stage = next(s for s in st["stages"] if s["id"] == c["stage"])
    return (f"**Stage {int(c['stage'][1:])} · Rung {r['n']} — {r['title']}**{mins}  \n"
            f"[Open the rung]({stage['brief']}#{r['anchor']}) · "
            f"{stage['rungs_done']} of {stage['rungs_total']} rungs done in this stage")


def outline_table(st: dict, compact: bool) -> str:
    lines = []
    if compact:
        lines += ["| | Stage | Tier | Progress |", "|---|---|---|---|"]
    for tier, tname in st["tiers"].items():
        if not compact:
            lines += [f"**Tier {tier} — {tname}**", "", "| | Stage | Progress | Rungs | Time |", "|---|---|---|---|---|"]
        for s in st["stages"]:
            if s["tier"] != tier:
                continue
            here = " ← you are here" if s["learner"] == "in_progress" else ""
            name = f"[{int(s['id'][1:])} · {s['name']}]({s['brief']})" if s["brief"] else f"{int(s['id'][1:])} · {s['name']}"
            if s["learner"] == "in_progress":
                name = f"**{name}**"
            pct = f"{round(s['fraction']*100)}%"
            rungs = f"{s['rungs_done']}/{s['rungs_total']}" if s["rungs_total"] else "—"
            if compact:
                lines.append(f"| {LEARNER_ICON[s['learner']]} | {name}{here} | {tier} | `{bar(s['fraction'])}` {pct} |")
            else:
                lines.append(f"| {LEARNER_ICON[s['learner']]} | {name}{here} | `{bar(s['fraction'])}` {pct} | {rungs} | {s['hours']} h |")
        if not compact:
            lines.append("")
    if compact:
        lines.append("")
    return "\n".join(lines)


def stage_checklist(s: dict) -> str:
    if not s["parts"]:
        return "_Not yet rung-numbered; this stage is written one stage ahead of you._"
    out = []
    for p in s["parts"]:
        if p["id"]:
            out.append(f"**Part {p['id']} — {p['title']}**")
        for r in p["rungs"]:
            box = "[x]" if r["done"] else "[ ]"
            mins = f" · {r['minutes']} min" if r["minutes"] else ""
            label = f"Rung {r['n']} — {r['title']}{mins}"
            link = f"[{label}]({s['brief']}#{r['anchor']})"
            if r["current"]:
                link = f"**▶ {link}**"
            out.append(f"- {box} {link}")
        out.append("")
    return "\n".join(out)


def render_board_md(st: dict) -> str:
    cur_stage = next((s for s in st["stages"] if s["learner"] == "in_progress"), None)
    lines = [
        f"# Course — {st['learner']} · curriculum {st['curriculum_version']} · updated {st['updated']}",
        "",
        "> Rendered by `scripts/render_board.py` from `status/board.json`, the stage briefs and `PROGRESS.md`. Do not edit by hand. "
        "Interactive version: open `site/` (see [Course player](#course-player)).",
        "",
        "## Continue",
        "",
        continue_line(st),
        "",
        f"Overall: `{bar(st['hours_done']/st['hours_total'] if st['hours_total'] else 0)}` "
        f"{st['hours_done']} / {st['hours_total']} h · {st['stages_passed']} / {len(st['stages'])} stages passed",
        "",
        "## Course content",
        "",
        outline_table(st, compact=False),
    ]
    if cur_stage:
        lines += [
            f"## In this stage — Stage {int(cur_stage['id'][1:])}: {cur_stage['name']}",
            "",
            stage_checklist(cur_stage),
            "A rung is ticked when its Run, See and Say are all ☑ in [`PROGRESS.md`](PROGRESS.md). "
            "When every rung is ticked, file [`STAGE_FEEDBACK.md`](templates/STAGE_FEEDBACK.md) in the stage directory.",
            "",
        ]
    lines += [
        "## What happens next",
        "",
        f"**Now:** {st['now']['detail']}  ",
        f"**Next:** {st['now']['next']}  ",
        f"**Later:** {st['now']['later']}",
        "",
        "## Course player",
        "",
        "[wvlt.github.io/python-developer-101](https://wvlt.github.io/python-developer-101/) (published from `main`) or `just site` locally at `http://localhost:8000/site/`: "
        "a left pane with every stage, part and rung and how far you are into each, and the brief on the right.",
        "",
        "<details>",
        "<summary><b>Maintainer view</b> — build state per stage, queue, activity</summary>",
        "",
        "| Stage | Build | Learner | Note |",
        "|---|---|---|---|",
        *[f"| **{s['id']}** {s['name']} | {s['build_label']} | {s['learner_label']} | {s['note']} |" for s in st["stages"]],
        "",
        "Build states: *outline* (outcome, gate, contract fixed) → *rung-numbered* (every rung has Run/See/Say) → *verified* (every code block run against `PINS.md` pins) → *ready* (reference run done).",
        "",
        "| When | Task |",
        "|---|---|",
        *[f"| {q['when']} | {q['task']} |" for q in st["maintainer_queue"]],
        "",
        *[f"- **{a['date']}** — {a['event']}" for a in st["activity"]],
        "",
        "</details>",
        "",
    ]
    return "\n".join(lines)


def render_readme_block(st: dict) -> str:
    return "\n".join([
        START,
        "## Where you are",
        "",
        continue_line(st),
        "",
        outline_table(st, compact=True),
        "Full outline with the rung checklist for the current stage: [BOARD.md](BOARD.md). "
        "Course player (left pane: stages, parts, rungs and your progress; right pane: the brief): "
        "[wvlt.github.io/python-developer-101](https://wvlt.github.io/python-developer-101/) or `just site` locally.",
        END,
    ])


def stamp_assets() -> None:
    """Cache-bust style.css / app.js references in site/index.html with content hashes."""
    import hashlib
    idx = ROOT / "site" / "index.html"
    html = idx.read_text()
    for name in ("style.css", "app.js"):
        digest = hashlib.sha1((ROOT / "site" / name).read_bytes()).hexdigest()[:8]
        html = re.sub(rf'{re.escape(name)}(\?v=[0-9a-f]+)?"', f'{name}?v={digest}"', html)
    idx.write_text(html)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    b = json.loads(BOARD.read_text())
    st = compile_state(b)
    board_md = render_board_md(st)
    data_json = json.dumps(st, indent=1, ensure_ascii=False) + "\n"
    readme = README.read_text()
    if START not in readme or END not in readme:
        sys.exit("README.md lacks board markers")
    pre, rest = readme.split(START, 1)
    _, post = rest.split(END, 1)
    new_readme = pre + render_readme_block(st) + post
    outputs = {OUT_BOARD: board_md, OUT_DATA: data_json, README: new_readme}
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, content in outputs.items() if not p.exists() or p.read_text() != content]
        if stale:
            print("stale:", ", ".join(stale), "— run scripts/render_board.py")
            sys.exit(1)
        print("board up to date")
        return
    OUT_DATA.parent.mkdir(exist_ok=True)
    for p, content in outputs.items():
        p.write_text(content)
    stamp_assets()
    print("wrote BOARD.md, README block, site/data.json")


if __name__ == "__main__":
    main()
