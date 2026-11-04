# Rung authoring template

Every rung in a rung-numbered brief has this shape. Copy the block, fill every field, delete the comments. Rules are in [docs/15-authoring-guide.md](../docs/15-authoring-guide.md); the rubric is in [docs/14-rubrics.md](../docs/14-rubrics.md#the-rung-rubric-run--see--say).

```markdown
### Rung M — <imperative title, ≤ 7 words>

*~<minutes> min · feeds <sNN-rK, sMM-rJ or "gate sNN-gK">*

<!-- WHY: one sentence. What this rung lets you do or see that you could not before. -->

<!-- WORKED EXAMPLE: the code, complete, then its output. Shown before the concept is named. Type it, do not paste it, in stages 0–2 (say so). -->

<!-- NAME IT: at most three new terms, each in the sentence that first uses it. Link the bestiary entry if the rung meets one. -->

<!-- EXERCISES: `exercises/rMeK_name.py`, K = 1..n, one line each: the task and `just test NN`. From stage 2, one may be a planted bug (rMbK). -->

**Check**
- **Run:** `<command>` → <exact observable result>.
- **See:** <one question with a checkable answer about what the rung reveals>.
- **Say:** <one sentence the learner should be able to produce without notes, connecting this rung to a later one or to a principle>.
```

## Example (from stage 1)

```markdown
### Rung 7 — Truth, nothing, and the two kinds of same

*~60 min · feeds s02-r1, s03-r4 (aliasing)*

A condition is a value like any other; and "equal" and "the same object" are different questions.

Type this into the REPL:

    >>> 3 < 5
    True
    >>> type(3 < 5)
    <class 'bool'>
    >>> a = 1000
    >>> b = 1000
    >>> a == b
    True
    >>> a is b
    False

`True` and `False` are the two values of the type `bool`. `==` asks "do these have the same value?"; `is` asks "are these the very same object?" — a question you will need at stage 3 and should use only for `None` until then. ...

Exercises r7e1–r7e5: `just test 01`.

**Check**
- **Run:** `just test 01 -k r7` → `5 passed`.
- **See:** what did `a is b` print for `a = 1000; b = 1000`, and what for `a = 5; b = 5`?
- **Say:** why is `x is None` right and `x == None` merely usually right?
```

## Rules of thumb

- One concept per rung. If the *See* question needs "and", split the rung.
- *Run* is binary and local: no judgment, no "it should look reasonable".
- *See* must be answerable from something the learner produced in this rung (output, a test result, a traceback). Never from the brief.
- *Say* is the self-explanation; it is the item most likely to fail, and that failure is the most useful signal. The gate's Say questions are drawn from these.
- Time estimates include the exercises and are for the learner in [CONTEXT.md](../CONTEXT.md), typing not pasting. Re-estimate from feedback; do not pad.
- "Feeds" is how the cascade check finds dependents. Keep it accurate.
- A rung with no code and no exercise is a paragraph, not a rung. Move it into the previous rung's WHY or the stage intro.
- Nothing in the rung may use a construct a later rung introduces. If the example needs a loop and loops are next stage, find another example.
