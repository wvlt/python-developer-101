# 09 — Reading list

Curated, not comprehensive. Each item has a stage and a reason. Nothing here costs money; nothing requires an account. When a rung says "Reading", it points at one of these. Items are swapped, not accumulated; a reading that is no longer the best for its slot is removed.

Read *after* the rung, not before: the course teaches by worked example first, and reading about a concept you have already used lands differently from reading about one you have not.

Live links and versions are checked at every re-pin (see [11 — Curriculum maintenance](11-curriculum-maintenance.md)).

## Stage 0 — Hello Python

- **The Python Tutorial, chapter 1–3** (docs.python.org/3/tutorial) · Read "Using the Python Interpreter" and "An Informal Introduction" after rung 7. It is the canonical voice and it is free; you will come back to it for the rest of your life.
- **"Errors and Exceptions" — the first two sections only** (Python Tutorial, chapter 8) · After rung 5. Syntax errors versus exceptions, in the language's own words.

## Stage 1 — Values and names

- **Ned Batchelder, "Facts and Myths about Python names and values"** (nedbatchelder.com/text/names.html) · After rung 3. The single most useful 30 minutes a Python beginner can spend. Names are labels, not boxes. Read it again at stage 3.
- **Python Tutorial 3.1.2, "Text"** · After rung 5. Indexing, slicing, immutability, in the canonical voice.
- **Format Specification Mini-Language** (docs.python.org/3/library/string.html#formatspec) · Reference only, after rung 6. You do not read it; you look things up in it.
- **"What every programmer should know about floating point", the two-page summary** — e.g. floating-point-gui.de · After rung 1's break-lab. Why `0.1 + 0.2` is what it is.
- **Pro Git, chapters 1–2** (git-scm.com/book) · After rung 8. Free online. Read only "Getting Started" and "Git Basics".

## Stage 2 — Decisions and repetition

- **Python Tutorial, chapter 4 "More Control Flow Tools"** · After rung 6. `if`, `for`, `range`, `break`/`continue`/`else`, `match`.
- **PEP 636, "Structural Pattern Matching: Tutorial"** · After rung 3. Read the first half; the rest is for stage 7.
- **The `ruff` rules documentation, entries E722, F632, B006, A001** (docs.astral.sh/ruff/rules) · After rung 9. Each rule page is a one-screen explanation of a bestiary entry.
- **GitHub Docs, "Hello World" and "Fork a repository"** · With rung 10.

## Stage 3 — Collections

- **Python Tutorial, chapter 5 "Data Structures"** · After rung 4. Lists, tuples, sets, dicts, comprehensions, in order.
- **Ned Batchelder, "Facts and Myths" — second read** · After the aliasing break-lab. It will read differently now.
- **Sorting HOW TO** (docs.python.org/3/howto/sorting.html) · After the `sorted()` rung. `key=`, stability, `reverse`, `operator.itemgetter`.
- **`collections` module docs, `Counter` and `defaultdict` sections** · After the mini-project. Two tools that replace ten lines each.

## Stage 4 — Functions

- **Python Tutorial 4.8–4.9, "Defining Functions" and "More on Defining Functions"** · After rung 2. Defaults, keyword arguments, `*args`, `**kwargs`, docstrings.
- **"Python Scope & the LEGB Rule"** — any clear explanation; Real Python's is free to read · After the scope rung.
- **`pdb` module documentation, the command list** · Reference, after the debugger rung. Eight commands do 95 % of the work: `n`, `s`, `c`, `p`, `pp`, `l`, `w`, `q`.
- **PEP 8, sections "Naming Conventions" and "Programming Recommendations"** · After the mini-project. Not before; conventions without code to apply them to are noise.

## Stage 5 — Errors, files and the outside world

- **Python Tutorial, chapter 8 "Errors and Exceptions" — all of it this time** · After rung 2.
- **Python Tutorial 7.2, "Reading and Writing Files"** and **the `pathlib` basic use section** · After the files rung.
- **"Pragmatic Unicode" (Ned Batchelder, PyCon 2012)** — the text version · After the encoding break-lab. The "Unicode sandwich".
- **Python docs, `pickle` module — the red warning box, then "Comparison with json"** · After the pickle rung. Read the warning aloud.
- **`argparse` tutorial** (docs.python.org/3/howto/argparse.html) · With the argparse rung.
- **Logging HOWTO, "Basic Logging Tutorial"** · With the logging rung. Stop at "Advanced".

## Stage 6 — Modules, packages and tooling

- **Python Tutorial, chapter 6 "Modules"** · After rung 1.
- **Python Standard Library index — "Brief Tour", chapters 10 and 11** · With the stdlib tour rung. You are not learning these; you are learning that they exist.
- **`uv` guide, "Working on projects"** (docs.astral.sh/uv/guides/projects) · With the `uv add` rung.
- **pytest documentation, "How to write and report assertions" and "How to parametrize fixtures and test functions"** · With your first written tests.
- **`requests` quickstart** · With the Open Library rung. Only the quickstart.

## Stage 7 — Classes and objects

- **Python Tutorial, chapter 9 "Classes" (9.1–9.5)** · After rung 2.
- **`dataclasses` module docs, down to `field()`** · After the dataclass rung.
- **Raymond Hettinger, "Python's Class Development Toolkit" (PyCon 2013 talk)** — free on YouTube; the slides alone work · After the mini-project. Why each piece of a class exists.

## Stage 8 — Design and the data model

- **Python Language Reference, 3.3 "Special method names"** · Reference, with the data model rung. Skim headings; look up as needed.
- **Luciano Ramalho, "Fluent Python", chapter 1 "The Python Data Model"** — the first chapter is often free as a sample · After the dunder rung.
- **"Composition over inheritance"** — any clear statement; Brandon Rhodes's "The Composition Over Inheritance Principle" (python-patterns.guide) · With the comparison memo.
- **`contextlib` docs, `contextmanager`** · With the context-manager authoring rung.
- **Python Tutorial 9.8–9.10, "Iterators", "Generators", "Generator Expressions"** · With the iteration protocol rung.

## Stage 9 — Writing Python well

- **PEP 8 in full, and PEP 20 (`import this`)** · After the first ruff-format rung. Now you have enough code to see what they are about.
- **mypy documentation, "Getting started" and "The mypy command line — strict"** · With the typing rung.
- **`timeit` docs, "Basic Examples"; `cProfile` docs, "Instant User's Manual"** · With the measurement rung.
- **Coverage.py docs, "Quick start"** · With the coverage rung.
- **Code reading:** one standard-library module per the brief (`statistics.py` first; it is short, pure Python and well documented). Read it in the editor with the debugger attached.
- **Brandon Rhodes, "Stop Writing Classes" (PyCon 2012)** · With the kill-criteria rung.

## Stage 10 — Capstone

- **Python Packaging User Guide, "Packaging Python Projects"** — the `pyproject.toml` section · With `uv build`.
- **"Writing a good README"** — any clear guide (makeareadme.com is free and short) · Before writing yours.
- **The AI Agents 101 Stage 0 brief** (sibling course) · For the hand-off rung: read its Contract and tick each *Assumes* against your own rungs.
- **The Data Science 101 Stage 0 brief** (sibling course, when published) · Same.

## Books (optional, none required)

- **"Python Crash Course" (Eric Matthes)** — for a learner who wants a second, slower pass over stages 1–5.
- **"Fluent Python" (Luciano Ramalho)** — for after stage 8. Not before; it assumes you can already write Python.
- **"The Pragmatic Programmer" (Hunt & Thomas)** — for after stage 9; the habits in the Oath, at book length.

## What is deliberately not here

Video courses, interactive sandboxes, LeetCode-style puzzle sites, and anything that writes the code for you. Puzzle sites teach puzzle solving; the course's destination is useful in a team on day one, which is a different skill. If you find a resource you think belongs here, open a stage-feedback issue with the stage, the rung it supports and the reason.
