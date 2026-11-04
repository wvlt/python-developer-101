# ADR-002 — A literal hello-world Stage 0 and a tooling ramp that starts at the terminal

- **Status:** accepted
- **Date:** 2026-11-04
- **Deciders:** curriculum author
- **Amends:** ADR-001 (fixes the entry point and the order in which tools arrive)

## Context

The learner has never opened a terminal. Most beginner material assumes the terminal, the editor and "run the file" are already understood, and begins at variables. For this learner the first ninety minutes are the terminal, the difference between the REPL and a file, and the discovery that an error message is readable. If those are folded into stage 1, stage 1 carries installation, the terminal, the REPL, files, numbers, strings, variables, `uv`, tests and git in one 12-hour block, which violates the cognitive-load rule in docs/03.

A second question is which tools arrive when. The destination requires `uv`, git, pytest, ruff, mypy and a debugger in daily use; introducing them all in stage 1 would bury the Python under tooling, and deferring them to stage 9 would mean the learner forms habits without them.

## Options considered

### Option A — Start at stage 1 with a "setup" rung

- One rung for Python, VS Code, terminal, REPL and running a file, then straight into numbers.
- A single rung cannot carry five first-time experiences and a Check; the stall rate would be invisible because it would be inside stage 1's feedback.

### Option B — An ungated two-hour Stage 0 that is literally `print("Hello, world")` (chosen)

- Install Python and VS Code from the pinned links; open a terminal for the first time; type `python` and see the REPL; type `print("Hello, world")`; save the same line in `hello.py`; run `python hello.py`. Then one change at a time: change the text; print two things; a number and a word (discover quotes); make it fail on purpose three ways and read each error slowly; `input()` and a greeting; and finish with the habit — a three-line script, saved in a folder the learner made, with a comment on top, run from the terminal. Eight rungs, every line shown, no gate, a Done-when list.
- Zero accounts, zero cost, under two hours. **No git, no `uv`, no tests yet.** Those are stage 1's first rung, because a learner who has run a file from the terminal can install a tool from the terminal; one who has not, cannot.

### Option C — Start in an online editor to skip installation

- Removes the terminal and the file system from the first hour; both are destination skills and both are where this learner is least sure. Postponing them makes stage 1 harder, not easier. Rejected.

## Decision

Option B for stage 0. The tooling ramp is fixed as follows and written into docs/02, docs/17 and each brief's entry condition:

| Stage | Tools that arrive | Why then |
|---|---|---|
| 0 | the terminal, Python, VS Code, running a file | enough to say hello |
| 1 | `uv` (`uv sync`, `uv run`), `just test`, git locally (`init`/`add`/`commit`/`log` — "save points", nothing else) | the first exercises with tests need a runner; the first work worth keeping needs save points |
| 2 | GitHub (free account, fork, push; the course player shows your `PROGRESS.md`), `ruff check` | enough code to want a second copy and a second opinion |
| 4 | the debugger (`breakpoint()`, VS Code's debug pane) | functions make "where am I?" a real question |
| 5 | `logging` | programs that touch files need a record of what they did |
| 6 | virtual environments as a concept, `uv add`, `pyproject.toml`, pytest written by the learner | the first third-party package and the first test the learner writes |
| 9 | `mypy`, `timeit`, coverage | craft: types checked, speed measured, tests measured |

Until a tool appears in this table, its absence is not a gate failure. There is no hosted or paid tool at any rung; the ledger tracks hours, not money.

## Consequences

- The curriculum genuinely starts from the first terminal.
- Stage 0 is the one brief with the most literal, platform-specific instructions (Windows and macOS differ in the command name for Python and the terminal application). It rots fastest; the maintenance cadence in docs/11 re-runs it every cohort against the pins.
- Stage 1 begins with a 40-minute tooling rung before any Python. That is accepted: the alternative is tests that the learner cannot run.
- Revisit if learners who completed stage 0 still stall on stage 1's first rung (install `uv`, clone, `uv sync`, `just test`); that would argue for moving `uv` into stage 0.

## Kill criteria for this decision

If a learner who completed stage 0 cannot, unaided, create a folder, save a file in it, and run it from the terminal, stage 0 is not doing its job and should be rewritten rather than extended.
