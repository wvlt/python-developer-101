# Stage 1 — Values and names

*Tier A · ~12 hours · Cost: zero · Toolchain arrives: `uv`, `just`, tests, git (locally)*

## Why this stage exists

Everything a program does, it does to values: numbers, text, true-or-false. Everything it keeps, it keeps under a name. This stage is where you learn that a value has a *type*, that the type decides what `+` means, that text is not a number even when it looks like one, and that a name is a label you stick on a value, not a box you put it in. Every quiet bug in the bestiary from aliasing to float precision starts with one of those four sentences.

It is also the stage where the course's machinery arrives: someone else's tests tell you whether you are done, and git keeps a save point for every rung. From here on, you never again have to wonder "does it work?": you run `just test` and read the answer.

## Contract

**Assumes** (from [stage 0](../00-hello-python/README.md)): you can open a terminal in a folder and run a `.py` file (`s00-r2`); print text, a number and two things on one line (`s00-r3`, `s00-r4`); read the last line of a traceback and act on it (`s00-r5`); use `input()` inside `print()` (`s00-r6`); and you have a practice folder with the comment-on-top habit (`s00-r7`).

**Provides** (stage 2 takes these for granted):
- The course repository is on your machine; `uv run`, `just test 01`, `just eval 01` and `just break 01` work (`s01-r0`).
- You can do arithmetic with `+ - * / // % **` and brackets, and know `/` gives a decimal and `//` a whole number (`s01-r1`).
- You can name the type of a value with `type()` and convert between `int`, `float` and `str`; you know `input()` always gives text (`s01-r2`).
- You can bind a name with `=`, update it with `+=`, and swap two names (`s01-r3`).
- You can index, slice and measure text; you know text cannot be changed in place (`s01-r4`).
- You can use `upper`, `lower`, `strip`, `title`, `count`, `replace`, `startswith`, `endswith`, `isdigit` and look up the rest (`s01-r5`).
- You can build output with f-strings, including `:.2f`, `:<10`, `:>8`, and debug with `f"{x=}"` (`s01-r6`).
- You can write a condition with `< <= == != >= >`, `and`, `or`, `not`; you know what is false in Python; you know `==` is not `is` (`s01-r7`).
- You can make a git save point: `git status`, `git add`, `git commit -m`, `git log --oneline` (`s01-r8`).
- You have written a whole program from a description, with tests passing, and filled its Artefact Card (`s01-r9`).

Rung IDs: rung M here is `s01-rM`; its checks are `s01-rM.run`, `.see`, `.say`. Exercises are `exercises/rMeK_name.py`; hidden case IDs are `s01-rMeK-x`. Feedback on any rung goes in a [stage feedback](../../templates/STAGE_FEEDBACK.md); changes land in [`REVISIONS.md`](REVISIONS.md).

## Entry condition

Stage 0's done-when list ticked. Two hours free for rung 0, which installs tools and ends with a wall of red test failures that you will spend the rest of the stage turning green.

## Break-lab (first)

After rung 0 and before rung 1. In `stages/01-values-and-names/breaklab/` are eight short files. Open each in the editor, read it, and write in your journal what you think it will print, line by line, **before** running anything. Then run them all at once:

```
just break 01
```

