# Changelog

Semantic versioning per [11 — Curriculum maintenance](docs/11-curriculum-maintenance.md): major = stage structure; minor = substantive rung, gate, convention or pin-policy change, a stage rung-numbered; patch = pins, reading-list swaps, bestiary additions, fixes.

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
