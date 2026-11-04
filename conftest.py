"""Root pytest configuration: makes `course` importable and gives tests the stage directory and target.

COURSE_TARGET=exercises (default) runs tests against the learner's files; COURSE_TARGET=solutions runs them
against the reference solutions (used by CI and `just eval --solutions`).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from course.runner import check as _check  # noqa: E402


@pytest.fixture
def stage_dir(request: pytest.FixtureRequest) -> Path:
    """The stages/NN-name/ directory that contains the running test file."""
    p = Path(request.fspath).resolve()
    for parent in p.parents:
        if parent.parent.name == "stages":
            return parent
    raise RuntimeError(f"test file {p} is not inside stages/NN-name/")


@pytest.fixture
def target_dir(stage_dir: Path) -> Path:
    """exercises/ by default; solutions/ when COURSE_TARGET=solutions."""
    return stage_dir / os.environ.get("COURSE_TARGET", "exercises")


@pytest.fixture
def run_exercise(target_dir: Path):
    """run_exercise("r1e1_add", "3\\n4\\n", "7") asserts the program prints 7 for that input."""

    def _run(name: str, stdin: str, expected: str) -> None:
        _check(target_dir / f"{name}.py", stdin, expected)

    return _run


@pytest.fixture
def data_dir() -> Path:
    """The generated fixture (stage 3 onward); built on demand."""
    d = ROOT / os.environ.get("LIBRARY_DATA_DIR", "data/library")
    if not (d / "reference.json").exists():
        import subprocess

        subprocess.run([sys.executable, str(ROOT / "data" / "build_files.py"), "--out", str(d)], check=True)
    return d
