# 17 — Focus map

Each stage has one dominant concept, but several other things are also changing underneath: which tools the learner must use, how they reach the data, what shape their exercises take. If those change silently, the learner cannot tell which change caused what they are seeing. This map makes every lane explicit, per stage, and names what is **deliberately deferred** so that nobody teaches it early.

Within a stage, rungs are grouped into **parts** — a part is a run of rungs with one focus. Parts are headings, not identifiers; rungs keep their IDs. For stages not yet rung-numbered, the part plan below is the authoring plan and the reference target for [docs/12](12-capability-map.md).

## Lanes

- **Concept** — the one idea the stage installs.
- **Exercise shape** — what the learner fills in and how it is tested.
- **Data** — how the learner reaches the library fixture.
- **Inspect** — the tool for seeing inside the program at this stage.
- **Tooling** — what the learner is required to use from this stage on (the [tooling ramp](02-getting-started.md#tooling-ramp)).
- **Deferred** — what is explicitly *not* taught yet, and where it lands.

## The tool ladder

One new tool per stage, never two; each arrival carries a lesson.

| Step | Stage | Tool arrives | The lesson it carries |
|---|---|---|---|
| 1 | s00 | Terminal, the Python installer, the editor, the REPL | The machine runs what you typed, nothing more. Errors are messages. |
| 2 | s01 | `uv run`, `just test`, git locally | Someone else's tests tell you whether you are done. A save point is a sentence about what changed. |
| 3 | s02 | `ruff check`, GitHub (fork, push, PR) | A program can be wrong in ways that do not crash; a tool can see some of them. Your work has a public address. |
| 4 | s04 | `breakpoint()`, the editor's debugger | Stop the program and look, instead of guessing and printing. |
| 5 | s05 | `logging`, `argparse` | A program that will be run by others reports what it did and accepts instructions properly. |
| 6 | s06 | `uv add`, `pyproject.toml`, writing `pytest` tests | Dependencies are declared, not installed by hand. Your tests are your definition of done. |
| 7 | s09 | `mypy`, `timeit`, coverage, `ruff format`, pre-commit (stretch) | Claims about types, speed and testedness get numbers. |
| 8 | s10 | `uv build` | A program becomes a thing someone else can install. |

Stages 3, 7 and 8 add no tool on purpose: their concepts (aliasing; classes; the data model) are enough new load.

## Stage by stage

### Stage 0 — Hello Python

- **Concept:** the computer runs exactly the line you wrote; when it cannot, it tells you where.
- **Parts:** A *the machine* (r0–r2: install, REPL, a file); B *one change at a time* (r3–r6: change text, two things, number vs word, fail on purpose, `input()`); C *the habit* (r7: a folder, a file, a comment, run from the terminal).
- **Exercise shape:** none; eight rungs each with a Run/See/Say. No tests.
- **Data:** none.
- **Inspect:** `print`.
- **Tooling:** terminal, installer, editor, REPL.
- **Deferred:** variables as a concept (s01), `uv` and git (s01), every control structure (s02). The learner uses `input()` without the word "function" being said.

### Stage 1 — Values and names

- **Concept:** a value has a type; a name is a label on a value; text is not a number.
- **Parts:** A *the toolchain* (r0); B *numbers* (r1–r2); C *names* (r3); D *text* (r4–r6); E *truth* (r7); F *save and ship* (r8 git, r9 receipt).
- **Exercise shape:** whole programs over `input()`/`print()`, tested as subprocesses.
- **Data:** none; the receipt's items are typed in.
- **Inspect:** `print`, then `f"{x=}"`, `just trace`.
- **Tooling:** `uv run`, `just test`, `just eval`, git locally.
- **Deferred:** `if` (s02; every exercise is straight-line), loops, lists (s03; "two things" are two names), functions (s04), GitHub (s02), `ruff` (s02). Aliasing is *mentioned* at r7 only as `is` vs `==` on small values.

### Stage 2 — Decisions and repetition

- **Concept:** a program chooses and repeats; the half-open range; a loop that validates input.
- **Parts:** A *decisions* (r1–r3); B *repetition* (r4–r8); C *tools and the game* (r9 `ruff`, r10 GitHub, r11 text game).
- **Exercise shape:** whole programs; the first planted bug (r11 break item).
- **Data:** none; the game's rules are literals.
- **Inspect:** an f-string print inside the loop; `just trace` to catch an infinite loop.
- **Tooling:** `ruff check`, GitHub fork/push/PR, the course player.
- **Deferred:** lists (s03; loops here are over `range` and strings), functions (s04), exceptions (s05; validation is by loop and `str.isdigit`).

### Stage 3 — Collections

- **Concept:** many values in one name; two names can be one object.
- **Parts (plan):** A *lists* (lists and methods; `sorted()` and `lambda` as key; `min`/`max`/`sum`/`any`/`all`/`in`); B *aliasing* (mutability, copying, shallow vs deep, mutating while iterating); C *tuples and dicts* (unpacking; dict access patterns; nested data); D *sets and comprehensions*; E *choosing* (which collection, and the spreadsheet kill criterion); F *mini-project: the catalogue* (answers five questions over the book list).
- **Exercise shape:** whole programs; the fixture arrives as a Python literal at the top of the exercise file (a list of dicts of books).
- **Data:** literals generated from the fixture; the held-out gate sample is a second literal.
- **Inspect:** `print(id(a), id(b))`; `f"{a=} {b=}"`.
- **Tooling:** none new.
- **Deferred:** functions (s04; the catalogue is one script), files (s05; literals instead), classes (s07; dicts instead), generators (s08).

### Stage 4 — Functions

- **Concept:** a named piece of program with inputs and an output; where names live.
- **Parts (plan):** A *defining* (`def`/`return`; arguments and defaults; the mutable default); B *scope* (LEGB, `global`/`nonlocal`); C *documenting* (docstrings, basic type hints, pure vs side effects); D *functions as values* (`lambda` deepened, `map`/`filter` vs comprehensions, multi-key `sorted`, closures, a timing decorator); E *recursion*; F *Inspect: the debugger*; G *mini-project: the catalogue as functions* (the stage 3 script refactored and extended).
- **Exercise shape:** function stubs with signature and docstring; tests import and call.
- **Data:** literal, as s03.
- **Inspect:** `breakpoint()`; the editor's debugger.
- **Tooling:** the debugger.
- **Deferred:** exceptions (s05; functions return `None` for "not found"), modules (s06; one file), classes (s07).

### Stage 5 — Errors, files and the outside world

- **Concept:** things outside the program go wrong; the program must say so without crashing or hiding.
- **Parts (plan):** A *exceptions* (`try`/`except`/`else`/`finally`, specific types, `raise`, custom exceptions, long tracebacks, `assert`); B *files* (`with`, `pathlib`, text and encoding, `csv`, `json`, `pickle`); C *time and the command line* (`datetime`, `sys.argv` → `argparse`, environment variables); D *Inspect: logging*; E *mini-project: the loans report* (reads all three fixture files, skips and logs bad lines, prints overdue loans).
- **Exercise shape:** function stubs reading paths; tests use `tmp_path` copies of the fixture and the broken files.
- **Data:** files in `data/library/` for the first time; the four broken files.
- **Inspect:** `logging` at DEBUG/INFO/WARNING; `exc_info=True`.
- **Tooling:** `logging`, `argparse`.
- **Deferred:** packages (s06), own tests (s06; the course still writes them), classes for records (s07; dicts and tuples), writing context managers (s08).

### Stage 6 — Modules, packages and tooling

- **Concept:** code you did not write, and how to reach it; tests you do write.
- **Parts (plan):** A *modules* (`import` forms, `__name__ == "__main__"`, a module, a package); B *the standard-library tour* (`collections`, `itertools`, `functools`, `re`, `os`/`shutil`/`time`; one stdlib function replacing hand-written code); C *packages* (virtual environments, `uv add`, `pyproject.toml`, the HTTP client against the public API, the terminal-output library, reading documentation); D *your own tests* (`assert`, `parametrize`, fixtures; the planted-bug mutation check); E *mini-project: the library package* (the stage 5 report as a package with the learner's own tests).
- **Exercise shape:** modules and a package in `src/`; the learner's own tests in `tests/` for the first time; hidden cases include the mutation check (how many of the learner's tests fail under the planted bug).
- **Data:** files; the recorded API sample for offline tests.
- **Inspect:** logging per module.
- **Tooling:** `uv add`, `pyproject.toml`, writing `pytest` tests, `ruff` on `src/`.
- **Deferred:** classes (s07), typing beyond basics (s09), coverage (s09), publishing (s10).

### Stage 7 — Classes and objects

- **Concept:** data and the behaviour that belongs to it, in one thing with a name.
- **Parts (plan):** A *a first class* (why; `class`, `__init__`, `self`; methods; `__repr__`/`__str__`); B *attributes* (class vs instance, the shared mutable attribute; `@property`; `@classmethod`/`@staticmethod`); C *equality* (`__eq__`/`__hash__`); D *records* (`@dataclass`, `field`, `frozen`; `Enum`; objects in collections); E *mini-project: Book, Member, Loan, Library* (the package's dicts become classes; an ADR on dataclass vs class).
- **Exercise shape:** class stubs; tests construct and call.
- **Data:** files, loaded into objects.
- **Inspect:** `__repr__` in the debugger.
- **Tooling:** none new; the first required ADR.
- **Deferred:** inheritance (s08), the data model beyond `__repr__`/`__eq__` (s08), `Protocol` (s08).

### Stage 8 — Design and the data model

- **Concept:** objects that behave like Python's own; choosing between inheritance and composition with numbers.
- **Parts (plan):** A *relationships* (inheritance, `super()`, overriding; duck typing, ABCs, `Protocol`; the composition memo); B *the data model* (`__len__`, `__getitem__`, `__contains__`, operator dunders, `__call__`, `__bool__`); C *iteration* (iterators vs iterables, generators, lazy pipelines over the loans file); D *context managers as authors* (`__enter__`/`__exit__`, `@contextmanager`; exceptions as classes revisited); E *mini-project: a Library you can iterate, index and `with`* (plus a comparison memo).
- **Exercise shape:** class stubs; tests exercise the protocols (`len()`, `in`, `for`, `with` raising inside).
- **Data:** files; the loans file streamed by a generator.
- **Inspect:** the debugger stepping *into* a dunder call.
- **Tooling:** none new.
- **Deferred:** `__slots__` and metaclasses (stretch, never required), typing of protocols (s09), concurrency (s09 stretch).

### Stage 9 — Writing Python well

- **Concept:** the difference between a program that works and one a colleague will accept; every claim with a number.
- **Parts (plan):** A *style and idiom* (`ruff format`, PEP 8, EAFP/LBYL, unpacking, walrus, `with` everywhere); B *types* (`Optional`/`|`, generics, `TypedDict`, `Protocol`, `mypy --strict`); C *tests in depth* (`tmp_path`, `monkeypatch`, coverage); D *measure* (`timeit`, the profiler, list vs set vs dict, generators vs lists, string building); E *refactor* (the 200-line script into modules and classes, tests first); F *read* (a stdlib module; a stranger's pull request); G *mini-project: the planted-bug hunt* (twelve bugs in a provided package; a test per bug).
- **Exercise shape:** a provided package to type, test, measure and fix; memos.
- **Data:** files.
- **Inspect:** `timeit`, `cProfile`; logging configured from the CLI.
- **Tooling:** `mypy`, `timeit`, coverage, `ruff format`, pre-commit (stretch).
- **Deferred:** concurrency (`threading`, `asyncio` as vocabulary only), packaging (s10).

### Stage 10 — Capstone

- **Concept:** the whole thing, for a stranger, with the evidence.
- **Parts (plan):** A *plan* (the failure review; the skeleton and `pyproject.toml`); B *build* (domain and JSON persistence; `argparse` sub-commands; search against the public API; logging and custom exceptions); C *craft* (tests to ≥ 90 %, `mypy --strict`, `ruff`); D *ship* (README, `uv build`); E *review* (break-my-program and post-mortem; teach-back; the sibling course hand-off read-through).
- **Exercise shape:** the learner's package; hidden cases run the CLI.
- **Data:** files; the API live or the recorded sample.
- **Inspect:** logging to a file; the profiler on `report`.
- **Tooling:** `uv build`.
- **Deferred:** nothing; the stretch list is the sibling courses.

## What is never taught here

Named so nobody adds it: web frameworks, databases beyond a one-rung `sqlite3` stretch if the hand-off shows a gap, `numpy`/`pandas` (Data Science 101), calling a language model (AI Agents 101), concurrency beyond vocabulary, metaclasses, packaging to an index, GUIs, notebooks.
