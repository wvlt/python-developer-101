# Course — first learner · curriculum v1.0.0 · updated 2026-11-04

> Rendered by `scripts/render_board.py` from `status/board.json`, the stage briefs and `PROGRESS.md`. Do not edit by hand. Interactive version: open `site/` (see [Course player](#course-player)).

## Continue

**Stage 0 · Rung 0 — Install Python and the editor** · ~25 min  
[Open the rung](stages/00-hello-python/README.md#rung-0--install-python-and-the-editor) · 0 of 8 rungs done in this stage

Overall: `▱▱▱▱▱▱▱▱▱▱` 0 / 140 h · 0 / 11 stages passed

## Course content

**Tier A — Talking to the machine**

| | Stage | Progress | Rungs | Time |
|---|---|---|---|---|
| ▶ | **[0 · Hello Python](stages/00-hello-python/README.md)** ← you are here | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/8 | 2 h |
| 🟢 | [1 · Values and names](stages/01-values-and-names/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/10 | 12 h |
| 🔒 | [2 · Decisions and repetition](stages/02-decisions-and-repetition/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 12 h |
| 🔒 | [3 · Collections](stages/03-collections/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 14 h |

**Tier B — Structure**

| | Stage | Progress | Rungs | Time |
|---|---|---|---|---|
| 🔒 | [4 · Functions](stages/04-functions/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 14 h |
| 🔒 | [5 · Errors and files](stages/05-errors-and-files/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 14 h |
| 🔒 | [6 · Modules and tooling](stages/06-modules-and-tooling/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/10 | 12 h |

**Tier C — Objects**

| | Stage | Progress | Rungs | Time |
|---|---|---|---|---|
| 🔒 | [7 · Classes and objects](stages/07-classes-and-objects/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/9 | 12 h |
| 🔒 | [8 · Design and the data model](stages/08-design-and-the-data-model/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/9 | 14 h |

**Tier D — Craft**

| | Stage | Progress | Rungs | Time |
|---|---|---|---|---|
| 🔒 | [9 · Writing Python well](stages/09-writing-python-well/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 14 h |
| 🔒 | [10 · Capstone](stages/10-capstone/README.md) | `▱▱▱▱▱▱▱▱▱▱` 0% | 0/11 | 20 h |

## In this stage — Stage 0: Hello Python

**Part A — The machine**
- [ ] **▶ [Rung 0 — Install Python and the editor · 25 min](stages/00-hello-python/README.md#rung-0--install-python-and-the-editor)**
- [ ] [Rung 1 — Hello in the prompt · 10 min](stages/00-hello-python/README.md#rung-1--hello-in-the-prompt)
- [ ] [Rung 2 — The same line in a file · 15 min](stages/00-hello-python/README.md#rung-2--the-same-line-in-a-file)

**Part B — One change at a time**
- [ ] [Rung 3 — Change the text; print two things · 10 min](stages/00-hello-python/README.md#rung-3--change-the-text-print-two-things)
- [ ] [Rung 4 — A number and a word · 10 min](stages/00-hello-python/README.md#rung-4--a-number-and-a-word)
- [ ] [Rung 5 — Make it fail on purpose, three ways · 20 min](stages/00-hello-python/README.md#rung-5--make-it-fail-on-purpose-three-ways)
- [ ] [Rung 6 — Ask a question · 10 min](stages/00-hello-python/README.md#rung-6--ask-a-question)

**Part C — The habit**
- [ ] [Rung 7 — A folder, a file, a comment · 15 min](stages/00-hello-python/README.md#rung-7--a-folder-a-file-a-comment)

A rung is ticked when its Run, See and Say are all ☑ in [`PROGRESS.md`](PROGRESS.md). When every rung is ticked, file [`STAGE_FEEDBACK.md`](templates/STAGE_FEEDBACK.md) in the stage directory.

## What happens next

**Now:** Install Python and the editor from the links in PINS.md, open a terminal, print one line, then change one thing at a time. Eight rungs, about two hours, no account, no git yet. Tick Run/See/Say in PROGRESS.md after each rung; when all eight are ticked, start stage 1 rung 0.  
**Next:** Stage 1 — Values and names: rung 0 installs uv, just and git, clones the course and turns 57 tests red; rungs 1–9 turn them green and end with the receipt.  
**Later:** Stage 2 — Decisions and repetition (ruff, GitHub, the text game). Stage 3 is rung-numbered while you are in stage 2.

## Course player

[wvlt.github.io/python-developer-101](https://wvlt.github.io/python-developer-101/) (published from `main`) or `just site` locally at `http://localhost:8000/site/`: a left pane with every stage, part and rung and how far you are into each, and the brief on the right.

<details>
<summary><b>Maintainer view</b> — build state per stage, queue, activity</summary>

| Stage | Build | Learner | Note |
|---|---|---|---|
| **s00** Hello Python | verified | In progress | Ungated. Every code block run on macOS against the 3.13 interpreter in PINS.md (Reference runs) on 2026-11-04; three rung changes; Windows run before the first Windows learner. |
| **s01** Values and names | rung-numbered | Ready | 63 hidden cases, threshold 57; solutions green in CI. Verified when a maintainer runs every code block on the pins. |
| **s02** Decisions and repetition | rung-numbered | Locked | 62 hidden cases, threshold 56; planted bug r9b1; GitHub at r10. |
| **s03** Collections | outline | Locked | Rung-numbered while the learner is in s02; fixture literals generated from data/library/. |
| **s04** Functions | outline | Locked | Exercise shape changes to function stubs; debugger at r10. |
| **s05** Errors and files | outline | Locked | Fixture arrives as files; the four broken files are gate cases. |
| **s06** Modules and tooling | outline | Locked | Learner writes tests from r8; mutation check in just eval 06 is new harness work. |
| **s07** Classes and objects | outline | Locked | First required ADR; AI review of own code allowed from here. |
| **s08** Design and the data model | outline | Locked | Comparison memo; context managers as author. |
| **s09** Writing Python well | outline | Locked | Three fixtures to build: 200-line script, stranger's PR branch, twelve-bug package. |
| **s10** Capstone | outline | Locked | Break-my-program, teach-back, hand-off to the sibling courses. |

Build states: *outline* (outcome, gate, contract fixed) → *rung-numbered* (every rung has Run/See/Say) → *verified* (every code block run against `PINS.md` pins) → *ready* (reference run done).

| When | Task |
|---|---|
| on s00 feedback | Classify feedback items; apply rung changes to s00; cascade to s01 Assumes; log in REVISIONS.md. Run s00 on Windows on a machine without Python. |
| before s01 unlock | Run every s01 code block on the pins (both platforms for r0); confirm the 57-red / `-k r1e` counts match the brief; mark s01 verified. |
| before s02 unlock | Run every s02 code block on the pins; verify the GitHub fork, Pages and PR steps end to end on a fresh account; mark s02 verified. |
| while learner in s02 | Rung-number s03 with s00–s02 feedback: exercises with embedded fixture literals, hidden cases, solutions, break-lab, rubric anchors; reconcile threshold; `just progress`. |
| before s04 readiness | Extend course/runner.py and conftest for function-stub exercises (import and call); provide the debugger rung's buggy program. |
| before s06 readiness | Mutation check in scripts/eval.py; confirm the public API still returns the three fields (PINS.md step 6). |
| before s09 readiness | Build the 200-line script, the stranger's PR branch in upstream, and the twelve-bug package with its answer key outside the learner path; decide pre-commit rung vs stretch. |
| before s10 readiness | Confirm the sibling course's Stage 0 Contract is stable; capstone hidden cases as subprocess runs on the fixture and broken files. |

- **2026-11-04** — v1.0.0: Stage 0 reference run (22 blocks, 3 brief changes); learner read-through of stages 0–2 (isdigit added to s01-r5; s02 first-run count corrected); identifier grep, link check and board check green; tagged.
- **2026-11-04** — v0.5: board.json, PROGRESS.md generated from the briefs, BOARD.md and README block rendered, course player published on Pages.
- **2026-11-04** — v0.4: stages 0–2 rung-numbered with Checks, exercises, visible and hidden tests, solutions and break-labs; stages 3–10 outlined with binding Contracts and Gate IDs.
- **2026-11-04** — v0.3: docs/01–17, domain templates (FAILURE_REVIEW, BREAK_MY_PROGRAM, PROJECT_README), AGENTS.md, CONTRIBUTING.md, CHANGELOG.md, LEDGER.md (hours).
- **2026-11-04** — v0.2: course player, scripts and workflows copied verbatim from the reference course; PINS.md verified live; deterministic library fixture; eval harness.
- **2026-11-04** — v0.1: CONTEXT.md, intent, ADR-001..004, repository created.

</details>
