# 02 — Getting started

## If you have never programmed: start at stage 0, not here

[Stage 0](../stages/00-hello-python/README.md) installs everything, opens a terminal for the first time, and ends with a program you wrote running from it. It assumes nothing. Read this page *after* stage 0; it will make sense then. If you already know the terminal, read on.

## How to use this repository

This repository is the curriculum and the scaffold. From stage 2 you work in **your own fork** on GitHub; in stage 1 you work in a plain clone, because git arrives before GitHub does. Each stage's work lives in `stages/NN-name/` — the exercises you fill in, the mini-project, your journal, your artefact card. The upstream repository holds the briefs, tests, docs and templates; your fork holds your work.

Do not do the stages in a scratch directory. The portfolio *is* the outcome.

## Environment

Everything is free and runs on your laptop. Exact versions and download links are in [`PINS.md`](../PINS.md); the briefs refer to them by role.

- **Python** — the pinned version, from python.org, installed in stage 0.
- **The editor** — Visual Studio Code with the Python extension, installed in stage 0. Turn off AI completions until stage 7 (see the AI-assistance policy below).
- **`uv`** — installs Python versions, creates the project environment, runs scripts and tests. Installed in stage 1, rung 0. You never type `pip`.
- **`just`** — runs the standard commands (`just test`, `just eval`, `just break`, `just trace`). Installed in stage 1, rung 0.
- **git** — stage 1, rung 8. **GitHub** — stage 2, rung 10.

Initial setup (stage 1, rung 0, with the exact commands in the brief):

```bash
git clone https://github.com/wvlt/python-developer-101.git
cd python-developer-101
uv sync --extra dev
uv tool install rust-just
just test 01        # red: you have not written anything yet
```

## Tooling ramp

You do not need the whole toolchain on day one, and trying to adopt it all at once is the fastest way to stall. Tools arrive when they earn their place. Until a tool appears in this table, its absence is not a gate failure.

