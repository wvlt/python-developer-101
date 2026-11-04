# 01 — Syllabus

Ten stages, four tiers, about 140 hours; roughly 15 weeks at 8–10 hours per week. Every stage has the same skeleton so the learner always knows what is expected:

- **Entry condition** — the previous gate passed.
- **Break-lab** — predict-the-output snippets and a planted bug, done *before* reading the Build section.
- **Four strands** — Build, Measure (tests), Break, Inspect — each with concrete content for this stage.
- **Rungs** — one concept, one worked example, four to eight micro-exercises with tests, one Check.
- **Mini-project** — the last rung; combines the stage's concepts into one program.
- **Artefact** — what you ship. It lives in `stages/NN-name/` in your fork and carries an [Artefact Card](../templates/ARTIFACT_CARD.md).
- **Gate** — `just eval` on the hidden tests, plus the Say questions. You do not start the next stage until you pass. Full rubrics in [06 — Assessment](06-assessment-and-gates.md).
- **Kill criteria** — when *not* to write the code this stage taught.

Per-stage briefs live in each `stages/NN-name/README.md`. Topics marked ★ were named by the course owner and must appear exactly where listed; the [capability map](12-capability-map.md) traces every topic to its rung.

---

## Tier A — Talking to the machine

The goal of Tier A is one mental model, held firmly: **the computer does exactly what you wrote, not what you meant.** A program is text; the interpreter reads it literally; an error is the computer talking back; a wrong answer with no error is the computer agreeing with a mistake. Everything in programming follows from taking that seriously.

### Stage 0 — Hello, Python (on-ramp)

*~2 hours · ungated · zero accounts, zero cost*

Install the Python version and the editor pinned in `PINS.md`. Open a terminal for the first time. Type `python` and see the REPL; type `print("Hello, world")`; save the same line in `hello.py` and run `python hello.py`. Then one change at a time: change the text; print two things; print a number and a word and discover what quotes are for; make it fail on purpose three ways (misspell `print`, forget a quote, forget a bracket) and read each error message slowly; `input()` and a greeting; and finish with the habit — a three-line script, in a folder you made, with a comment on top saying what it does, run from the terminal.

No tests, no git, no artefact, no gate. The Done-when list is six things you can now do without looking. Stage 1's first rung assumes all of them.

### Stage 1 — Values and names

*~1.5 weeks · 12 h*

**Entry:** Stage 0 done. Rung 0 installs `uv`, `just` and git, clones the course, and runs the stage's tests — red, because you have not written anything yet.

**Break-lab:** eleven one-line snippets (`7 / 2`, `7 // 2`, `-7 // 2`, `0.1 + 0.2`, `"3" + "4"`, `3 + "4"`, `2 ** 3 ** 2`, `-10 % 3`, `x = 5; y = x; x = 6; print(y)`, `"a" * 3`, `bool("0")`). Predict each output in your journal, then run them.

**Build:** `int`, `float`, `bool`, `str`, `None`; arithmetic and precedence; `/` vs `//` and `%`; `**`; `type()` and conversions; variables and assignment; naming rules and PEP 8 names; augmented assignment; strings — quotes, escape sequences, multi-line strings, `len`, indexing, slicing, immutability; string methods; f-strings and format specs (`:.2f`, `:>10`); comparison operators; `and`/`or`/`not`; truthiness; `is` vs `==` (first contact).

**Measure:** every rung has four to eight exercises with visible tests (`just test 01`); the gate runs the hidden set (`just eval 01`).

**Break:** `TypeError` from mixing `str` and `int`; integer vs true division; float precision; `NameError` from a typo; a string method that returns a new string nobody kept.

**Inspect:** `print()` with labels, then `print(f"{x=}")`. The REPL as a calculator for trying one line.

**Tooling:** `uv run`, `just test`, git locally — `init`, `status`, `add`, `commit`, `log` as save points, nothing more.

**Artefact:** a receipt formatter: reads a name, a price and a quantity, prints an aligned receipt with a total, a tax line and a thank-you.

**Gate:** ≥ 44 of 49 hidden tests pass; three Say questions answered without notes; git log shows ≥ 5 commits with messages that say what changed.

