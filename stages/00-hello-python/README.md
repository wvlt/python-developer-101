# Stage 0 — Hello Python

*Tier A · ~2 hours · Cost: zero · No account, no git, no tests yet*

## Why this stage exists

This is the first time you tell a computer what to do in its own language and it does it. Before variables, before loops, before anything with a name, you will install Python and an editor, type one line, and watch the computer print it back. Then you will change one thing at a time and watch what each change does. Nothing here is graded. Everything here is the foundation the rest of the ladder assumes you can do without thinking: open a terminal, run a file, read what the computer says when it cannot.

Do every rung in order. Type everything; do not paste. Typing is where the learning is.

## Contract

**Assumes:** nothing about programming. You can install an application, make a folder, and follow precise written instructions. A laptop running macOS or Windows (Linux: follow the macOS lines).

**Provides** (stage 1 takes these for granted):
- Python and the editor are installed and you can open a terminal and run `python3 --version` (`s00-r0`).
- You can type a line into the Python prompt and read what comes back (`s00-r1`).
- You can save a `.py` file in the editor and run it from the terminal (`s00-r2`).
- You can print text, print two things on one line, and tell the difference between a number and text in quotes (`s00-r3`, `s00-r4`).
- You have broken a program three ways on purpose and read the last line of each error (`s00-r5`).
- You have made a program that asks a question and answers with what was typed (`s00-r6`).
- You have a practice folder, and the habit of a comment on the first line and running from the terminal (`s00-r7`).

Rung IDs: rung M here is `s00-rM`; its checks are `s00-rM.run`, `.see`, `.say`. Feedback on any rung goes in a [stage feedback](../../templates/STAGE_FEEDBACK.md); changes land in [`REVISIONS.md`](REVISIONS.md).

## Entry condition

A laptop you can install software on, with about 2 GB of free disk space, an internet connection for the two downloads, and two hours. That is all. You do not need to create any account.

**Two platforms, one course.** Where macOS and Windows differ, both are shown, macOS first. The one difference that matters all the way through: on macOS the command is `python3`; on Windows it is `python`. Every command in this brief is written as `python3`; if you are on Windows, type `python`.

## Break-lab (first)

Before you touch the computer, open the journal you will keep for this course (a paper notebook is fine until rung 7) and write down what you think the computer will do with each of these three lines. Guess. Being wrong is the point.

1. `print("Hello, world")`
2. `print(Hello, world)`
3. `print("2 + 3")`

You will find out at rungs 1, 5 and 4. Journal it: three guesses, one line each, and the question: *what do the quotes do?*

## Part A — The machine

### Rung 0 — Install Python and the editor

*~25 min · feeds every later rung*

Two installations and one check. Both installers are linked from [`PINS.md`](../../PINS.md), which is the one place in this course that version numbers live; use the links there, not a search engine.

**1. Python.** Download the installer for your platform from the link in PINS.md and run it.

- *macOS:* click through the installer with the defaults. When it finishes, a Finder window opens on the Python folder; you can close it.
- *Windows:* on the **first screen** of the installer, tick the box at the bottom that says **Add python.exe to PATH** before clicking *Install Now*. If you miss it, uninstall and run the installer again; this box is what lets the terminal find Python.

**2. The editor.** Download the editor from its link in PINS.md and install it. Open it. On the left edge, click the Extensions icon (four squares). Search for `Python`, and install the extension published by Microsoft (the top result; PINS.md names it). The editor will suggest it again when you open your first `.py` file; either route is fine.

**3. Open a terminal.** A terminal is a window where you type a command, press Enter, and read what comes back. Everything in this course runs from one.

- *macOS:* press Cmd+Space, type `Terminal`, press Enter.
- *Windows:* press the Windows key, type `PowerShell`, press Enter.

You will see a line of text ending in a symbol such as `%`, `$` or `>` with a cursor after it. That is the prompt: the terminal waiting for you. Type this and press Enter:

