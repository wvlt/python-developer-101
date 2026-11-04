# Stage 2 — Decisions and repetition

*Tier A · ~12 hours · Cost: zero · Toolchain arrives: `ruff`, GitHub (the only account in the course)*

## Why this stage exists

Until now every program ran top to bottom once. A program that can *choose* a line and *repeat* a block can do anything a computer does; everything after this stage is about doing it clearly. The two ideas are small. The mistakes they invite are not: the loop that runs one time too many, the condition that is always true, the `while` that never ends. This stage teaches the ideas with worked examples and the mistakes with a break-lab, and by the end you will have written a program that keeps asking until it gets a sensible answer, which is the first thing any user of your programs will need.

It is also the stage where your work gets a public address. GitHub is the one account you create in this course, and from here every stage ends with a pull request you can show to anyone.

## Contract

**Assumes** (from [stage 1](../01-values-and-names/README.md)): the toolchain works and `just test`, `just eval`, `just break` and `just trace` mean something to you (`s01-r0`); arithmetic including `//` and `%` (`s01-r1`); `int()`, `str()`, `float()` and that `input()` gives text (`s01-r2`); names and `+=` (`s01-r3`); indexing and slicing with "up to but not including" (`s01-r4`); string methods including `isdigit`, `lower`, `strip` (`s01-r5`); f-strings and `f"{x=}"` (`s01-r6`); comparisons, `and`/`or`/`not`, truthiness (`s01-r7`); git save points (`s01-r8`).

**Provides** (stage 3 takes these for granted):
- You can write `if`/`elif`/`else`, nest them, and use the one-line conditional expression (`s02-r1`, `s02-r2`).
- You can use `match`/`case` with literals, `|` and `_` (`s02-r3`).
- You can write a `while` loop that ends, including the ask-until-valid pattern with `break` (`s02-r4`).
- You can write `for ... in range(...)` with start, stop and step, and say which numbers it produces (`s02-r5`).
- You can use `break`, `continue`, `pass` and `else` on a loop (`s02-r6`).
- You can use `enumerate` and `zip` in a `for` loop and unpack the pairs (`s02-r7`).
- You can keep a running total, a running best and a flag; you can nest loops (`s02-r8`).
- `ruff check` is clean on everything you write; you have found a shadowed built-in with it (`s02-r9`).
- Your fork is on GitHub, your work is on a branch, and you have opened a pull request (`s02-r10`).
- You have written a program with a loop, state, validation and a stopping condition, from a description (`s02-r11`).

Rung IDs: rung M here is `s02-rM`; its checks are `s02-rM.run`, `.see`, `.say`. Exercises are `exercises/rMeK_name.py`; hidden case IDs are `s02-rMeK-x`. Feedback on any rung goes in a [stage feedback](../../templates/STAGE_FEEDBACK.md); changes land in [`REVISIONS.md`](REVISIONS.md).

## Entry condition

Stage 1 gate passed (`just eval 01` PASS, card filled, commits in place). `just test 02` shows `54 failed`, every one `nothing written below the marker yet` except `r9b1`, which is a planted bug and fails differently.

## Break-lab (first)

Nine files in `breaklab/`. For each, write in the journal what it will print, line by line, before running. Files 06 and 08 raise on purpose; predict the last line of the traceback. File 09 is not to be run at all: read it and write down why it would never end, then what one line would fix it. Then:

```
just break 02
```

