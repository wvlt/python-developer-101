# Stage 9 — Writing Python well

*Tier D · ~14 hours · Cost: zero · Tools arrive: `mypy`, `timeit` and the profiler, coverage, `ruff format`*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

There is a difference between a program that works and one a colleague will accept into a shared codebase, and the difference is measurable: does the type checker pass, what does coverage say, how long does it take, can a stranger read it. This stage attaches a number to every claim you are tempted to make with an adjective, and then spends its second half on the skill junior developers are least prepared for: reading code you did not write — a standard-library module, a 200-line script that needs refactoring, a stranger's pull request — and saying what it does and where it breaks.

## Contract

**Assumes** (from [stage 8](../08-design-and-the-data-model/README.md)): inheritance, protocols, composition (`s08-r1`–`r3`); the data model and iteration (`s08-r4`–`r7`); context managers as author (`s08-r8`); the library package with tests and two ADRs (`s08-r9`); `logging` (`s05-r10`); your own tests with fixtures (`s06-r8`, `s06-r9`).

**Provides** (stage 10 takes these for granted):
- `ruff format` and PEP 8 as a habit; the idioms: EAFP vs LBYL, unpacking, `enumerate`/`zip` over indices, comprehensions vs loops, the walrus, `with` for every resource (`s09-r1`, `s09-r2`).
- Typing in depth: `X | None`, generics (`list[Book]`, `dict[str, int]`), `TypedDict`, `Protocol`, `Callable`; `mypy --strict` clean on the package (`s09-r3`).
- Testing in depth: fixtures with scope, `parametrize` with ids, `tmp_path`, `monkeypatch` for the environment and the API, coverage measured and read (`s09-r4`, `s09-r5`).
- `timeit` and `cProfile`; list vs set vs dict lookup measured; generators vs lists; string building; big-O intuition from measurements, not from a table (`s09-r6`, `s09-r7`).
- A 200-line script refactored into modules and classes, tests first (`s09-r8`).
- A code-reading memo on a standard-library module and a review of a stranger's pull request (`s09-r9`, `s09-r10`).
- Twelve planted bugs in a provided package found, classified and fixed with a test each (`s09-r11`).

Rung IDs: `s09-rM`; hidden case IDs `s09-rMeK-x`. The stage's measure is the planted-bug hunt (≥ 10 of 12), `mypy`, `ruff` and coverage, not a hidden stdout set.

## Entry condition

Stage 8 gate passed; `uv sync --extra dev` has `mypy` and `pytest-cov`; the stranger's PR branch exists in upstream (fixture, see `REVISIONS.md`).

## Break-lab (first)

Seven snippets. Targets: a type hint lying (`def f(x: int)` called with a string, runs fine); a test with 100 % coverage that asserts nothing; `"".join` vs `+=` in a loop timed; `x in list` vs `x in set` timed at 10 000; a `try` around twenty lines; `ruff format` changing nothing semantically but 40 lines; a `global` that a refactor broke.

Question to carry: *what is the number behind this claim?*

## Part A — Style and idiom

### Rung 1 — `ruff format` and PEP 8

*~40 min · feeds every later rung*

`ruff format` on the package; what changed and what did not; the few PEP 8 rules a formatter cannot apply (names, docstrings, comments); pre-commit (stretch) to run both on every commit. Exercise: format the package; commit the diff alone.

### Rung 2 — Idioms

*~60 min · feeds s09-r8, s10*

EAFP (`try: d[k] except KeyError`) vs LBYL (`if k in d`); unpacking over indexing; `enumerate`/`zip` over `range(len())`; comprehensions where they read better and loops where they do not; the walrus in a `while` reading loop; `with` for every file, lock and connection. Exercises: ten before/after rewrites with a test each.

## Part B — Types

### Rung 3 — Typing in depth and `mypy --strict`

*~80 min · feeds s10*

`X | None` and the `None` check `mypy` forces; `list[Book]`; `TypedDict` for the JSON shape; `Protocol` from stage 8 now checked; `Callable`; `TypeVar` once; `# type: ignore` with a reason, rarely; `mypy --strict` on the package until clean. Exercise: the package, typed.

## Part C — Tests in depth

