# CONTEXT.md — who this is for, where it ends, and how it changes

This file is the contract between the curriculum and reality. Every brief, gate and template is subordinate to it. When a brief and this file disagree, the brief is wrong and gets revised per [docs/13-revision-protocol.md](docs/13-revision-protocol.md).

## The learner

- **Programming: 0/10.** Has never written a line of code in any language. Does not know what a variable, a loop, a file path, a package, an IDE, a terminal or a bug report is. Has never used git.
- **Computer: comfortable.** Installs applications, uses a browser and a spreadsheet, manages files and folders. Can follow written instructions with screenshots-level precision when the instructions are precise.
- **Reads English well. Motivated. 8–10 h/week**, roughly 15 weeks. Solo or in a cohort.
- **Budget: zero.** No paid tool, no cloud, no model anywhere in the course. The only account ever created is a free GitHub account, at stage 2.
- **Machine:** a laptop with 16 GB of memory on which they can install software. Windows or macOS; Linux works with the macOS instructions.

Every brief is written for this person. If a rung uses a word this person does not know, the rung is missing a definition or a rung below it. If a rung explains something an earlier rung already taught, it is wasting their time. Vocabulary arrives at most three new terms per rung, and every term is in the [glossary](docs/08-glossary.md).

## The destination

On completing stage 10, the learner is a **junior Python developer** who can be dropped into a tier-1 engineering or data team and be useful in week one. Concretely, on day one of that job they can:

1. **Read and write idiomatic Python fluently** — collections, comprehensions, functions, classes, dataclasses, generators, context managers, type hints — at the level the sibling courses assume on entry.
2. **Turn a plain-language task into a working command-line program**: modules and a package, classes where they earn their place, persistence to files (CSV, JSON), error handling that neither crashes nor hides, a `--help` that a stranger can use.
3. **Test it**: write pytest tests before trusting the program, parametrise them, use fixtures and `tmp_path`, measure coverage, and know what a test does and does not prove.
4. **Read a traceback and fix the bug** — including the quiet bugs that produce no traceback: aliasing, mutable defaults, `is` vs `==`, float precision, off-by-one, swallowed exceptions, encoding.
5. **See inside a running program**: `print`, f-string debugging, the debugger, `logging`, `timeit` and the profiler; and never ship a program they cannot see inside.
6. **Reach for the standard library before a package**, and for a package before writing it themselves; read documentation to find out which.
7. **Use the professional toolchain daily**: `uv`, `git` (branch, commit, push, pull request), `pytest`, `ruff`, `mypy`, a debugger, a terminal.
8. **Read other people's code**: a 200-line script, a module in the standard library, a colleague's pull request; and explain what it does and where it would break.
9. **Know when not to write code**: the standard library already does it, a shell one-liner does it, a spreadsheet does it, or the task is one-off.
10. **Explain their program** to a non-programmer in five sentences and to a senior engineer in a code review, including why they chose each structure.

