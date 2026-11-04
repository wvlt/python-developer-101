# 08 — Glossary

Precise definitions as used in this curriculum. Where the field uses a term loosely, we pick one meaning and stick to it. Stage in brackets is where the term is first needed; a brief never uses a term before its stage, and a rung introduces at most three.

**`__init__`** [S7] — The method Python calls on a new instance right after creating it; where per-instance attributes are set. Not the constructor (that is `__new__`), though everyone calls it that.

**`__repr__`** [S7] — The method that returns the developer-facing text for an object; what the REPL and the debugger show. A good one lets you recreate the object.

**Aliasing** [S3] — Two names bound to one object, so a change through either is seen through both. The first quiet failure the course meets. Bestiary C01.

**Argument / parameter** [S4] — A parameter is the name in the `def` line; an argument is the value passed in the call. `def greet(name)` has a parameter; `greet("Ada")` passes an argument.

**`argparse`** [S5] — The standard-library module that turns `python prog.py --count 3 file.txt` into named values and writes `--help` for you.

**Artefact Card** [S1] — The one-page summary every stage mini-project ships with: what it does, how it was tested, how it fails, what was decided, what was assisted.

**Assertion** [S1] — A statement that a condition is true at this point, written `assert x == 3`. In tests, the thing that makes the test fail.

**Attribute** [S7] — A name attached to an object, reached with a dot: `book.title`. Methods are attributes that happen to be functions.

**Bestiary** [S0] — The catalogue of failures in [docs/07](07-failure-bestiary.md), each with a stable ID.

**Block** [S2] — The indented lines after a colon. Python uses indentation, not brackets, to say where a block begins and ends.

**Boolean** [S1] — The type with two values, `True` and `False`. The result of a comparison.

**Branch (git)** [S2] — A movable name for a line of commits. You work on `stage/NN-name` and merge into `main`.

**Break-lab** [all] — A deliberately induced failure performed before instruction. The first activity of every stage: predict, run, compare.

**`breakpoint()`** [S4] — A built-in that pauses the program at that line and opens the debugger.

**Built-in** [S1] — A function or type available without importing anything: `print`, `len`, `int`, `list`. Do not shadow them.

**Call** [S1] — Running a function: the name followed by parentheses, with any arguments inside. `print("hi")` is a call; `print` alone is a reference.

**CLI (command-line interface)** [S5] — A program driven from the terminal by arguments and options rather than clicks. The course's standard shape of program.

**Class** [S7] — A blueprint for objects: the attributes they have and the methods they answer to. Instances are made by calling the class.

**Commit** [S1] — A saved snapshot of your files in git with a message. One per rung at least.

**Comprehension** [S3] — A one-line expression that builds a list, set or dict from a loop: `[b.title for b in books if b.year > 2000]`.

**Context manager** [S5 as user, S8 as author] — An object usable in a `with` statement; it runs setup on entry and cleanup on exit, even if the body raises. Files are the first one you meet.

**Contract** [S1] — A stage's *Assumes* and *Provides* lists. The dependency graph of the curriculum.

**Coverage** [S9] — The fraction of lines (or branches) run by the tests. 90 % is the capstone bar; 100 % is not the goal.

**Dataclass** [S7] — A class generated from its field list by `@dataclass`, with `__init__`, `__repr__` and `__eq__` written for you. For records; use a plain class when there is behaviour or an invariant.

**Debugger** [S4] — A tool that runs your program one line at a time and lets you look at every variable. In the terminal, `pdb`; in the editor, the Run and Debug panel.

**Dictionary (`dict`)** [S3] — A mapping from keys to values; lookup by key, insertion order kept.

**Docstring** [S4] — The string on the first line of a function, class or module, describing what it does. `help()` shows it.

**Duck typing** [S8] — Caring what an object can *do*, not what class it is. If it has `__iter__`, you can loop over it.

**Dunder** [S7] — "Double underscore": methods like `__len__` that Python calls for you when you use `len()`, `+`, `in`, `with`. The data model.

**Encoding** [S5] — The rule that turns text into bytes and back. UTF-8 unless you have been told otherwise. Bestiary E02.

**Entry condition** [S1] — What must be true before a stage starts.