(File 08 asks you to type something; type `5`.) Compare. The bestiary IDs are in the comments: [F01](../../docs/07-failure-bestiary.md#f--flow) twice, F03, F06, F04, F02, and two you have met: T04 and T02. Journal the ones you got wrong and what you believed.

Question to carry through the stage: *when exactly does a loop stop?*

## Part A — Decisions

### Rung 1 — `if` and `else`

*~40 min · feeds s02-r2, s02-r4, every later stage*

A program chooses a line to run by testing a condition. The test ends with a colon; the lines that depend on it are indented four spaces; the indentation *is* the structure.

```python
score = int(input("Score? "))
if score >= 50:
    print("pass")
else:
    print("fail")
print("done")
```

Run it with `60`, then `20`. `pass` or `fail` prints, then `done` prints both times, because `done` is not indented and so does not belong to either branch. The indented lines are a **block**. The editor indents for you after a colon; if you ever see `IndentationError`, a line is indented where no block was opened or is misaligned with its block ([S04](../../docs/07-failure-bestiary.md#s--syntax-and-names-always-loud)). Four spaces, always; never the Tab key unless the editor turns it into spaces (it does by default).

`else` is optional. The condition is any expression that can be true or false, which is any expression at all (rung 7 of stage 1): `if name:` runs when `name` is not empty.

**Exercises** (`just test 02 -k r1e`): `r1e1_pass_or_fail`, `r1e2_even_or_odd` (what does `%` give for an even number?), `r1e3_larger` (three outcomes; you will want the next rung's `elif`, but two `if`s and an `else` also work).

**Check**
- **Run:** `just test 02 -k r1e` → `6 passed`.
- **See:** in your `r1e1`, remove the indentation from the `print("pass")` line and run it: what is the last line of the error?
- **Say:** what decides whether a line belongs to the `if` branch?

### Rung 2 — `elif`, nesting, and the one-line form

*~50 min · feeds s02-r3, s02-r11, s04*

More than two outcomes: `elif` (else-if), tested in order, first match wins, `else` catches the rest.

```python
score = int(input("Score? "))
if score >= 85:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 55:
    grade = "C"
else:
    grade = "F"
print(grade)
```

Order matters: with the tests reversed (`>= 55` first), every score over 55 would be a C. Write the conditions from most to least specific, and test the boundaries: 85, 84, 70, 69.

Blocks nest: an `if` inside an `if`, indented eight spaces. Nesting two deep is normal; four deep is a sign to rethink (stage 4 gives you functions for that).

For a choice between two *values*, there is a one-line form, the **conditional expression**:

```python
label = "even" if n % 2 == 0 else "odd"
print("Fizz" if n % 3 == 0 else n)
```

Read it as "A if condition else B". Use it when the two outcomes are values, not actions.

**Exercises** (`just test 02 -k r2e`): `r2e1_letter_grade` (five grades; test every boundary), `r2e2_sign`, `r2e3_fizz` (one `print`, one conditional expression).

**Check**
- **Run:** `just test 02 -k r2e` → `7 passed`.
- **See:** swap the first two `elif` tests in your `r2e1` and run `just test 02 -k r2e1`: which case IDs fail?
- **Say:** why does the order of `elif` tests matter, and what order is safe for ranges?

### Rung 3 — `match` and `case`

*~40 min · feeds s02-r11, s07*

When one value is compared against several literals, `match` says it more clearly than a chain of `elif`:

```python
command = input("> ")
match command:
    case "north" | "n":
        print("You walk north.")
    case "look":
        print("You see a door.")
    case "quit":
        print("Goodbye.")
    case _:
        print("I do not understand.")
```

Each `case` is tried in order; `|` means "or" between literals; `case _:` is the catch-all and goes last. `match` can do a great deal more (take apart lists and objects, which stage 7 uses); for now it is the tidy way to dispatch on one value.

**Exercises** (`just test 02 -k r3e`): `r3e1_weekday` (seven cases and a catch-all), `r3e2_command`.

**Check**
- **Run:** `just test 02 -k r3e` → `6 passed`.
- **See:** what does your `r3e2` print for `LOOK` in capitals, and which line decides that?
- **Say:** when would you choose `match` over `elif`, and when the reverse?

## Part B — Repetition

### Rung 4 — `while`, and asking until the answer is valid

*~55 min · feeds s02-r6, s02-r11, s05 · bestiary F02*

`while` repeats a block as long as a condition is true. Every `while` needs a line inside it that moves toward the condition becoming false, or it never ends ([F02](../../docs/07-failure-bestiary.md#f--flow); that was break-lab 09).

```python
n = 3
while n > 0:
    print(n)
    n -= 1
print("Go")
```

Trace it by hand first: `n` is 3, print, now 2; 2, print, now 1; 1, print, now 0; `0 > 0` is false, stop, `Go`. Then `just trace` it and compare.

The pattern you will use in every program that talks to a person — **ask until valid**:

```python
while True:
    text = input("A number from 1 to 10: ")
    if not text.isdigit():
        print("not a number")
    elif int(text) < 1 or int(text) > 10:
        print("out of range")
    else:
        break
number = int(text)
print("Got", number)
```

`while True:` loops forever on purpose; `break` is the only way out, and it is reached only when the input passes both checks. `text.isdigit()` is true when every character is a digit, so it is safe to call `int()` afterwards; note that it rejects `-3` and `7.5`, which is what you want here. Try it: type letters, type `0`, type `11`, type `7`. Nothing you type can crash it. That property is the whole point of the pattern, and stage 5 will give you a more general tool for it.

If a loop of yours runs away, press Ctrl-C in the terminal; it stops the program with `KeyboardInterrupt`.

**Exercises** (`just test 02 -k r4e`): `r4e1_until_stop` (read lines until one says `stop`; count them), `r4e2_valid_number` (the pattern above, printing each rejection), `r4e3_countdown`.

**Check**
- **Run:** `just test 02 -k r4e` → `6 passed`.
- **See:** in `r4e2`, what does your program print for an empty line, and which test rejected it?
- **Say:** what must be true of a `while` loop's body for the loop to end?

### Rung 5 — `for` and `range`

*~50 min · feeds s02-r6, s02-r7, s03 · bestiary F01*

When you know how many times, or you have a sequence to walk, use `for`:

```python
for i in range(5):
    print(i)
```

Prints 0, 1, 2, 3, 4. **Not 5.** `range(5)` is five numbers starting at 0, up to but not including 5, the same rule as slices in stage 1. `range(1, 6)` is 1 to 5. `range(0, 10, 2)` is 0, 2, 4, 6, 8: start, stop, step. `range(10, 0, -1)` counts down from 10 to 1.

The variable after `for` takes each value in turn. You name it; `i` for a plain counter, something better when it means something (`for day in range(1, 8)`). It keeps its last value after the loop (break-lab 03), which is occasionally useful and often a surprise.

`for` walks any sequence, not just `range`. A string is a sequence of characters:

```python
for ch in "abc":
    print(ch.upper())
```

Stage 3 adds lists; the loop is the same.

Off-by-one errors ([F01](../../docs/07-failure-bestiary.md#f--flow)) are the commonest bug in loops in every language. Say the range aloud as "from start, up to but not including stop", and test the first and last values the loop produces, every time.

**Exercises** (`just test 02 -k r5e`): `r5e1_count_up` (1 to n *inclusive*), `r5e2_sum_to` (a running total: stage 1 rung 3 inside a loop), `r5e3_evens_between` (a loop with an `if` inside), `r5e4_times_table` (an f-string per line).

**Check**
- **Run:** `just test 02 -k r5e` → `7 passed`.
- **See:** what does `range(1, 5)` produce, and what did you have to write to get 1 to 5 inclusive?
- **Say:** why does `range(n)` start at 0 and stop before n, and what else in Python follows the same rule?

### Rung 6 — `break`, `continue`, `pass`, and `else` on a loop

*~40 min · feeds s02-r11, s03 · bestiary F06*

Four small words that change what a loop does mid-way.

- `break` leaves the loop at once (you used it in rung 4).
- `continue` skips the rest of the body and goes to the next iteration.
- `pass` does nothing; it holds a place where Python requires a block and you have nothing to put there yet.
- `else` on a loop runs when the loop finished *without* `break`. Read it as "no break".

```python
n = int(input("A number from 2 up: "))
for d in range(2, n):
    if n % d == 0:
        print("not prime: divisible by", d)
        break
else:
    print("prime")
```

If any `d` divides `n`, print and `break`, and the `else` is skipped. If the loop runs out of candidates without breaking, the `else` runs. Break-lab 05 was this; most people predict it wrong the first time ([F06](../../docs/07-failure-bestiary.md#f--flow)), which is why it is here as a rung rather than a footnote.

**Exercises** (`just test 02 -k r6e`): `r6e1_first_multiple_over` (`while True` and `break`), `r6e2_skip_threes` (`continue`), `r6e3_is_prime` (`for`/`break`/`else`).

**Check**
- **Run:** `just test 02 -k r6e` → `6 passed`.
- **See:** in `r6e3` with input `9`, which value of `d` triggered the `break`?
- **Say:** when does the `else` of a `for` loop run?

### Rung 7 — `enumerate` and `zip`

*~45 min · feeds s03, s04, s09*

Two helpers that remove the commonest reasons to write `range(len(...))`.

**`enumerate`** gives you the position and the item together:

```python
for i, ch in enumerate("abc", start=1):
    print(f"{i}. {ch}")
```

`1. a`, `2. b`, `3. c`. The `for` line names *two* variables and each iteration fills both: that is **unpacking**, and you will use it constantly.

**`zip`** walks two sequences side by side, stopping at the shorter:

```python
for name, score in zip("AB", "xy", strict=True):
    print(name, score)
```

`A x`, `B y`. `strict=True` makes `zip` raise if the two are different lengths instead of silently dropping the tail; use it unless you have a reason not to. The hidden cases for this rung fish for the silent version.

In these two exercises the given lines build a **list** of the inputs for you (`[input() for _ in range(n)]`); lists are stage 3's subject, and all you need today is that a list is a sequence a `for` loop can walk, like a string.

**Exercises** (`just test 02 -k r7e`): `r7e1_numbered_lines`, `r7e2_names_and_scores`.

**Check**
- **Run:** `just test 02 -k r7e` → `4 passed`.
- **See:** what does `enumerate` give on each iteration, and how many names does the `for` line need to catch it?
- **Say:** what does `zip` do when one sequence is longer than the other, with and without `strict=True`?

### Rung 8 — Accumulators, flags and nested loops

*~60 min · feeds s02-r11, s03, every later stage*

Three patterns you will write for the rest of your life, named so you can recognise them.

**Accumulator**: a name that starts at a neutral value and gathers something each time round.

```python
total = 0
for i in range(1, 11):
    total += i
```

The neutral value for adding is 0, for multiplying 1, for text `""`.

**Running best**: an accumulator that keeps the largest (or smallest) so far. Start it with the *first value*, not with 0: a list of negative numbers has a largest, and it is not 0. (That is the quiet half of rung 9's planted bug.)

**Flag**: a `bool` that starts `False` and becomes `True` if something is ever seen.

```python
found = False
for ch in text:
    if ch == "!":
        found = True
print("shouting" if found else "calm")
```

**Nested loops**: a loop inside a loop; the inner one runs completely for each turn of the outer one. To print a 3-by-2 box of stars, the outer loop is rows and the inner loop builds one row. Use different variable names for the two loops.

**Exercises** (`just test 02 -k r8e`): `r8e1_largest` (running best; no `max()`), `r8e2_count_vowels` (accumulator; `ch in "aeiou"` asks whether a character is in a string), `r8e3_star_box` (nested), `r8e4_any_negative` (flag).

**Check**
- **Run:** `just test 02 -k r8e` → `8 passed`.
- **See:** in `r8e1`, what did your program print for `4, -3, -1, -2, -9` before and after you fixed the starting value?
- **Say:** why does a running best start with the first value rather than zero?

## Part C — Tools and the game

### Rung 9 — `ruff`, and a planted bug

*~30 min · feeds every later rung; u7*

A **linter** reads your code without running it and reports things that are probably wrong: a name that hides a built-in, a variable never used, a comparison that is always true. The course's linter is `ruff`, already installed by `uv sync`:

```
just check 02
```

It reports two problems in `exercises/r9b1_total_bug.py`, both the same: a variable named `max` is shadowing a built-in ([F04](../../docs/07-failure-bestiary.md#f--flow)). Open the file. It is complete, it runs, and it passes the first visible test. Rename the variable to what it actually is. Run `just check 02` again: clean. Run `just test 02 -k r9b`: one case still fails. That is the quiet bug from rung 8. Put `print(f"{v=} {largest=}")` inside the loop, run the exercise yourself with the failing input, and read what it shows. Fix it; commit with `fix(s02): r9b1 ...` and say in the message what the bug was.

From now on `just check NN` must be clean before every commit, and the gate checks it. `ruff` cannot find the quiet bug; only a test with the right input did. Keep both.

**Check**
- **Run:** `just check 02` → `ruff: clean`; `just test 02 -k r9b` → `2 passed`.
- **See:** what did `ruff` say, word for word, about the name `max`?
- **Say:** which of the two bugs in `r9b1` could `ruff` see and which could only a test see, and why?

### Rung 10 — GitHub, your fork, and a pull request

*~45 min · feeds every later stage; u6*

Your save points live on your machine. GitHub is where they go to be seen, reviewed and kept safe. It is the only account you create in this course, it is free, and the link is in [`PINS.md`](../../PINS.md).

1. **Create the account.** Use an email you keep. Turn on two-factor authentication when it asks; a free authenticator app is enough.
2. **Fork the course.** On the course repository's page, click *Fork*. You now have your own copy under your username.
3. **Point your clone at your fork.** In the course folder:

   ```
   git remote rename origin upstream
   git remote add origin https://github.com/<your-username>/python-developer-101.git
   git push -u origin main
   ```

   The first push asks you to sign in; follow the prompts (a browser window opens). `upstream` is the course; `origin` is yours. Changes to the course arrive with `git pull upstream main`.
4. **Work on a branch.** From here, each stage's work lives on its own branch and arrives in `main` by a pull request:

   ```
   git switch -c stage/02-decisions-and-repetition
   git push -u origin stage/02-decisions-and-repetition
   ```

   (Your stage 2 commits so far are on `main`; that is fine this once. The branch starts from where you are.)
5. **See your progress.** Open `https://github.com/<your-username>/python-developer-101`; your commits are there. Your fork also has the course player: enable Pages in the fork's settings (Settings → Pages → Source: GitHub Actions) and a few minutes later `https://<your-username>.github.io/python-developer-101/` shows your `PROGRESS.md` ticks against the briefs. Or run `just site` locally.
6. **Open a pull request** at the end of this stage (rung 11): on GitHub, *Compare & pull request* from your branch to your own `main`. The template asks for the gate checklist; fill it. Merge it yourself when the gate passes; a reviewer, if you have one, reviews it there.

**Check**
- **Run:** `git remote -v` → `origin` is your fork, `upstream` is the course; `git branch` → you are on `stage/02-...`.
- **See:** on GitHub, how many commits does your fork show, and does the most recent one match `git log --oneline | head -1`?
- **Say:** what is the difference between `origin` and `upstream`, and which do you push to?

### Rung 11 — Mini-project: guess the number

*~100 min · feeds gate s02-g1–g4; s03, s05*

A whole program with a loop, state, validation and a stopping condition. Read the top of `exercises/r11e1_guess_the_number.py`. The secret arrives first (so tests can play), then guesses one per line; each guess is answered, invalid guesses are rejected without counting, and the game ends on the correct guess with the count of valid tries.

Plan on paper before typing: what state does the game keep (one number); what are the five possible responses and in what order are they tested (validity first, then range, then comparison); where does `continue` go and where does `break`. Then build it in this order, running `just test 02 -k r11e` after each step: (1) the loop that reads and compares, no validation; (2) the digit check with `continue`; (3) the range check; (4) the count.

When it passes:

1. Play it yourself: `uv run python stages/02-decisions-and-repetition/exercises/r11e1_guess_the_number.py` with a secret of your choosing. Try to break it: letters, an empty line, `0`, `101`, `1e2`, a very long number.
2. Write down three inputs you expect would break a careless version, and what yours does with each. That list goes in the card's "how it fails".
3. `just check 02` clean. Card filled (`templates/ARTIFACT_CARD.md` → `stages/02-decisions-and-repetition/ARTIFACT_CARD.md`). The kill-criteria field: which of the game's rules could be a table rather than a chain of `elif`? (Stage 3 gives you the table.)
4. Commit, push, open the pull request, run `just eval 02`.

**Check**
- **Run:** `just test 02` → `54 passed`; `just check 02` → clean; `just eval 02` → `PASS`.
- **See:** which hidden case in your eval summary tested the range check, and did it pass?
- **Say:** why are invalid guesses rejected with `continue` before the count is increased, and what would change if the count came first?

## Measure, Break, Inspect in this stage

- **Measure:** the visible tests include the boundary values on purpose; read them before writing. The hidden tests fish for off-by-one, the always-true `or`, `zip` without `strict`, and a running best started at zero.
- **Break:** the break-lab, the planted bug in rung 9, and your own attempts to break the game in rung 11. Each failure gets its bestiary ID in the journal.
- **Inspect:** an f-string print *inside the loop* shows a value changing; `just trace` shows the loop's path. Use the first for one value, the second for "why did it go that way?"

## Artefact

- `exercises/r1e1` … `r11e1` complete, tests green, `ruff` clean.
- `JOURNAL.md` with the break-lab table and a line per session.
- `ARTIFACT_CARD.md` for the game, with three breaking inputs.
- Fork on GitHub; branch `stage/02-decisions-and-repetition`; a pull request with the gate checklist.
- `eval/runs/<ts>-<sha>/summary.json` cited in the card.

## Gate

The universal checklist `u1`–`u10` in [docs/06](../../docs/06-assessment-and-gates.md) applies, and:

- [ ] **s02-g1** `just eval 02` ≥ 56 of 62 hidden cases, run directory cited in the card.
- [ ] **s02-g2** `just check 02` clean; the journal names the shadowed built-in `ruff` found and the quiet bug it did not.
- [ ] **s02-g3** Fork on GitHub with ≥ 8 commits on the stage branch, a pull request open or merged, and the course player (Pages or `just site`) showing your `PROGRESS.md`.
- [ ] **s02-g4** The game rejects every input the reviewer types for two minutes (letters, blanks, out-of-range, huge numbers) with a message and no traceback; the card lists three such inputs.
- [ ] **s02-g5** Three Say questions answered without notes, from rungs 4, 5 and 6.

Rubric anchors for this stage are in [docs/14](../../docs/14-rubrics.md#anchors-stage-2).

## Kill criteria

A loop that runs three times over three known values is three lines without a loop, and clearer. A chain of ten `elif`s mapping a value to a word is a table, and stage 3's dictionary is the table. Before you write a loop, ask how many times it will really run; before you write an `elif` chain, ask whether you are writing a lookup.

## Stretch

- Make the game pick the secret itself with `random.randint(1, 100)` (two lines: `import random` at the top, then the call) and give the player seven tries.
- Rewrite `r2e1_letter_grade` with the boundaries in a different order and find the smallest set of tests that would catch the mistake.
- Read the `ruff` rule page for A001 and for E722; the second is a stage 5 bug you have not met yet.

## Reading

[docs/09 — Stage 2](../../docs/09-reading-list.md#stage-2--decisions-and-repetition): the tutorial's control-flow chapter after rung 6; the `match` tutorial after rung 3.
