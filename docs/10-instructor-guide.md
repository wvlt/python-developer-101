# 10 — Instructor guide

For anyone running this curriculum with a cohort, a study group, or a single mentee. Self-paced learners should read it too; it tells you what a good reviewer looks for, and the [break-my-program protocol](#break-my-program-protocol) is how you get a peer review even when working alone.

## Your job

Not to lecture. The briefs carry the content. Your job is:

1. Run the break-labs so the failure lands before the explanation.
2. Watch learners read tracebacks. Most instruction time at stages 0–2 is this.
3. Review gates honestly and quickly, with the eval run open.
4. Catch the misconceptions below early.
5. Protect the kill criteria: praise the learner who concludes "a spreadsheet does this" with the spreadsheet attached.
6. Enforce the AI-assistance policy by asking learners to explain their own lines. Not as a trap; as the habit.

## Cohort format

- **Cadence:** stage 0 in the first session; then one stage per 1–1.5 weeks at 8–10 h/week; stage 10 gets two weeks. About sixteen weeks.
- **Session structure (2 h, twice a week):** 20 min break-lab debrief (learners report predictions vs results); 30 min concept, taught from the learners' own wrong predictions; 70 min lab with instructors circulating, reading tracebacks over shoulders and asking "what do you expect this line to print?"
- **Office hours:** traceback-only until stage 5, test-only after. A learner may not ask a question without the full error text or a failing test. "It doesn't work" is returned with "show me what it said."
- **Pairs:** for the break-my-program sessions (stage 5 onward, mandatory at 10); for the stage 8 comparison memo; rotate for stage 10 teach-back.
- **Gate reviews:** 20 minutes per learner per stage, per the [procedure in docs/14](14-rubrics.md#how-a-gate-review-runs-20-minutes). Two reviewers if possible.

## Pacing signals

- If more than a third of the cohort has not finished stage 0 in one sitting, the installation step is the problem, not the learners. Check [PINS.md](../PINS.md) and the platform notes in the stage 0 brief.
- Stage 1 is where "I am not a programmer" surfaces. The receipt mini-project is designed to be finishable; make sure everyone finishes it.
- Stage 3 (aliasing) and stage 4 (scope, mutable defaults) are where cohorts stall. Run the break-labs as a group and let the wrong predictions be seen.
- If stage 6 goes quickly, that is expected: the tools were introduced one at a time earlier and this stage names what they already use.
- Stage 7 learners over-build. Ask "what would this be without the class?" before "does it work?"
- Stage 9 should feel like measurement, not building. If it is slow, they are rewriting instead of timing.

## Misconceptions, in order of appearance

**"The computer is being difficult / I broke it."** (S0) The traceback is the computer being as helpful as it can. Read it aloud with the learner, bottom line first, every time, until they do it without you.

**"A variable is a box that holds the value."** (S1–S3) It is a label on an object. The box model works until two labels are on one list. Ned Batchelder's article and the stage 3 aliasing break-lab; do not try to pre-empt it in stage 1 beyond the single `is` vs `==` rung.

**"`input()` gave me a number because I typed a number."** (S1) It gave a string. The `TypeError` on `+ 1` is the lesson; let it happen.

**"The loop variable should keep its value."** (S2) It does, actually; the surprise is that it does. Shadowing is the real problem.

**"`if answer == 'yes' or 'y'`"** (S2) Truthiness. Let them test it with `"no"`.

**"`sort()` sorted it, so why is it `None`?"** (S3) In place versus returned. One `print(items.sort())` ends the confusion.

**"Printing inside the function is returning."** (S4) `result = f(); print(result)` shows `None`. Have them write the function twice, once each way, and call it from a test.

**"`except: pass` makes the error go away."** (S5) It makes the *message* go away. Run the program with the file missing and watch it report success.

**"Pickle is just saving."** (S5) Show the eight-line pickle that opens a calculator. It takes two minutes and nobody forgets it.

**"Tests are for after it works."** (S6) The planted-bug exercise: tests written after the fact pass on buggy code with surprising frequency. Count how many of each learner's tests catch the bug.

**"Classes are what professionals use."** (S7) A class is for state plus behaviour plus an invariant. The kill criterion question, every mini-project.

**"Type hints make it faster / safer at runtime."** (S9) Python ignores them. `mypy` reads them. Demonstrate by hinting `int` and passing a string.

**"The capstone needs to be impressive."** (S10) It needs to run on bad input, be tested, and be handed to a stranger with a README. Say so on day one of the stage.

## Break-my-program protocol

The peer-review equivalent of the agents course's red-team. From stage 5 it is recommended at every mini-project; at stage 10 it is a gate criterion. The form is [`templates/BREAK_MY_PROGRAM.md`](../templates/BREAK_MY_PROGRAM.md).

1. **Owner prepares (10 min).** Pushes the branch; writes the one-paragraph "what it does" and the list of inputs it is supposed to handle; opens `FAILURE_REVIEW.md` and does *not* show it to the breaker yet.
2. **Breaker reads (10 min).** The README and the CLI `--help` only. Not the code, not the tests. Writes down five inputs they expect to break it, drawing on the [quiet failures list](07-failure-bestiary.md#q--the-quiet-failures-the-risk-model).
3. **Breaker breaks (40 min).** Runs the program on each planned input and anything it suggests: empty files, the broken fixtures, a file in Latin-1, a negative count, a date in the future, the same ID twice, a huge number, Unicode in a name, `--count abc`, Ctrl-C mid-write, running from a different directory, running twice. Every unexpected behaviour is a finding: the input, what happened, what should have happened, and whether it was **loud** (traceback) or **quiet** (wrong output, no error). Quiet findings count double.
4. **Owner fixes (in their own time, before the next session).** For every finding: a test that fails on the old code, a fix, and a line in the post-mortem. Findings the owner disagrees with are argued in the report, not ignored.
5. **Compare (10 min, together).** Open `FAILURE_REVIEW.md`. Which findings were anticipated and prevented? Which were anticipated and not prevented? Which were not anticipated? The third list is the lesson.
6. **Swap roles.**

Solo learners: do steps 2–3 yourself *the next day*, on a fresh clone, reading only the README. It is less effective than a peer (you know where the bodies are buried) and far more effective than nothing. Record it in the same form.

## Reading a traceback with a learner

The highest-value five minutes at stages 0–5. Script:

1. "Read me the last line." (Exception type and message.)
2. "Which file and line does the line above point at? Open it."
3. "What did you expect that line to do? What does the message say it did?"
4. "Is this a loud failure of *this* line, or did this line get a bad value from somewhere above? Read up one frame."
5. "Before you change anything, say what you think the fix is and what you expect to see after."

Do not touch their keyboard. Do not say the fix. If they are stuck after step 4, ask them to put `print(f"{name=}")` (stage 1) or `breakpoint()` (stage 4) on the line above and run it again.

## Reviewing a mini-project (checklist for the 20 minutes)

- Open the eval run directory; the counts match the card.
- Run the program on one input from the brief and two of your own, one of them malformed.
- Pick one function; ask the learner to explain it line by line.
- Ask the three Say questions.
- Ask the kill-criterion question: "if I asked you to do this once, for one file, what would you do instead?"
- Check the commit log: one per rung at least, messages that say what changed.
- From stage 7: pick one AI-review note in the card and ask what the learner did with it.

## When you suspect assistance beyond the policy

Ask the learner to add a feature live, in front of you, of the same size as one rung. Not as punishment: as the only measurement that cannot be faked. If they can, the number on the card stands. If they cannot, the number does not, and the conversation is about what they want from the course, not about rules.
