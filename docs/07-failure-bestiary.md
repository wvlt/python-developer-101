# 07 — Failure bestiary

A living catalogue of the ways Python programs fail. Each entry records the symptom you will see, the mechanism underneath, how to detect it, the fix, and the stage where it is first met. Learners add entries as they discover new ones; see [Contributing](../CONTRIBUTING.md).

Entry format: **ID — Name** · *Stage* · Symptom · Cause · Detection · Fix · Related.

## Loud and quiet

Every failure here is one of two kinds, and the distinction is the course's risk model:

- **Loud failures** raise an exception. The program stops and prints a traceback. The traceback is the computer talking back: it names the exception, the line and, in current Python, often the fix ("Did you mean `print`?"). Loud failures are the *good* kind. You read them bottom-up and fix the cause. Stage 0 teaches the reading; every stage practises it.
- **Quiet failures** raise nothing. The program runs, finishes, and is wrong. Nobody tells you. These are the ways Python lies to you, and they are what tests, the debugger and the failure review exist for. In the agents course the equivalent was the lethal trifecta; here it is the catalogue in category **Q** below, and the two templates built around it — [`FAILURE_REVIEW.md`](../templates/FAILURE_REVIEW.md) (where could this program be quietly wrong?) and [`BREAK_MY_PROGRAM.md`](../templates/BREAK_MY_PROGRAM.md) (a peer tries to make it quietly wrong).

IDs are stable. Categories: `S` syntax and names (loud), `T` types and values, `F` flow, `C` collections, `N` functions and scope, `E` errors and I/O, `Q` the quiet failures (cross-reference list), `O` objects, `H` human and process.

---

## S — Syntax and names (always loud)

**S01 — `SyntaxError: unterminated string literal`** · *S0* · The traceback points at a line with a quote; the caret sits at the opening quote. · A string was opened and never closed, or the closing quote is a different kind. · The error says `unterminated string literal` and the line number. · Count the quotes on that line; they must pair. · S02.

**S02 — `SyntaxError: '(' was never closed`** · *S0* · The error points at the *opening* bracket, sometimes a line above where you were typing. · A bracket, parenthesis or brace was opened and never closed. · The message names the bracket. · Every `(` needs a `)`; the editor highlights the match when the cursor is on one. · S01.

**S03 — `NameError: name 'pirnt' is not defined`** · *S0* · Python says it has never heard of a word you are sure you wrote. · A typo in a name, a variable used before assignment, or a name defined in a different scope. · The message quotes the name; from 3.10 it adds `Did you mean: 'print'?`. · Read the name character by character. If it is spelled right, find where it is assigned and check that line runs before this one. · N03.

**S04 — `IndentationError` / `unexpected indent`** · *S2* · A line that looks fine is rejected. · Indentation in Python is structure: a line indented where no block was opened, or a block whose lines are not aligned, or a mix of tabs and spaces. · The message names the line; the editor shows whitespace if you turn on *Render Whitespace*. · Use four spaces, always; let the editor indent after a colon; never press Tab unless the editor converts it. · F02.

**S05 — `SyntaxError: invalid syntax` at an `=` in a condition** · *S2* · `if x = 5:` is rejected. · `=` assigns; `==` compares. · Message points at the `=`; from 3.10: `Maybe you meant '==' or ':='`. · Use `==`. · T05.

**S06 — Forgetting the colon** · *S2* · `SyntaxError: expected ':'` after `if`, `for`, `while`, `def`, `class`. · Compound statements end their header line with `:`. · The message says `expected ':'`. · Add it. · S04.

**S07 — Forgetting the brackets on a call** · *S4* · `print(len)` shows `<built-in function len>`; `if ready:` is always true when `ready` is a function. · A name alone refers to the function object; `name()` calls it. · The output contains `<function` or `<built-in`. · Add `()`. · N05.

