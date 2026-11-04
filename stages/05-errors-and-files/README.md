# Stage 5 — Errors, files and the outside world

*Tier B · ~14 hours · Cost: zero · Tools arrive: `logging`, `argparse`; the fixture arrives as files*

> **Outline.** Part level: parts, planned rungs, Contract and Gate are fixed; Checks, exercises and hidden tests arrive at rung-numbering. See [`REVISIONS.md`](REVISIONS.md).

## Why this stage exists

Until now every input came from a test. Real inputs come from files that are missing, malformed, in the wrong encoding, or edited by hand; from users who type the wrong thing; from a clock. A program meets the outside world through exceptions, and the two wrong responses are to crash on the first bad line or to swallow the error and report success. This stage teaches the third response — handle what you can, log what you skipped, raise what you cannot — on the library's four deliberately broken files. It is also where `pickle` is met once, understood, and put away: you will see the eight lines that make loading a pickle run arbitrary code, and you will never load one you did not write.

## Contract

**Assumes** (from [stage 4](../04-functions/README.md)): functions with docstrings and hints (`s04-r1`, `s04-r5`); defaults and `*args` (`s04-r2`); scope (`s04-r4`); functions as values (`s04-r6`); the debugger (`s04-r10`); dicts and nested data (`s03-r6`, `s03-r7`).

**Provides** (stage 6 takes these for granted):
- `try`/`except`/`else`/`finally`; catching specific types; `raise`; re-raising; the exception hierarchy; custom exception classes with a message a user can act on (`s05-r1`, `s05-r2`).
- Reading a traceback through three function calls to its root (`s05-r3`).
- `with open(...)` with `encoding="utf-8"`; `pathlib.Path`; reading and writing text; newline handling (`s05-r4`).
- `csv.DictReader`/`writer` with `newline=""`; `json.load`/`dump` with `indent` (`s05-r5`, `s05-r6`).
- `pickle`: what it is, where it is useful (a cache you wrote yourself), why never on untrusted data, and the JSON-vs-pickle comparison (`s05-r7`).
- `datetime`, `date`, `timedelta`, parsing and formatting dates (`s05-r8`).
- `argparse` with positional arguments, options, `--help`; environment variables via `os.environ` (`s05-r9`).
- `logging` with levels, `basicConfig`, a logger per file, `exc_info=True`; debugging prints replaced (`s05-r10`).
- A program that reads all three fixture files, skips and logs bad lines with line numbers, and reports overdue loans as of a date (`s05-r11`).

Rung IDs: `s05-rM`; hidden case IDs `s05-rMeK-x`. Exercises are functions taking paths; tests copy fixture files into `tmp_path`, including the broken ones, and check both the return value and the log.

## Entry condition

Stage 4 gate passed. `just data` run; `data/library/` contains `books.csv`, `members.json`, `loans.txt`, `broken/` and `reference.json`.

## Break-lab (first)

