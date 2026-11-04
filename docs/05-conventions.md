# 05 — Conventions

Conventions exist so that any stage, in any learner's fork, can be read, run and reviewed by someone who has never seen it. Follow them exactly; deviate only with an ADR.

## Repository layout

```
python-developer-101/
├── README.md
├── AGENTS.md                  # instructions for AI coding assistants working in this repo
├── CONTEXT.md                 # learner, destination, stage/rung model, feedback flow
├── PINS.md                    # pinned versions, links, the public API, the fixture
├── PROGRESS.md                # the learner's rung log (one row per rung; Run/See/Say)
├── LEDGER.md                  # hours per stage, actual vs budget
├── BOARD.md                   # rendered: outline, progress, maintainer view
├── CHANGELOG.md               # curriculum changes (upstream)
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml             # one project; the dev toolchain as an extra
├── justfile                   # test / eval / break / trace / check / board / site
├── conftest.py                # pytest plumbing: stage_dir, run_exercise, data_dir
├── course/                    # runner.py (subprocess exercise runner), tracer.py (just trace)
├── data/                      # build_files.py; generated output in data/library/ (gitignored)
├── scripts/                   # render_board.py, check_links.py, check_pins.py, eval.py, make_progress.py
├── site/                      # the course player
├── status/board.json          # stage-level state and the Now/Next strip
├── docs/                      # the curriculum
├── templates/                 # documents you copy into stage directories
└── stages/
    ├── 00-hello-python/           # on-ramp; README and REVISIONS only
    ├── 01-values-and-names/
    ├── 02-decisions-and-repetition/
    ├── 03-collections/
    ├── 04-functions/
    ├── 05-errors-and-files/
    ├── 06-modules-and-tooling/
    ├── 07-classes-and-objects/
    ├── 08-design-and-the-data-model/
    ├── 09-writing-python-well/
    └── 10-capstone/
```

## Stage directory layout