**S08 — Forgetting `self`** · *S7* · `TypeError: Book.title() takes 0 positional arguments but 1 was given`. · Methods receive the instance as their first parameter; Python passes it whether or not you declared it. · The "takes 0 … but 1 was given" shape. · Add `self` as the first parameter. · O01.

## T — Types and values

**T01 — `TypeError: can only concatenate str (not "int") to str`** · *S1* · `"Age: " + 30` crashes. · `+` on a string needs another string; `input()` returns a string, so `input() + 1` also fails. · The message names both types. · Convert: `str(30)`, or use an f-string: `f"Age: {age}"`. · T02.

**T02 — `input()` is always text** · *S1* · `age = input(); age + 1` → T01; `age > 18` → `TypeError: '>' not supported between 'str' and 'int'`. · `input()` returns `str`, whatever the user typed. · Any comparison or arithmetic on it fails loudly, or — `"9" > "10"` is `True` — compares as text, quietly. · `int(input())`, and handle `ValueError` from stage 5. · **Q**.

**T03 — Integer vs true division** · *S1* · `7 / 2` is `3.5`; `7 // 2` is `3`; `-7 // 2` is `-4`, not `-3`. · `/` always returns a float; `//` floors toward negative infinity. · Quiet: the number is simply different. · Choose the operator for the meaning; test negative inputs. · **Q**.

**T04 — Float precision** · *S1* · `0.1 + 0.2 == 0.3` is `False`; a total prints as `19.999999999999996`. · Binary floating point cannot represent most decimal fractions exactly. · Quiet. Comparing floats with `==`, or summing money. · `round(x, 2)` for display; `math.isclose` for comparison; `decimal.Decimal` or integer cents for money. · **Q**.

**T05 — `is` vs `==`** · *S1 (first contact), S3* · `a == b` is `True` but `a is b` is `False`; or small ints and short strings make `is` *look* like `==` until they do not. · `==` compares values; `is` compares identity (same object). · Quiet; `ruff` F632 flags `is` with a literal. · Use `==` for values; `is` only for `None`, `True`, `False`. · C01, **Q**.

**T06 — Truthiness surprises** · *S1* · `if count:` skips when `count == 0`; `if name:` skips when `name == ""`; `bool("0")` is `True`, `bool("False")` is `True`. · Every object has a truth value; empty and zero are false, everything else true — including non-empty strings that spell falsehood. · Quiet. · Compare explicitly when zero or empty is a valid value: `if count is not None:`. · **Q**.

**T07 — `ValueError: invalid literal for int()`** · *S1, S5* · `int("12 ")` works, `int("12a")` and `int("")` do not. · The text is not a whole number. · Loud. · Strip, validate, or catch `ValueError` and ask again (stage 2 loop; stage 5 exception). · T02.

## F — Flow

**F01 — Off-by-one** · *S2* · `range(1, 10)` prints 1–9; the last item is skipped; the loop runs one time too many. · Ranges and slices are half-open: start included, stop excluded. · Quiet. · Say the range aloud as "from start up to but not including stop"; test the boundary values. · **Q**.

**F02 — Infinite `while`** · *S2* · The program never ends; the terminal shows nothing or scrolls forever. · The condition never becomes false: the variable it tests is never changed inside the loop, or is changed the wrong way. · The program does not return to the prompt; Ctrl-C raises `KeyboardInterrupt`. · Every `while` needs a line inside it that moves toward the exit; or use `for` when the count is known. · F03.

**F03 — The always-true `or`** · *S2* · `if answer == "yes" or "y":` runs for every answer. · `"y"` is a non-empty string and therefore true; the `or` is between a comparison and a string, not between two comparisons. · Quiet. · `if answer == "yes" or answer == "y":` or `if answer in ("yes", "y"):`. · T06, **Q**.

