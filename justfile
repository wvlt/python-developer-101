# Standard targets for every stage (docs/05-conventions.md, "Standard commands").
# Usage:  just <target> [STAGE]      e.g.  just test 01      just eval 02      just break 03
# STAGE is the two-digit stage number. It defaults to the stage the board says you are on.

set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

# The stage currently "in progress" on the board, e.g. 01.
_current:
    @python3 -c 'import json; s=[x for x in json.load(open("status/board.json"))["stages"] if x["learner"]=="in_progress"]; print(s[0]["id"][1:] if s else "01")'

# Resolve a stage number ("02") to its directory.
_dir stage:
    @ls -d stages/{{stage}}-*/ 2>/dev/null | head -1 || { echo "no stage {{stage}}"; exit 1; }

# ---- setup ----------------------------------------------------------------

# Install the toolchain (pytest, ruff, mypy, coverage) into the project's own environment. Stage 1, rung 0.
setup:
    uv sync --extra dev

# Build the fixture: the neighbourhood library world in data/library/ (stage 3 onward). Deterministic.
data:
    python3 data/build_files.py

# ---- the standard targets --------------------------------------------------

# Visible tests for a stage: the ones each rung tells you to run.
test stage="" *flags:
    @s="{{stage}}"; [ -n "$s" ] || s=$(just _current); d=$(just _dir $s); \
    if [ -d "$d/tests" ]; then uv run pytest "$d/tests" --import-mode=importlib {{flags}}; \
    else echo "stage $s: no tests/ (stage 0 has no tests; it has a Done-when list)"; fi

# The eval harness: hidden tests for a stage; writes eval/runs/<timestamp>-<sha>/summary.json and prints the verdict.
eval stage="" *flags:
    @s="{{stage}}"; [ -n "$s" ] || s=$(just _current); uv run python scripts/eval.py "$s" {{flags}}

# Run a Python file and print every line as it executes (your second Inspect tool after print).
trace file *args:
    uv run python -m course.tracer "{{file}}" {{args}}

# The stage's break-lab snippets: predict each output in your journal first, then run this.
break stage="":
    @s="{{stage}}"; [ -n "$s" ] || s=$(just _current); d=$(just _dir $s); \
    if [ -d "$d/breaklab" ]; then for f in "$d"/breaklab/*.py; do echo; echo "== $(basename $f)"; uv run python "$f" || true; done; \
    else echo "stage $s: break-lab is in the brief (no runnable snippets)"; fi

# Lint and format-check the exercises you have written (stage 2 onward).
check stage="":
    @s="{{stage}}"; [ -n "$s" ] || s=$(just _current); d=$(just _dir $s); \
    uv run ruff check "$d/exercises" && echo "ruff: clean"

# Stage 9 onward: type-check and coverage.
craft stage="09":
    @d=$(just _dir {{stage}}); uv run mypy "$d/src" && uv run pytest "$d/tests" --cov="$d/src" --cov-report=term-missing -q

# ---- maintainers -----------------------------------------------------------

# Docs CI equivalents, locally.
docs:
    python3 scripts/check_links.py
    python3 scripts/check_pins.py
    python3 scripts/render_board.py --check

# Grade every stage's reference solutions against its hidden tests (what CI does).
solutions:
    uv run python scripts/eval.py --solutions --all

# Re-render BOARD.md, the README outline and site/data.json from board.json, the briefs and PROGRESS.md.
board:
    python3 scripts/render_board.py

# Regenerate PROGRESS.md rows from the briefs (keeps existing ticks).
progress:
    python3 scripts/make_progress.py

# Course player: left pane = stages, parts, rungs and your progress; right pane = the brief.
site: board
    @echo "open http://localhost:8000/site/"
    python3 -m http.server 8000 --bind 127.0.0.1
