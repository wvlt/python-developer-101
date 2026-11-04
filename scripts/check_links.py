#!/usr/bin/env python3
"""Fail if any relative markdown link in the repo points at a missing file."""
import re
import sys
from pathlib import Path

LINK = re.compile(r"\]\(([^)\s]+)\)")
broken: list[tuple[str, str]] = []
for md in Path(".").rglob("*.md"):
    if ".git/" in str(md) or ".venv" in str(md):
        continue
    for m in LINK.finditer(md.read_text()):
        link = m.group(1)
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        path = link.split("#", 1)[0]
        if path and not (md.parent / path).resolve().exists():
            broken.append((str(md), link))
for src, link in broken:
    print(f"{src}: broken link -> {link}")
print(f"{len(broken)} broken link(s)")
sys.exit(1 if broken else 0)