**Hand-off.** The exit level is the **7/10 Python** that the sibling courses [AI Agents 101](https://github.com/wvlt/ai-agents-101) and Data Science 101 assume on entry: idiomatic, typed Python; packaging and virtual environments; pytest; dataclasses; context managers; reading a traceback; using git and a debugger without thinking. The stage-10 gate includes reading the AI Agents 101 Stage 0 brief and confirming, item by item, that the learner can start it unaided. The [capability map](docs/12-capability-map.md) breaks the ten capabilities above into competencies and names the rung that delivers each. Where the map says **GAP**, the curriculum does not yet deliver that competency, and that is the next revision.

## The vocabulary of this course

This curriculum shares its structure with the sibling courses, and some of their generic words mean something specific here:

- The **core object** is a **program**: text the learner wrote, that the interpreter runs, that produces output or an error. Every rung ends with a program that runs.
- **Measure** means **tests**. From stage 1 every rung ships with pytest tests the learner runs (`just test`); every stage gate runs a visible set and a hidden set of test cases (`just eval`) and writes a run directory with pass counts per exercise. Thresholds are "≥ N of M hidden tests pass" plus the Say questions. The course writes the tests until stage 6; from stage 6 the learner writes their own.
- **Break** means **productive failure with code**: predict the output, then run it, on short snippets chosen to expose a misconception; and find-and-fix exercises with planted bugs. Reading a traceback is taught in stage 0 and practised in every stage.
- **Inspect** (this course's name for the Observe strand) means **seeing what the program does**: `print` → f-string debugging → the debugger → `logging` → `timeit` and the profiler. The habit is *never ship a program you cannot see inside*.
- **Kill criteria** mean **when not to write code**: the standard library already does it; a shell one-liner does it; a spreadsheet does it; the task is one-off. Every stage names at least one.
- The **risk model** is the catalogue of **quiet failures** — the ways Python code lies to you without a traceback — in [docs/07](docs/07-failure-bestiary.md). The threat-model and red-team instruments become [`FAILURE_REVIEW.md`](templates/FAILURE_REVIEW.md) (where could this program be quietly wrong?) and [`BREAK_MY_PROGRAM.md`](templates/BREAK_MY_PROGRAM.md) (a peer tries to crash or mislead it with inputs).

## The model of the curriculum: stages are stable, rungs are not

- A **stage** is defined by its **outcome** (what the learner can do afterwards), its **gate** (how we know), and its **contract** (what it assumes from earlier stages and what later stages rely on). Stages are numbered 0–10 and change rarely; changing one requires an ADR.
- A **rung** is a unit of instruction inside a stage: one concept, one worked example, a handful of micro-exercises with tests, one thing to see. Rungs are numbered within the stage (`s02-r4` is rung 4 of stage 2) and **change freely**. Rungs may be inserted (`s02-r4b`), split, merged, rewritten or removed without touching the stage's outcome or gate. This is where learning from feedback lands.
- Each stage brief carries a **Contract** section: *Assumes* (what the learner must already be able to do, with the rung IDs that taught it) and *Provides* (what later stages take for granted, with the rung IDs that deliver it). Contracts are how a change cascades: alter a stage's *Provides*, and every later stage whose *Assumes* references it is checked.
- Each stage directory carries a `REVISIONS.md`: the log of rung changes to that stage, each tied to the feedback that caused it and the cascade check that followed.

The principle: **when a learner gets stuck, the response is a new or better rung, not a new stage.**

## How feedback flows

1. A learner works a stage and files a [stage feedback](templates/STAGE_FEEDBACK.md): where they stalled, how long each rung took, what was assumed but not taught, what was taught but already known, which exercise they could not do, which error message they could not read.
2. The maintainer classifies each item as a **rung change** (apply directly), a **contract change** (apply, then run the cascade check downstream), or a **stage change** (ADR first). See [docs/13](docs/13-revision-protocol.md).
3. Rung changes are logged in that stage's `REVISIONS.md`. Contract changes are logged there *and* in every downstream stage touched by the cascade. Stage changes go in `CHANGELOG.md` and `docs/decisions/`.
4. The capability map is updated if a competency moved or a gap closed.
5. Progress is visible in three places rendered from the same sources (`status/board.json`, the briefs' rung headings, and the learner's `PROGRESS.md`): the **course player**, [`BOARD.md`](BOARD.md), and the README outline. The learner's stage moves *in progress → feedback filed → revising → passed*; the next stage's build state moves *rung-numbered → verified → ready* before it unlocks. If the board and reality disagree, the board is wrong and gets fixed in the same commit.

Stage 0 and stage 1 feedback is expected to cascade the furthest, because every later stage's *Assumes* chain leads back to them. Fixing the bottom rungs well is the highest-leverage revision in the curriculum, and for an absolute beginner the bottom rungs are where every unexplained word lives.

**Division of labour.** The learner's only jobs are: work the rungs, tick Run/See/Say in `PROGRESS.md`, file `STAGE_FEEDBACK.md`. Everything else — pinning tool versions, writing exercises and their tests, verifying code against the pins, cascading changes, moving the board — is the maintainer's, and a brief never hands a design task to the learner.

## Rolling readiness

Briefs are brought to full rung granularity **one stage ahead of the learner**. Stages 0–2 are fully rung-numbered now, with exercises, visible tests, hidden tests and reference solutions. Stages 3–10 have complete outcomes, gates, contracts, break-labs and build sections at part level; their rungs are numbered as the learner approaches, incorporating everything learned from the stages before. A brief that has not yet been rung-numbered says so in its `REVISIONS.md`.

## What this file is not

It is not the syllabus ([docs/01](docs/01-syllabus.md)), not the pedagogy ([docs/03](docs/03-pedagogy.md)), and not the conventions ([docs/05](docs/05-conventions.md)). It is the statement of who, where to, and how change happens. Keep it short enough to reread before every revision.
