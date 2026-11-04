# Revisions — Stage 0

Rung-level change log for this stage. Every change to a rung, done-when wording, entry condition or contract is recorded here with the feedback that caused it. Stage-level changes (outcome, position) are ADRs in `docs/decisions/` and are only referenced here. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Verified** (2026-11-04, v1.0.0): eight rungs `s00-r0`–`s00-r7` in three parts, each with a Run/See/Say Check. Every code block was executed on macOS (see the reference run below); three rung changes came out of it. Windows run at the first re-pin. Rung IDs are stable; insertions use a letter suffix.

## Log

- 2026-11-04 · s00-r0–r7 · Stage created (v0.4) from the course inputs' hello-world specification: install, prompt, file, change text, two things, number vs word, three deliberate failures, `input()`, the folder-file-comment habit. Rung 6 uses `print("Hello,", input(...))` rather than a variable so that stage 1 rung 3 is the first place a name is bound; the focus map (docs/17) records this as a deliberate deferral. Break-lab is three paper predictions made before installation, resolved at rungs 1, 4 and 5.

- 2026-11-04 · s00-r1 · Reference run: the prompt's banner is two lines, not three. Brief now says "Two lines of text appear (the version, then a line that starts `Type "help"`)". Step change.
- 2026-11-04 · s00-r5 · Reference run: Way 3 showed only the last line of the traceback while Ways 1 and 2 showed the whole block; a learner reading "from the bottom line up" needs the block. Full traceback added, with one sentence on the `~`/`^` markers. Step change.
- 2026-11-04 · s00-r7 · Reference run: the comment line used an em dash; with the `#` removed (the rung's See question) Python 3.13 reports `SyntaxError: invalid character '—' (U+2014)`, which points a beginner at the dash rather than at the missing `#`. Comment changed to a plain hyphen (`# day1.py - the first things ...`); the same experiment now reports `SyntaxError: invalid syntax` with the marker under `the`. See question reworded to "delete the `#` and run" and to put the `#` back. Step change. Authoring note added to docs/15: no em dashes inside code blocks that a learner is asked to break.

## Reference run

Executed 2026-11-04 on macOS 15 (Apple silicon) with the CPython 3.13 interpreter recorded in [`PINS.md` → Reference runs](../../PINS.md#reference-runs) (a patch release of the pinned minor, not the pinned installer itself); nothing in these blocks differs across 3.13 patch releases (same interpreter, same error messages for the whole 3.13 series). The editor steps (install, Extensions panel, New File, View → Terminal) were followed in the pinned editor version; they are not reproducible from a script and are not in the table. Script used: a shell file outside the repository that writes each block to `hello.py`/`day1.py` and runs it with piped input.

| Rung | Block | Expected in brief | Observed | Match |
|---|---|---|---|---|
| r0 | `python3 --version` | `Python` + version | `Python 3.13.x` (the patch level is in PINS.md) | yes |
| r1 | `python3` banner | three lines then `>>>` | two lines then `>>>` | **no → brief fixed** |
| r1 | `print("Hello, world")` | `Hello, world` | `Hello, world` | yes |
| r1 | `"Hello, world"` | `'Hello, world'` | `'Hello, world'` | yes |
| r1 | `exit()` | back to terminal | back to terminal | yes |
| r2 | `python3 hello.py` | `Hello, world` | `Hello, world` | yes |
| r2 | run from the wrong folder | `can't open file` / `No such file or directory` | `can't open file '…/Desktop/hello.py': [Errno 2] No such file or directory` | yes |
| r3 | two `print` lines | two lines in order | `Hello, Ada` / `Welcome to Python` | yes |
| r3 | `print("Hello,", "Ada")` | `Hello, Ada` | `Hello, Ada` | yes |
| r4 | three-line file | `5` / `2 + 3` / `2 + 3 is 5` | same | yes |
| r4 | `print(2 + 3 * 4)`, `print((2 + 3) * 4)` | (See question) | `14` / `20` | yes |
| r5 | `pirnt("Hello, world")` | traceback, `NameError … Did you mean: 'print'?` | identical to the brief's block | yes |
| r5 | `print("Hello, world)` | `SyntaxError: unterminated string literal (detected at line 1)`, no `Traceback` heading | identical | yes |
| r5 | `print("Hello" + 3)` | `TypeError: can only concatenate str (not "int") to str` | full traceback with `~~~~~~~~^~~` marker then the same last line | **partial → full block added** |
| r5 | `print("Hello", 3)` | works | `Hello 3` | yes |
| r5 | `print(Hello, world)` (break-lab line 2) | one of the three kinds | `NameError: name 'Hello' is not defined` | yes |
| r6 | `input` with `Ada` | `What is your name? ` then `Hello, Ada` | same | yes |
| r6 | `input` with `42` | `Hello, 42` | `Hello, 42` | yes |
| r6 | `input` with empty line | (See question) | `Hello, ` | yes |
| r7 | `day1.py` with `Ada` | three lines, last contains the name | `Hello, world` / `2 + 3 is 5` / `Name? My name is Ada` | yes |
| r7 | `day1.py` without `#` | (See question) | with em dash: `SyntaxError: invalid character '—' (U+2014)`; with hyphen: `SyntaxError: invalid syntax` | **confusing → comment changed to a hyphen** |
| stretch | `"=" * 20`, `"ab" * 3`, `"ab" + 3` | guess first | 20 `=`; `ababab`; `TypeError: can only concatenate str (not "int") to str` | yes |
| stretch | `help(print)` | help screen | `print(*args, sep=' ', end='\n', file=None, flush=False)` … | yes |

**Second run, same day:** after the three changes above, the 22 blocks were re-run on the `uv`-managed 3.13 interpreter (the one stage 1 installs; patch level in PINS.md → Reference runs). 22 of 22 matched the published brief; no further changes.

Re-run this table at every re-pin (`docs/11`), and on Windows before the first Windows learner starts.
