# data/ — fixtures

Everything a brief points at that is not code the learner writes. Generated, not committed, so a fresh clone is small and the build step is part of the stage-3 entry condition. Specs are in [docs/15 — Authoring guide](../docs/15-authoring-guide.md#fixtures-and-data).

| Fixture | Build | Used from | Committed? |
|---|---|---|---|
| `library/` — the neighbourhood library world | `python data/build_files.py` (or `just data`) | s03 | no (regenerated; ~90 KB; deterministic) |

## The neighbourhood library world

A small, fictional, suburban lending library. Purpose-built so that learners have not seen the answers, so that the files are messy in the ways real exports are messy, and so that there is nothing external to download.

**Schema v1, seed 42:**

| File | Shape | Size |
|---|---|---|
| `books.csv` | `book_id,title,author,year,genre,pages,isbn,copies` | 120 rows |
| `members.json` | list of `{member_id, name, email, suburb, joined}` | 60 members |
| `loans.txt` | one loan per line, `loan_id\|member_id\|book_id\|out\|due\|returned\|status`; a comment line, blank lines, stray spaces, inconsistent capitalisation of `status` | 400 loans |
| `broken/books_latin1.csv` | `books.csv` saved in Latin-1 with one accented author; opening it as UTF-8 raises `UnicodeDecodeError` | |
| `broken/books_missing_column.csv` | no `pages` column; `row["pages"]` raises `KeyError` | |
| `broken/members_duplicate_ids.json` | two members share `M007` | |
| `broken/loans_bad_dates.txt` | lines 3, 17 and 25 carry impossible or mis-formatted dates | |
| `openlibrary_sample.json` | a response in the shape of the public API pinned in `PINS.md`, synthetic content, for offline use at stage 6 | |
| `reference.json` | the right answer to thirty questions (`q01`…`q30`) plus the facts about the broken files | |

**Why these files.** CSV, JSON and a line-oriented text file are the three shapes a junior meets in week one. `loans.txt` is deliberately messy so that stage 5's "read a file without crashing" has something to survive. The broken files exist so that `UnicodeDecodeError`, `KeyError` and duplicate keys are met on purpose, with a known cause, before they are met by accident. `reference.json` makes every exercise that reads the fixture gradable without a human.

**"Today" is fixed.** Every overdue calculation uses `as_of` from `reference.json` (2026-03-01), never the real clock, so answers are stable.

**Determinism.** Same seed, byte-identical files; CI rebuilds twice and diffs. `--seed N` produces a different world with the same shape, used for the held-out hidden tests from stage 3 (seed 42 to develop, seed 7 to grade).

**Licence.** Generated synthetic data, CC0. Names are drawn from short word lists and do not refer to real people; titles are generated from word lists and do not refer to real books; email addresses use `example.com`.

## Rebuilding

```bash
python data/build_files.py            # writes data/library/
python data/build_files.py --seed 7   # a held-out world
```

or `just data`.