**Kill criteria:** if a calculator or a spreadsheet cell does it once, do not write a program.

### Stage 2 — Decisions and repetition

*~1.5 weeks · 12 h*

**Break-lab:** a `while` that never ends (run it, then stop it with Ctrl-C and read what the interrupt says); `range(1, 10)` printing nine numbers; `if x = 5` as a `SyntaxError`; `if answer == "yes" or "y"` always being true; an `else` on a loop.

**Build:** `if`/`elif`/`else`; nested conditions; the conditional expression; `match`/`case`; `while`; `for` and `range` (start/stop/step, half-open); `break`, `continue`, `pass`, `else` on loops; `enumerate`; `zip` ★; nested loops; accumulator and flag patterns; input-validation loops.

**Measure:** as stage 1; the hidden set includes inputs the visible tests did not show (empty, negative, mixed case).

**Break:** off-by-one; infinite `while`; `=` vs `==`; the always-true `or`; shadowing the loop variable.

**Inspect:** `just trace FILE` prints every line as it runs — watch the loop go round.

**Tooling:** GitHub (free account, fork, push; the course player shows your `PROGRESS.md`); `ruff check` as a second pair of eyes.

**Artefact:** a text game (number guessing with a guess limit and hints, then hangman-lite) that loops until win or loss and validates every input.

**Gate:** ≥ 50 of 56 hidden tests pass; `ruff check` clean on `exercises/`; the fork is on GitHub with ≥ 8 commits; three Say questions.

**Kill criteria:** if the decision table has three rows and will never change, write the three rows down, not the program.

### Stage 3 — Collections

*~1.5 weeks · 14 h*

**Break-lab:** `a = [1, 2, 3]; b = a; b.append(4); print(a)`; `x = [1, 2, 3].sort(); print(x)`; `for item in items: items.remove(item)`; `d["missing"]`; `t = (1, 2); t[0] = 9`; `[[0] * 3] * 3` then change one cell.

**Build:** lists and their methods; `sorted()` ★ with `key` and `reverse`, `sort` vs `sorted`, stability; `lambda` ★ (introduced with `key`); `min`/`max`/`sum`/`any`/`all`; `in`; mutability, aliasing and copying (slice copy, `copy`, `deepcopy`); tuples and unpacking (swap, `*rest`); dicts (`[]` vs `get`, `setdefault`, `keys`/`values`/`items`, iteration, nested dicts, insertion order); sets and set operations; list/dict/set comprehensions with conditions; nested data (a list of dicts); `del`; shallow vs deep copy; choosing the right collection.

**Measure:** hidden tests run on a held-out sample of the library world (different books, same shape).

**Break:** aliasing; mutation during iteration; `KeyError`; the shared inner list; `sort()` returning `None`.

**Inspect:** `print(id(a), id(b))`; `just trace` on an aliasing snippet.

**Data:** a sample of the neighbourhood library world as Python literals at the top of each exercise (the files themselves arrive at stage 5).

**Artefact:** the catalogue: a list-of-dicts program that answers questions about books, members and loans — counts, groupings, sorting by several keys, the most-borrowed, the never-borrowed.

**Gate:** ≥ 54 of 60 hidden tests; the aliasing Say question answered with a drawing or a sentence about names and objects.

**Kill criteria:** if the data fits in one spreadsheet and the question is asked once, use the spreadsheet.

---

## Tier B — Structure

Tier B gives the program shape: functions to name a piece of work, errors as values you handle rather than crashes you suffer, files so the program outlives the process, modules so it can grow, and your own tests so you know when it broke.

### Stage 4 — Functions

*~1.5 weeks · 14 h*

**Break-lab:** a function with no `return` whose result is printed as `None`; `def add(items, acc=[])` called twice; `total = 0` inside a function that reads an outer `total`; calling `f` instead of `f()`; a lambda in a loop capturing the last value.

**Build:** `def`, parameters, `return` (and returning `None`); positional vs keyword arguments, defaults; `*args`/`**kwargs`; the mutable-default trap; scope and LEGB, `global`/`nonlocal`; docstrings; type hints (basic); pure functions vs side effects; functions as values; `lambda` ★ deepened; `map`/`filter` vs comprehensions; `sorted` with a multi-key `lambda`; closures; a first decorator (timing); recursion (factorial, a nested-list walk) and when not to recurse; the debugger (`breakpoint()`, step, inspect).

