"""`just trace FILE`: run a Python file and print every line of it as it executes.

A beginner's first Inspect tool after print(): see the order in which lines run, watch a loop go round,
see which branch of an if was taken. Only lines in the traced file are shown; library code is skipped.

    python -m course.tracer path/to/file.py  [< input.txt]
"""
from __future__ import annotations

import linecache
import runpy
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: python -m course.tracer FILE.py")
    target = Path(sys.argv[1]).resolve()
    sys.argv = [str(target), *sys.argv[2:]]
    counter = {"n": 0}

    def tracer(frame, event, arg):  # noqa: ANN001
        if Path(frame.f_code.co_filename).resolve() != target:
            return None
        if event == "line":
            counter["n"] += 1
            lineno = frame.f_lineno
            src = linecache.getline(str(target), lineno).rstrip()
            local_vars = {k: v for k, v in frame.f_locals.items() if not k.startswith("__")}
            shown = ", ".join(f"{k}={v!r}" for k, v in list(local_vars.items())[:6])
            print(f"{counter['n']:>4} | line {lineno:>3} | {src:<48} | {shown}", file=sys.stderr)
        return tracer

    sys.settrace(tracer)
    try:
        runpy.run_path(str(target), run_name="__main__")
    finally:
        sys.settrace(None)
        print(f"---- {counter['n']} line executions in {target.name}", file=sys.stderr)


if __name__ == "__main__":
    main()