**F04 — Shadowing the loop variable or a built-in** · *S2, S4* · `for list in lists:` then `list(x)` fails; `sum = 0` then `sum(values)` → `TypeError: 'int' object is not callable`. · A name you assigned hides a built-in function of the same name. · `'int' object is not callable` is the loud form; the quiet form is a loop variable reused outside the loop with the last value. · Never name a variable `list`, `dict`, `str`, `sum`, `max`, `min`, `id`, `input`, `type`. `ruff` A001 flags it. · **Q**.

**F05 — Mutating a list while iterating it** · *S3* · `for x in items: items.remove(x)` skips every other item. · The iterator tracks an index; removing shifts the items under it. · Quiet. · Iterate over a copy (`for x in items[:]`) or build a new list with a comprehension. · C01, **Q**.

**F06 — `else` on a loop misread** · *S2* · The `else` block runs when you expected it not to. · `else` on `for`/`while` runs when the loop finished *without `break`*, not when the loop body never ran. · Quiet. · Read it as "nobreak"; use a flag if clearer. · F01.

## C — Collections

**C01 — Aliasing** · *S3* · `b = a; b.append(4); print(a)` shows the 4 in `a` too. · Assignment binds a name to an object; it does not copy. Two names, one list. · Quiet; `id(a) == id(b)`. · Copy when you need a copy: `a[:]`, `list(a)`, `a.copy()`, `copy.deepcopy(a)` for nested. · C04, N02, **Q**.

**C02 — `sort()` returns `None`** · *S3* · `x = items.sort(); print(x)` prints `None`; `return items.sort()` returns nothing. · `list.sort()` sorts in place and returns `None`; `sorted(items)` returns a new list. · Quiet unless you use the result. · Use `sorted()` when you want the value; `.sort()` when you want the list changed. · C01.

**C03 — `KeyError`** · *S3* · `d["missing"]` crashes. · The key is not in the dict. · Loud; the message quotes the key. · `d.get(key, default)`, `key in d`, `setdefault`, or `collections.defaultdict`. · E01.

**C04 — Shallow copy of nested data** · *S3* · `grid = [[0] * 3] * 3; grid[0][0] = 1` changes every row. · The outer list holds three references to the *same* inner list. · Quiet. · `[[0] * 3 for _ in range(3)]`; `copy.deepcopy` for existing structures. · C01, **Q**.

**C05 — Modifying a tuple** · *S3* · `TypeError: 'tuple' object does not support item assignment`. · Tuples are immutable. · Loud. · Build a new tuple, or use a list if it must change. · T01.

**C06 — Relying on `dict` order before 3.7, or on set order ever** · *S3* · Set iteration order differs between runs. · Sets are unordered; dicts keep insertion order (guaranteed since 3.7). · Quiet; tests that compare set output as a list are flaky. · `sorted(the_set)` when order matters. · —

## N — Functions and scope

**N01 — Forgetting `return`** · *S4* · `result = add(2, 3); print(result)` prints `None`. · A function without `return` returns `None`; printing inside the function is not returning. · Quiet until the value is used. · `return` the value; print at the call site. · **Q**.

**N02 — Mutable default argument** · *S4* · `def add(item, items=[])` remembers items across calls. · Default values are evaluated once, at `def` time, and shared by every call. · Quiet; `ruff` B006 flags it. · Default to `None` and create the list inside. · C01, **Q**.

**N03 — `UnboundLocalError`** · *S4* · `total = 0` at module level; `def f(): total += 1` → `UnboundLocalError: cannot access local variable 'total'`. · Assigning to a name anywhere in a function makes it local for the whole function. · Loud. · Pass it in and return it; `global` only if you have read why not. · S03.

**N04 — Late-binding closures** · *S4* · `fs = [lambda: i for i in range(3)]; [f() for f in fs]` is `[2, 2, 2]`. · The lambda looks up `i` when called, after the loop has finished. · Quiet. · Bind at definition: `lambda i=i: i`, or use a factory function. · **Q**.

**N05 — Calling vs referring** · *S4* · see S07. · · · · S07.

