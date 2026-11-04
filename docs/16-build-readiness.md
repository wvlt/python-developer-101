# 16 — Build readiness

What must be true before authoring the learning materials for a stage, and the status of each item. This is the pre-flight list; it is short on purpose. The live version of the queue is the maintainer view on the [board](../BOARD.md).

## Global (once, before stage 0 materials)

| # | Item | Why it blocks | Status |
|---|---|---|---|
| G1 | **Pins in `PINS.md`** — Python patch version with a binary installer on both platforms; editor and extension; `uv`, `just`, `pytest`, `ruff`, `mypy`, coverage, the HTTP client, the terminal-output library; the public API; the fixture seed | Stage 0–2 code runs verbatim; a pin is a precondition for a reference run | **done 2026-11-04** in [`PINS.md`](../PINS.md), every entry verified against its live source that day |
| G2 | **Platform path for stage 0** | Determines the first screen the learner sees and the command they type | **decided**: the official installer from the link in PINS.md on both platforms; `python3` on macOS, `python` on Windows; `uv` installs its own Python from stage 1 so the platform difference ends there (ADR-002) |
| G3 | **Fixture in `data/`** | s03 onward reference it; s05 needs the broken files | **done**: `build_files.py`, deterministic (CI diffs two builds), `reference.json` with q01–q30, four broken files, a recorded API response |
| G4 | **CI for docs** — link check, board check, identifier grep, gitleaks | Every PR to briefs stays consistent | done (v0.2) |
| G5 | **CI for code** — hidden tests against `solutions/` for every stage; fixture determinism | Guarantees the tests and the reference solutions agree | done for the harness (v0.2); populated as each stage is rung-numbered |
| G6 | **Repo scaffolding** — `pyproject.toml`, `justfile`, `conftest.py`, `course/runner.py`, `scripts/eval.py`, `.pre-commit-config.yaml` | Learners and CI run the same commands | done (v0.2–v0.3) |
| G7 | **Reference run** — every stage completed on the pins by a maintainer; recorded in each `REVISIONS.md` | Validates briefs and gates before learners meet them | s00 at v1.0.0 on macOS; Windows run and s01+ as each stage reaches *verified* on the board |
| G8 | **Rubrics and instruments** — rung rubric, stage rubric, gate review form, progress log, feedback form, rung template | Reviews and feedback are structured from the first learner | done (v0.3) |
| G9 | **Authoring guide** — content model, voice, code rules, exercise shape, DoD | Consistency across stages and authors | done (v0.3) |
| G10 | **Licence for fixtures** | Public repo | fixtures CC0 (synthetic); recorded API sample under the API's own terms, noted in `data/README.md` |
| G11 | **Exercise model** — how a stage 1 learner's program can be tested before functions exist | Without it, Measure cannot start at stage 1 | **decided** (ADR-004): programs over stdin/stdout run as subprocesses; function stubs from s04; class stubs from s07 |

## Per stage (before rung-numbering stage N)

| # | Item | s00 | s01 | s02 | s03–s10 |
|---|---|---|---|---|---|
| P1 | Previous stage's `REVISIONS.md` read and open feedback applied | n/a | pending s00 feedback | pending | — |
| P2 | Rungs written per `templates/RUNG.md`, Checks present | v0.4 | v0.4 | v0.4 | outline; part plan in docs/17 |
| P3 | Exercises, visible tests, hidden cases, solutions; `eval.py --solutions` green | n/a | v0.4 | v0.4 | at rung-numbering |
| P4 | Break-lab snippets in `breaklab/` with bestiary IDs | n/a (in brief) | v0.4 | v0.4 | at rung-numbering |
| P5 | Contract matches neighbours | v0.4 | v0.4 | v0.4 | v0.4 (part level) |
| P6 | Code blocks run on the pins | v1.0.0 (macOS) | at s01 verification | at s02 verification | — |
| P7 | Gate IDs and thresholds assigned; threshold.json agrees with brief and docs/01 | n/a (done-when) | v0.4 | v0.4 | v0.4 (IDs, thresholds; no threshold.json yet) |
| P8 | Rubric anchors written | done (docs/14) | done (docs/14) | done (docs/14) | at rung-numbering |
| P9 | `PROGRESS.md` rows generated | v0.5 | v0.5 | v0.5 | at rung-numbering |
| P10 | Time estimates per rung sum to budget | v0.4 | v0.4 | v0.4 | — |
| P11 | Read-through as the CONTEXT.md learner | v1.0.0 | v1.0.0 | v1.0.0 | at rung-numbering |
| P12 | Stage-specific fixture present | n/a | n/a | n/a | s09: a stranger's PR branch; s10: sibling course Stage 0 brief reachable |

## Decisions (resolved 2026-11-04)

1. **Platform path:** official installer, both platforms, in stage 0; `uv`-managed Python from stage 1 (ADR-002).
2. **Exercise model:** programs over stdin/stdout until functions exist (ADR-004).
3. **Fixture:** purpose-built neighbourhood library, generated with a fixed seed, broken files included.
4. **Strand name:** Observe → Inspect (ADR-001).
5. **Hidden tests in a public repo:** convention plus Say questions, not obfuscation (ADR-004).

## Order of work from here

1. ~~Pins (G1).~~ Done.
2. ~~Fixture (G3, G10).~~ Done.
3. ~~Scaffold, harness, CI (G4–G6).~~ Done.
4. Stages 0–2 rung-numbered with exercises, tests, hidden cases, solutions, break-labs (v0.4).
5. Board, progress, player live (v0.5).
6. Stage 0 reference run on macOS; learner read-through of 0–2; v1.0.0.
7. Stage 0 reference run on Windows; file the first `STAGE_FEEDBACK.md`; apply rung changes; cascade to s01.
8. Rung-number stage 3 with everything s0–2 taught; continue one stage ahead of the learner.
