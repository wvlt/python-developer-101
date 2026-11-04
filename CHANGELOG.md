# Changelog

Semantic versioning per [11 — Curriculum maintenance](docs/11-curriculum-maintenance.md): major = stage structure; minor = substantive rung, gate, convention or pin-policy change, a stage rung-numbered; patch = pins, reading-list swaps, bestiary additions, fixes.

## [1.0.0] — 2026-11-04

Verified and published.

- **Stage 0 reference run** on macOS against the 3.13 interpreter recorded in `PINS.md` (Reference runs): 22 code blocks, 19 matched the brief as written, three rung changes: the prompt's banner is two lines; Way 3's traceback shown in full with its marker line; the `day1.py` comment uses a plain hyphen so that removing the `#` reports `invalid syntax` rather than an invalid-character error about an em dash. Table in `stages/00-hello-python/REVISIONS.md`.
- **Learner read-through of stages 0–2**: `isdigit` was assumed by stage 2 rung 4 and listed in stage 1's Provides but never shown; added to stage 1 rung 5. Stage 2's entry condition said `54 failed`; the first run is `53 failed, 1 passed` because one planted-bug case passes with the bug in place. Prompt examples in stage 1 evaluated; visible-test counts per rung confirmed for both stages.
- Authoring rule 8 (docs/15): plain punctuation inside code blocks. All exercise, solution and break-lab headers changed from em dash to hyphen; stage code formatted with `ruff format`; pre-commit `ruff` hooks scoped to `stages/` and excluding break-lab and planted-bug files.
- `PINS.md` gains a *Reference runs* table so that the patch version a stage was verified on lives there and nowhere else; `check_pins.py` enforces this for `REVISIONS.md` too.
- Board: stage 0 `verified`; curriculum version 1.0.0.

## [0.5.0] — 2026-11-04

The board and the player.

- `status/board.json`: course identity, four tiers, eleven stages with hours and build/learner states (stage 0 in progress, stage 1 ready, the rest locked; stages 3–10 `outline`), a maintainer queue of eight items keyed to unlock events, activity log.
- `PROGRESS.md` created from the template and populated by `scripts/make_progress.py` with the 29 rungs of stages 0–2 (outline stages contribute no rows).
- `BOARD.md`, the README board block and `site/data.json` rendered by `scripts/render_board.py`; `--check` in CI.
- GitHub Pages enabled (workflow build); the course player is live and opens on stage 0 rung 0.
- Thresholds in docs/01, docs/06, docs/14 and the progress template reconciled with the authored counts (s01 57/63; s02 56/62).

## [0.4.0] — 2026-11-04

The briefs.

- **Stage 0** rung-numbered: eight rungs in three parts (the machine; one change at a time; the habit), each with a Run/See/Say Check, both platforms at every terminal step, three deliberate failures with their bestiary IDs, `input()` inside `print()` so no name is bound before stage 1, a paper break-lab, a done-when list in place of a gate.
- **Stage 1** rung-numbered: ten rungs (toolchain and clone; arithmetic; types and conversions; names; strings; string methods; f-strings and `f"{x=}"`; truth, `None`, `is` vs `==`; git save points; the receipt). 29 exercises as whole programs over `input()`/`print()`, 57 visible tests, 63 hidden cases (threshold 57), eight break-lab snippets, reference solutions; gate `s01-g1`–`g4`.
- **Stage 2** rung-numbered: eleven rungs (`if`/`else`; `elif` and the conditional expression; `match`; `while` and ask-until-valid; `for`/`range`; `break`/`continue`/`else`; `enumerate`/`zip`; accumulators, flags, nesting; `ruff` with a planted bug carrying one loud and one quiet fault; GitHub fork, branch, PR; guess-the-number). 26 exercises, 54 visible, 62 hidden (threshold 56), nine break-lab snippets; gate `s02-g1`–`g5`.
- **Stages 3–10** at outline level: parts and planned rungs with time estimates and rung IDs, binding Contracts, Break-lab targets by bestiary ID, Gate IDs with thresholds, kill criteria, stretch, reading; each `REVISIONS.md` states the outline status and the open items for rung-numbering.
- Harness: `just test NN -k rMe` filters by rung (visible test ids are `rMeK-a`); `--tb=short` for beginner-readable failures; `ruff` rule set `A` enabled for shadowed built-ins; long header comments in exercises exempt from E501; `.python-version` pins the minor for `uv`.
- The threshold rule in docs/06 restated as "about 90 %".