**Measure:** exercises become fill-in-the-function; tests import and call them with inputs the stubs did not show.

**Break:** forgotten `return`; mutable default; `UnboundLocalError`; late-binding closure; recursion with no base case (`RecursionError`).

**Inspect:** `breakpoint()`, `n`/`s`/`p`/`c`; the editor's debug pane; watching a local change.

**Artefact:** a toolkit of twenty small, pure, documented, type-hinted functions over the library sample, plus one timing decorator.

**Gate:** ≥ 54 of 60 hidden tests; every function has a docstring and type hints (checked by a script); a debugger session journaled with the variable you watched.

**Kill criteria:** if it is called once and is four lines, it is not a function yet.

### Stage 5 — Errors, files and the outside world

*~1.5 weeks · 14 h*

**Break-lab:** read `loans.txt` with `int()` on every field and watch it crash on line 3; open `broken/books_latin1.csv` as UTF-8; `except: pass` around a typo and watch the program "succeed"; open a file without closing it in a loop of 10 000.

**Build:** exceptions (`try`/`except`/`else`/`finally`, catching specific types, `raise`, re-raising, custom exception classes, the hierarchy); `assert`; reading long tracebacks; `with` and context managers ★ (as users: `open`); `pathlib`; reading and writing text (modes, `encoding="utf-8"`, newline handling); `csv` (reader, `DictReader`, writer); `json` (`load`/`dump`, `loads`/`dumps`, `indent`); `pickle` ★ (what it is, when it is useful, why you never unpickle untrusted data, JSON vs pickle); `datetime` and `timedelta`; `sys.argv` then `argparse`; environment variables; `logging` (levels, `basicConfig`, a logger per module).

**Measure:** tests run functions against the fixture files, including the broken ones; a hidden test checks that the program logs what it skipped.

**Break:** `UnicodeDecodeError`; `KeyError` on the missing column; swallowed exceptions; the un-closed file; a relative path that depends on where you ran it from.

**Inspect:** `logging` replaces `print` for anything that touches a file; the log file is the record of what the program did.

**Artefact:** `loans_report.py`: reads the three fixture files, skips and logs bad lines, writes an overdue report as CSV and JSON, takes its paths and the as-of date from `argparse`.

**Gate:** ≥ 54 of 60 hidden tests including the four broken-file cases; a four-screen traceback read to its root and journaled; the pickle Say question.

**Kill criteria:** if the file is read once by a human, `cat` or a spreadsheet does it; if it is one line of shell, write the shell.

### Stage 6 — Modules, packages and tooling

*~1.5 weeks · 12 h*

**Break-lab:** name a file `random.py` and `import random`; a circular import; `from x import *` shadowing `open`; a test that passes because it tests nothing (`assert True`).

**Build:** `import` forms; `__name__ == "__main__"`; writing a module; writing a package (`__init__.py`); the standard-library tour (`math`, `random`, `statistics`, `string`; `collections`: `Counter`, `defaultdict`, `deque`, `namedtuple`; `itertools`: `chain`, `product`, `groupby`, `islice`; `functools`: `partial`, `reduce`, `lru_cache`; `re` basics: `search`, `findall`, `sub`, groups; `os`, `shutil`, `time`); virtual environments and `uv add`; `pyproject.toml`; a third-party package (the HTTP client against the public API named in `PINS.md`, the terminal-output library); reading documentation; writing your own pytest tests (`assert`, `parametrize`, fixtures); `ruff` revisited.

**Measure:** the learner writes the visible tests for the mini-project; the course's hidden set still gates. A hidden test checks that the learner's tests fail when a planted bug is introduced (mutation check).

**Break:** the shadowed standard-library module; the test that cannot fail; the import that works from one directory and not another.

**Inspect:** `python -c "import x; print(x.__file__)"` — where did that come from?

**Artefact:** a `library` package (`catalogue.py`, `loans.py`, `report.py`, `cli.py`) with the learner's own tests, one `uv add`-ed dependency, and a `pyproject.toml`.

