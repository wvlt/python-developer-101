# 12 — Capability map

The destination in [CONTEXT.md](../CONTEXT.md) broken into competencies, each traced to the stage and rung that first teaches it, the stage that deepens it, and the gate that proves it. **GAP** marks a competency the curriculum does not yet deliver; **PARTIAL** marks one that is taught but not gated or not practised on a realistic input. Gaps are the revision backlog, in priority order at the bottom.

Rung references use `sNN-rM`. Stages 3–10 are not yet rung-numbered (see rolling readiness in CONTEXT.md); their references are to the brief's build part (`s05 B`) as planned in [docs/17](17-focus-map.md), and will be replaced by rung IDs when each stage is numbered.

The second half of this document traces the **topic ladder** from the course inputs, so that every named topic appears exactly once as "first taught".

## 1. Read and write idiomatic Python

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Values, types, names, conversions | s01-r1, r2, r3 | s03 | s01-g1 | ok |
| Strings: indexing, slicing, methods, f-strings | s01-r4, r5, r6 | s05 (encoding) | s01-g1, g4 | ok |
| Comparisons, booleans, truthiness, `None`, `is` vs `==` | s01-r7 | s03 B (aliasing) | s01-g2 | ok |
| Conditionals including `match` | s02-r1, r2, r3 | s07 (match on class) | s02-g1 | ok |
| Loops: `while`, `for`/`range`, `break`/`continue`/`else`, `enumerate`/`zip` | s02-r4–r8 | s03, s08 C | s02-g1, g4 | ok |
| Lists, tuples, dicts, sets; choosing between them | s03 A, C, D, E | s07 (objects in collections) | s03 gate | ok |
| `sorted()` with `key`, stability; `lambda` | s03 A; s04 D | s09 D | s03, s04 gates | ok |
| Comprehensions | s03 D | s04 D (vs `map`/`filter`), s09 A | s03 gate | ok |
| Functions: parameters, defaults, `*args`/`**kwargs`, return | s04 A | s06, s09 | s04 gate | ok |
| Scope and LEGB | s04 B | s04 D (closures) | s04 gate | ok |
| Closures and a first decorator | s04 D | s09 D (timing decorator) | s04 gate | ok |
| Classes, `__init__`, methods, `__repr__` | s07 A | s08 | s07 gate | ok |
| Properties, classmethods, equality and hashing | s07 B, C | s08 B | s07 gate | ok |
| Dataclasses and `Enum` | s07 D | s10 | s07 gate | ok |
| Inheritance, `super()`, composition, `Protocol` | s08 A | s10 | s08 gate | ok |
| The data model: `__len__`, `__getitem__`, `__iter__`, operators | s08 B, C | s10 | s08 gate | ok |
| Generators and lazy pipelines | s08 C | s09 D (memory) | s08 gate | ok |
| Context managers as users; as authors | s05 B; s08 D | s10 | s05, s08 gates | ok |
| Type hints: basic; in depth | s04 C; s09 B | s10 (`mypy --strict`) | s09, s10 gates | ok |
| Idioms: EAFP, unpacking, walrus, `with` for every resource | s09 A | s10 | s09 gate | ok |

## 2. Turn a task into a command-line program

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| A program that reads input and prints output | s00-r6; s01-r9 | every mini-project | s01-g4 | ok |
| Input validation loops | s02-r4 | s05 A (exceptions) | s02-g3 | ok |
| Modules and a package | s06 A | s09 E, s10 | s06 gate | ok |
| Persistence: text, CSV, JSON | s05 B | s10 B | s05 gate, s10 criterion 3 | ok |
| `pickle`: what it is, when, and why not for untrusted data | s05 B | s10 (comparison memo) | s05 gate (Say) | ok |
| Error handling that neither crashes nor hides | s05 A | s10 B | s05 gate, s10 criterion 4 | ok |
| Custom exceptions with actionable messages | s05 A | s08 (exceptions as classes), s10 | s10 criterion 4 | ok |
| `argparse` with sub-commands and `--help` | s05 C | s10 B | s10 criterion 1 | ok |
| Environment variables and `.env`-style configuration | s05 C | s10 | — | PARTIAL: taught, not gated before s10 |
| `logging` with levels and a logger per module | s05 D | s09 C, s10 | s05 gate, s10 criterion 4 | ok |
| Dates and durations (`datetime`, `timedelta`) | s05 C | s10 (overdue) | s05 hidden cases | ok |
| A README a stranger can use | s10 D | — | s10 criterion 1 | ok |
| `pyproject.toml`, `uv build` | s06 C; s10 D | — | s10 criterion 1 | ok |

