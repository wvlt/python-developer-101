# Stage 4 — Functions

*Tier B · ~14 hours · Cost: zero · Tool arrives: the debugger*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering, one stage ahead of the first learner. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

Every program so far was one long page. A function is a named piece of program with inputs and an output, and it is the unit of everything that follows: of reuse, of testing (from this stage the exercises are functions and the tests call them directly), of reading other people's code, and of the debugger, which stops *inside* one. It is also where two quiet failures live that every Python developer meets once the hard way: a default argument that remembers, and a name that is local when you thought it was not.

## Contract

**Assumes** (from [stage 3](../03-collections/README.md)): lists, `sorted` with a `lambda` key, built-in reducers (`s03-r1`–`r3`); aliasing and copying (`s03-r4`); tuples and unpacking (`s03-r5`); dicts and nested data (`s03-r6`, `s03-r7`); sets and comprehensions (`s03-r8`, `s03-r9`).

**Provides** (stage 5 takes these for granted):
- `def`, parameters, `return`, and that a function without `return` returns `None`; positional and keyword arguments; defaults; `*args`/`**kwargs` read and written (`s04-r1`, `s04-r2`).
- The mutable-default trap, predicted and avoided with `None` (`s04-r3`).
- Scope: local, enclosing, global, built-in; `UnboundLocalError`; why not `global` (`s04-r4`).
- A docstring and basic type hints on every function; pure functions vs side effects (`s04-r5`).
- Functions as values; `lambda` beyond `key=`; `map`/`filter` vs comprehensions; multi-key sorting (`s04-r6`, `s04-r7`).
- Closures and one decorator that times a function (`s04-r8`).
- Recursion on a nested list, and when a loop is better (`s04-r9`).
- `breakpoint()`, the terminal debugger's eight commands, and the editor's debugger with breakpoints and watches (`s04-r10`).
- The stage 3 catalogue rebuilt as functions with tests calling each (`s04-r11`).

Rung IDs: `s04-rM`; hidden case IDs `s04-rMeK-x`. From this stage exercises are function stubs with signature, type hints and docstring; tests import and call them.

## Entry condition

Stage 3 gate passed. The editor's Python extension installed (stage 0); the debugger it bundles is used at rung 10.

## Break-lab (first)

