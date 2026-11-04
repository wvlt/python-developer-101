#!/usr/bin/env python3
"""Generate the rung rows of PROGRESS.md from the briefs' rung headings, keeping any ticks already there.

    python scripts/make_progress.py          # rewrite PROGRESS.md rung table
    python scripts/make_progress.py --check  # exit 1 if a rung in a brief has no row (CI-friendly)

Only stages whose board build state is rung_numbered, verified or ready contribute rows; outline stages have no rungs yet.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = json.loads((ROOT / "status" / "board.json").read_text())
PROGRESS = ROOT / "PROGRESS.md"
RUNG_RE = re.compile(r"^#{2,3} Rung (\w+) — ", re.M)
ROW_RE = re.compile(r"^\| (s\d\d-r\w+) \|")


def rung_ids() -> list[str]:
    ids = []
    for s in BOARD["stages"]:
        if s["build"] == "outline":
            continue
        hits = sorted((ROOT / "stages").glob(f"{s['id'][1:]}-*/README.md"))
        if not hits:
            continue
        for m in RUNG_RE.finditer(hits[0].read_text()):
            ids.append(f"{s['id']}-r{m.group(1)}")
    return ids


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = PROGRESS.read_text()
    existing = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            existing[m.group(1)] = line
    ids = rung_ids()
    missing = [i for i in ids if i not in existing]
    if a.check:
        if missing:
            print("PROGRESS.md lacks rows for:", ", ".join(missing))
            sys.exit(1)
        print("PROGRESS.md has a row for every rung")
        return
    rows = [existing.get(i, f"| {i} | | | ☐ | ☐ | ☐ | | |") for i in ids]
    head, _, rest = text.partition("| Rung | Started | Minutes | Run | See | Say | Stall? | Note |")
    _, _, tail = rest.partition("\n\n")  # skip the old table body
    sep = "|---|---|---|---|---|---|---|---|"
    new = head + "| Rung | Started | Minutes | Run | See | Say | Stall? | Note |\n" + sep + "\n" + "\n".join(rows) + "\n\n" + tail
    PROGRESS.write_text(new)
    print(f"PROGRESS.md: {len(rows)} rung rows ({len(missing)} added)")


if __name__ == "__main__":
    main()