## 3. Test it

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Run tests; read a failing test | s01-r0 | every stage | every gate | ok |
| Understand what a test asserts and what it does not prove | s01-r0, r9 (Say) | s06 D (planted bug) | s06-g2 | ok |
| Write tests: `assert`, `parametrize`, fixtures | s06 D | s09 C | s06 gate (≥ 15 tests, ≥ 12 catch the planted bug) | ok |
| `tmp_path` and `monkeypatch` | s09 C | s10 | s09 gate | ok |
| Coverage: measure and interpret | s09 C | s10 | s09, s10 (≥ 90 %) | ok |
| Write the test first for a bug | s06 D | s09 G, s10 E | s09 gate (test per planted bug) | ok |

## 4. Read a traceback and fix the bug, including the quiet ones

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Read a traceback bottom-up; fix the named line | s00-r5 | every stage | s01 Say | ok |
| Long tracebacks through several calls | s05 A | s09 | s05 gate | ok |
| Aliasing (C01) | s03 B | s04 (mutable default), s07 (class attribute) | s03 gate (Say) | ok |
| Mutable default (N02) | s04 A | s07 D (`default_factory`) | s04 gate (Say) | ok |
| `is` vs `==` (T05) | s01-r7 | s03 B | s01-g2 | ok |
| Float precision (T04) | s01-r1 break-lab | s09 (`decimal`) | s01 hidden case | ok |
| Integer vs true division (T03) | s01-r1 | — | s01 hidden case | ok |
| Off-by-one (F01) | s02-r5 | s03 (slices) | s02 hidden cases | ok |
| Shadowing built-ins (F04) | s02-r9 (`ruff`) | s04 B | s02-g2 | ok |
| Swallowed exceptions (E01) | s05 A | s09 | s05 gate | ok |
| Late-binding closures (N04) | s04 D | — | s04 hidden case | ok |
| Mutating while iterating (F05) | s03 B | — | s03 hidden case | ok |
| Encoding (E02) | s05 B | s10 | s05 gate (broken files) | ok |
| `pickle` untrusted / `eval` (E06, E07) | s05 B | s10 | s05 Say | ok |
| Planted-bug find-and-fix with a test | s02-r11 (first planted bug) | s06 D, s09 G | s09 gate (≥ 10/12) | ok |
| Failure review before building | s10 A | — | s10 criterion 5 | ok |

## 5. See inside a running program

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| `print` as a tool | s00-r3 | — | — | ok |
| f-string debugging (`f"{x=}"`) | s01-r6 | every stage | s01-g1 | ok |
| `just trace`: watch every line execute | s01-r3 | s02 | — | ok |
| `breakpoint()` and the terminal debugger | s04 F | s09 | s04 gate (journaled session) | ok |
| The editor's debugger: breakpoints, step, watch | s04 F | s09 | s04 gate | ok |
| `logging` instead of print | s05 D | s09 C | s05 gate | ok |
| `timeit` and the profiler | s09 D | s10 memo | s09 gate (3 comparisons) | ok |
| The habit: never ship a program you cannot see inside | s01 (Oath) | every Artefact Card "how it fails" | u2 | ok |

## 6. Standard library first, package second, own code last

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Know the stdlib exists and how to find things in it | s03 (`collections` in reading) | s06 B (tour) | s06 gate (one stdlib replacement) | ok |
| `csv`, `json`, `pathlib`, `datetime`, `argparse`, `logging` | s05 | s10 | s05 gate | ok |
| `collections`, `itertools`, `functools`, `re` | s06 B | s09 | s06 hidden cases | ok |
| Add a package with `uv add`; read its documentation | s06 C | s10 | s06 gate | ok |
| Call a public HTTP API | s06 C | s10 (search sub-command) | s06 gate | ok |
| Decide: stdlib / package / write it | s06 (kill criteria) | s09, s10 | s06 card | ok |

## 7. Use the professional toolchain daily

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Terminal: navigate, run, read output | s00-r0, r2 | every stage | — | ok |
| Editor: open folder, run, see problems | s00-r2 | s04 (debugger) | — | ok |
| `uv run`, `uv sync` | s01-r0 | s06 (`uv add`) | — | ok |
| `just test` / `just eval` | s01-r0 | every stage | every gate | ok |
| git: init, add, commit, log | s01-r8 | s02 | s01-g3 (≥ 5 commits) | ok |
| GitHub: fork, push, branch, pull request | s02-r10 | every stage from 2 | s02-g3 | ok |
| `ruff check`; `ruff format` | s02-r9; s09 A | every stage | u7 | ok |
| `pytest` as runner; as author | s01-r0; s06 D | s09 | s06 gate | ok |
| `mypy` | s09 B | s10 | s09, s10 | ok |
| Virtual environments explained | s06 C | — | — | ok |
| Pre-commit hooks | s09 A | s10 | — | PARTIAL: configured in repo, taught only as stretch |

