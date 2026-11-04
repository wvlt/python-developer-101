"""Run a learner's exercise file as a separate process and compare its output.

Exercises in stages 1–3 are programs: they read `input()` and `print()`. Tests feed stdin and compare stdout,
normalised so that trailing spaces and a missing final newline do not count as failures (a beginner's
`print` should not fail on invisible characters) but everything else is exact.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

TIMEOUT_S = 10.0


class ExerciseError(AssertionError):
    """Raised with a message a beginner can read."""


def normalise(text: str) -> str:
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def run_script(path: Path, stdin: str = "", timeout: float = TIMEOUT_S) -> tuple[str, str, int]:
    """Return (stdout, stderr, returncode) of running `path` with `stdin`, from the file's own directory."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    try:
        proc = subprocess.run(
            [sys.executable, str(path)],
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            cwd=path.parent,
            env=env,
        )
    except subprocess.TimeoutExpired as e:
        raise ExerciseError(
            f"{path.name} did not finish within {timeout:.0f} s. Is there a loop that never ends, "
            f"or an input() waiting for a line the test did not provide?\n--- stdin given ---\n{stdin}"
        ) from e
    return proc.stdout, proc.stderr, proc.returncode


def check(path: Path, stdin: str, expected: str) -> None:
    """Assert that running `path` with `stdin` prints `expected`."""
    if not path.exists():
        raise ExerciseError(f"{path} does not exist")
    source = path.read_text(encoding="utf-8")
    body = source.split("# --- your code below this line ---", 1)[-1].strip()
    if body == "" or all(ln.strip().startswith("#") or not ln.strip() for ln in body.splitlines()):
        raise ExerciseError(f"{path.name}: nothing written below the marker yet")
    out, err, rc = run_script(path, stdin)
    if rc != 0:
        tail = err.strip().splitlines()[-1] if err.strip() else "(no error text)"
        raise ExerciseError(
            f"{path.name} crashed. Last line of the error:\n    {tail}\n"
            f"Run it yourself and read the whole traceback, bottom up:\n    uv run {path}\n--- stdin given ---\n{stdin}"
        )
    got, want = normalise(out), normalise(expected)
    if got != want:
        raise ExerciseError(
            f"{path.name}: output differs.\n--- stdin given ---\n{stdin}--- expected ---\n{want}\n--- got ---\n{got}\n"
        )
