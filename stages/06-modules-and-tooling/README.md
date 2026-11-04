# Stage 6 — Modules, packages and tooling

*Tier B · ~12 hours · Cost: zero · Tools arrive: `uv add`, `pyproject.toml`, writing your own `pytest` tests; the public API (no key)*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

Most of the code in any program you will work on was written by someone else: the standard library, a package, a colleague's module. This stage is about reaching it — `import`, the stdlib tour, `uv add` — and about the moment the course stops writing your tests. From rung 8 you write them, and the planted-bug check measures whether they catch anything: a test suite that passes on buggy code is the quietest failure of all.

## Contract

**Assumes** (from [stage 5](../05-errors-and-files/README.md)): exceptions and custom exceptions (`s05-r1`, `s05-r2`); files, CSV, JSON (`s05-r4`–`r6`); dates (`s05-r8`); `argparse` and environment variables (`s05-r9`); `logging` (`s05-r10`); the loans report (`s05-r11`).

**Provides** (stage 7 takes these for granted):
- `import x`, `from x import y`, `import x as z`; `__name__ == "__main__"`; a module of your own; a package with `__init__.py` and relative imports (`s06-r1`, `s06-r2`).
- Working knowledge of `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`), `itertools` (`chain`, `product`, `groupby`, `islice`), `functools` (`partial`, `reduce`, `lru_cache`), `re` basics, `os`/`shutil`/`time`; and the habit of looking there first (`s06-r3`, `s06-r4`).
- Virtual environments explained; `uv add`; `pyproject.toml` dependencies; `uv sync` reproducing an environment (`s06-r5`).
- The HTTP client against the public API named in `PINS.md`, with a timeout, status check, JSON parse, and an offline fallback to the recorded sample (`s06-r6`).
- The terminal-output library for a table; reading a package's documentation to find the one function you need (`s06-r7`).
- Your own `pytest` tests: `assert`, `parametrize`, fixtures, `tmp_path`; a test written before the fix (`s06-r8`, `s06-r9`).
- The loans report as an installed package with your tests (`s06-r10`).

Rung IDs: `s06-rM`; hidden case IDs `s06-rMeK-x`. From this stage the mini-project lives in `src/` and the learner's tests in `tests/`; the hidden set includes the mutation check (how many of the learner's tests fail when the planted bug is applied).

## Entry condition

Stage 5 gate passed; the loans report runs; `data/library/openlibrary_sample.json` exists (built by `just data`).

## Break-lab (first)

Seven snippets. Targets: a file named `random.py` shadowing the module; `from x import *` hiding a name; a mutable module-level list changed by an importer (aliasing across files, [C01](../../docs/07-failure-bestiary.md#c--collections)); `import` of a package without `__init__.py` behaving differently; `requests.get` without a timeout (read, not run); a test with no `assert` passing; a test that asserts the wrong thing and passes on the planted bug.

Question to carry: *what does a passing test prove?*

## Part A — Modules

### Rung 1 — `import`, and a module of your own

*~50 min · feeds every later rung*

The three import forms; where Python looks; `__name__ == "__main__"`; moving the report's helpers into `library_io.py` and importing them. Exercises: a module with three functions and a script that uses it.

### Rung 2 — A package

*~50 min · feeds s06-r10, s07, s10*

`src/library/__init__.py`, `catalogue.py`, `loans.py`, `cli.py`; relative imports; `uv run python -m library.cli`. Exercise: the report as a package skeleton.

## Part B — The standard-library tour

### Rung 3 — `collections`, `itertools`, `functools`

*~70 min · feeds s06-r10, s09*

`Counter` replacing rung 7 of stage 3; `defaultdict(list)` replacing `setdefault`; `deque` for a queue; `namedtuple` as a preview of stage 7; `chain`, `product`, `groupby` (sorted first), `islice`; `partial`, `reduce`, `lru_cache` on the slow question. Each shown beside the hand-written version it replaces, with the line count. Exercises: five replacements.

### Rung 4 — `re`, `os`, `shutil`, `time`, and the rest

*~50 min · feeds s09, s10*

`re.search`, `findall`, `sub`, groups, on the messy loans lines; `os.environ`, `shutil.copy`, `time.perf_counter`; how to read the library index and the "Brief Tour". Exercises: parse the loan line with one regular expression; back up a file before writing.

## Part C — Packages

### Rung 5 — Virtual environments, `uv add`, `pyproject.toml`

*~45 min · feeds s06-r6, s10*

What `.venv` is and why `uv run` works; `uv add` writes `pyproject.toml` and `uv.lock`; `uv sync` on a fresh clone; never `pip install` into the system Python. Exercise: add the two packages the course uses.

### Rung 6 — The public API

*~70 min · feeds s10 (`search`)*

`urllib.request` first, for what it costs; then the HTTP client: `get` with `timeout=`, `raise_for_status`, `.json()`, the three fields the brief reads, a descriptive `User-Agent`; `LIBRARY_OFFLINE=1` switches to the recorded sample so tests run without a network. Exercises: `search_books(query, limit)` with the fallback.

### Rung 7 — A table on the terminal

*~40 min · feeds s10*

Find the one function in the terminal-output library's documentation that prints a table; use it for the overdue report; `--plain` falls back to f-strings. Exercise: `print_table(rows)`.

## Part D — Your own tests

### Rung 8 — Writing tests

*~70 min · feeds every later stage*

`tests/test_loans.py`; `assert`; one test per behaviour; names that say what is tested; `pytest.mark.parametrize` for tables; `pytest.raises` for the custom exceptions. Target: 15 tests on the package. Exercise: the tests.

### Rung 9 — Fixtures, `tmp_path`, and the planted bug

*~60 min · feeds s09-r4, s10*

A fixture that copies the library files into `tmp_path`; a test that writes and reads back; then `just eval 06` applies a planted bug to a copy of your package and counts how many of your tests fail. Under 12 of 15 means the tests assert too little; fix the tests, not the number. Exercise: raise the count.

## Part E — The library package

### Rung 10 — Mini-project: the library package

*~110 min · feeds gate s06-g1–g3; s07-r9, s10*

The stage 5 report as `src/library/` with `cli.py` (`report`, `search` sub-commands), the learner's tests, `pyproject.toml` with the two dependencies, `ruff` clean, `README.md` from the project template, one stdlib function replacing hand-written code and named in the card.

## Artefact

Package in `src/`; ≥ 15 tests in `tests/`; `pyproject.toml`; README; Artefact Card with the mutation count; eval run; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s06-g1** `just eval 06` ≥ 45 of 50 hidden cases (count confirmed at rung-numbering; 90 %).
- [ ] **s06-g2** ≥ 15 learner-written tests, of which ≥ 12 fail under the planted bug (the eval prints both numbers).
- [ ] **s06-g3** One standard-library function replacing hand-written code, named in the card with the lines saved; the `search` sub-command works online and with `LIBRARY_OFFLINE=1`.
- [ ] **s06-g4** Three Say questions from rungs 1, 5 and 9.

## Kill criteria

Before writing a function, search the standard library index for its name. Before adding a package, ask whether the stdlib does 80 % of it. Before writing a test, ask what bug it would catch; if none, do not write it.

## Stretch

`functools.cache` vs `lru_cache(maxsize=…)` measured; `itertools.pairwise` on the loans by date; `python -m json.tool`; a second API query the brief did not ask for.

## Reading

[docs/09 — Stage 6](../../docs/09-reading-list.md#stage-6--modules-packages-and-tooling).