**Eval harness** [S1] — `just eval NN`: the hidden tests, run against your work, producing a run directory with counts.

**Exception** [S0 seen, S5 handled] — Python's signal that something went wrong: an object raised at a point, propagating up the calls until something catches it, otherwise printed as a traceback.

**Expression / statement** [S1] — An expression produces a value (`2 + 3`, `len(x)`); a statement does something (`x = 5`, `if`, `for`). The REPL prints expressions back to you.

**f-string** [S1] — A string prefixed with `f` in which `{...}` is replaced by the value of the expression inside: `f"{name} is {age}"`. The course's standard way to format output and the first debugging tool: `f"{x=}"`.

**Fixture (data)** [S3] — The neighbourhood library: `books.csv`, `members.json`, `loans.txt` and the broken files, generated by `data/build_files.py` with a fixed seed.

**Fixture (pytest)** [S6] — A function that provides something to a test, declared as an argument by name.

**Floor division (`//`)** [S1] — Division rounding toward negative infinity. `7 // 2 == 3`; `-7 // 2 == -4`.

**Fork** [S2] — Your own copy of the course repository on GitHub, where your work lives.

**Function** [S4] — A named block of code with parameters that returns a value. The unit of reuse and of testing.

**Gate** [S1] — The pass/fail criteria at the end of a stage, with IDs `sNN-gK` and numeric thresholds.

**Generator** [S8] — A function with `yield`; it produces values one at a time on demand instead of building a list.

**Git** [S1] — The version-control program. Locally from stage 1; with GitHub from stage 2.

**Hidden tests** [S1] — Tests in `eval/` that you do not open before the gate; the inputs you have not seen.

**Identity** [S1] — Whether two names refer to the same object. `is` tests identity; `id()` shows it.

**Immutable / mutable** [S3] — Whether an object can be changed in place. Strings, numbers and tuples cannot; lists, dicts and sets can. Aliasing only bites on mutable objects.

**Import** [S3 use, S6 own] — Bringing a module's names into your program. `import csv`; `from pathlib import Path`.

**Indentation** [S2] — Leading spaces that mark a block. Four spaces. Always.

**Index** [S1] — Position in a sequence, counted from zero. `word[0]` is the first character; `word[-1]` the last.

**`input()`** [S0] — Pauses, waits for the user to type a line, returns it as a string. Always a string.

**Inspect (strand)** [S0] — The course's name for the Observe strand: seeing inside a running program. print → f-string debugging → debugger → logging → timeit/profiler.

**Instance** [S7] — One object made from a class. `Book("Dune", 1965)` is an instance of `Book`.

**Interpreter** [S0] — The program `python` that reads your file and runs it.

**Iterable / iterator** [S2 use, S8 define] — An iterable is anything a `for` loop can walk; an iterator is the object that hands out the items one at a time and is used up when done.

**JSON** [S5] — A text format for data (lists, dicts, strings, numbers, booleans, null) readable by almost every language. `json.load` / `json.dump`.

**Kill criteria** [S1] — The conditions under which you should not write the program: the standard library does it, a shell one-liner does it, a spreadsheet does it, it runs once.

**Keyword argument** [S4] — An argument passed by name: `greet(name="Ada")`. Order-independent; self-documenting.

**Lambda** [S3 intro, S4 deepened] — An anonymous one-expression function, most often as a `key=`: `sorted(books, key=lambda b: b.year)`.

**List** [S3] — An ordered, mutable sequence. The workhorse collection.

**Logging** [S5] — The `logging` module: timestamped, levelled messages you can turn up or down without editing the program. Replaces debugging `print`s that would otherwise ship.

**Method** [S1 use, S7 define] — A function attached to an object, called with a dot: `name.upper()`.

**Mini-project** [S1] — The last rung of every stage: a whole program using the stage's concepts, with its own Artefact Card.

**Module** [S6] — A `.py` file. A package is a folder of them with `__init__.py`.

**`mypy`** [S9] — A static type checker; reads the type hints and reports mismatches without running the program.

**Namespace** [S4] — Where names live. A function has its own; a module has its own; lookup goes local → enclosing → global → built-in.

**`None`** [S1] — The value that means "nothing here". What a function returns when it has no `return`. Test with `is None`.