```
python3 --version
```

(Windows: `python --version`.) The reply is one line: the word `Python` and a version number. If it matches the version in PINS.md, you are done. If it says `command not found` or `not recognized`, close the terminal, open a new one, and try again; if it still fails, on Windows re-run the installer with the PATH box ticked, and on macOS run `python3` on its own and follow what it says.

**Check**
- **Run:** `python3 --version` → `Python` followed by the version in PINS.md.
- **See:** what symbol does your terminal's prompt end with, and what does the editor's Extensions panel show next to the Python extension?
- **Say:** in one sentence, what is a terminal for?

### Rung 1 — Hello in the prompt

*~10 min · feeds s00-r2, s01-r1*

Python has its own prompt, where you type one line and it answers at once. In the terminal, type:

```
python3
```

Three lines of text appear, then a new prompt: `>>>`. You are now talking to Python, not to the terminal. Type exactly this, including the quotes, and press Enter:

```
>>> print("Hello, world")
Hello, world
```

(You type the part after `>>>`; Python prints the second line.) That is a program. `print` shows whatever is inside the brackets; the quotes mark where the text begins and ends. Now try without `print`:

```
>>> "Hello, world"
'Hello, world'
```

The prompt shows you the value, in quotes, because it is text and the prompt always shows you what a line is worth. `print` shows text the way a person would read it, without the quotes. You will use `print` in files; the bare form is for looking at things at the prompt.

To leave the prompt and return to the terminal:

```
>>> exit()
```

Check your break-lab guess for line 1.

**Check**
- **Run:** `python3`, then `print("Hello, world")` → `Hello, world` on the next line.
- **See:** what is the difference between what `print("Hello, world")` shows and what `"Hello, world"` on its own shows?
- **Say:** what does `exit()` do, and how do you know you are back in the terminal?

### Rung 2 — The same line in a file

*~15 min · feeds every later rung*

The prompt forgets everything when you leave. A file keeps it.

**1. Make a folder.** On your Desktop, make a new folder called `hello`. (Finder: File → New Folder. Explorer: right-click → New → Folder.) No spaces in the name; the terminal treats a space as the end of a word.

**2. Open the folder in the editor.** In the editor: File → Open Folder, choose `hello`, confirm. If it asks whether you trust the authors, say yes; you are the author. The left pane now shows the folder, empty.

**3. Make the file.** In the left pane, click the *New File* icon (or File → New File), name it `hello.py`, press Enter. The `.py` ending tells the editor and Python that this is a Python file. Type, in the file:

```python
print("Hello, world")
```

Save it: Cmd+S on macOS, Ctrl+S on Windows. A dot on the tab means unsaved; it goes away when you save.

**4. Run it from the terminal.** You need a terminal that is *in* the `hello` folder. The simplest way: in the editor, View → Terminal. A terminal opens at the bottom of the editor, already in your folder. Type:

```
python3 hello.py
```

You see `Hello, world`. The terminal ran Python, Python read your file top to bottom, and the one line in it printed.

If instead you see `can't open file` or `No such file or directory`, the terminal is not in the folder. In the editor's terminal, type `pwd` (macOS) or `Get-Location` (Windows) and read the path: it should end in `hello`. If not, close that terminal and open a new one from View → Terminal.

**Check**
- **Run:** `python3 hello.py` → `Hello, world`.
- **See:** in the editor, what colour is the text inside the quotes compared with the word `print`? (The editor colours the parts of a line by what they are; this is the first tool you have for seeing what Python sees.)
- **Say:** why does the file still work after you close the editor and the prompt does not?

## Part B — One change at a time

From here, each rung changes `hello.py` in one way. Save and run after every change; the loop is edit → save → run → read. You will do it a thousand times in this course; make it a reflex now.

### Rung 3 — Change the text; print two things

*~10 min · feeds s01-r4*

Change the text inside the quotes to your own name. Save. Run. It prints your name. Now add a second line:

