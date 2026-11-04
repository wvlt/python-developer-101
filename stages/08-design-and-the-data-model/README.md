# Stage 8 — Design and the data model

*Tier C · ~14 hours · Cost: zero · No new tool; the comparison memo*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

`len(books)`, `for book in library`, `book in library`, `with open(...)`: Python's own objects answer to a small set of special methods, and when yours do too, they read like the language. This stage teaches the data model by making `Library` iterable, indexable, sizable and usable in a `with`; teaches generators so that 400 000 loans cost the same memory as 400; and teaches the one design decision every object-oriented codebase gets wrong at least once — inheritance where composition was wanted — by having you build both and count.

## Contract

**Assumes** (from [stage 7](../07-classes-and-objects/README.md)): classes with `__init__`, methods, `__repr__` (`s07-r1`, `s07-r2`); properties and classmethods (`s07-r4`, `s07-r5`); `__eq__`/`__hash__` (`s07-r6`); dataclasses and `Enum` (`s07-r7`, `s07-r8`); the library as objects with an ADR (`s07-r9`); context managers as a user (`s05-r4`); comprehensions (`s03-r9`).

**Provides** (stage 9 takes these for granted):
- Inheritance, `super().__init__`, overriding; when a subclass is wrong (`s08-r1`).
- Duck typing; an abstract base class; `typing.Protocol` as the lighter alternative (`s08-r2`).
- A comparison memo, inheritance vs composition, on the same requirement with tests, lines and change-count measured (`s08-r3`).
- `__len__`, `__getitem__`, `__contains__`; slicing your own class (`s08-r4`).
- Operator dunders (`__add__`, `__lt__`), `__call__`, `__bool__`; `functools.total_ordering` (`s08-r5`).
- Iterators vs iterables; `__iter__`/`__next__`; `StopIteration`; why an iterator is used up (`s08-r6`).
- Generators with `yield`; generator expressions; a lazy pipeline over the loans file; memory measured (`s08-r7`).
- Writing a context manager two ways; cleanup on error tested by raising inside the `with` (`s08-r8`).
- A `Library` you can `len`, index, iterate, test membership on and `with` (`s08-r9`).

Rung IDs: `s08-rM`; hidden case IDs `s08-rMeK-x`. Tests exercise the protocols directly (`len(lib)`, `list(lib)`, `"isbn" in lib`, raising inside `with lib:`).

## Entry condition

Stage 7 gate passed; `Library`, `Book`, `Member`, `Loan` exist with tests and an ADR.

## Break-lab (first)

Seven snippets. Targets: a subclass `__init__` that forgets `super()` ([O04](../../docs/07-failure-bestiary.md#o--objects)); iterating an iterator twice ([O05](../../docs/07-failure-bestiary.md#o--objects)); `list(gen)` for a look, then an empty loop ([O06](../../docs/07-failure-bestiary.md#o--objects)); a `@contextmanager` whose cleanup is after `yield` without `finally` ([O07](../../docs/07-failure-bestiary.md#o--objects)); `__eq__` defined, `__lt__` not, `sorted()` called; `__len__` returning a float; a class with `__bool__` returning `False` used in `if obj:`.

Question to carry: *what does `for` actually call?*

## Part A — Relationships

### Rung 1 — Inheritance and `super()`

*~60 min · feeds s08-r2, s08-r3*

`class StaffMember(Member)`; `super().__init__(...)`; overriding `loan_limit`; `isinstance`; the Liskov sentence in plain words (anywhere a `Member` works, a `StaffMember` must). Exercises: `StaffMember`, `ReferenceBook(Book)` that cannot be lent.

### Rung 2 — Duck typing, ABCs, `Protocol`

*~50 min · feeds s09-r3, s10*

If it has `__iter__`, you can loop over it; `abc.ABC` and `@abstractmethod` for "you must implement this"; `typing.Protocol` for "anything with this method", checked by `mypy` at stage 9. Exercises: a `Storage` protocol with `save`/`load`.

### Rung 3 — Composition over inheritance: the memo

*~80 min · feeds s08-r9, s10 (ADR)*

The same requirement (a library that logs every lend) built twice: `LoggingLibrary(Library)` and `Library(storage=…, logger=…)`; tests passing, lines, places to change for a new requirement, minutes to find a planted bug in each; the [comparison memo](../../templates/COMPARISON_MEMO.md). Exercise: the memo.

## Part B — The data model

### Rung 4 — `__len__`, `__getitem__`, `__contains__`

*~60 min · feeds s08-r9*

`len(library)`; `library[0]` and `library[1:3]` (handle `slice`); `isbn in library`; what Python falls back to when `__contains__` is missing. Exercises: the three methods on `Library`.

### Rung 5 — Operators, `__call__`, `__bool__`

*~50 min · feeds s10*

`Money.__add__` and `__lt__` with `total_ordering`; `__call__` for a callable object; `__bool__` for "empty library is false"; `NotImplemented`. Exercises: `Duration` arithmetic.

## Part C — Iteration

### Rung 6 — Iterators and iterables

*~50 min · feeds s08-r7 · bestiary O05*

`iter()` and `next()` by hand; `StopIteration`; `__iter__` returning a fresh iterator each time vs returning `self`; why a file object is used up. Exercises: `Library.__iter__`; a `Countdown` iterator.

### Rung 7 — Generators and lazy pipelines

*~70 min · feeds s09-r6, s10 · bestiary O06*

`yield`; a generator function over the loans file one line at a time; generator expressions; `sum(1 for loan in loans if loan.overdue(today))`; `tracemalloc` peak for list vs generator on a 400 000-line file (the generator built by repeating the fixture). Exercises: `read_loans(path)` as a generator; `overdue(loans, today)` as a pipeline.

## Part D — Context managers as authors

### Rung 8 — `__enter__`/`__exit__` and `@contextmanager`

*~60 min · feeds s10 · bestiary O07*

`class Timer` with `__enter__`/`__exit__`; the three arguments `__exit__` receives; `@contextlib.contextmanager` with `try: yield finally:`; a test that raises inside the `with` and asserts the cleanup ran; `Library` as a context manager that saves on exit. Exercises: both forms.

## Part E — The library, as a Python object

### Rung 9 — Mini-project: a `Library` that behaves like Python

*~120 min · feeds gate s08-g1–g4; s09-r8, s10*

`len`, `[]`, `in`, `for`, `with`; the loans loaded lazily; composition for storage and logging per the memo; tests for every protocol including the error path of `with`; ADR-002 recording the composition decision with the memo's numbers.

## Artefact

`src/library/` with the protocols; tests; `reports/comparison-<date>.md`; `decisions/ADR-002`; Artefact Card; eval run; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s08-g1** `just eval 08` ≥ 45 of 50 hidden cases (count confirmed at rung-numbering; 90 %).
- [ ] **s08-g2** The comparison memo passes the artefact rubric: both options measured on the same fields; differences inside noise called "not demonstrated".
- [ ] **s08-g3** The context manager cleans up when the body raises (the reviewer raises inside the `with` and checks).
- [ ] **s08-g4** The iterator-vs-iterable Say question with a one-line demonstration; two more Say questions from rungs 1 and 7.

## Kill criteria

A subclass that overrides most of its parent is a new class. A dunder nobody calls is noise. A generator over 400 items is a list; write the generator when the data does not fit, or arrives over time.

## Stretch

`__slots__` on `Loan` and memory measured; `__getattr__` for a proxy; `itertools.tee` and why it is rarely what you want.

## Reading

[docs/09 — Stage 8](../../docs/09-reading-list.md#stage-8--design-and-the-data-model).
