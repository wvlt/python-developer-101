# 15 — Authoring guide

How to write a brief, a rung, an exercise, a test set and a break-lab for this curriculum so that every stage reads, runs and reviews the same way. Read [CONTEXT.md](../CONTEXT.md) and [03 — Pedagogy](03-pedagogy.md) first; this document turns them into rules.

## Content model

| Unit | Lives in | Purpose | Changes |
|---|---|---|---|
| Stage | `stages/NN-name/README.md` (the brief) | One outcome, one gate, one contract | rarely (ADR) |
| Part | `## Part X — title` heading inside the brief | A run of rungs with one focus; a heading, not an identifier | with rung-numbering |
| Rung | `### Rung N — title` inside the brief | One concept, one working program, one Check | often (`REVISIONS.md`) |
| Exercise | `exercises/rMeK_name.py` + `tests/` + `eval/` + `solutions/` | One task per concept with visible and hidden tests | with the rung |
| Break-lab snippet | `breaklab/NN_name.py` | One misconception, exposed by predict-then-run | with the rung |
| Mini-project | last rung; `exercises/` or `src/` | The stage's concepts in one whole program | with the stage |
| Gate | Gate section of the brief; `eval/threshold.json` | Criteria with `sNN-gK` IDs and numeric thresholds | rarely |
| Template | `templates/` | Documents learners fill in | with docs |

What deliberately does not exist: slides, video, quizzes separate from rung Checks, and solutions hidden from learners. Solutions are in the repo, in `solutions/`, with a rule (open only after the Check) rather than a lock.

## Structure of a brief

Fixed order, fixed headings, so a learner always knows where they are:

1. Title line: `# Stage N — <name>` then the italic meta line (tier, hours, cost: none).
2. **Why this stage exists** — one paragraph. The story, not the syllabus.
3. **Contract** — Assumes / Provides with rung IDs; the rung-ID sentence; links to feedback and revisions.
4. **Entry condition** — what must be true before starting, including `just test NN` red.
5. **Break-lab (first)** — numbered snippets with a prediction line each; ends with "Journal it" and one question.
6. **Build** — rungs, each per [`templates/RUNG.md`](../templates/RUNG.md). Rung 1 is always the smallest working thing. Headings are exactly `## Part X — title` and `### Rung N — title`; the course player and `BOARD.md` are parsed from them, and `*~N min · feeds …*` must be the first line under each rung.
7. **Measure / Break / Inspect** — short sections where they are lenses on the rungs; rungs where they are activities (the debugger rung, the logging rung).
8. **Artefact** — a list of files.
9. **Gate** — `- [ ]` items with `sNN-gK` IDs and numbers; the universal checklist referenced, not repeated; rubric anchors for the stage.
10. **Kill criteria** — when not to write what this stage taught.
11. **Stretch** — optional, never required by a later stage's *Assumes*.
12. **Reading** — pointer into docs/09.

## Voice

- Second person, present tense, imperative for instructions. "Run it. Read the last line."
- Worked example first, every time. Show the code and its output; then name the concept; then the exercise. Never the rule before the instance.
- Nothing before it is introduced. A rung may use only what an earlier rung or an earlier stage's *Provides* taught. If you need a `for` loop in stage 1, you need a different example.
- At most three new terms per rung, each defined in the sentence that first uses it and present in the glossary with that stage's tag.
- Terse. One idea per sentence where possible. Cut every adjective that is not load-bearing.
- Numbers over adjectives. Never "better", "cleaner", "faster" without a figure or a comparison.
- Explain *why* in one sentence at the top of a rung; do not lecture. If the learner needs more, it belongs in the reading list.
- Name failures by their bestiary ID when they are first met; link the entry.
- The computer does not "want", "think" or "get confused". It runs the line. The error message *says*; the traceback *shows*.
- British/Australian spelling. No emojis.

## Writing for the learner in CONTEXT.md

- Assume nothing about programming. Assume everything about using a computer: the learner can open a folder, install an application and follow precise instructions.
- Give both platforms at every terminal step where they differ: the macOS command and the Windows command, in that order, labelled. `python3` on macOS; `python` on Windows; `uv run python` everywhere from stage 1.
- The learner types, never pastes. Say so at every code block over three lines in stages 0–2.
- Respect the time estimate. Eight to ten hours a week means a stage must finish inside roughly twelve hours including the mini-project and the gate.

## Code rules

1. **Runs verbatim.** Every code block in a brief runs as shown on the current `PINS.md` pins. Stage 0 is executed by hand on both platforms at every re-pin; every stage's `solutions/` are run against the hidden tests in CI.
2. **No volatile identifiers.** No version numbers, download URLs, marketplace names or API hostnames in a brief. `scripts/check_pins.py` fails CI if there are.
3. **Short.** A code block longer than ~20 lines in a stage 1–4 brief is a sign the rung is too big. From stage 5, code may be longer where a program is the point; the brief shows the whole file.
4. **Deterministic.** If a *Run* check asserts an exact output, the code must produce it exactly (fixed input, no randomness without a seed).
5. **Idiomatic for the stage.** Code in stage 2 uses no functions; code in stage 4 uses no classes. The brief models the Python the learner can write at that point, not the Python the author would write.
6. **Conventions modelled.** From the rung that introduces them: type hints and docstrings from s04; `with` and `encoding` from s05; tests alongside code from s06.
7. **Comments explain intent, not syntax.**
8. **Plain punctuation inside code.** No em dashes, curly quotes or other non-keyboard characters inside a code block, including in comments: when a learner removes a `#` or a quote on purpose, the error must be about what they removed, not `invalid character '—' (U+2014)`. (Found in the stage 0 reference run.)