**Object** [S1] — Everything in Python: a value with a type and an identity. Numbers, strings, functions, modules, classes.

**Oath (Programmer's)** [S0] — The eight habits in [docs/00](00-intent.md#the-programmers-oath).

**Off-by-one** [S2] — Looping one time too many or too few; the half-open range misread. Bestiary F01.

**Package manager** [S1] — `uv`: installs Python, creates environments, runs commands, adds dependencies.

**Parameter** — see *Argument*.

**Pickle** [S5] — Python's binary serialisation of arbitrary objects. Fast, convenient, and executes code on load; never load one you did not write. Bestiary E06.

**Pin** [S0] — An exact version of a tool recorded in [PINS.md](../PINS.md). Briefs never name versions.

**Planted bug** [S2] — A working-looking exercise with one deliberate fault; the task is to find and fix it with a test.

**Predict-then-run** [S0] — Write down what a snippet prints before running it. The core move of every break-lab.

**Property** [S8] — A method accessed like an attribute via `@property`; computed on read.

**Pull request (PR)** [S2] — A request to merge one branch into another on GitHub, with a description and review.

**`pyproject.toml`** [S6] — The file that names a project, its Python version and its dependencies.

**`pytest`** [S1 run, S6 write] — The test runner. Finds `test_*.py`, runs every `test_*` function, reports which assertions failed.

**REPL** [S0] — Read–Eval–Print Loop: the `>>>` prompt where you type one line and see its result.

**Return value** [S4] — What a function hands back to its caller via `return`. Distinct from what it prints.

**Rung** [S0] — One unit of instruction, ID `sNN-rM`, with a time estimate and a Run/See/Say Check.

**`ruff`** [S2] — The linter and formatter. Reports probable bugs and style; fixes many of them.

**Scope** — see *Namespace*.

**Sequence** [S1] — An ordered collection you can index and slice: `str`, `list`, `tuple`, `range`.

**Set** [S3] — An unordered collection of unique items; fast membership test.

**Shadowing** [S2] — Giving a variable the name of a built-in or an outer variable, hiding it. Bestiary F04.

**Slice** [S1] — A sub-sequence: `word[1:4]`, start included, stop excluded.

**`sorted()`** [S3] — Returns a new sorted list from any iterable; `key=` says what to sort by. Contrast `list.sort()`, which sorts in place and returns `None`.

**Standard library (stdlib)** [S3] — The modules that ship with Python: `csv`, `json`, `pathlib`, `collections`, `itertools`, `datetime`, `logging`, `argparse`, `unittest`… The first place to look before writing anything.

**Strand** [S0] — One of the four threads in every stage: Build, Measure, Break, Inspect.

**String** [S0] — Text. Immutable. Quotes of either kind.

**Terminal** [S0] — The text window where you type commands. Terminal on macOS, Windows Terminal or PowerShell on Windows.

**Test** [S1] — A small program that runs your code on a known input and asserts the output. The course's unit of measurement.

**Traceback** [S0] — The printout when an exception is not caught: the chain of calls, the line, the exception type and message. Read it bottom-up.

**Truthiness** [S1] — Every object counts as true or false in a condition: zero, empty and `None` are false; everything else true.

**Tuple** [S3] — An ordered, immutable sequence. For fixed-shape records; unpackable: `title, year = row`.

**Type** [S1] — The kind of a value: `int`, `str`, `float`, `bool`, `list`… `type(x)` tells you.

**Type hint** [S4] — An annotation on a parameter or return: `def area(w: float, h: float) -> float`. Documentation that `mypy` can check; Python itself ignores it.

**Unpacking** [S2] — Assigning several names at once from a sequence: `first, second = pair`; `for i, book in enumerate(books)`.

**`uv`** [S1] — The tool the course uses to install Python, run programs (`uv run`), manage environments and add packages (`uv add`).

**Variable** [S1] — A name bound to an object. Not a box; a label.

**Virtual environment** [S6] — A private folder of installed packages for one project, so projects do not interfere. `uv` makes and uses it for you.

**`with`** — see *Context manager*.

**`zip()`** [S2] — Pairs up items from two or more iterables, stopping at the shortest; `strict=True` to insist they match.
