# Rung authoring template

Every rung in a rung-numbered brief has this shape. Copy the block, fill every field, delete the comments. Rules are in [docs/15-authoring-guide.md](../docs/15-authoring-guide.md); the rubric is in [docs/14-rubrics.md](../docs/14-rubrics.md#the-step-rubric-run--see--say).

```markdown
### Rung M — <imperative title, ≤ 7 words>

*~<minutes> min · feeds <sNN-rK, sMM-rJ or "gate sNN-gK">*

<!-- WHY: one sentence. What this rung lets you do or see that you could not before. No more than one sentence; motivation beyond that belongs in the stage's "Why this stage exists". -->

<!-- DO: the instruction. Numbered steps only if order matters. Code shown in full for Tier A; shape or constraints only from Tier C. Every code block must run verbatim against MODELS.md pins. No model identifiers; use MODEL from config. -->

<!-- OBSERVE (optional): what to look at while it runs, if not obvious from the Check. -->

**Check**
- **Run:** `<command>` → <exact observable result>.
- **See:** <one question with a checkable answer about what the rung reveals>.
- **Say:** <one sentence the learner should be able to produce without notes, connecting this rung to a later one or to a principle>.
```

## Example (from stage 0)

```markdown
### Rung 4 — The model has no memory

*~10 min · feeds s02-r3 (state), s05 (compaction)*

Nothing persists on the server between calls; every "conversation" is the client re-sending the whole list.

Run the two-call version first, then the version that appends the history. (code)

**Check**
- **Run:** second script prints "Ada" (or equivalent); first does not.
- **See:** how many messages were in `history` on the second call, and who put them there?
- **Say:** in one sentence, why did the first version fail?
```

## Rules of thumb

- One concept per rung. If the *See* question needs "and", split the rung.
- *Run* is binary and local: no judgment, no "it should look reasonable".
- *See* must be answerable from something the learner produced in this rung (output, log line, trace, number). Never from the brief.
- *Say* is the self-explanation; it is the item most likely to fail, and that failure is the most useful signal.
- Time estimates are for the learner in [CONTEXT.md](../CONTEXT.md). Re-estimate from feedback; do not pad.
- "Feeds" is how the cascade check finds dependents. Keep it accurate.
- A rung with no code and no artifact is a paragraph, not a rung. Move it into the previous rung's WHY or the stage intro.
