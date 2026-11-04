# Stage 7 — Classes and objects

*Tier C · ~12 hours · Cost: zero · No new tool; the first required ADR; AI review of your own code allowed from here*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

Your library package passes dicts around: a book is `{"title": …, "year": …}` and every function that touches one must know its keys. A class puts the data and the behaviour that belongs to it in one thing with a name, so that `book.is_overdue(today)` reads as what it is. This stage teaches classes by converting the package you already have, and teaches the question that matters more than the syntax: *does this need to be a class?* Half the mini-projects reviewers see at this stage have a class that should have been a dict and a dict that should have been a class; the kill criterion is the lesson.

From this stage the AI-assistance policy changes: you may ask an assistant to *review* code you have written. You still write every line.

## Contract

**Assumes** (from [stage 6](../06-modules-and-tooling/README.md)): a package with modules and your own tests (`s06-r2`, `s06-r8`, `s06-r9`); `namedtuple` seen (`s06-r3`); custom exception classes in their two-line form (`s05-r2`); dicts of dicts (`s03-r7`); aliasing (`s03-r4`).

**Provides** (stage 8 takes these for granted):
- Why classes; `class`, `__init__`, `self`; instance attributes; methods; `__repr__` and `__str__` (`s07-r1`, `s07-r2`).
- Class attributes vs instance attributes and the shared-mutable trap; `@property` with a setter and a computed attribute; `@classmethod` as an alternate constructor; `@staticmethod` (`s07-r3`, `s07-r4`, `s07-r5`).
- `__eq__` and `__hash__` together; objects in sets and as dict keys (`s07-r6`).
- `@dataclass` with `field(default_factory=…)`, `frozen=True`, `order=True`; `Enum` (`s07-r7`, `s07-r8`).
- An ADR choosing dataclass vs class vs dict for each record in the library (`s07-r9`).
- `Book`, `Member`, `Loan` and `Library` classes driving the package, tests updated (`s07-r9`).

Rung IDs: `s07-rM`; hidden case IDs `s07-rMeK-x`. Exercises are class stubs; tests construct and call.

## Entry condition

Stage 6 gate passed; the library package has ≥ 15 tests.

## Break-lab (first)

Seven snippets. Targets: a method without `self` ([S08](../../docs/07-failure-bestiary.md#s--syntax-and-names-always-loud)); `class Member: loans = []` shared across instances ([O02](../../docs/07-failure-bestiary.md#o--objects)); `__eq__` without `__hash__` in a set ([O03](../../docs/07-failure-bestiary.md#o--objects)); the default `__repr__` (`<Book object at 0x…>`) in the debugger; a dataclass with a list default (refused by Python, read the message); comparing two dataclass instances with `==` vs `is` ([T05](../../docs/07-failure-bestiary.md#t--types-and-values)); `self.title` vs `title` inside a method.

Question to carry: *what does `self` refer to?*

## Part A — A first class

### Rung 1 — Why, `class`, `__init__`, `self`

*~60 min · feeds every later rung*

The dict version of a book beside the class version; `__init__` sets attributes on `self`; constructing two instances; `self` is the instance the method was called on. Exercises: `Book`, `Member`.

### Rung 2 — Methods, `__repr__`, `__str__`

*~60 min · feeds s07-r9, s08*

A method is a function that receives the instance; `book.is_overdue(today)`; `__repr__` so the debugger shows `Book('Dune', 1965)` instead of an address; `__str__` for people. Exercises: `Loan` with `days_overdue`.

## Part B — Attributes

### Rung 3 — Class vs instance attributes

*~45 min · feeds s07-r7 · bestiary O02*

A class attribute is one object shared by all; `self.loans = []` in `__init__` is per instance; the trap and the dataclass that refuses it. Exercises: find-and-fix.

### Rung 4 — `@property`

*~50 min · feeds s08, s10*

A computed attribute (`loan.due_date`); a setter that validates; when a property is better than a method (no arguments, cheap, no side effects). Exercises: `Member.active_loans`.

### Rung 5 — `@classmethod` and `@staticmethod`

*~45 min · feeds s10 (`from_json`)*

`Book.from_csv_row(row)` and `Member.from_json(d)` as alternate constructors; `@staticmethod` for a helper that belongs with the class but needs no instance. Exercises: the two constructors.

## Part C — Equality

### Rung 6 — `__eq__` and `__hash__`

*~50 min · feeds s07-r7, s08 · bestiary O03*

By default two instances are equal only if they are the same object; defining `__eq__` by `isbn`; why `__hash__` must agree; books in a set. Exercises: `Book.__eq__`/`__hash__`.

## Part D — Records

### Rung 7 — `@dataclass`

*~60 min · feeds s08, s10*

The same `Book` in five lines; `field(default_factory=list)`; `frozen=True` gives `__hash__` for free; `order=True`; `asdict` for JSON; when a dataclass is not enough (an invariant between fields, behaviour that owns state). Exercises: convert `Book` and `Loan`; keep `Library` a class.

### Rung 8 — `Enum`

*~30 min · feeds s10*

`class Status(Enum): ON_LOAN = "on_loan"`; `Status("on_loan")`; `match` on an enum member. Exercise: loan status.

## Part E — The library, as objects

### Rung 9 — Mini-project: `Book`, `Member`, `Loan`, `Library`

*~120 min · feeds gate s07-g1–g4; s08-r9, s10*

The package's dicts become instances; `Library` holds the collections and owns `lend`, `return_book`, `overdue(as_of)`; tests updated and extended; an ADR (`decisions/ADR-001-…`) for each record type: dataclass, class or dict, with the fields in the template measured (lines, tests, places to change when a field is added).

## Artefact

Classes in `src/library/`; tests; `decisions/ADR-001`; Artefact Card with the AI-review field filled for the first time; eval run; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s07-g1** `just eval 07` ≥ 45 of 50 hidden cases (count confirmed at rung-numbering; 90 %).
- [ ] **s07-g2** The dataclass-vs-class Say question answered with one example of each from the learner's own package and the reason.
- [ ] **s07-g3** Every class has a `__repr__` that the reviewer finds useful when they break into the debugger.
- [ ] **s07-g4** ADR-001 passes the artefact rubric (≥ 2 options with the same measured fields; one decisive reason); two more Say questions from rungs 3 and 6.

## Kill criteria

A class with no methods and no invariant is a dict or a dataclass. A class with one method is a function. A class because "it is more professional" is the bestiary's [H06](../../docs/07-failure-bestiary.md#h--human-and-process). Ask: what state does it own, what must stay true about that state, and what behaviour belongs to it? Two of three, or no class.

## Stretch

`__slots__` and the memory difference measured on 10 000 books; `functools.total_ordering`; `dataclasses.replace`.

## Reading

[docs/09 — Stage 7](../../docs/09-reading-list.md#stage-7--classes-and-objects).