**N06 — Recursion without a base case** · *S4* · `RecursionError: maximum recursion depth exceeded`. · The function calls itself on every path. · Loud, after about a thousand calls. · Every recursive function has a case that returns without recursing, and every recursive call moves toward it. · F02.

## E — Errors and I/O

**E01 — Swallowed exception** · *S5* · `try: … except: pass` and the program "works" with nothing done. · A bare `except` (or `except Exception: pass`) catches everything, including typos and the Ctrl-C, and discards it. · Quiet; `ruff` E722 and S110 flag it. · Catch the specific exception; log what you caught; re-raise what you cannot handle. · **Q**.

**E02 — `UnicodeDecodeError`** · *S5* · `'utf-8' codec can't decode byte 0xe9 in position 1234`. · The file is not UTF-8; or you did not say which encoding and the platform default differed. · Loud, usually deep in the file. · Always pass `encoding="utf-8"` and know when a file is not; `errors="replace"` only when you have decided that losing characters is acceptable and logged it. · E03.

**E03 — The relative path that depends on where you ran it** · *S5* · `FileNotFoundError` when run from one directory and fine from another. · Relative paths resolve against the current working directory, not the script's location. · Loud. · `Path(__file__).parent / "data"`, or take the path as an argument. · E04.

**E04 — File not closed** · *S5* · Writes missing from a file; "too many open files" in a loop. · `open()` without `with` relies on garbage collection to close. · Quiet until it is not. · `with open(...) as f:` always. · E05.

**E05 — Newline and `print` differences** · *S5* · An extra blank line between every row of a CSV on Windows; `readline()` strings ending in `\n`. · Text mode translates newlines; `csv.writer` needs `newline=""`; `print` adds `\n`. · Quiet. · `open(..., newline="")` for CSV; `.rstrip("\n")` or `splitlines()` when reading. · —

**E06 — `pickle` of untrusted data** · *S5* · Loading a pickle runs arbitrary code. · Unpickling constructs objects by executing instructions in the stream; anyone who can write the file can run code on your machine. · Quiet — it just works, including the attack. `ruff` S301 flags it. · Never `pickle.load` data you did not write yourself in this program; use JSON for anything that crosses a boundary. · E07, **Q**.

**E07 — `eval()` on input** · *S5* · `eval(input())` to "parse a number". · `eval` runs any Python; the input `__import__("os").system("rm -rf ~")` is a number to nobody. · Quiet. `ruff` S307 flags it. · `int()`, `float()`, `json.loads`, `ast.literal_eval` for literals. · E06, **Q**.

**E08 — Catching too much, too high** · *S5* · One `except Exception` around the whole program hides which line failed. · The handler is far from the cause. · Quiet-ish: the user sees a generic message. · Catch close to the cause; let the rest propagate; log with `exc_info=True`. · E01.

## Q — The quiet failures (the risk model)

The cross-reference list. These are the entries above that raise nothing. The failure review asks, for each one, "could this program be quietly wrong this way, and which test or structure prevents it?"

| ID | Name | First met | `ruff` rule |
|---|---|---|---|
| C01 | Aliasing and mutation of shared objects | S3 | — |
| N02 | Mutable default argument | S4 | B006 |
| T05 | `is` vs `==` | S1, S3 | F632 |
| T04 | Float precision | S1 | — |
| T03 | Integer vs true division | S1 | — |
| F01 | Off-by-one; half-open ranges | S2 | — |
| F04 | Shadowing built-ins | S2, S4 | A001 |
| E01 | Swallowed exceptions | S5 | E722, S110 |
| N04 | Late-binding closures | S4 | B023 |
| F05 | Mutating a list while iterating | S3 | — |
| E02 | Encoding errors (when silenced with `errors="ignore"`) | S5 | — |
| E06 | `pickle` of untrusted data | S5 | S301 |
| E07 | `eval` | S5 | S307 |
| T02 | `input()` compared as text | S1 | — |
| T06 | Truthiness of `0`, `""`, `"0"` | S1 | — |
| F03 | The always-true `or` | S2 | — |
| C02 | `sort()` returns `None` | S3 | — |
| C04 | Shallow copy of nested data | S3 | — |
| N01 | Forgotten `return` | S4 | — |
| F06 | `else` on a loop | S2 | — |
| O02 | Mutable class attribute shared by instances | S7 | RUF012 |