Compare. For each wrong prediction write one sentence on what you believed. Snippets 01, 02, 03 and 06 are quiet failures in waiting (the bestiary IDs are in the comments: [T04](../../docs/07-failure-bestiary.md#t--types-and-values), T03, T02, T06); 08 raises on purpose, and your prediction for it is the last line of the traceback. Do not look anything up yet; the rungs explain every one.

Journal it. Question to carry through the stage: *what does `+` do, and how does Python decide?*

## Part A — The toolchain

### Rung 0 — Install the toolchain and clone the course

*~45 min · feeds every later rung*

Three tools, one download of the course, one command that turns everything red.

**1. `uv`.** The tool that installs Python versions, runs programs and manages packages for the rest of the course. Run the one-line install command for your platform from the *Toolchain* table in [`PINS.md`](../../PINS.md) (it is a `curl` line on macOS and a `powershell` line on Windows). Close the terminal, open a new one, and check:

```
uv --version
```

**2. `just`.** A command runner: `just test` instead of a long `pytest` line you would otherwise mistype. Install it through `uv`:

```
uv tool install rust-just
just --version
```

**3. git.** The save-point tool; rung 8 teaches it, rung 0 just installs it.

- *macOS:* run `git --version`. If git is not installed, macOS offers to install the command-line tools; accept, wait, run it again.
- *Windows:* install Git for Windows from the link in PINS.md, with the defaults. Open a new terminal; `git --version`.

**4. The course.** Choose where it lives (your Desktop is fine), open a terminal there, and copy the course repository to your machine:

```
git clone https://github.com/wvlt/python-developer-101.git
cd python-developer-101
```

You now have a folder `python-developer-101` with everything in this course inside it. Open that folder in the editor (File → Open Folder). From now on, every terminal you open for the course is opened in this folder (View → Terminal inside the editor does it).

**5. The project.** One command installs the course's Python and its tools into a private folder inside the project:

```
uv sync --extra dev
```

It takes a minute the first time. Nothing it does touches the rest of your machine. Then:

```
uv run python --version
```

This is the course's Python, and from now on `uv run python file.py` replaces `python3 file.py` on both platforms; the macOS/Windows difference is over.

**6. Red.** Run the tests for this stage:

```
just test 01
```

You will see a screen of `F`s and, near the bottom, a summary line `57 failed` (followed by a line from `just` saying the recipe failed, which is the same news). Every failure says the same thing: `nothing written below the marker yet`. Each one is an exercise in `stages/01-values-and-names/exercises/`; the rungs tell you which to do when, and you will watch this number fall to zero. Scroll up and read one failure in full: the file name, the input that was typed in, the output that was expected. The tests are the course telling you exactly what "done" means.

**Check**
- **Run:** `just test 01` → summary line `57 failed`.
- **See:** open `exercises/r1e1_sum_and_product.py`. Which lines are already there, and what does the comment on top tell you the program must print?
- **Say:** what is the difference between `python3 file.py` and `uv run python file.py`, and why does the course use the second?

## Part B — Numbers

### Rung 1 — Arithmetic

*~50 min · feeds s01-r2, s01-r9, s02-r5 · bestiary T03*

Python is a calculator first. Open the prompt with `uv run python` and type each line; read each answer before the next.

```
>>> 7 + 2
9
>>> 7 - 2
5
>>> 7 * 2
14
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> 7 % 2
1
>>> 2 ** 10
1024
>>> 7 + 2 * 3
13
>>> (7 + 2) * 3
27
```

Two kinds of number. `7` is an **int** (a whole number, any size). `3.5` is a **float** (a number with a decimal point, limited precision). Two kinds of division: `/` always gives a float, even for `8 / 2`, which is `4.0`; `//` gives the whole number of times the divisor fits, rounding *down* (so `-7 // 2` is `-4`, not `-3`), and `%` gives what is left over. `**` is "to the power of". Brackets and the usual order of operations apply.

Now the break-lab's snippet 01 again, at the prompt: `0.1 + 0.2`. The answer ends in `...0004`. A float holds a binary fraction, and most decimal fractions cannot be written exactly in binary, the same way one third cannot be written exactly in decimal. For now: never compare floats with `==` and never use them for money without rounding; stage 5 shows what to use instead. It is [T04](../../docs/07-failure-bestiary.md#t--types-and-values) in the bestiary and you will meet it in every language you ever learn.

**Exercises.** Open each file in `exercises/`, read the comment at the top, and write the program below the marker line. The lines above the marker are given: they read the inputs and give them names (`a`, `b`, `hours`, `n`), which rungs 2 and 3 explain; for now, treat each name as the number it holds. Run the tests for this rung only:

```
just test 01 -k r1e
```

`-k r1e` means "only the tests whose name contains `r1e`". Read every failure; the expected and actual output are shown side by side.

- `r1e1_sum_and_product` — two numbers; print the sum, then the product.
- `r1e2_three_divisions` — print `/`, `//` and `%` on three lines.
- `r1e3_seconds_in` — hours to seconds.
- `r1e4_power_and_root` — cube, then square root (a power of `0.5`).

**Check**
- **Run:** `just test 01 -k r1e` → `8 passed`.
- **See:** what did `r1e2` print for `-7` and `2` on its second line, and why is it not `-3`?
- **Say:** which operator gives a float even when the answer is a whole number?

### Rung 2 — Types and conversions

*~45 min · feeds s01-r3, s01-r7, s02-r4 · bestiary T01, T02*

Every value has a type, and the type decides what the operators do. At the prompt:

```
>>> type(7)
<class 'int'>
>>> type(7.0)
<class 'float'>
>>> type("7")
<class 'str'>
>>> "7" + "7"
'77'
>>> 7 + 7
14
>>> "7" + 7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

`str` is text (a **string** of characters). `+` on two strings joins them; on two numbers it adds; on one of each it refuses, loudly, with the `TypeError` you met in stage 0. This is the break-lab's snippets 04 and 08.

Conversion is a call with the type's name:

```
>>> int("7") + 7
14
>>> str(7) + "7"
'77'
>>> float("3.5")
3.5
>>> int(3.9)
3
>>> int("3.9")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: '3.9'
```

`int()` of a float drops the fraction (toward zero). `int()` of text that is not a whole number raises `ValueError`: the type is fine, the value is not.

Now the rule that explains half the bugs in stage 1 and 2: **`input()` always gives a string.** Type `type(input())` at the prompt, enter `42`, and read the answer. Whatever the user types is text until you convert it. This is why the given lines in the exercises say `int(input())`, and it is [T02](../../docs/07-failure-bestiary.md#t--types-and-values): compared as text, `"9" > "10"` is `True`, because `"9"` comes after `"1"` in the alphabet. That was snippet 03.

**Exercises** (`just test 01 -k r2e`):

- `r2e1_plus_one` — text in, number plus one out.
- `r2e2_decimal_sum` — two decimals as text; print their sum.
- `r2e3_twice_as_text` — `12` → `1212`, then `24`. The same value, used as text and as a number.
- `r2e4_whole_part` — `-3.7` → `-3`. Two conversions in a row.

**Check**
- **Run:** `just test 01 -k r2e` → `8 passed`.
- **See:** what does `type(input())` print when you type `42`?
- **Say:** why does `"3" + "4"` give `"34"` and `3 + 4` give `7`?

## Part C — Names

### Rung 3 — Names

*~50 min · feeds every later rung; s03-r4 (aliasing)*

A **variable** is a name bound to a value with `=`. The right side is worked out first; then the name is attached to the result.

```
>>> price = 4
>>> price
4
>>> price = price + 1
>>> price
5
>>> price += 2
>>> price
7
>>> total = price * 3
>>> total
21
```

`price = price + 1` is not an equation; it is an instruction: work out `price + 1` (which is 5), then make `price` the name for that. `+=` is the same thing shorter; `-=`, `*=`, `/=` exist too.

The picture that will keep you out of trouble at stage 3: a name is a **label on a value**, not a box containing it. `total = price * 3` makes a new value, 21, and labels it `total`; later changing `price` does nothing to `total`, because `total` was never attached to `price`, only to the 21.

Names: letters, digits and underscores, not starting with a digit, case-sensitive (`Price` and `price` are two names). Use lower case with underscores (`unit_price`), say what the thing is (`total`, not `t`), and never reuse the names of things Python gives you: `print`, `input`, `int`, `str`, `len`, `type`, `sum`, `max`, `min`, `list`. (Reusing one hides the original: [F04](../../docs/07-failure-bestiary.md#f--flow).)

Two names can be swapped in one line: `a, b = b, a`. The right side makes both values first, then both names are attached.

**Your second Inspect tool.** Any file can be run so that every line prints itself and the names it changed:

```
just trace stages/01-values-and-names/solutions/r3e2_running_total.py
```

(It will ask for the three inputs.) Watch `total` change line by line. Use this whenever you cannot see what a program is doing; from rung 6 you will have a quicker tool for one value at a time.

**Exercises** (`just test 01 -k r3e`): `r3e1_swap`, `r3e2_running_total` (use `+=`), `r3e3_rectangle` (name the area and the perimeter before printing them), `r3e4_to_fahrenheit`.

**Check**
- **Run:** `just test 01 -k r3e` → `8 passed`.
- **See:** in the trace of `r3e2`, what was `total` after the second input line?
- **Say:** after `a = 5` then `b = a` then `a = 6`, what is `b`, and why?

## Part D — Text

### Rung 4 — Strings: length, index, slice

*~60 min · feeds s01-r5, s02-r5, s03-r1*

A string is a sequence of characters, and you can ask it how long it is and reach into it by position. Positions count from **zero**, and negative positions count from the end.

```
>>> word = "python"
>>> len(word)
6
>>> word[0]
'p'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[6]
Traceback (most recent call last):
  ...
IndexError: string index out of range
>>> word[1:4]
'yth'
>>> word[:2]
'py'
>>> word[2:]
'thon'
>>> word[::-1]
'nohtyp'
```

A **slice** `word[start:stop]` takes from `start` up to *but not including* `stop`: `word[1:4]` is positions 1, 2, 3. Leave out `start` for "from the beginning", `stop` for "to the end". The third number is the step; `-1` walks backwards. "Up to but not including" is the single most important convention in Python; it is why `len(word)` is 6 and the last position is 5, and why rung 5 of stage 2 will say the same thing about `range`.

Quotes: `"..."` and `'...'` are the same; use one inside the other when you need a quote in the text (`"it's"`). `\n` inside a string is a line break. Three quotes `"""..."""` make a string that spans lines.

Strings cannot be changed in place:

```
>>> word[0] = "P"
Traceback (most recent call last):
  ...
TypeError: 'str' object does not support item assignment
```

You make a new string instead: `"P" + word[1:]`. Every string operation in this course returns a *new* string and leaves the old one alone; rung 5's methods included.

**Exercises** (`just test 01 -k r4e`): `r4e1_how_long` (spaces count; the empty line has length 0), `r4e2_first_and_last`, `r4e3_inside` (drop the first and last character), `r4e4_backwards`.

**Check**
- **Run:** `just test 01 -k r4e` → `8 passed`.
- **See:** what are the positions of the characters in `word[1:4]`, and which character is *not* included?
- **Say:** why is the last character of a six-character string at position 5?

### Rung 5 — String methods

*~60 min · feeds s01-r9, s02-r4, s05-r4*

A **method** is an operation that belongs to a value, called with a dot: `word.upper()`. Strings have about forty. Try these:

```
>>> name = "  ada LOVELACE "
>>> name.strip()
'ada LOVELACE'
>>> name.strip().title()
'Ada Lovelace'
>>> name.upper()
'  ADA LOVELACE '
>>> "banana".count("a")
3
>>> "the cat sat".replace("cat", "dog")
'the dog sat'
>>> "hello.py".endswith(".py")
True
>>> "hello.py".startswith("h")
True
>>> "42".isdigit()
True
>>> "4.2".isdigit()
False
>>> "a,b,c".split(",")
['a', 'b', 'c']
>>> "  x  ".strip() == "x"
True
```

`isdigit()` answers whether every character is a digit; stage 2 uses it to check an answer before calling `int()` on it. Two things to notice. Methods can be chained (`name.strip().title()`): each returns a new string, and the next method is called on that. And `name` itself is unchanged after all of it; look at it again.

To see every method: `dir("")` at the prompt, or `help(str.strip)`. You are not expected to memorise them; you are expected to know they exist and to look.

(`split` gives back a list, in square brackets; lists are stage 3. You may use `split` now where an exercise needs it, and treat the result as something you can index with `[0]` and `[1]`, exactly like a string.)

**Exercises** (`just test 01 -k r5e`): `r5e1_shout`, `r5e2_tidy_name`, `r5e3_count_letter`, `r5e4_cat_to_dog`, `r5e5_is_python_file`.

**Check**
- **Run:** `just test 01 -k r5e` → `10 passed`.
- **See:** after `name.upper()`, what does `name` on its own show, and why?
- **Say:** what is the difference between `len(word)` and `word.upper()` in how you write them, and what does the dot mean?

### Rung 6 — f-strings and your third Inspect tool

*~50 min · feeds s01-r9, s02-r11, every later stage*

To put values inside text, write the text with an `f` in front and the values in braces:

```
>>> name = "Ada"
>>> age = 36
>>> f"{name} is {age} years old"
'Ada is 36 years old'
>>> price = 4.5
>>> f"${price:.2f}"
'$4.50'
>>> f"{name:<10}|{age:>5}|"
'Ada       |   36|'
>>> f"{name=}"
"name='Ada'"
```

After a colon comes a **format spec**: `.2f` means "a float with two decimal places"; `<10` means "left-aligned in a field ten wide"; `>5` means "right-aligned in five"; `^8` centres. They combine: `{price:>8.2f}` right-aligns a two-decimal float in eight characters. This is how every table, receipt and report in the course is laid out.

`f"{name=}"` prints the name *and* its value. It is the fastest way to see what a program is doing at a particular line, and it is your third Inspect tool after `print` and `just trace`. Put `print(f"{total=}")` on the line before the one that prints the wrong answer; read it; remove it when you are done. You will do this a hundred times.

**Exercises** (`just test 01 -k r6e`): `r6e1_introduce`, `r6e2_price_tag`, `r6e3_table_row`. The last one is a row of the receipt you will build in rung 9; count the spaces in the expected output carefully.

**Check**
- **Run:** `just test 01 -k r6e` → `6 passed`.
- **See:** in `r6e3`'s expected output, how wide is each of the three columns, and which spec produces each?
- **Say:** what does `print(f"{x=}")` show that `print(x)` does not?

## Part E — Truth

### Rung 7 — Truth, nothing, and the two kinds of same

*~60 min · feeds s02-r1, s02-r4, s03-r4 · bestiary T05, T06*

A comparison is a value like any other: its type is `bool`, and it has exactly two values.

```
>>> 3 < 5
True
>>> type(3 < 5)
<class 'bool'>
>>> 3 == 3.0
True
>>> 3 != 4
True
>>> 1 <= 5 <= 10
True
>>> "abc" == "ABC"
False
>>> "abc" < "abd"
True
>>> not True
False
>>> 3 < 5 and 5 < 4
False
>>> 3 < 5 or 5 < 4
True
```

`==` asks "equal?"; one `=` binds a name. Python itself will catch `if x = 5` with a `SyntaxError`, which is kinder than most languages. `and`, `or`, `not` combine conditions; `and` is only true if both sides are; `or` if either is.

**Truthiness.** Every value can be asked whether it is true. Zero, empty text, and `None` are false; everything else is true, including the text `"0"` and the text `"False"`, because they are not empty. That was snippet 06, and it is [T06](../../docs/07-failure-bestiary.md#t--types-and-values): `if name:` will skip an empty name, which is often what you want, and `if count:` will skip a count of zero, which often is not.

**`None`** is the value that means "nothing here". It is what `print()` returns, and what a function without a `return` gives back at stage 4. Its type is `NoneType`, and the way to test for it is `x is None`.

**`is` versus `==`.** `==` asks whether two values are equal. `is` asks whether two names are attached to the *same object*. Snippet 07 showed `a == b` true and `a is b` false for two separately-made thousands. For small numbers and short strings Python happens to reuse one object, so `is` will *look* like `==` until the day it does not ([T05](../../docs/07-failure-bestiary.md#t--types-and-values)). Rule: use `==` for values; use `is` only for `None`, `True` and `False`. You will see why `is` exists at stage 3, where two names on one list is the whole lesson.

**Exercises** (`just test 01 -k r7e`): `r7e1_three_questions`, `r7e2_in_range` (one comparison with two `<=` does it), `r7e3_truth_of_text` (the text `"0"` versus the number `0`), `r7e4_same_ignoring_case`.

**Check**
- **Run:** `just test 01 -k r7e` → `8 passed`.
- **See:** what did `bool("False")` print in the break-lab, and what did `bool("")` print?
- **Say:** why is `x is None` right and `x == None` merely usually right?

## Part F — Save and ship

### Rung 8 — Save points with git

*~40 min · feeds every later rung; s02-r10*

You have been editing files for ten hours with no record of what changed when. git is the record. In the course folder:

```
git status
```

It lists every exercise file you changed, in red, under "Changes not staged". Tell git which changes to include in the next save point, then make the save point with a message that says what changed:

```
git add stages/01-values-and-names/exercises/
git commit -m "feat(s01): r1-r7 exercises pass visible tests"
git status
git log --oneline
```

`git add` chooses; `git commit` saves; `git log --oneline` lists the save points, newest first, each with a short code and your message. The message is in the imperative and says what, with the stage in brackets; the shapes are in [docs/05](../../docs/05-conventions.md#commits). `update` or `stuff` is not a message.

The first time, git asks who you are: run the two `git config --global` lines it suggests, with your name and an email address (nothing is sent anywhere; this is a label on your save points).

From now on: one commit per rung at least. When something breaks that worked before, `git log` tells you what changed since, and `git diff` shows the exact lines. GitHub, where save points go to be shared, is stage 2.

Now go back and make a commit per rung for rungs 1–7, so the history reads as the work happened: `git add` just that rung's files, `git commit -m "feat(s01): r4 strings ..."`, and so on. It is a little artificial this once; from the next rung on, you commit as you go.

**Check**
- **Run:** `git log --oneline` → at least five lines, each a rung.
- **See:** what does `git status` say immediately after a commit?
- **Say:** what is the difference between `git add` and `git commit`?

### Rung 9 — Mini-project: the receipt

*~90 min · feeds gate s01-g1, s01-g4; s02-r11*

A whole program from a description, with nothing new in it. Read the comment at the top of `exercises/r9e1_receipt.py`: nine inputs, a header, three rows, a rule, a total, all in the column layout from rung 6. Before writing a line, run `just test 01 -k r9e` and read the expected output character by character; count the widths.

Plan it in the journal first: which names you need (one per input, one per line total, one for the grand total), which line prints what. Then write it top to bottom, running the test after every print line you add. When the test shows a difference, put `print(f"{line1=}")` above the first row and look.

When it passes:

1. Run it yourself: `uv run python stages/01-values-and-names/exercises/r9e1_receipt.py` and type a receipt of your own.
2. Try a quantity of zero. Try a price with three decimals. Does the output still line up? What happens with a name longer than ten characters? (The test does not check that; you should know anyway. Write the answer in the journal.)
3. Copy [`templates/ARTIFACT_CARD.md`](../../templates/ARTIFACT_CARD.md) to `stages/01-values-and-names/ARTIFACT_CARD.md` and fill every field. The kill-criteria field: would you write this program for one receipt? For a hundred?
4. Commit: `feat(s01): r9 receipt mini-project`.

Then the gate: `just eval 01`. It runs tests you have not seen, on inputs you have not seen, and writes the result to a folder you will cite in the card. Do not open `eval/` first; the number is only a measurement if you did not.

**Check**
- **Run:** `just test 01` → `57 passed`; `just eval 01` → `PASS`.
- **See:** in your eval run directory's `summary.json`, which exercise had the most hidden cases, and did any fail?
- **Say:** what would make this receipt program give a wrong total without crashing? (Hint: rung 1, snippet 01.)

## Measure, Break, Inspect in this stage

- **Measure** is the tests. Visible ones in `tests/` tell you when a rung is done; hidden ones in `eval/` tell you whether you understood or memorised. Read failures in full; the expected output is the specification.
- **Break** was the break-lab and will be every traceback you meet. Each time you hit one, say the kind and the line before you fix it.
- **Inspect** gained three tools: `print`, `just trace`, and `f"{x=}"`. The habit: when the output is wrong, look at the value on the line before, not at the code.

## Artefact

- `exercises/r1e1` … `r9e1` complete, tests green.
- `JOURNAL.md` with the break-lab table (predictions and results) and one entry per session.
- `ARTIFACT_CARD.md` for the receipt.
- `eval/runs/<ts>-<sha>/summary.json` from the run cited in the card.
- git history with one commit per rung.

## Gate

The universal checklist `u1`–`u10` in [docs/06](../../docs/06-assessment-and-gates.md) applies, and:

- [ ] **s01-g1** `just eval 01` ≥ 57 of 63 hidden cases, run directory cited in the card.
- [ ] **s01-g2** Three Say questions answered without notes, from rungs 1, 4 and 7 (the reviewer picks which; solo: write them in the journal from memory, then check).
- [ ] **s01-g3** `git log --oneline` shows ≥ 5 commits with messages that say what changed.
- [ ] **s01-g4** The receipt runs from the terminal on the reviewer's inputs and its columns align; the card's "how it fails" names at least one input that misaligns or miscounts it.

Rubric anchors for this stage are in [docs/14](../../docs/14-rubrics.md#anchors-stage-1).

## Kill criteria

A receipt for three items is a calculator job; the program earns its place when the layout must be identical every time, or there are thirty items, or someone else will run it. You wrote it to learn; the card should say so honestly. More generally: before you write a program that does arithmetic on a handful of numbers once, ask whether a spreadsheet already is that program.

## Stretch

- Make the receipt accept a discount percentage as a tenth input and show it as a negative line.
- At the prompt, find out what `round(2.675, 2)` gives, and why ([T04](../../docs/07-failure-bestiary.md#t--types-and-values) again).
- Read `help(str)` from the top until you find a method you did not know; use it once.

## Reading

[docs/09 — Stage 1](../../docs/09-reading-list.md#stage-1--values-and-names): Ned Batchelder's *Facts and myths about Python names and values* after rung 3 is the one not to skip.