| Introduced in | Tool | Why then |
|---|---|---|
| Stage 0 | the terminal, Python, the editor, running a file | enough to say hello |
| Stage 1 | `uv run`, `just test`, git locally (`init`, `status`, `add`, `commit`, `log` — "save points") | the first exercises with tests need a runner; the first work worth keeping needs save points |
| Stage 2 | GitHub (free account, fork, push; the course player shows your `PROGRESS.md`), `ruff check`, `just trace` | enough code to want a second copy and a second opinion |
| Stage 4 | the debugger (`breakpoint()`, the editor's debug pane) | functions make "where am I?" a real question |
| Stage 5 | `logging`, environment variables, `argparse` | programs that touch files need a record and a command line |
| Stage 6 | virtual environments as a concept, `uv add`, `pyproject.toml`, pytest written by you | the first third-party package and the first test you write |
| Stage 9 | `mypy`, `timeit`, coverage, `ruff format`, `pre-commit` | craft |

## Cost caps

There are none, because there is no cost. No model, no cloud, no paid tool. The only account is GitHub (free) at stage 2. Instead of money, the course asks you to track **hours** in `LEDGER.md`: actual against budget, per stage. That number is how the next learner's rungs get re-estimated.

## How to work a stage

1. Read the stage `README.md` end to end before writing code. Read the Contract: *Assumes* is a checklist of what you should already be able to do; if an item is shaky, go back to the rung it names.
2. Do the **break-lab first**, before reading the Build section. For each snippet, write your predicted output in `JOURNAL.md`, then run `just break NN` and write what actually happened. The gap between the two columns is the lesson.
3. Work the rungs in order. Each rung is: a worked example (type it, run it, see it), then four to eight exercises in `exercises/`, then a **Check**. Run `just test NN` after each exercise; watch tests go from red to green.
4. Tick **Run**, **See** and **Say** in `PROGRESS.md` with the minutes spent. Be honest about the minutes; they are the data.
5. Commit after every rung (from stage 1, rung 8) with a message that says what changed.
6. When every rung is ticked, run `just eval NN`. It runs the hidden tests and writes a run directory with pass counts per exercise. Read the table; fix what it points at; run it again. The threshold is in the brief's Gate.
7. Fill in `ARTIFACT_CARD.md` for the mini-project. If a field is empty, you are not done.
8. Check every gate item. Answer the Say questions out loud, without notes, to a rubber duck, a peer or a recording.
9. Open a pull request in your fork from `stage/NN-name` to `main` (from stage 2). Use the PR template. If solo, review it yourself the next morning.
10. Merge. Tag `sNN-passed`. File `STAGE_FEEDBACK.md`. Start the next stage.

## Exercises, tests and the eval harness

- **Exercises** are files in `stages/NN-name/exercises/`. In stages 1–3 each is a small program: it reads `input()` and prints; the lines that read input are already written, and you write below the marker line. From stage 4 each is a function stub with a docstring; from stage 7, a class.
- **Visible tests** (`just test NN`) are in `tests/`. They show you exactly what input they give and what output they expect. A failing test prints the input, the expected output and yours, side by side.
- **Hidden tests** (`just eval NN`) are in `eval/`. They use inputs the visible tests did not show you (empty input, negative numbers, odd spacing). The harness prints pass counts per exercise and the IDs of failing cases, not the assertions. The files are in the repository; the convention is that you do not open `eval/` before the gate. Nobody checks. Your fluency does.
- **Reference solutions** are in `solutions/`. Open a solution **only after the rung's Check is ticked**, to compare against your own. Opening it before is a choice you make against yourself; the hidden tests will not care, but stage 4 will.
- **Break-lab snippets** are in `breaklab/`; `just break NN` runs them all.

## Rung checks

Every rung ends with a **Check**: *Run* (a command and what it should show), *See* (one question about your own output), *Say* (one sentence you should be able to produce without notes). A rung is done when all three hold. Tick them in `PROGRESS.md` as you go, with minutes spent. The course player (`just site`, or the published page linked from the README) reads `PROGRESS.md` and shows which rung you are on; a rung turns green when Run, See and Say are all ticked. Rubric details in [14 — Rubrics](14-rubrics.md).

## Journal, progress and ledger

- **Journal** (`stages/NN-name/JOURNAL.md`): dated entries. Break-lab predictions and results, surprises, the error message you could not read and how you read it, things you would tell your past self. Minimum one entry per session. Terse is fine.
- **Progress** (`PROGRESS.md` at the root): one row per rung, Run/See/Say, minutes, stall notes.
- **Ledger** (`LEDGER.md` at the root): hours per stage, actual against budget.

## AI-assistance policy

The destination is **fluency**: reading and writing Python without a translator. Fluency comes from writing many small programs yourself and reading the errors they produce; a tool that writes the program for you removes exactly the repetitions that build it. So:

1. **Through stage 6, you write every line unassisted.** An AI assistant may *explain* an error message or a concept in its own words, and may *ask you questions* about code you wrote. It may not write code, complete a line, or fix a bug for you. Turn off code completion in the editor; the Python extension's own suggestions (names of methods you have already typed the start of) are fine.
2. **From stage 7, you may use an AI assistant to review code you wrote** — "what would you change about this class and why?" — and to explain unfamiliar code you are reading. You still type every line you ship.
3. **You must be able to explain every line you ship.** A gate reviewer may point at any line and ask what it does and why. "The assistant wrote it" is a failing answer at any stage.
4. **Disclose.** Each Artefact Card has an "AI assistance" field. Fill it honestly.

A repository-level [`AGENTS.md`](../AGENTS.md) tells coding assistants these rules so they help rather than hinder. The policy is not moral; it is mechanical. If you prompt your way through stage 3, stage 5's traceback will be the first one you have ever read alone.

## If you are self-paced and alone

The curriculum assumes a peer for the stage-10 break-my-program session and teach-back, and benefits from one at every gate. If you have none:

- Gates: review your own pull request the next morning, as a stranger, with the [gate review form](../templates/GATE_REVIEW.md). Answer the Say questions into a voice recorder and listen back.
- Stage 10: run the break-my-program protocol against your own program from a written attack plan you drafted a week earlier; write the teach-back as a tutorial a stranger could follow, and publish it.
- Better: find one other learner anywhere and swap repositories.

## If you get stuck

In order: read the whole error message, bottom line first; run the program with a `print` or `just trace` to see what it is actually doing; reread the rung; look up the failure in the [bestiary](07-failure-bestiary.md); ask a peer with the error message and the input attached. Never ask without the error message. If you have been stuck on one thing for more than 30 minutes, write it in `PROGRESS.md` under Stall and move to the next exercise; a stall is a signal to the maintainer, not a verdict on you.
