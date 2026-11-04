# 00 — Intent

## The problem this curriculum solves

Most "learn Python" material for beginners teaches syntax. The student finishes able to recognise a `for` loop and unable to do the only things that matter on a team:

- Turn a sentence from a colleague into a program that runs, with a test that says so.
- Read an error message without panic, and a wrong-but-silent result with suspicion.
- Find the bug, in their own code and in someone else's.
- Know whether the standard library already does it, and whether it should be code at all.
- Use the tools a team uses — a terminal, git, a package manager, a test runner, a linter, a debugger — without stopping to think about them.

Syntax is the easy part and the cheapest to look up. The habits above are what employers are short of in a junior, and they are formed by repetition from the first hour, not by a module in week twelve. This curriculum teaches the habits, with the syntax arriving in the order the habits need it.

## The one-sentence goal

Take a person who has never written a line of code, and produce a junior developer who can be handed a plain-language task on day one, write a tested, documented command-line program for it, read the traceback when it fails, see inside it when it is quietly wrong, and say so when it should not have been a program at all.

## What mastery means here

Mastery is **fluency plus judgment, proven by tests**. Concretely, a graduate:

1. Reads and writes idiomatic Python without translating from another notation in their head; the collection, the comprehension, the dataclass and the `with` block are reflexes, not look-ups.
2. Never says a program works without having run its tests, and never trusts a test they have not seen fail.
3. Reads a traceback bottom-up, names the exception, finds the line, and fixes the cause rather than the symptom. Knows the quiet failures — aliasing, mutable defaults, `is` vs `==`, float precision, off-by-one, swallowed exceptions — by name and by smell.
4. Can see inside any program they wrote: a `print` in the right place, a breakpoint, a log line, a timing. Never ships one they cannot see inside.
5. Reaches for the standard library before a package and for documentation before guessing; can read a module's source and a colleague's pull request.
6. Knows that most small tasks do not need a class, that many do not need a program, and can say which, with reasons.

## Why the shape is what it is

- **Ten gated stages plus a two-hour on-ramp**, because one stage equals one working program with tests and a measurable gate, and ten of those is a portfolio. Five would put gates three weeks apart, too far for a beginner's misconceptions to be caught; twenty would turn capabilities into topics and lose the thread. Argued in [ADR-001](decisions/ADR-001-ten-stages-four-tiers-four-strands.md).
- **Four tiers** — *Talking to the machine*, *Structure*, *Objects*, *Craft* — because working memory holds about four chunks, and the learner should be able to say where they are in the arc without looking.
- **Four strands in every stage** — Build, Measure, Break, Inspect — because testing, debugging and reading failures are not modules you reach after the syntax. They are habits, and habits form by repetition from day one.
- **Worked example first, then exercises**, because novices learn more from studying complete, running code than from unguided problem-solving, and the effect is largest for exactly this learner. Every rung shows the code in full, has the learner run it, and only then asks for variations.
- **Break-labs open every stage**, because students who struggle with a problem before instruction learn the concept more deeply than those instructed first. "Predict the output, then run it" is that finding in six lines of code.
- **Tests from stage 1, written by the course**, because a beginner cannot yet write a test but can run one, watch it go from red to green, and learn what "it works" means before learning how to say it in code. The learner writes their own tests from stage 6.
- **Exercise volume**, because fluency is the destination and fluency comes from many small repetitions, not a few large projects. Every rung carries four to eight micro-exercises; every stage ends with a mini-project that combines them.

The full evidence base is in [03 — Pedagogy](03-pedagogy.md).

## What we deliberately leave out

- Web frameworks, GUIs and notebooks. The artefact is always a command-line program; the skills transfer, the frameworks churn.
- Data science libraries and machine learning. That is the sibling course; this one delivers the Python it assumes.
- Concurrency beyond vocabulary. `threading` and `asyncio` are named in stage 9 so the words are not frightening later; using them is a different course.
- Metaclasses, descriptors, the import system's internals, C extensions. A junior does not need them in week one.
- Any single vendor's certification path.

Each omission is a trade: it buys time for exercises, tests, debugging and reading, which are the parts a beginner is actually short of.

## The Programmer's Oath

Learners write this into their stage-1 journal and are held to it at every gate.

> 1. I will run my program before I say it works.
> 2. I will read the whole error message before I change anything.
> 3. I will not trust a test I have never seen fail.
> 4. I will not ship a program I cannot see inside.
> 5. I will reach for the standard library before a package, and for no code at all before either.
> 6. I will name a thing for what it is.
> 7. I will be able to explain every line I ship, including the ones I did not write.
> 8. I will say "this should not be a program" when a spreadsheet does it.

## Success, as a story

Day one, the learner has never opened a terminal. Two hours later they have typed `print("Hello, world")` into one, saved it in a file, broken it on purpose three times and read each error message. By the end of stage 2 they have written a text game that loops until the player wins, and watched forty tests go green. By the end of stage 3 they can say, unprompted, why two names can point at the same list and why that bit them. By the end of stage 5 they have read a four-screen traceback to its root and written a program that reads a messy file without crashing. By the end of stage 6 they have written their own first test and seen it fail before it passed. By the end of stage 8 a colleague's "break my program" session finds two bugs in their code, and they fix both with a test for each. By the end of stage 10 they have shipped a tested, typed, documented command-line application, written its post-mortem, explained a dataclass to a non-programmer, and opened the Stage 0 brief of the next course to find they already know every word in it.

That is the deliverable. Everything else in this repository exists to produce it.