Eight snippets, predict first. Targets: `print(f())` where `f` only prints ([N01](../../docs/07-failure-bestiary.md#n--functions-and-scope)); `def add(item, items=[])` called twice ([N02](../../docs/07-failure-bestiary.md#n--functions-and-scope)); `total += 1` inside a function ([N03](../../docs/07-failure-bestiary.md#n--functions-and-scope)); `[lambda: i for i in range(3)]` ([N04](../../docs/07-failure-bestiary.md#n--functions-and-scope)); `print(len)` without brackets ([S07](../../docs/07-failure-bestiary.md#s--syntax-and-names-always-loud)); a function that mutates its argument list; recursion without a base case ([N06](../../docs/07-failure-bestiary.md#n--functions-and-scope)); a function called before it is defined.

Question to carry: *where does a name live?*

## Part A — Defining

### Rung 1 — `def` and `return`

*~60 min · feeds every later rung*

The smallest function; calling it; the difference between printing and returning; `None` when there is no `return`; a function with two parameters. Exercises: `area(w, h)`, `last_character(word)`, `is_even(n)`.

### Rung 2 — Arguments: positional, keyword, default, `*args`, `**kwargs`

*~60 min · feeds s04-r3, s05-r9, s06*

Call shapes; defaults for the common case; reading a signature in documentation; writing `*args` once so `print` stops being magic. Exercises: `greet(name, greeting="Hello")`, `mean(*numbers)`.

### Rung 3 — The default that remembers

*~45 min · feeds s07-r3, s10 · bestiary N02*

Defaults are evaluated once; a list default is shared across calls; the `None` idiom. Exercises: find-and-fix.

## Part B — Scope

### Rung 4 — Where names live

*~60 min · feeds s04-r8, s06 · bestiary N03*

Local, enclosing, global, built-in; assignment makes a name local for the whole function; `UnboundLocalError`; pass it in and return it instead of `global`. `just trace` on a two-function program shows the locals change. Exercises: predict-and-fix.

## Part C — Documenting

### Rung 5 — Docstrings, type hints, and purity

*~50 min · feeds every later stage; s09-r3*

A one-line docstring that says what it returns; `help()` shows it; type hints as documentation (`mypy` checks them at stage 9); a pure function (same inputs → same output, nothing else changed) is easy to test and the course's default. Exercises: add docstrings and hints to the stage 3 catalogue's helpers.

## Part D — Functions as values

### Rung 6 — Functions are values; `lambda` deepened

*~50 min · feeds s04-r7, s08, s09*

A function assigned to a name, passed as an argument, stored in a dict (the command dispatch from stage 2's `match` as a dict of functions); `lambda` for any one-expression function and the rule for when to use `def` instead. Exercises: a dict of operations.

### Rung 7 — `map`, `filter`, and multi-key sorting

*~45 min · feeds s08-r7, s09*

`map`/`filter` vs comprehensions (prefer the comprehension; recognise the other); `sorted(key=lambda b: (b["author"], -b["year"]))`. Exercises: sort books by two keys; filter with a function.

### Rung 8 — Closures and a first decorator

*~60 min · feeds s08, s09-r6 · bestiary N04*

A function that returns a function; what it remembers; late binding in a loop and the `i=i` fix; a `@timed` decorator in ten lines, used on the catalogue's slowest function. Exercises: `make_counter()`, `@timed`.

## Part E — Recursion

### Rung 9 — Recursion and when not to

*~50 min · feeds s08 · bestiary N06*

Base case and recursive case; walk a nested list of lists; `RecursionError`; the loop version beside it, and the rule: recurse on recursive data, loop on flat data. Exercises: `flatten`, `total_size`.

## Part F — Inspect: the debugger

### Rung 10 — Stop the program and look

*~70 min · feeds every later stage; s09*

`breakpoint()` on a line; `n`, `s`, `c`, `p`, `pp`, `l`, `w`, `q`; watch a variable change step by step; then the same in the editor: a red dot, the Run and Debug panel, Variables and Watch, step over / into / out. The habit: a wrong value is found by stopping on the line before it, not by staring at the code. Exercise: a provided program with a wrong total; find the line with the debugger; journal the session (`templates/JOURNAL.md`, debugger entry).

## Part G — The catalogue, as functions

### Rung 11 — Mini-project: the catalogue, tested

*~120 min · feeds gate s04-g1–g4; s05-r11, s06*

The stage 3 program split into functions, one per question, each with a docstring and hints, each called directly by the tests. Plus a `main()` that asks which question and prints the answer. The hidden set calls the functions on the held-out sample.

## Artefact

Exercises green; journal with break-lab table and a debugger-session entry naming the variable watched; Artefact Card; eval run; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s04-g1** `just eval 04` ≥ 54 of 60 hidden cases (count confirmed at rung-numbering; 90 %).
- [ ] **s04-g2** Every function in `exercises/` and the mini-project has a docstring and type hints (a script checks).
- [ ] **s04-g3** A debugger session journaled: the line, the variable, what it showed, what was expected; and at review the learner sets a breakpoint and shows a value on request.
- [ ] **s04-g4** The mutable-default Say question, with the fix, from memory; two more Say questions from rungs 4 and 8.

## Kill criteria

A function called once, from one place, that fits in three lines, is three lines. A one-off task (this file, today) is a script, not a function library. Recursion on flat data is a loop.

## Stretch

`functools.lru_cache` on a recursive function and the timing before and after; a decorator that counts calls; read `help(sorted)` in full.

## Reading

[docs/09 — Stage 4](../../docs/09-reading-list.md#stage-4--functions).
