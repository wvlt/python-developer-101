# Stage 3 — Collections

*Tier A · ~14 hours · Cost: zero · No new tool; the library fixture arrives (as Python literals)*

> **Outline.** This brief is at part level: the parts and planned rungs are fixed, the Contract and Gate are binding, but rungs have no Checks, exercises or hidden tests yet. It is rung-numbered one stage ahead of the first learner, after stage 2's feedback ([docs/13](../../docs/13-revision-protocol.md#rolling-readiness)). See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

Real programs work on many values at once: the books in a library, the lines of a file, the scores of a class. Python's four collections — list, tuple, dict, set — are how you hold them, and comprehensions are how you transform them in one line. This stage is also where the course's deepest quiet failure lives: two names on one list. You will put a second label on a list, change it through one label, see the change through the other, and never again be surprised when a "copy" was not one. From here the exercises use the neighbourhood library: 120 books, 60 members, 400 loans, as Python literals at the top of each exercise file until stage 5 teaches files.

## Contract

**Assumes** (from [stage 2](../02-decisions-and-repetition/README.md)): `if`/`elif`/`else` and the conditional expression (`s02-r1`, `s02-r2`); `while` with `break` (`s02-r4`); `for` over `range` and strings with the half-open rule (`s02-r5`); `continue` and loop `else` (`s02-r6`); `enumerate`, `zip` and unpacking two names (`s02-r7`); accumulators, running best, flags, nested loops (`s02-r8`); `ruff` clean and a GitHub fork with branches (`s02-r9`, `s02-r10`).

**Provides** (stage 4 takes these for granted):
- Lists: literal, index, slice, `append`, `insert`, `pop`, `remove`, `index`, `in`, `len`, iteration; `sorted()` with `key` and `reverse`; `sort()` vs `sorted()`; `min`/`max`/`sum`/`any`/`all` (`s03-r1`, `s03-r2`, `s03-r3`).
- A one-expression `lambda` as a `key=` (`s03-r2`).
- Aliasing: you can say "two names, one object", predict it, and copy with `[:]`, `list()`, `.copy()` and `copy.deepcopy` (`s03-r4`).
- Tuples, unpacking including `*rest`, swap (`s03-r5`).
- Dicts: `[]` vs `.get`, `setdefault`, `keys`/`values`/`items`, iteration, nested dicts, insertion order, a dict as a lookup table replacing `elif` (`s03-r6`, `s03-r7`).
- Sets: membership, `add`, `|`, `&`, `-`, deduplication (`s03-r8`).
- List, dict and set comprehensions with a condition (`s03-r9`).
- Choosing a collection for a task; shallow vs deep copy of nested data (`s03-r10`).
- A program that answers questions over a list of dicts of books (`s03-r11`).

Rung IDs: `s03-rM`; hidden case IDs `s03-rMeK-x`. Exercises are still whole programs over `input()`/`print()`, with the fixture data as a literal above the marker.

## Entry condition