## [0.3.0] — 2026-11-04

Curriculum documents, templates and the maintainer surface.

- `docs/01`–`17`: syllabus with the 140-hour budget; getting started with the tooling ramp and the AI-assistance policy (unassisted through stage 6); pedagogy; platform and tooling (local, free, no accounts but GitHub); conventions (exercise shape, case IDs, commit scopes); assessment and gates (universal checklist `u1`–`u10`, per-stage criteria, capstone criteria including the "a spreadsheet would do" pass); failure bestiary with stable IDs in categories S/T/F/C/N/E/Q/O/H and the **quiet failures** list as the course's risk model; glossary with stage tags; reading list (all free); instructor guide with the **break-my-program protocol**; maintenance with the identifier grep and the Python minor-version policy; capability map tracing all ten destination capabilities and every topic on the ladder to a rung or part; revision protocol; rubrics (strand **Inspect**; anchors for stages 0–2); authoring guide; build readiness; focus map with the tool ladder and the part plan for stages 3–10.
- Templates adapted to the domain: `THREAT_MODEL.md` → `FAILURE_REVIEW.md`; `RED_TEAM_REPORT.md` → `BREAK_MY_PROGRAM.md`; `RUNBOOK.md` → `PROJECT_README.md`; Artefact Card measures tests and inputs, not cost; Comparison memo and ADR measure lines, tests and `timeit`; Error analysis is the stage-9 planted-bug hunt; Journal has the prediction table and a debugger-session entry; Progress gate log has an Inspect column and hidden-test counts.
- `AGENTS.md` rule 1: no code from an assistant through stage 6; solutions and `eval/` only after the Check and the gate. `CONTRIBUTING.md`. `LEDGER.md` counts hours, not money.

## [0.2.0] — 2026-11-04

Verbatim machinery, pins, fixture.

- Copied from the reference course: `site/` (course player), `scripts/render_board.py`, `scripts/check_links.py`, Pages workflow, PR and issue templates, `.gitignore`, pre-commit, licence layout.
- `PINS.md`: every version, link and the public API verified against live sources on the pin date; Python pinned to the last 3.13 release with a binary installer, with the reasoning; deprecation log started.
- `data/build_files.py`: the neighbourhood library — 120 books, 60 members, 400 loans; CSV, JSON and a messy text file; four broken files (encoding, missing column, duplicate IDs, bad dates); a recorded public-API response; `reference.json` with thirty answers. Deterministic; CI diffs two builds.
- `scripts/check_pins.py` (identifier grep), `scripts/eval.py` (hidden-test harness writing run directories with stable case IDs), `course/runner.py` (subprocess exercise runner with beginner-readable failures), `course/tracer.py` (`just trace`), `conftest.py`, `justfile`, `pyproject.toml`, `.env.example`, docs CI.

## [0.1.0] — 2026-11-04

Intent and structure.

- `CONTEXT.md`: the learner (programming 0/10, 8–10 h/week, zero budget), the destination (ten day-one capabilities; 7/10 Python at exit, the entry level of AI Agents 101 and Data Science 101), the vocabulary translation (program; tests; predict-then-run; Inspect; kill criteria; quiet failures), the stage/rung/contract model, the feedback flow and the division of labour.
- `docs/00-intent.md` with the Programmer's Oath.
- ADR-001 ten stages, four tiers, four strands (Observe renamed Inspect); ADR-002 stage 0 and the tooling ramp; ADR-003 stable stages, revisable rungs; ADR-004 exercises as programs, tests by the course.
- `README.md` with the ladder, start here, the doc map and the board markers.
