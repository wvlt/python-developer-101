# Stage 10 — Capstone

*Tier D · ~20 hours · Cost: zero · Tool arrives: `uv build`; the break-my-program session; the hand-off*

> **Outline.** Part level: parts, planned rungs, Contract and the pass criteria are fixed; the rung Checks arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

A command-line application for the library, built the way a junior developer would be expected to build one in their first month: planned against the ways it could be quietly wrong, tested to a number, typed, logged, documented for a stranger, installable, broken on purpose by a peer, and explained twice — to a non-programmer and to a reviewer. Then the hand-off: you open the first brief of the sibling course and tick every item it assumes against the rung here that taught it. If one item does not tick, that is a finding for this course, not for you.

A capstone that concludes, with evidence, that a spreadsheet serves the library better passes on equal terms. The destination is judgment, not volume.

## Contract

**Assumes** (from [stage 9](../09-writing-python-well/README.md)): the typed, tested, formatted package (`s09-r3`–`r5`); measurement (`s09-r6`, `s09-r7`); refactoring under tests (`s09-r8`); code review (`s09-r10`); everything in the *Provides* of stages 1–8.

**Provides** (the exit level; the sibling courses' Stage 0 *Assumes*):
- A failure review written before building, with each quiet failure mapped to a test or a structure (`s10-r1`).
- A package with `pyproject.toml`, a console entry point, and `uv build` producing a wheel (`s10-r2`, `s10-r8`).
- Dataclasses and classes for the domain; JSON persistence to the fixture directory; a pickle memo cache behind a flag with the comparison memo (`s10-r3`).
- `argparse` sub-commands `add`, `lend`, `return`, `report`, `search` with `--help` each (`s10-r4`, `s10-r5`).
- `logging` to stderr and a file; custom exceptions for every user-facing failure; no traceback reaches a user (`s10-r6`).
- Tests ≥ 40, coverage ≥ 90 %, `mypy --strict`, `ruff` (`s10-r7`).
- A README from the project template that a stranger used (`s10-r8`).
- A break-my-program session with findings, tests and a blameless post-mortem (`s10-r9`).
- A teach-back of one concept per tier (`s10-r10`).
- The sibling course's Stage 0 Contract ticked item by item against this course's rungs (`s10-r11`).

Rung IDs: `s10-rM`; hidden case IDs `s10-rMeK-x` run the CLI as a subprocess on the fixture and on the broken files.

## Entry condition

Stage 9 gate passed. A peer for rung 9, or the solo protocol (next day, fresh clone). The sibling course's Stage 0 brief reachable (link in [docs/09](../../docs/09-reading-list.md#stage-10--capstone)).

## Break-lab (first)

Not snippets this time: the [`FAILURE_REVIEW.md`](../../templates/FAILURE_REVIEW.md) template, filled for the program you are about to write, before you write it. Every quiet failure row answered; every function that touches a file or an argument listed with its reach; the ten standard inputs a breaker will try and what you intend each to do.

Question to carry: *what would make this program wrong without telling anyone?*

## Part A — Plan

### Rung 1 — The failure review

*~90 min · feeds s10-r6, s10-r9*

The template, filled. Structure over tests where a structure exists (return new lists; `default_factory`; `encoding` everywhere; JSON not pickle across the boundary). Residual risk stated.

### Rung 2 — Skeleton and `pyproject.toml`

*~60 min · feeds every later rung*

`src/library/` with `cli.py`, `models.py`, `storage.py`, `report.py`, `search.py`, `errors.py`; `[project.scripts] library = "library.cli:main"`; `uv run library --help` works and lists five sub-commands that do nothing yet; `tests/` with one test per sub-command that asserts `--help` exits 0.

## Part B — Build

### Rung 3 — Domain and persistence

*~150 min · feeds s10-r4, s10-r7*

`Book`, `Member`, `Loan` as frozen dataclasses; `Library` as the class that owns them; `storage.py` loads the three fixture files through one function that logs and skips bad lines, and saves to JSON in the data directory; a pickle memo cache for `report` behind `--cache`, with the [comparison memo](../../templates/COMPARISON_MEMO.md) (size, speed, safety, readability; numbers for the first two) and the rule in a comment.

### Rung 4 — Sub-commands

*~120 min · feeds s10-r7*

`add` (a book from arguments), `lend` (member, isbn, date), `return`, `report` (`--as-of`, `--json`, `--plain`); `argparse` sub-parsers; every argument validated with a custom exception and a one-line message; exit codes.

### Rung 5 — `search`

*~60 min · feeds s10-r7*

`search <query> --limit N` against the public API with the offline fallback from stage 6; results as a table; the three fields; a timeout; what the user sees when the network is down (a message, exit 2, not a traceback).

### Rung 6 — Logging and errors

*~60 min · feeds s10-r9*

`logging` to stderr at WARNING and to `library.log` at DEBUG; `--verbose`; every `except` either handles and logs or re-raises as a `LibraryError` with a message a non-programmer could act on; `main()` catches `LibraryError` only, prints the message, exits 1; everything else is a bug and tracebacks (and is a finding in rung 9).

## Part C — Craft

### Rung 7 — Tests, coverage, types

*~120 min · feeds gate*

≥ 40 tests: unit tests on the models and storage, CLI tests through `subprocess` on `tmp_path` copies of the fixture including the four broken files, `monkeypatch` for the API; coverage ≥ 90 % with the gaps named; `mypy --strict` and `ruff` clean; `just craft 10`.

## Part D — Ship

### Rung 8 — README and `uv build`

*~60 min · feeds s10-r9*

The [project README](../../templates/PROJECT_README.md) filled; `uv build` produces `dist/*.whl`; a fresh virtual environment installs the wheel and `library --help` works there; the README's install section is what you just did.

## Part E — Review

### Rung 9 — Break my program, and the post-mortem

*~150 min · feeds gate*

The [protocol](../../docs/10-instructor-guide.md#break-my-program-protocol): a peer, one hour, README and `--help` only; findings in [`BREAK_MY_PROGRAM.md`](../../templates/BREAK_MY_PROGRAM.md); every finding gets a test that fails on the old commit and a fix; the comparison with the failure review (anticipated and prevented / anticipated and not / not anticipated); the [post-mortem](../../templates/POSTMORTEM.md) with the capstone reflections. Solo: the next day, on a fresh clone, reading only the README.

### Rung 10 — Teach-back

*~60 min · feeds gate*

One concept per tier — a traceback, a function, a class, a test — explained to a non-programmer in five minutes each, with a running example and a deliberate mistake read aloud; the reviewer applies the six-dimension rubric to the session.

### Rung 11 — The hand-off

*~45 min · feeds the sibling courses*

Open the sibling course's Stage 0 brief; for every item in its Contract *Assumes*, write "I can do this" with the rung ID here that taught it, or "I cannot" with what is missing. Any "cannot" is filed as stage feedback against this course with the capability map row it belongs to. Then read its first rung and do nothing else: you are ready for it, and that is the point.

## Artefact

`src/library/`, `tests/`, `pyproject.toml`, `README.md`, `dist/*.whl`; `reports/failure-review`, `comparison`, `break-my-program`, `postmortem`; `decisions/ADR-003` (persistence); the hand-off checklist; Artefact Card; PR; tag `capstone-v1`.

## Gate

The universal checklist and the nine [capstone criteria](../../docs/06-assessment-and-gates.md#capstone-criteria), restated with IDs:

- [ ] **s10-g1** Builds and runs: `uv build` wheel; `uv run library --help`; every sub-command has `--help`.
- [ ] **s10-g2** Tested: `just eval 10` ≥ threshold (set at rung-numbering; 90 %); ≥ 40 own tests; coverage ≥ 90 %; `mypy --strict` and `ruff` clean.
- [ ] **s10-g3** Persists: JSON round-trip; the pickle comparison memo with numbers for size and speed.
- [ ] **s10-g4** Handles the outside world: bad lines skipped and logged with line numbers; custom exceptions with actionable messages; no traceback reaches the user in ten minutes of reviewer input.
- [ ] **s10-g5** Failure review written before building; each risk mapped to a test or a structure.
- [ ] **s10-g6** Break-my-program ≥ 1 h, ≥ 1 finding, every finding with a failing-then-passing test; blameless post-mortem naming mechanisms.
- [ ] **s10-g7** Teach-back: one concept per tier, rubric applied to the session.
- [ ] **s10-g8** Hand-off: the sibling course's Stage 0 *Assumes* ticked item by item with rung IDs.
- [ ] **s10-g9** Or: a post-mortem concluding with evidence that a spreadsheet serves the library better, plus the spreadsheet. Passes on equal terms with g1–g8.

## Kill criteria

They are criterion g9. Ask it seriously on day one of the stage: 120 books, 60 members, one librarian. If the honest answer is a spreadsheet, build the spreadsheet, write the post-mortem, and pass. If the answer is the program, the card says why: multiple users, an audit log, the API search, the broken files that a spreadsheet import would silently mangle.

## Stretch

`sqlite3` as the storage backend behind the same `Storage` protocol (one rung's worth; the only database in the course, and only here). A `--format` option. Publishing the wheel to a private index. The Data Science 101 Stage 0 brief, when it exists, ticked the same way.

## Reading

[docs/09 — Stage 10](../../docs/09-reading-list.md#stage-10--capstone).