Every gated stage directory (1–10) has the same shape. Stage 0 is exempt: it is a README, a REVISIONS log and a scratch folder the learner makes themselves. Tooling arrives progressively per the [tooling ramp](02-getting-started.md#tooling-ramp); a tool not yet introduced is not a gate failure.

```
stages/NN-kebab-name/
├── README.md              # the brief (upstream; do not edit in your fork — add to NOTES.md instead)
├── REVISIONS.md           # upstream: rung-level change log and contract cascade notes
├── NOTES.md               # your notes on the brief, deviations, questions
├── JOURNAL.md             # dated lab-notebook entries; break-lab predictions first
├── ARTIFACT_CARD.md       # filled from templates/ARTIFACT_CARD.md for the mini-project (stage 1 onward)
├── breaklab/              # upstream: predict-then-run snippets, NN_name.py; `just break NN`
├── exercises/             # upstream stubs that YOU fill in, in place; rMeK_name.py
├── tests/                 # upstream: visible tests; `just test NN`
├── eval/                  # upstream: hidden tests and threshold.json; `just eval NN` writes eval/runs/<ts>-<sha>/summary.json
├── solutions/             # upstream: reference solutions; open only after the rung's Check
├── src/                   # stage 6 onward: your package (the mini-project)
└── decisions/             # ADRs, stage 7 onward when a design choice was made
```

## Naming

### Stages and rungs

`NN-kebab-name`, two-digit, zero-padded. Referred to in prose as "stage 3" and in identifiers as `s03`.

Rungs: `sNN-rM`, where M is the rung number in the brief. Insertions take a letter suffix (`s02-r4b`) so existing references stay valid; renumbering happens only at a major curriculum version. Rung headings in briefs are exactly `## Part X — title` and `### Rung N — title`; the course player and `BOARD.md` are parsed from them.

### Exercises and cases

- Exercise file: `exercises/rMeK_short_name.py` — rung M, exercise K. The name is the same in `solutions/`.
- Planted-bug exercise: `exercises/rMbK_short_name.py` (b for bug). The file contains working-looking code with one bug; the task is to find and fix it.
- Visible test id: `rMeK_short_name` (pytest parametrize id).
- Hidden case id: `sNN-rMeK-x`, where x is a letter: `s01-r4e3-b` is stage 1, rung 4, exercise 3, case b. Stable forever; a retired case keeps its id and is marked in the table.
- Mini-project exercise: `rMe1_project_name.py` where M is the last rung; from stage 6 the mini-project is `src/`.

### Break-lab snippets

`breaklab/NN_short_name.py`, two-digit order. Each is self-contained, under 12 lines, and prints something whose value the learner must predict first. A snippet that raises on purpose says so in a comment at the top.

### Exercise file shape (stages 1–3)

```python
# r4e3 — the last character
# Read one word. Print its last character.
# Example: input "python" -> prints "n"
word = input()
# --- your code below this line ---
```

The lines above the marker are given; everything below is the learner's. Tests detect an empty body and say so.

### Exercise file shape (stage 4 onward)

```python
def last_character(word: str) -> str:
    """Return the last character of word. word is never empty."""
    ...
```

### Python packages and modules (stage 6 onward)

- Package per stage mini-project in `src/`, named for the thing, not the stage: `library/`.
- Standard module names, so reviewers know where to look: `catalogue.py` (books), `members.py`, `loans.py`, `report.py`, `storage.py` (files), `cli.py` (entry point), `errors.py` (custom exceptions).
- snake_case for functions and variables, PascalCase for classes, UPPER_SNAKE for constants, `_leading_underscore` for "not for use outside this module". `ruff` enforces the rest.

### Decision records

`decisions/ADR-NNN-short-title.md` from [the template](../templates/ADR.md). Required from stage 7 whenever you choose: class vs dataclass vs dict, inheritance vs composition, JSON vs pickle, loop vs comprehension vs generator for a hot path, or to deviate from a convention.

### Reports

`reports/<kind>-<date>.md` where kind is one of `error-analysis`, `comparison`, `failure-review`, `break-my-program`, `postmortem`, `reading`.

## Git

### Branches

- `main` holds passed stages only (from stage 2, when GitHub arrives; stage 1 commits straight to `main` in the clone).
- `stage/NN-name` is where a stage is worked. One branch per stage; merge on gate pass.

### Commits

Conventional-commit style with the stage as scope. Say what changed, in the imperative:

```
feat(s02): r5 range exercises pass visible tests
fix(s03): r4e2 aliasing — copy the list before sorting
test(s06): add parametrised tests for overdue()
break(s04): journal the mutable-default break-lab
docs(s07): ADR-001 dataclass for Book, class for Library
```

`break` is course-specific: it documents a break-lab and should never be squashed away; it is the evidence of learning. A commit message that says `update` or `fix stuff` is a convention violation and the reviewer will say so.

### Tags

`sNN-passed` on the merge commit of each stage. `capstone-v1` on the capstone.

### Pull requests

From stage 2: one PR per stage from `stage/NN-name` to `main`, using `.github/PULL_REQUEST_TEMPLATE.md`. The PR body links the Artefact Card and the eval run directory and walks the gate checklist. Self-review the next day if solo.

## Code standards

- `ruff check` clean from stage 2; `ruff format` from stage 9; `mypy --strict` on stage 9 and 10 `src/`.
- Type hints on every function signature from stage 4. Docstrings on every function from stage 4: one line saying what it returns, not how.
- No bare `except:`. Catch the specific exception; if you must catch broadly, log it and re-raise or return a value the caller can see.
- `with` for every file. `encoding="utf-8"` on every text open.
- No `eval()`. No `pickle.load` of anything you did not write yourself in this program.
- Names say what the thing is: `overdue_loans`, not `ol` or `data2`. Do not shadow built-ins (`list`, `dict`, `input`, `id`, `sum`).
- A function that mutates its argument says so in its name or docstring; prefer returning a new value.
- Comments explain intent, not syntax: `# skip the header line` yes; `# loop over lines` no.

## Documentation standards

- One idea per heading. Numbers over adjectives. If you write "better", "faster", "cleaner", attach the number (test count, seconds, lines) and the comparison.
- Reports open with a three-line summary: what was measured, what was found, what was changed.
- Dates in ISO 8601. British/Australian spelling. No emojis in briefs.

## Standard commands

Every stage supports the same `just` targets:

```
just test NN     # visible tests for a stage
just eval NN     # hidden tests; writes eval/runs/<ts>-<sha>/summary.json; prints the verdict
just break NN    # run the break-lab snippets (predict first)
just trace FILE  # run a file and print every line as it executes
just check NN    # ruff check on your exercises (stage 2 onward)
just craft NN    # stage 9 onward: mypy and coverage
just data        # rebuild the fixture
just board       # re-render BOARD.md, the README block and site/data.json
just site        # the course player at http://localhost:8000/site/
```

If a target does not apply to a stage, it prints why and exits 0.