## Exercises

- One concept per exercise; four to eight exercises per rung; the title line says the task in one sentence and gives one example input and output.
- Stages 1–3: a whole program reading from `input()` and printing. Inputs above the marker, the learner's code below. Multiple inputs are one per line, in the order the title line lists them.
- Stages 4–6: a function stub with signature, type hints and docstring; the learner fills the body. Tests import the file.
- Stages 7–8: a class stub.
- Stage 9–10: files and packages; tests run the CLI or import the package.
- Every exercise has: a visible test table with 2–4 cases including the example from the title line; a hidden table with 2–4 cases that differ in surface (empty input, boundary value, Unicode, negative number, whitespace) but not in concept; a solution; and, where relevant, the bestiary ID the hidden cases are fishing for.
- The visible and hidden cases for an exercise are written *before* the solution, and the solution must pass both; CI enforces the second half.
- Hidden cases test the rung's concept. A hidden case that needs something from a later rung is a bug.

## Break-labs

- Six to ten snippets, each under twelve lines, each self-contained, each printing one thing.
- Each snippet targets one misconception with a bestiary ID. Snippets are ordered from the most likely to be predicted wrong to the least.
- The learner writes the prediction in the journal before running; the brief says so and provides the table.
- At least one snippet in each break-lab raises on purpose; the prediction for that one is "what will the last line of the traceback say?"
- From stage 2, one break-lab item is a planted bug: a short program that runs and is wrong, with the question "which input shows it?"

## Rung checks

- *Run* names a command and an exact observable. Prefer `uv run ...` (stage 1 onward) or `python3`/`python` (stage 0) and a printed line or a file appearing.
- *See* is a question about the learner's own output, with an answer a reviewer can check in seconds.
- *Say* is a one-sentence explanation request. Good *Say* prompts start with "why" or "what would happen if".
- Time estimate in minutes, for the CONTEXT.md learner, typing not pasting, including the exercises.
- "Feeds" lists the rungs or gate items that depend on this one.

## Fixtures and data

- Live in `data/` at the repo root with a `README.md` giving provenance, licence, size and the one-command rebuild.
- Generated, not committed: `data/build_files.py` with a fixed seed writes `data/library/`; CI checks two builds are byte-identical.
- The library world has three clean files (CSV, JSON, messy text) and four broken files (bad encoding, missing column, duplicate IDs, bad dates). Every stage from 3 uses it; stages 3 and 4 as Python literals embedded in the exercise, stage 5 onward as files.
- `reference.json` holds the answers to the questions the briefs ask (how many overdue; most-borrowed author), so a test can check a learner's answer without the author recomputing it.
- The one public API (named in PINS.md) needs no key; `openlibrary_sample.json` is a recorded response so the stage 6 tests run offline.

## Terminology

The glossary (docs/08) is the authority. Specific choices to hold to:

- *program*, not *script* or *app*, until stage 6 where *package* and *module* arrive; *CLI* from stage 5.
- *name*, not *variable*, when the point is binding ("the name `a` refers to the list"); *variable* is fine in ordinary use.
- *traceback*, not *stack trace* or *error dump*.
- *exception* for the object; *error* for the human experience; *raise*, not *throw*.
- *parameter* in the `def`, *argument* in the call.
- *method* for a function on an object; *attribute* for anything reached with a dot.
- *test* and *case*; *visible* and *hidden*; *threshold*.
- *Inspect* for the strand; *debugger* for the tool.

## Definition of done for a rung-numbered brief

Before a stage is marked rung-numbered in its `REVISIONS.md`:

- [ ] Every rung has Why (one sentence), Do, Check (Run/See/Say), time, feeds.
- [ ] Rung 1 is the smallest working thing; rungs are in dependency order; no rung's *See* needs "and".
- [ ] Every exercise has visible tests, hidden cases with stable IDs, and a solution; `python scripts/eval.py --solutions NN` is green.
- [ ] `eval/threshold.json` matches the Gate and docs/01.
- [ ] Break-lab snippets exist in `breaklab/` and each names a bestiary ID.
- [ ] Contract *Assumes* matches the previous stage's *Provides* item for item; *Provides* lists only things later stages actually assume.
- [ ] Gate items have `sNN-gK` IDs and each names its evidence.
- [ ] Rubric anchors for the stage written (Pass and Strong per dimension).
- [ ] No term used before its glossary stage; ≤ 3 new terms per rung; all in the glossary.
- [ ] `scripts/check_pins.py` passes.
- [ ] Bestiary IDs and reading-list anchors resolve.
- [ ] `PROGRESS.md` rows for this stage's rungs generated (`just progress`).
- [ ] Time estimates sum to within ±20 % of the stage budget in docs/01, or the budget is updated.
- [ ] Read once end to end as the CONTEXT.md learner: nothing assumed that an earlier rung did not provide; nothing explained that the learner already knows.

## Maintaining consistency across authors

- One author writes a stage end to end; a second reads it as the learner and files a `STAGE_FEEDBACK.md` before it ships. Solo: write, sleep, read as the learner.
- Any new term, convention or file type introduced in a brief is added to docs/05 or docs/08 in the same PR.
- Do not fork style within a stage. If a later stage needs a different structure, change this guide first.