**Gate:** ≥ 45 of 50 hidden tests; the learner's own tests number ≥ 15, and ≥ 12 of them fail under the planted bug; one standard-library function used where the learner had written their own.

**Kill criteria:** if the standard library already does it, delete your version. This gate checks that you did.

---

## Tier C — Objects

Tier C answers the question stage 3 left open — "a dict of dicts of dicts is getting hard to think about" — with classes, and then with the data model that makes your classes behave like Python's own.

### Stage 7 — Classes and objects

*~1.5 weeks · 12 h*

**Break-lab:** the dict-of-dicts pain: add a field to every book in the stage-6 package and count the places that changed; a method without `self`; a class attribute list shared between instances; printing an object and getting `<__main__.Book object at 0x…>`.

**Build:** why classes; `class`, `__init__`, `self`; instance attributes and methods; `__repr__` and `__str__`; class attributes vs instance attributes; `@property` (getters, setters, computed attributes); `@classmethod` (alternate constructors) and `@staticmethod`; `__eq__` and `__hash__`; `dataclasses` (`@dataclass`, `field`, `frozen`, ordering); `Enum`; objects in collections.

**Measure:** fill-in-the-class exercises; hidden tests construct objects with inputs the stubs did not show.

**Break:** forgetting `self`; the shared class-attribute list; `__eq__` without `__hash__` and the object that cannot go in a set; a mutable default in a dataclass field.

**Inspect:** `__repr__` is what the debugger shows; `vars(obj)`; `dataclasses.asdict`.

**Artefact:** the library world as classes — `Book`, `Member`, `Loan`, `Library` — with equality, representation, properties and an `Enum` for loan status.

**Gate:** ≥ 45 of 50 hidden tests; the Say question "when is a dataclass enough and when do you need a class?" answered with an example of each.

**Kill criteria:** if it has no behaviour and no invariant, it is a dict or a dataclass, not a class.

### Stage 8 — Design and the data model

*~1.5 weeks · 14 h*

**Break-lab:** a subclass that forgets `super().__init__()`; a `len()` call on your own collection; a `for` over your own object; isinstance checks everywhere where a method call would do.

**Build:** inheritance and `super()`; method overriding; polymorphism and duck typing; composition over inheritance; abstract base classes and `Protocol`; the data model: `__len__`, `__getitem__`, `__iter__`/`__next__`, `__contains__`, operator dunders (`__add__`, `__lt__`), `__call__`, `__bool__`; iterators vs iterables; generators (`yield`, generator expressions, lazy pipelines, memory); writing context managers ★ with `__enter__`/`__exit__` and `@contextlib.contextmanager`; exceptions as classes revisited; `__slots__` as stretch.

**Measure:** hidden tests exercise the dunders through Python's own syntax (`len(lib)`, `for book in lib`, `book in lib`, `sorted(books)`).

**Break:** the missing `super()` call; an iterator that cannot be iterated twice; a generator consumed by a `print` before the loop; a context manager that does not clean up on error.

**Inspect:** `dir(obj)`; `type(obj).__mro__`; `sys.getsizeof` on a list vs a generator.

**Artefact:** the library package with a `Library` that is a real collection (len, iteration, membership, indexing), a lazy loan-report pipeline of generators, and a context manager that opens, validates and closes the data files.

**Gate:** ≥ 45 of 50 hidden tests; the comparison memo "inheritance vs composition for `Member` and `StaffMember`" with the test counts for each; the Say question on iterators vs iterables.

**Kill criteria:** if the hierarchy is two levels deep and has one subclass, it is a flag on the parent, not a hierarchy.

---

## Tier D — Craft

Tier D is about doing it well, reading it when others did it, and knowing when not to.

### Stage 9 — Writing Python well

*~1.5 weeks · 14 h*

**Break-lab:** a 200-line script with twelve quiet bugs planted (`is` for equality, `except Exception: pass`, string built in a loop, a list used for membership in a loop of 100 000, a mutable default, a late-binding closure, an unclosed file…). Find as many as you can in 45 minutes before reading on; `ruff` and `mypy` find some of them for you afterwards.