### Rung 4 — Fixtures, `parametrize`, `tmp_path`, `monkeypatch`

*~60 min · feeds s10*

Fixture scope; `parametrize` with `ids=`; `monkeypatch.setenv("LIBRARY_OFFLINE", "1")`; `monkeypatch.setattr` to replace the HTTP call; `pytest.raises(match=)`; `caplog` for the log lines. Exercises: test the `search` sub-command offline; test the log.

### Rung 5 — Coverage

*~40 min · feeds s10*

`pytest --cov=library --cov-report=term-missing`; reading the missing lines; writing the test for an uncovered branch; why 100 % is not the target and what 90 % means. Exercise: the package to ≥ 90 %.

## Part D — Measure

### Rung 6 — `timeit` and the profiler

*~60 min · feeds s09-r7, s10*

`timeit` at the prompt and as a module; repeats and the spread; `cProfile` on the report command and reading the top ten by cumulative time; `@timed` from stage 4 revisited. Exercise: three before/after measurements on the package with the numbers in the journal.

### Rung 7 — Choosing structures with numbers

*~50 min · feeds s10*

`in` on list vs set vs dict at 1 000, 10 000, 100 000; generator vs list memory (stage 8) and time; `"".join` vs `+=`; `sorted` once vs `min` in a loop; the big-O words attached to the curves you measured. Exercise: a table in the journal.

## Part E — Refactor

### Rung 8 — The 200-line script

*~90 min · feeds s10*

A provided 200-line script that works and is unreadable (one function, globals, repeated code, bare `except`); characterisation tests first (capture its current output on the fixture); then extract functions, then modules, then one class, keeping the tests green at every step; `ruff` and `mypy` clean at the end; diff size per step recorded. Exercise: the refactor.

## Part F — Read

### Rung 9 — A standard-library module

*~60 min · feeds s10*

`statistics.py` in the editor with the debugger attached: public functions and what each returns; one place it would break on bad input and the input; one idiom learned; the [code-reading memo](../../docs/14-rubrics.md#artefact-rubrics) in under a page. Exercise: the memo.

### Rung 10 — A stranger's pull request

*~60 min · feeds s10 (break-my-program)*

The fixture PR in upstream: read the diff, run its tests, find the bug it introduces and the test it should have added; write the review as comments on the PR in your fork; the three questions a reviewer always asks (what does it do, what does it break, what is not tested). Exercise: the review.

## Part G — The planted-bug hunt

### Rung 11 — Mini-project: twelve bugs

*~120 min · feeds gate s09-g1–g5; s10*

A provided package with twelve planted bugs drawn from the quiet-failures list and the loud classics; for each: locate (tool recorded), classify (bestiary ID), test (fails before, passes after), fix, commit; the [error-analysis report](../../templates/ERROR_ANALYSIS.md) with time per bug and the slowest bug analysed.

## Artefact

The typed, formatted, covered package; `reports/error-analysis-<date>.md`; the code-reading memo; the PR review; the refactored script with its characterisation tests; journal with the measurement tables; Artefact Card; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s09-g1** ≥ 10 of 12 planted bugs found and fixed, each with a test that fails on the old code (`just eval 09` applies the tests to the original and the fixed package).
- [ ] **s09-g2** `mypy --strict` clean on `src/`; `ruff check` and `ruff format --check` clean.
- [ ] **s09-g3** Coverage ≥ 90 % on `src/`, with the uncovered lines named in the card and a reason each.
- [ ] **s09-g4** Three `timeit` comparisons with before/after numbers and the spread; no adjective without one.
- [ ] **s09-g5** The code-reading memo and the PR review pass the artefact rubric; two Say questions from rungs 2 and 6.

## Kill criteria

Do not optimise what you have not measured; do not measure what does not matter (the report runs in 40 ms; the user takes 2 s to read it). Do not type-annotate a ten-line script. Do not refactor working code without a characterisation test. Do not add a test that cannot fail.

## Stretch

`threading` and `asyncio` as vocabulary: read one page on each and write three sentences on when the course's programs would need them (they do not). Pre-commit installed and the hooks run. `python -X importtime`.

## Reading

[docs/09 — Stage 9](../../docs/09-reading-list.md#stage-9--writing-python-well).