## 8. Read other people's code

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Predict what a snippet prints before running it | s00 break-lab | every break-lab | journal (u3) | ok |
| Read a planted-bug exercise and find the fault | s02-r11 | s06, s09 | s09 gate | ok |
| Read a 200-line script and refactor it | s09 E | s10 | s09 gate | ok |
| Read a standard-library module | s09 F | — | s09 gate (memo) | ok |
| Review a stranger's pull request | s09 F | s10 (break-my-program) | s09 gate | ok |
| Explain what code does and where it would break | s09 F | s10 E | s09, s10 criterion 7 | ok |

## 9. Know when not to write code

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| The stdlib already does it | s03 (`sorted`, `Counter`) | s06 | s06 gate | ok |
| A shell one-liner does it | s05 (kill criteria) | s09 | s05 card | ok |
| A spreadsheet does it | s03 (kill criteria) | s10 criterion 9 | s03 card | ok |
| The task is one-off | s04 (kill criteria) | s10 | s04 card | ok |
| Not every record needs a class | s07 (kill criteria) | s08 | s07 gate (Say) | ok |
| Not every slow thing needs optimising | s09 D | — | s09 gate (`timeit` before/after) | ok |

## 10. Explain the program

| Competency | First taught | Deepened | Gated | Status |
|---|---|---|---|---|
| Say what a rung taught, without notes | s00 (Say checks) | every rung | every gate (3 Say questions) | ok |
| Artefact Card: what, how tested, how it fails, decisions | s01-r9 | every mini-project | u2 | ok |
| Commit messages that say what changed | s01-r8 | every stage | u6 | ok |
| ADR for a design choice | s07 | s08, s10 | s07, s08 gates | ok |
| Comparison memo with numbers | s08 A | s10 (JSON vs pickle) | s08 gate | ok |
| Post-mortem, blameless, mechanisms | s10 E | — | s10 criterion 6 | ok |
| Teach-back to a non-programmer | s10 E | — | s10 criterion 7 | ok |
| Five-sentence summary for a non-engineer | s01-r9 (card) | s10 README | u2 | ok |
| Hand-off: tick the sibling course's *Assumes* | s10 E | — | s10 criterion 8 | ok |

## The topic ladder, traced

Every topic from the course inputs, where it is first taught. ★ marks the owner-named placements, each of which appears here exactly once as a first teaching.