**Build:** PEP 8 and `ruff format`; idioms (EAFP vs LBYL, unpacking, `enumerate`/`zip` over indices, comprehensions vs loops, the walrus `:=`, `with` for every resource); typing in depth (`Optional`, `Union`/`|`, generics, `TypedDict`, `Protocol`, `mypy`); testing in depth (fixtures, `parametrize`, `tmp_path`, mocking with `monkeypatch`, coverage); debugging and `logging` in depth; performance basics (`timeit`, big-O intuition, list vs set vs dict lookups, generators vs lists, string building); refactoring the 200-line script into modules and classes; reading other people's code (a standard-library module and a stranger's pull request); a first look at concurrency vocabulary (`threading`, `asyncio`) as stretch only.

**Measure:** `mypy --strict` clean; coverage ≥ 90 %; `timeit` before and after each performance change, in a table.

**Break:** the twelve quiet bugs; a test that passes for the wrong reason; a type hint that lies.

**Inspect:** `timeit`, `cProfile`, `logging` with a logger per module.

**Artefact:** the refactored script as a package with types, tests, coverage and a performance table; a code-reading memo on a standard-library module.

**Gate:** ≥ 10 of 12 planted bugs found and fixed with a test each; `mypy --strict` and `ruff` clean; coverage ≥ 90 %; three `timeit` comparisons with numbers; the reading memo passes the artefact rubric.

**Kill criteria:** if it runs in 0.2 s once a day, do not optimise it; if you cannot name the hot spot from a profile, do not optimise anything.

### Stage 10 — Capstone

*~2.5 weeks · 20 h*

**Build:** a command-line application for the library world — a package with dataclasses and classes, JSON persistence to the fixture directory (with a [comparison memo](../templates/COMPARISON_MEMO.md) against pickle), `argparse` sub-commands (`add`, `lend`, `return`, `report`, `search` against the public API), `logging`, custom exceptions, type hints checked by `mypy`, ≥ 90 % test coverage, `ruff` clean, a README with usage, a `pyproject.toml` built with `uv build`.

**Failure review:** before building, a [`FAILURE_REVIEW.md`](../templates/FAILURE_REVIEW.md): where could this program be quietly wrong, and which test or structure prevents each.

**Break-my-program:** a peer runs the [protocol](10-instructor-guide.md#the-break-my-program-protocol) against your program for an hour; you fix every finding with a test and write the [post-mortem](../templates/POSTMORTEM.md).

**Teach-back:** explain one concept from each tier to a non-programmer, in five minutes each, with a running example and a deliberate mistake.

**Hand-off:** read the Stage 0 brief of AI Agents 101 and tick, item by item, that you can start it unaided.

**Artefact:** the application, its tests, its README, the failure review, the comparison memo, the post-mortem, the teach-back notes, and the hand-off checklist.

**Gate:** all of the build criteria met and checked by script; ≥ 90 % coverage; the peer session found ≥ 1 bug and every finding has a test; post-mortem reviewed by a peer; teach-back delivered; hand-off checklist complete with no unticked item.

**Kill criteria:** if, having built it, you conclude that the library would be better served by a spreadsheet, say so in the post-mortem with the reasons. That conclusion, with evidence, is a passing capstone.

---

## Time budget summary

| Stage | Weeks | Hours | Cumulative |
|---|---|---|---|
| 0 | — | 2 | 2 |
| 1 | 1.5 | 12 | 14 |
| 2 | 1.5 | 12 | 26 |
| 3 | 1.5 | 14 | 40 |
| 4 | 1.5 | 14 | 54 |
| 5 | 1.5 | 14 | 68 |
| 6 | 1.5 | 12 | 80 |
| 7 | 1.5 | 12 | 92 |
| 8 | 1.5 | 14 | 106 |
| 9 | 1.5 | 14 | 120 |
| 10 | 2.5 | 20 | 140 |

Absolute beginners routinely take 1.5× these figures in Tier A and catch up in Tier C. That is fine. The gates are the schedule, not the calendar. Track your actual hours in `LEDGER.md`; the ledger is the data that re-estimates the next cohort's rungs.

## Cost budget

Zero. There is no paid tool, no cloud and no model anywhere in this course. The only account is a free GitHub account at stage 2.
