#!/usr/bin/env python3
"""Fail if a pinned, volatile identifier has leaked out of PINS.md into a brief or doc.

Briefs and docs refer to roles ("the Python version in PINS.md", "the public API named in PINS.md");
PINS.md holds the identifiers. This check is the CI half of that convention. Extend PATTERNS when a new
kind of pin is added; the list is also the definition of "volatile" for docs/11.

    python scripts/check_pins.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN = [ROOT / "stages", ROOT / "docs", ROOT / "templates", ROOT / "CONTEXT.md", ROOT / "README.md", ROOT / "AGENTS.md"]
ALLOW = {"docs/11-curriculum-maintenance.md"}  # may quote a pattern as an example

PATTERNS = {
    "patch-level Python version": r"\b3\.1[0-9]\.[0-9]+\b",
    "tool or package with a version number": r"\b(uv|pytest|ruff|mypy|requests|rich|pre-commit|pytest-cov|gitleaks|just|VS Code|Code)\b[ =>~^]*v?[0-9]+\.[0-9]+(\.[0-9]+)?\b",
    "VS Code extension version": r"\b20[0-9]{2}\.[0-9]+\.20[0-9]{6,}\b",
    "download or marketplace URL": r"https?://(www\.)?(python\.org/(ftp|downloads/release)|marketplace\.visualstudio\.com|code\.visualstudio\.com/download|astral\.sh/uv/install|git-scm\.com/download)",
    "public API host": r"\bopenlibrary\.org\b",
}

bad: list[tuple[str, str, str]] = []
for base in SCAN:
    files = [base] if base.is_file() else sorted(base.rglob("*.md"))
    for md in files:
        rel = str(md.relative_to(ROOT))
        if rel in ALLOW:
            continue
        text = md.read_text(encoding="utf-8")
        for name, pat in PATTERNS.items():
            for m in re.finditer(pat, text):
                line = text.count("\n", 0, m.start()) + 1
                bad.append((f"{rel}:{line}", name, m.group(0)))

for where, name, hit in bad:
    print(f"{where}: {name}: {hit!r}")
print(f"{len(bad)} leaked identifier(s)")
sys.exit(1 if bad else 0)