Stage 2 gate passed. `just data` has run once (it builds `data/library/`; the stage 3 exercises embed samples from it, but the maintainer's generator reads it).

## Break-lab (first)

Eight snippets (`just break 03`), predict first. Planned targets: aliasing through assignment ([C01](../../docs/07-failure-bestiary.md#c--collections)); `print(items.sort())` ([C02](../../docs/07-failure-bestiary.md#c--collections)); `[[0] * 3] * 3` ([C04](../../docs/07-failure-bestiary.md#c--collections)); removing while iterating ([F05](../../docs/07-failure-bestiary.md#f--flow)); `d["missing"]` ([C03](../../docs/07-failure-bestiary.md#c--collections)); tuple item assignment ([C05](../../docs/07-failure-bestiary.md#c--collections)); set iteration order ([C06](../../docs/07-failure-bestiary.md#c--collections)); `"abc"[3]`. Two raise on purpose.

Question to carry: *when does `=` copy?* (Answer at rung 4: never.)

## Part A — Lists

### Rung 1 — Lists and their methods

*~60 min · feeds s03-r2, s03-r4, s03-r11*

Literal, index, slice (same rules as strings), `append`, `insert`, `pop`, `remove`, `index`, `in`, `len`, `for` over a list. Lists can change in place, which is the difference from strings and the reason rung 4 exists. Exercises: four whole programs over a literal list of book titles.

### Rung 2 — `sorted()`, `key`, and a first `lambda`

*~70 min · feeds s03-r11, s04-r6, s09*

`sorted(items)` returns a new list; `items.sort()` changes the list and returns `None`. `key=` says what to sort by; `lambda b: b["year"]` is a one-expression function written where it is used, and this rung introduces it only as a key (stage 4 deepens it). `reverse=True`. Stability: sorting twice by two keys. Exercises: sort books by year, by title length, by two keys.

### Rung 3 — `min`, `max`, `sum`, `any`, `all`, `in`

*~45 min · feeds s03-r11, s06*

The built-ins that replace a running-best or flag loop from stage 2 (and the first kill criterion of the stage: you wrote those loops in rung 8 of stage 2; now you do not). `min`/`max` with `key=`. Exercises: oldest book, most-borrowed, any overdue, all returned.

## Part B — Aliasing

### Rung 4 — Two names, one object

*~75 min · feeds s04-r3, s07-r3, s10 · bestiary C01, C04, F05*

`b = a` makes a second label, not a copy; `b.append(4)` is visible through `a`; `id()` and `is` show it; the box-versus-label picture from stage 1 rung 3 pays off. Copies: `a[:]`, `list(a)`, `a.copy()`; nested data needs `copy.deepcopy`. Mutating a list while iterating it skips items; iterate over a copy. Exercises: predict-and-fix programs where a "copy" was an alias.

## Part C — Tuples and dicts

### Rung 5 — Tuples and unpacking

*~45 min · feeds s03-r6, s04-r1, s07*

Immutable sequences for fixed-shape records: `("Dune", 1965)`. Unpacking: `title, year = book`; `first, *rest = items`; swap revisited. Tuples as dict keys. Exercises: a list of (title, year) tuples.

### Rung 6 — Dicts

*~70 min · feeds s03-r7, s03-r11, s05, s07*

Key → value; `d["k"]` raises `KeyError`, `d.get("k", default)` does not; `setdefault`; `keys()`, `values()`, `items()`; iteration in insertion order; a dict as a lookup table (the stage 2 kill criterion: `elif` chains become dicts). Exercises: count loans per member with `get`; translate a command word with a dict.

### Rung 7 — Nested data

*~60 min · feeds s03-r11, s05, s07*

A list of dicts (the books), a dict of lists (loans per member), a dict of dicts. Reaching in: `books[0]["title"]`. Building the nested structure in a loop. Exercises: group books by author; find the member with the most loans.

## Part D — Sets and comprehensions

### Rung 8 — Sets

*~40 min · feeds s03-r9, s09-r7*

Unique, unordered, fast membership. `set(items)` to deduplicate; `|`, `&`, `-` for union, intersection, difference. Exercises: authors in common between two members' loans; titles borrowed but never returned.

### Rung 9 — Comprehensions

*~70 min · feeds s04-r7, s08-r7, s09*

`[b["title"] for b in books if b["year"] > 2000]`; dict and set comprehensions; the loop it replaces shown side by side; when a loop is clearer (more than one condition, side effects). Exercises: rewrite four loops as comprehensions and one comprehension as a loop.

## Part E — Choosing

### Rung 10 — The right collection, and copies of nested things

*~45 min · feeds s03-r11, s07, s10*

A table: ordered? changeable? unique? lookup by key? → list, tuple, set, dict. Shallow vs deep copy on nested structures. The spreadsheet kill criterion: a list of dicts with 120 rows and five questions is a spreadsheet with five formulas, and that is a passing answer if you can show the spreadsheet.

## Part F — The catalogue

### Rung 11 — Mini-project: the catalogue

*~120 min · feeds gate s03-g1–g4; s04-r11*

A program over the embedded book list that answers five questions from `reference.json` (how many books by decade; the most prolific author; titles containing a word; the oldest and newest; members with overdue loans given a date), with the answers checked against the reference. The hidden set runs it on a second, held-out sample.

## Artefact

Exercises green; journal with the break-lab table and an aliasing drawing; Artefact Card; eval run directory; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s03-g1** `just eval 03` ≥ 54 of 60 hidden cases (count to be confirmed at rung-numbering; threshold stays 90 %).
- [ ] **s03-g2** The aliasing Say question answered with a drawing or the sentence "two names, one object", and a prediction for a fresh snippet the reviewer shows.
- [ ] **s03-g3** The catalogue answers the five questions on the held-out sample; the reviewer runs it.
- [ ] **s03-g4** Three Say questions from rungs 2, 4 and 6.

## Kill criteria

Five questions over 120 rows: a spreadsheet, and you should say so in the card. A lookup from word to word: a dict, not code. A running best: `max`, not a loop.

## Stretch

`collections.Counter` for rung 7's counting; `operator.itemgetter` instead of a `lambda` key; sort the books by (author, year) in one call.

## Reading

[docs/09 — Stage 3](../../docs/09-reading-list.md#stage-3--collections).