```python
print("Hello, Ada")
print("Welcome to Python")
```

Save, run: two lines, in the order they are in the file. Python runs a file from the top, one line at a time, and does not skip or reorder. Now put both on one line with a comma between them:

```python
print("Hello,", "Ada")
```

One line of output: `Hello, Ada`. `print` takes any number of things separated by commas and prints them on one line with a space between each.

**Check**
- **Run:** a file with `print("Hello,", "Ada")` → `Hello, Ada` on one line.
- **See:** where did the space between `Hello,` and `Ada` come from? You did not type it inside either pair of quotes.
- **Say:** if you swap the two `print` lines in the file, what changes in the output, and why?

### Rung 4 — A number and a word

*~10 min · feeds s01-r1, s01-r2*

Replace the file's contents with these three lines:

```python
print(2 + 3)
print("2 + 3")
print("2 + 3 is", 2 + 3)
```

Save, run:

```
5
2 + 3
2 + 3 is 5
```

The first line has no quotes: Python sees two numbers and a plus, and works it out. The second line has quotes: Python sees text, and text is printed as it is, even if it looks like arithmetic. The third line mixes them. Check your break-lab guess for line 3.

Now try `print(2 + 3 * 4)` and `print((2 + 3) * 4)`. Multiplication is `*`, and brackets decide what is done first, exactly as in school.

**Check**
- **Run:** the three-line file → `5`, `2 + 3`, `2 + 3 is 5`.
- **See:** what did `print(2 + 3 * 4)` print, and what did the version with brackets print?
- **Say:** in one sentence, what do quotes tell Python?

### Rung 5 — Make it fail on purpose, three ways

*~20 min · feeds every later rung; s01 break-lab*

Programs fail. The skill is not avoiding failure; it is reading what the computer says when it happens, because it always says *where* and usually says *what*. You will now break the program three ways and read each message. For each: make the change, save, run, and read the output **from the bottom line up**.

**Way 1 — misspell `print`.** Change the line to `pirnt("Hello, world")`. Run. You see something like:

```
Traceback (most recent call last):
  File "/Users/ada/Desktop/hello/hello.py", line 1, in <module>
    pirnt("Hello, world")
    ^^^^^
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
```

This block is a **traceback**: the computer's account of where it was when it stopped. Read the last line first: the kind of problem (`NameError`), then what it was (`name 'pirnt' is not defined`), then, when Python can guess, a suggestion. The line above it tells you *where*: the file, `line 1`, and the line itself with a marker under the problem. Fix the spelling; run; it works again. (Bestiary [S03](../../docs/07-failure-bestiary.md#s--syntax-and-names-always-loud).)

**Way 2 — forget a quote.** Change the line to `print("Hello, world)`. Run:

```
  File "/Users/ada/Desktop/hello/hello.py", line 1
    print("Hello, world)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

A `SyntaxError` means Python could not even read the line: the text was opened with a quote and never closed. Notice there is no `Traceback` heading this time, because the program never started. Fix it. (Bestiary [S01](../../docs/07-failure-bestiary.md#s--syntax-and-names-always-loud).)

**Way 3 — add text to a number.** Change the line to `print("Hello" + 3)`. Run:

```
TypeError: can only concatenate str (not "int") to str
```

A `TypeError`: you asked Python to join text (`str`) and a whole number (`int`) with `+`, and `+` does not know how to do that. (It would work with `print("Hello", 3)`; the comma is `print` putting two things side by side, not adding them.) Fix it. (Bestiary [T01](../../docs/07-failure-bestiary.md#t--types-and-values).)

Check your break-lab guess for line 2 by running `print(Hello, world)`. Which of the three kinds is it? Read the last line and decide.

Journal it: for each of the three (four, with the break-lab line), copy the last line of the message and write one sentence saying what you had done wrong.

**Check**
- **Run:** each of the three broken versions prints a message whose last line starts with `NameError`, `SyntaxError` or `TypeError`; each fixed version prints `Hello, world` again.
- **See:** in the `NameError` message, which line number did Python point at, and what suggestion did it make?
- **Say:** when a program stops with a traceback, which line do you read first, and what does the line above it tell you?

### Rung 6 — Ask a question

*~10 min · feeds s01-r9, s02-r4*

A program can wait for you to type something. `input()` prints a question, waits for a line, and hands back what was typed. Put the whole thing inside `print`:

```python
print("Hello,", input("What is your name? "))
```

Save, run. The program prints the question and stops with the cursor after it. Type your name, press Enter. It prints `Hello,` and your name. Python ran the inside bracket first (ask, wait, take the answer) and then the outside one (print). Notice the space before the closing quote in the question; without it, your typing would touch the question mark.

Run it again and type a number. It prints `Hello, 42`. To `input()`, everything typed is text; you will meet the consequences of that in stage 1.

**Check**
- **Run:** the one-line file asks `What is your name? `, waits, and prints `Hello,` and what you typed.
- **See:** what did the program print when you typed nothing at all and pressed Enter?
- **Say:** which bracket did Python finish first, the inner `input(...)` or the outer `print(...)`, and how do you know?

## Part C — The habit

### Rung 7 — A folder, a file, a comment

*~15 min · feeds every later stage*

Everything you write from now on goes in one place, every file says at the top what it is for, and every file is run from the terminal. This is the habit professionals have and beginners are not told about.

**1.** Make a folder on your Desktop called `python-practice`. Open it in the editor (File → Open Folder). This folder is where every stage's scratch work goes until stage 1 gives you the course folder.

**2.** New file: `day1.py`. First line is a **comment**: a line that starts with `#`, which Python ignores and people read. Then three lines of program:

```python
# day1.py — the first things I made Python do
print("Hello, world")
print("2 + 3 is", 2 + 3)
print("My name is", input("Name? "))
```

**3.** View → Terminal; `python3 day1.py`; answer the question.

**4.** Make the journal a file too: `JOURNAL.md` in the same folder, and move today's break-lab guesses and the three error lines from rung 5 into it. `.md` is plain text with light formatting; the editor shows it nicely with Cmd/Ctrl+Shift+V.

From now on, every program you write starts with a comment that says what it is, and you run it with `python3 name.py` from a terminal in the folder. When something goes wrong you read the last line of the traceback first.

**Check**
- **Run:** `python3 day1.py` from a terminal in `python-practice` → three lines, the last one containing your name.
- **See:** what does the editor do to the colour of the comment line, and what happens to the output if you delete the `#`?
- **Say:** three things every program of yours will have from now on.

## Done when

Stage 0 has no gate. It is done when every Check above is ticked in your journal, and you can do these from memory, without the brief:

- [ ] Open a terminal in a folder and run a `.py` file with `python3`.
- [ ] Open the Python prompt, print something, leave it.
- [ ] Make a new `.py` file in the editor with a comment on the first line.
- [ ] Print text, print a number, print two things on one line.
- [ ] Break a line on purpose and read the last line of the traceback aloud: the kind, the message, the line number.

Then start [Stage 1](../01-values-and-names/README.md), rung 0, which installs the rest of the toolchain and brings you into the course folder.

## Kill criteria

You wrote `print(2 + 3)`. For one sum, once, the calculator on your phone is the right tool and you should use it. A program earns its place when the same steps will run many times, on different inputs, or must be shown to someone else. Every stage from here asks you this question about the thing you just built.

## Stretch

- In the Python prompt, try `print("=" * 20)`. Then `print("ab" * 3)`. Then `print("ab" + 3)` and read the error. Guess first.
- Make `day1.py` ask two questions and print both answers on one line.
- Find out what `help(print)` shows at the prompt (press `q` to leave the help screen).

## Reading

[docs/09 — Stage 0](../../docs/09-reading-list.md#stage-0--hello-python): the first chapters of the official tutorial, after rung 7, not before.