## O — Objects

**O01 — Missing `self`** · *S7* · see S08. · · · · S08.

**O02 — Mutable class attribute shared by instances** · *S7* · `class Member: loans = []` and every member has every loan. · A class attribute is one object shared by all instances; only assignment in `__init__` makes it per-instance. · Quiet. `ruff` RUF012. · `self.loans = []` in `__init__`; `field(default_factory=list)` in a dataclass. · N02, **Q**.

**O03 — `__eq__` without `__hash__`** · *S7* · `TypeError: unhashable type: 'Book'` when putting a Book in a set or using it as a dict key. · Defining `__eq__` sets `__hash__` to `None` unless you define it too. · Loud. · Define `__hash__` consistently with `__eq__`, or use `@dataclass(frozen=True)`. · O04.

**O04 — Forgetting `super().__init__()`** · *S8* · `AttributeError: 'StaffMember' object has no attribute 'name'`. · The subclass `__init__` replaced the parent's without calling it. · Loud, at first use of the missing attribute. · Call `super().__init__(...)` first. · O01.

**O05 — An iterator that cannot be iterated twice** · *S8* · The second `for` over the same object does nothing. · An iterator is consumed; an iterable produces a fresh iterator each time. · Quiet. · Return a new iterator from `__iter__`; or make the thing a list if it must be re-read. · O06.

**O06 — Generator consumed early** · *S8* · `print(list(gen))` for a look, then the real loop sees nothing. · A generator yields each value once. · Quiet. · Look with `itertools.islice` on a fresh generator, or materialise once. · O05.

**O07 — Context manager that does not clean up on error** · *S8* · The file stays open or the lock held when the body raises. · `__exit__` not called because `__enter__` raised, or cleanup placed after the `yield` without `try/finally`. · Quiet. · `try: yield finally: cleanup` in `@contextmanager`; test by raising inside the `with`. · E04.

## H — Human and process

**H01 — "It works"** · *S1* · Said without running it, or after running it on one input. · No test, or n=1. · Ask: what input did you try? · Oath item 1 and 3. · —

**H02 — Reading only the first line of the traceback** · *S0* · The learner changes the top of the file when the error is at the bottom. · The traceback lists the call chain top-down; the error and its line are at the *bottom*. · Watch them fix the wrong line. · Read the last line first, then the line above it. · S03.

**H03 — Copy-paste without reading** · *S1* · A rung's worked example pasted, run, and not understood; the exercise after it cannot be started. · Typing is the learning. · The exercise stalls. · Type the examples. The brief says so at every one. · H04.

**H04 — Code you cannot explain** · *S1* · A reviewer points at a line and the learner cannot say what it does. · Assistance beyond the policy, or copying. · Ask. · Oath item 7; the AI-assistance policy. · H03.

**H05 — Optimising before measuring** · *S9* · A comprehension rewritten as a loop "for speed" with no `timeit`. · Folklore. · Absence of a number. · `timeit` before and after; kill criterion of stage 9. · —

**H06 — A class because classes are professional** · *S7* · A dataclass with no methods and no invariant, or a class wrapping one function. · Pattern-matching on status rather than need. · The kill criterion question. · A dict, a tuple or a function. · —

---

## Adding an entry

Open a PR against upstream with: ID (next free in category), name, stage first met, the five fields, related IDs, whether it is loud or quiet, the `ruff` rule if one exists, and a snippet under ten lines that shows it. Entries with a snippet are merged; entries from theory are discussed first.