Eight snippets. Targets: `except: pass` hiding a typo ([E01](../../docs/07-failure-bestiary.md#e--errors-and-io)); `open` without `encoding` on `broken/books_latin1.csv` ([E02](../../docs/07-failure-bestiary.md#e--errors-and-io)); a relative path run from another directory ([E03](../../docs/07-failure-bestiary.md#e--errors-and-io)); writing without `with` and reading back nothing ([E04](../../docs/07-failure-bestiary.md#e--errors-and-io)); CSV with doubled blank lines ([E05](../../docs/07-failure-bestiary.md#e--errors-and-io)); the pickle that opens a calculator ([E06](../../docs/07-failure-bestiary.md#e--errors-and-io)); `eval(input())` ([E07](../../docs/07-failure-bestiary.md#e--errors-and-io)); `int("12a")` ([T07](../../docs/07-failure-bestiary.md#t--types-and-values)).

Question to carry: *what should a program do with a line it cannot read?*

## Part A — Exceptions

### Rung 1 — `try`, `except`, `else`, `finally`

*~60 min · feeds every later rung · bestiary E01, E08*

The ask-until-valid loop from stage 2 rewritten with `try: int(text) except ValueError:`; the shape of each clause; catch the specific type; catch close to the cause. Exercises: `parse_int_or_none`, `safe_divide`.

### Rung 2 — `raise`, custom exceptions, the hierarchy

*~60 min · feeds s05-r11, s08, s10*

`raise ValueError("…")` with a message a user can act on; a `class LoanError(Exception)` in two lines (classes proper are stage 7; this is the one use that cannot wait); re-raising; `assert` for things that must be true in your own code, never for user input. Exercises: `member_or_raise`.

### Rung 3 — Reading a long traceback

*~40 min · feeds every later stage*

A provided program three functions deep that fails at the bottom; read bottom-up, find the frame that is yours, find the value that was wrong; then the same with the debugger's post-mortem (`pdb.pm()`). Exercise: journal the read.

## Part B — Files

### Rung 4 — `with`, `pathlib`, text and encoding

*~60 min · feeds s05-r5–r7, s05-r11 · bestiary E02, E04*

`with open(path, encoding="utf-8") as f:` and why both halves; `Path(__file__).parent / "data"`; `read_text`, `write_text`, `iterdir`; `splitlines`; the Latin-1 file and `UnicodeDecodeError`; the "Unicode sandwich". Context managers are *used* here; stage 8 writes one. Exercises: `count_lines`, `read_loans_text`.

### Rung 5 — CSV

*~45 min · feeds s05-r11, s10*

`csv.DictReader` on `books.csv`; `newline=""`; the missing-column file and the duplicate-IDs file; writing with `csv.writer`. Exercises: `load_books`, `write_report`.

### Rung 6 — JSON

*~45 min · feeds s05-r7, s05-r11, s10*

`json.load`/`dump`, `indent=2`; round-tripping `members.json`; what JSON can and cannot hold (no dates, no tuples); `json.dumps` for a quick look at nested data. Exercises: `load_members`, `save_members`.

### Rung 7 — `pickle`: once, properly

*~45 min · feeds s10 (comparison memo) · bestiary E06*

`pickle.dump`/`load` of a dict; it keeps types JSON loses; the eight-line pickle that runs code on load; the rule (never load a pickle you did not write, in this program, on this machine); the JSON-vs-pickle table (size, speed, safety, readability) measured on `members.json`. Exercise: a memo cache for the catalogue's slowest question, with a comment stating the rule.

## Part C — Time and the command line

### Rung 8 — Dates

*~45 min · feeds s05-r11, s10*

`date.fromisoformat`, `timedelta(days=21)`, comparison, `strftime`; the bad-dates file and how `ValueError` from parsing is handled per line. Exercises: `due_date`, `days_overdue`.

### Rung 9 — `argparse` and the environment

*~60 min · feeds s06, s10*

`sys.argv` once, then `argparse`: a positional path, `--as-of`, `--verbose`, automatic `--help`; `os.environ.get("LIBRARY_DATA_DIR", default)`; the `.env.example` file in the repo. Exercises: a CLI wrapper for `days_overdue`.

## Part D — Inspect: logging

### Rung 10 — `logging` instead of `print`

*~50 min · feeds s06, s09, s10*

`logging.basicConfig(level=…)`; `logger = logging.getLogger(__name__)`; `debug`/`info`/`warning`/`error`; `exc_info=True` inside `except`; `--verbose` flips the level; every skipped line logged with its line number. The debugging prints from stages 1–4 become `logger.debug`. Exercise: instrument `read_loans_text`.

## Part E — The loans report

### Rung 11 — Mini-project: the loans report

*~130 min · feeds gate s05-g1–g4; s06-r10, s10*

`uv run python report.py data/library --as-of 2026-03-01`: loads books, members and loans; skips and logs every bad line (the hidden set runs it on the four broken files and greps the log); prints members with overdue loans, days overdue, sorted; `--json` writes the same to a file; exit code 1 with a one-line message if the directory is missing. Custom exceptions for the user-facing failures.

## Artefact

Exercises green; journal including the long-traceback read and the pickle demonstration; `FAILURE_REVIEW.md` recommended from here; Artefact Card; eval run; PR.

## Gate

Universal `u1`–`u10`, and:

- [ ] **s05-g1** `just eval 05` ≥ 54 of 60 hidden cases, including the four broken-file cases (count confirmed at rung-numbering; 90 %).
- [ ] **s05-g2** The report's log names every skipped line with its line number (the reviewer greps for the three bad dates and the duplicate ID).
- [ ] **s05-g3** A long traceback read to its root and journaled; at review, the learner reads a fresh one aloud.
- [ ] **s05-g4** The pickle Say question ("why never unpickle untrusted data?") answered with the mechanism; two more Say questions from rungs 1 and 4.

## Kill criteria

A one-line question about a CSV (`how many rows?`) is `wc -l`. A conversion of one file, once, is a spreadsheet import. A program that reads a file and prints a column is a shell one-liner (`cut`); write the program when it must skip bad lines and say which.

## Stretch

`tempfile` for safe writes; `shutil.copy` to back up before writing; a `--format csv|json|text` option; read the `csv` module's dialect documentation.

## Reading

[docs/09 — Stage 5](../../docs/09-reading-list.md#stage-5--errors-files-and-the-outside-world).