| Topic | First taught |
|---|---|
| Install Python and the editor; terminal; REPL; `print`; a `.py` file; errors on purpose; `input()`; a comment | s00-r0–r7 |
| `int`, `float`, `bool`, `str`, `None`; arithmetic, precedence, `/` vs `//`, `%`, `**` | s01-r1 |
| `type()` and conversions | s01-r2 |
| Variables, assignment, naming rules, augmented assignment | s01-r3 |
| Strings: quotes, escapes, multi-line, `len`, indexing, slicing, immutability | s01-r4 |
| String methods | s01-r5 |
| f-strings and format specs; `f"{x=}"` | s01-r6 |
| Comparison operators, `and`/`or`/`not`, truthiness, `is` vs `==` (first contact) | s01-r7 |
| `if`/`elif`/`else`; nesting; conditional expression | s02-r1, r2 |
| `match`/`case` | s02-r3 |
| `while`; input-validation loops | s02-r4 |
| `for` and `range` (start/stop/step, half-open) | s02-r5 |
| `break`, `continue`, `pass`, `else` on loops | s02-r6 |
| `enumerate`; `zip` ★ | s02-r7 |
| Nested loops; accumulator and flag patterns | s02-r8 |
| Lists and their methods | s03 A |
| `sorted()` ★ with `key`/`reverse`, `sort` vs `sorted`, stability; `lambda` ★ (introduced) | s03 A |
| `min`/`max`/`sum`/`any`/`all`; `in` | s03 A |
| Mutability, aliasing, copying; shallow vs deep | s03 B |
| Tuples and unpacking (swap, `*rest`) | s03 C |
| Dicts: `[]` vs `get`, `setdefault`, views, iteration, nesting, order | s03 C |
| Sets and set operations | s03 D |
| List/dict/set comprehensions with conditions | s03 D |
| Nested data (a list of dicts); `del`; choosing the collection | s03 C, E |
| `def`, parameters, `return`; positional vs keyword, defaults; `*args`/`**kwargs` | s04 A |
| The mutable-default trap | s04 A |
| Scope and LEGB; `global`/`nonlocal` | s04 B |
| Docstrings; type hints (basic); pure functions vs side effects | s04 C |
| Functions as values; `lambda` ★ deepened; `map`/`filter` vs comprehensions; multi-key `sorted` | s04 D |
| Closures; a first decorator (timing) | s04 D |
| Recursion and when not to | s04 E |
| The debugger: `breakpoint()`, step, inspect; the editor's debugger | s04 F |
| `try`/`except`/`else`/`finally`; specific types; `raise`; re-raise; custom exceptions; the hierarchy; `assert` | s05 A |
| Reading long tracebacks | s05 A |
| `with` and context managers ★ (as users); `pathlib`; text modes, `encoding`, newlines | s05 B |
| `csv`; `json` | s05 B |
| `pickle` ★: what, when, why never untrusted; JSON vs pickle | s05 B |
| `datetime` and `timedelta` | s05 C |
| `sys.argv` then `argparse`; environment variables | s05 C |
| `logging` | s05 D |
| `import` forms; `__name__ == "__main__"`; a module; a package | s06 A |
| Standard-library tour (`math`, `random`, `statistics`, `string`, `collections`, `itertools`, `functools`, `re`, `os`, `shutil`, `time`) | s06 B |
| Virtual environments; `uv add`; `pyproject.toml`; the HTTP client against the public API; the terminal-output library; reading documentation | s06 C |
| Writing your own pytest tests: `assert`, `parametrize`, fixtures; `ruff` revisited | s06 D |
| Why classes; `class`, `__init__`, `self`; attributes and methods; `__repr__`/`__str__` | s07 A |
| Class vs instance attributes; `@property`; `@classmethod`/`@staticmethod` | s07 B |
| `__eq__` and `__hash__` | s07 C |
| `dataclasses`; `Enum`; objects in collections | s07 D |
| Inheritance, `super()`, overriding; polymorphism and duck typing; composition over inheritance; ABCs and `Protocol` | s08 A |
| The data model: `__len__`, `__getitem__`, `__contains__`, operator dunders, `__call__`, `__bool__` | s08 B |
| Iterators vs iterables; generators; lazy pipelines | s08 C |
| Writing context managers ★ (`__enter__`/`__exit__`, `@contextmanager`); exceptions as classes revisited; `__slots__` (stretch) | s08 D |
| PEP 8 and `ruff format`; idioms (EAFP/LBYL, walrus, `with` everywhere) | s09 A |
| Typing in depth (`Optional`, `|`, generics, `TypedDict`, `Protocol`); `mypy` | s09 B |
| Testing in depth (`tmp_path`, `monkeypatch`, coverage); debugging and `logging` in depth | s09 C |
| Performance basics (`timeit`, profiler, big-O intuition, list vs set vs dict, generators vs lists, string building) | s09 D |
| Refactoring the 200-line script | s09 E |
| Reading other people's code (a stdlib module; a stranger's pull request) | s09 F |
| Concurrency vocabulary (stretch only) | s09 stretch |
| Capstone: package, JSON persistence + pickle memo, `argparse` sub-commands, API search, `logging`, custom exceptions, `mypy`, ≥ 90 % coverage, `ruff`, README, `uv build`, failure review, break-my-program, post-mortem, teach-back, sibling hand-off | s10 A–E |

## Gaps and partials, prioritised

1. **Environment variables are taught (s05 C) but first gated only at s10.** Add a hidden case at s05 that reads `LIBRARY_NAME` from the environment. Step change at s05 rung-numbering.
2. **Pre-commit hooks are configured in the repository but taught only as a stage 9 stretch.** Decide at s09 rung-numbering whether it is a rung (20 min) or stays stretch; the destination says "toolchain daily", and hooks are part of most teams' daily toolchain.
3. **Reading a colleague's pull request (s09 F) depends on having a colleague.** The brief must ship a stranger's PR as a fixture (a branch in upstream with a deliberate review target). Fixture to build at s09 readiness.
4. **No stage uses a database.** Deliberate: `sqlite3` is in the sibling courses' Assumes only as "has seen SQL"; a one-rung `sqlite3` stretch at s10 is the cheapest closure if the hand-off read-through (s10 E) shows a gap. Decision deferred to the first s10 reference run.
