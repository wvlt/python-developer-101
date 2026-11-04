# Post-mortem — <program or session> — <date>

> Blameless. Specific. Written so that someone writing a similar program next year avoids the same thing.
> Used after a break-my-program session, after any bug that reached a user (a reviewer, a peer, you a week later), and for the stage-10 capstone (where it is written regardless of whether anything went wrong).

## Summary

Three sentences: what the program is, what happened (or what was learned), what changed as a result.

## Timeline

For a bug that reached someone. Who noticed, how, and how long each step took.

| Time | Event | Source (test / peer / reviewer / own use) |
|---|---|---|
| | | |

Time from the bug being written to being noticed: · Time to locate: · Time to fix: · Tool that located it:

## Impact

- Wrong outputs produced (count, which ones):
- Files changed or lost:
- Anyone who acted on a wrong output:

## Root cause

The mechanism, not the symptom. Reference a bestiary ID or propose one with a snippet. If several causes contributed, list all and mark the one without which it would not have happened. "I was careless" is a symptom; "the function mutated the list it was given, and the caller used the list again" is a mechanism.

## What the tests missed

Which test, had it existed, would have caught this before anyone saw it? Why did it not exist? Add it now and link the test name or case ID.

## What Inspect missed

Was the wrong value visible in the log? Would a breakpoint on the right line have shown it in under a minute? If a human noticed it by reading output, what should have reported it first?

## What went well

Specifically: the test that limited the damage, the log line that made it fast to find, the `with` that closed the file anyway.

## Action items

| Action | Owner | Due | Type (test / structure / log / docs / habit) | Done |
|---|---|---|---|---|
| | | | | |

"Be more careful" is not an action item. A test, a changed signature, a log line, a `ruff` rule enabled, or a README sentence is.

## For capstones only: reflections

- What would you build differently from the start?
- Where did the break-my-program session disagree with your failure review, and what does that say about how you predict failure?
- Was a program the right choice? Answer with the kill criteria. If the answer is "a spreadsheet", say so with the spreadsheet attached; that is a passing answer.
- Which of the ten day-one capabilities in `CONTEXT.md` do you now have, and which rung gave you each?
- What do you now believe about programming that you did not believe at stage 0?
