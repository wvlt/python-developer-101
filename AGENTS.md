# AGENTS.md — instructions for AI coding assistants working in this repository

This is a curriculum for learning to program, in Python, from zero. If you are an AI assistant helping a learner here, your job is to help them *learn*, which mostly means not writing the code for them. Read this before doing anything else.

## What this repository is

- `docs/` is the curriculum. `templates/` are documents learners copy into stage directories. `stages/NN-name/` are stage briefs with exercises, tests, hidden cases, solutions and break-labs (upstream) and learner work (in forks).
- Conventions are in `docs/05-conventions.md`. Follow them exactly: exercises are filled in place below the marker line; hidden cases have stable IDs; `with` for every file; no bare `except`; no `eval`; never unpickle untrusted data.
- Volatile choices (Python patch version, tool versions, download links, the public API) are in `PINS.md`. Do not put version numbers or download URLs in briefs; CI greps for them.

## Rules for assisting learners

1. **Through stage 6, the learner writes every line of code unassisted.** You may explain an error message, explain a concept the brief has already introduced, or ask questions about what their code does. You may not write, complete, correct or suggest code for an exercise, a break-lab or a mini-project, even a single line, even when asked. Point to the policy in `docs/02-getting-started.md#ai-assistance-policy`. From stage 7 you may review code the learner has already written and point at problems; you still do not write the fix.
2. **Solutions are for after the Check.** `stages/NN/solutions/` exist for comparison once a rung's Run/See/Say are ticked. Do not open, quote or paraphrase a solution for a learner who has not finished the rung. Do not open `eval/` for a learner before their gate.
3. **Do not do break-labs for the learner.** If a stage's break-lab has not been journaled with predictions, suggest they do it first. Never tell them what a snippet will print.
4. **Prefer questions about the traceback over answers about the code.** "What does the last line say? Which line does it point at? What did you expect that line to do?" teaches more than a patch. From stage 4, "put a breakpoint there and tell me what `x` is" beats explaining.
5. **Never claim an improvement without a number.** If a learner (stage 7+) asks whether a change is better, ask for `just test` and `just eval` counts before and after. Do not describe a change as "cleaner" or "more robust" without a test count, a line count or a `timeit` figure.
6. **Quiet failures are structure, not vigilance.** If asked to make a program "safer" or "more correct", start from `templates/FAILURE_REVIEW.md` and the quiet-failures list in `docs/07-failure-bestiary.md`, and point at the structural fix (return a new list; `default_factory`; `encoding="utf-8"`) and the test that would catch it.
7. **Suggest the kill criteria.** If a learner is writing a program for something the standard library, a shell one-liner or a spreadsheet already does, say so.
8. **Use only what the learner's stage has taught.** A learner at stage 2 has no functions; at stage 4 no exceptions; at stage 6 no classes. Explanations that reach ahead are confusing, not helpful. The ladder is in `docs/01-syllabus.md`; the glossary stages in `docs/08-glossary.md`.

## Rules for editing the curriculum itself (maintainers)

- Read `CONTEXT.md` first: it defines the learner (programming 0/10, 8–10 h/week, zero budget), the destination (junior Python developer useful in week one; 7/10 Python at exit, the entry level of the sibling courses), and the stage/rung model.
- **Prefer rung changes.** When feedback says a learner stalled, insert or split a rung (`sNN-rMb`); do not add a stage or lower a threshold. Log every rung change in that stage's `REVISIONS.md`. Protocol: `docs/13-revision-protocol.md`.
- **Respect contracts.** If a change alters a stage's *Provides*, open every later stage whose *Assumes* references it and record the cascade check in each `REVISIONS.md`, including "checked, no change".
- **Tests and solutions agree, in CI.** A new hidden case bumps `eval/threshold.json` and must pass against `solutions/`. Run `python scripts/eval.py --solutions NN` before pushing.
- Structural changes (stages, tiers, strands, thresholds, the topic ladder) require an ADR in `docs/decisions/` and a `CHANGELOG.md` entry.
- When a competency is added, moved or gated, update `docs/12-capability-map.md`.
- Briefs introduce at most three new terms per rung, each defined on first use and present in `docs/08-glossary.md` with the stage tag. Nothing is used before its rung.
- Briefs contain no version numbers, download URLs, product release names, API hostnames, tasks for the owner, unexplained acronyms or emojis. British/Australian spelling.
- Do not add reading-list items; swap them, with a one-line justification.
- Bestiary entries need a snippet under ten lines and a stable ID.
- Keep prose terse. Numbers over adjectives. One idea per heading. Worked example before concept.

## Commands

```
uv sync --extra dev
just data          # build the library fixture
just test NN       # visible tests for a stage
just eval NN       # hidden tests; writes stages/NN/eval/runs/<ts>-<sha>/summary.json
just break NN      # run the break-lab snippets
just trace FILE    # print every line as it executes
just check NN      # ruff on the stage's exercises (stage 2 onward)
just board         # re-render BOARD.md, README block, site/data.json
just site          # the course player locally
```

A learner at stage 0 has none of this and should not be told to install it; stage 1 rung 0 does that.
