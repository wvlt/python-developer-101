# 14 — Rubrics

The rubric system at both granularities: stage and rung. Gates say whether you passed; rubrics say what kind of understanding is missing when you did not, and what "strong" looks like when you did.

## Why two instruments

**Stages** have *gates*: binary criteria with numeric thresholds ([06 — Assessment](06-assessment-and-gates.md)). Gates are the right instrument for pass/fail. They are the wrong instrument for feedback: a learner who fails 7 of 60 hidden cases learns which cases, not *what kind of understanding* is missing. Gates also vary in shape stage to stage, so a reviewer cannot compare a stage-2 review with a stage-7 review and a learner cannot see a trajectory.

**Rungs** need a definite completion condition and a definite thing the learner was supposed to notice, or "stalled at r4" is not actionable and the revision protocol has nothing precise to carry.

**Qualitative artefacts** (cards, memos, ADRs, reports, teach-back) need the generic Pass/Revise/Redo rubric in docs/06 specialised per type.

## Principles

1. **The gate is the bar; the rubric is the shape.** Passing is binary. The rubric tells you where you are strong or weak and what strong would look like.
2. **Same dimensions every stage.** Six, fixed, so trajectories are visible across the ladder.
3. **Evidence or it did not happen.** Every rubric cell names the artefact that proves it: a run directory, a journal entry, a file, a sentence the learner says unprompted.
4. **Rungs are checked three ways, always.** Did it run; did you see the thing; can you say why.
5. **Everything addressable.** Rungs `sNN-rM`, checks `sNN-rM.run|see|say`, gate criteria `sNN-gK`, rubric cells `sNN/<dimension>`.

## The rung rubric: Run · See · Say

Every rung ends with a **Check** block containing exactly three items.

- **Run** — a command or action with the expected observable result. "`uv run exercises/r4e1_last_character.py` and type `python`: prints `n`." Binary.
- **See** — the one observation the rung exists to produce, phrased as a question with a checkable answer. "What does `print(items.sort())` print?" If the learner cannot answer, the rung has not done its job regardless of whether the code ran.
- **Say** — one sentence the learner should be able to produce without notes, connecting the rung to something later. "Why will `b = a` not give you a copy?" This is the self-explanation effect made mandatory and cheap, and the source of the gate's Say questions.

A rung is **complete** when all three hold. A rung is **broken** (and goes to `REVISIONS.md`) when learners routinely pass *Run* but fail *See* or *Say*: it produces the artefact without the understanding. A rung is **too small** when nobody ever fails any of the three; merge it. A rung is **too big** when learners stall for more than 30 minutes on *Run*; split it.

Each rung carries a **time estimate** in minutes on its first line, so the feedback table has something to compare against.

Authoring format is in [`templates/RUNG.md`](../templates/RUNG.md). Stage 0 is the worked example: every rung there has a Check.

## The stage rubric: six dimensions, three levels

Applied at every gate review alongside the binary gate. Dimensions are the four strands plus the two things the destination demands that strands do not capture.

| Dimension | What it assesses | Evidence lives in |
|---|---|---|
| **Build** | The program works as specified, follows conventions, and the learner can explain any line | `exercises/`, `src/`, the live explanation at review, the Artefact Card |
| **Measure** | Tests were run, the hidden set was met, the counts are reproducible, and a test drove at least one fix | `eval/runs/*/summary.json`, the card's test section, git history showing a test before a fix |
| **Break** | The learner predicted before running, met the stage's quiet failures deliberately, named them with bestiary IDs, and can predict them in new code | `JOURNAL.md` break-lab entries, planted-bug fixes with tests |
| **Inspect** | The learner looked inside the program with the stage's tool (print → f-string → debugger → logging → timeit) and the looking found something | journal entries naming the variable watched and what it showed; log output; the "how it fails" section of the card |
| **Judgment** | Structure choices are argued; alternatives considered; the kill criterion was answered honestly for this problem | ADRs (from s7), comparison memos, the kill-criteria field of the card |
| **Communication** | A stranger (engineer or not) could understand what was built, how well it works, and what to do next | Artefact Card, README, PR description, commit messages, teach-back |

Three levels per dimension:

- **Not yet** — evidence missing, or present but not connected to the claim. A "Not yet" on Build, Measure or Break blocks the gate regardless of the binary items. A "Not yet" on Inspect, Judgment or Communication blocks from stage 4 onward.
- **Pass** — evidence present, connected, and sufficient for the stage's gate.
- **Strong** — evidence present *and* the learner went beyond: predicted a failure before meeting it, wrote a test the brief did not ask for, found the stdlib function before the brief named it, or explained the thing more clearly than the brief does. "Strong" is recorded, not rewarded with anything but the record; by stage 10 the pattern of Strongs is the portfolio's real signal.

Per-stage anchors (what "Pass" and "Strong" look like concretely) are in each stage's gate section from the point it is rung-numbered; until then the table above plus the gate criteria are the anchors. Anchors for stages 0–2 are below.

### Anchors, stage 0

Stage 0 is ungated; the rubric is applied by the learner to themselves. Build: all eight *Run* checks pass; `hello.py` exists in a folder the learner made and runs from the terminal. Measure: not assessed (tests arrive at stage 1). Break: the three failures in rung 5 seen, and for each the last line of the traceback copied into the journal with one sentence on what it meant. Inspect: two values printed on one line (rung 3) and the difference between `print(2 + 3)` and `print("2 + 3")` stated (rung 4). Judgment: not assessed. Communication: the *Say* for rung 5 ("the last line names the error; the line above names where") stated correctly.

### Anchors, stage 1

- Build — Pass: every exercise r1e1–r9e1 passes its visible tests; the receipt program runs from the terminal on the brief's input and prints the aligned columns. Strong: the receipt handles a quantity of zero without being asked.
- Measure — Pass: ≥ 44/49 hidden; the run directory is cited in the card; the learner can say what one failing visible test told them. Strong: a visible test was read *before* the exercise was attempted and the learner says so.
- Break — Pass: the break-lab's six predictions written before running, with at least two wrong and corrected; `0.1 + 0.2`, `7 // 2`, `"9" > "10"` each named in the journal. Strong: a seventh snippet of the learner's own that surprised them.
- Inspect — Pass: `f"{x=}"` used to find a wrong value in at least one exercise, and the journal says which. Strong: `just trace` used on the receipt and one line of its output quoted in the journal.
- Judgment — Pass: the kill criterion answered for the receipt (a calculator would do for one receipt; the program earns its place at ten). Strong: the learner names the input on which the program is wrong and a spreadsheet is not.
- Communication — Pass: card complete; ≥ 5 commits with messages that say what changed. Strong: a non-programmer read the card's first paragraph and said back what the program does.

### Anchors, stage 2

- Build — Pass: every exercise passes; the text game runs; every `input()` in it is validated in a loop; `ruff check` clean. Strong: the game's state is a small number of named variables and the learner can draw the loop on paper.
- Measure — Pass: ≥ 50/56 hidden; the reviewer's malformed inputs produce a message, not a traceback. Strong: the learner wrote down three inputs they expected to break it *before* the reviewer tried.
- Break — Pass: the always-true `or` (F03) and the off-by-one (F01) each met in the break-lab and named; the planted bug in r11 found and the fix journaled with the line. Strong: the shadowed built-in (F04) found by `ruff` and explained in the learner's words.
- Inspect — Pass: an f-string print placed inside a loop to watch a value change, and the journal says what it showed. Strong: `just trace` output read to find an infinite loop's cause.
- Judgment — Pass: says which of the mini-project's rules could be a table (dict) instead of a chain of `elif`. Strong: did it.
- Communication — Pass: fork on GitHub; ≥ 8 commits; PR description walks the gate. Strong: the README of the game is enough for a stranger to play it without the brief.

## Gate criterion IDs

Every `- [ ]` item in a stage's Gate section carries an ID `sNN-gK`, numbered in order of appearance, stable once published; insertions take a letter suffix like rungs. The universal checklist items are `u1`–`u10` and apply to every stage. Reviews, feedback and `REVISIONS.md` entries reference these IDs.

## Artefact rubrics

The generic three-level rubric in docs/06 (Pass / Revise / Redo) specialised with the questions a reviewer asks per artefact type. Only "Pass" passes.

**Artefact Card** — Every numeric field has a run directory. "How it fails" names bestiary IDs and the input that triggers each. Kill criteria are specific to this problem, not generic. AI-assistance field is credible for the stage's policy.

**ADR** — Options ≥ 2, each with the same fields (lines of code, tests, what breaks if the requirement changes). The decision sentence names the single decisive reason. "Why not the others" cites the table. Consequences include what would make the decision wrong.

**Comparison memo** — Held-constant and varied factors stated. A table with numbers (tests passed, lines, seconds, bytes) per option. Differences that are within noise are called "not demonstrated". A qualitative section with at least one measured observation (minutes to find a bug in each version).

**Error-analysis report** (stage 9) — ≥ 12 planted bugs classified by bestiary ID *before* fixing. Each has a test that fails before and passes after. Time per bug recorded. The slowest bug analysed: what made it slow to find?

**Failure review** — Every function that takes input listed with its reach (what it reads, what it writes). Each quiet-failure row answered: could it happen here, and which test or structure prevents it. Architectural prevention ("the function returns a new list") distinguished from detection ("a test checks"). Residual risk stated.

**Break-my-program report** — Scope agreed. Each finding has the exact input, the observed output, the expected output, loud/quiet. Every finding has a test. Fixes that remove capability or input surface noted as such. Post-session comparison with the failure review filled by the owner.

**Post-mortem** — Blameless. Root cause is a mechanism with a bestiary ID or a candidate entry. "What the tests missed" produced new case IDs. Action items are tests or structure, not resolutions to be careful.

**Code-reading memo** (stage 9) — Names the module's public functions and what each returns. Identifies one place it would break on bad input, with the input. Names one idiom learned from it, with the line. Under one page.

**Teach-back** — A running example. A deliberate mistake made and read aloud. Learner taught from their own earlier failure. Reviewer applies the six-dimension rubric to the *session*, not the slides.

**Portfolio walkthrough** — Reviewer picks the stage. Learner opens the run directory for any number within a minute. One quiet failure narrated without the code. One ADR defended under pushback.

## How a gate review runs (20 minutes)

1. (2 min) Reviewer opens the PR; checks `u1`–`u10` are ticked with pointers.
2. (5 min) Reviewer runs `just eval NN` from a fresh checkout and compares with the card; runs the mini-project on one input from the brief and two of their own, one malformed.
3. (8 min) Reviewer picks one function and asks the learner to explain it line by line; asks the stage's *Say* questions from any three rungs; from stage 4, asks the learner to set a breakpoint and show one variable.
4. (3 min) Reviewer fills the six-dimension rubric with one evidence pointer per cell. Any "Not yet" in a blocking dimension → Revise, with the specific rung or artefact named.
5. (2 min) Verdict, logged in the PR with the [gate review form](../templates/GATE_REVIEW.md). Rubric rows are copied to the learner's `PROGRESS.md` so the trajectory accumulates.

## How rubric data feeds revision

- A rung whose *See* or *Say* fails for ≥ 2 of 3 learners is broken → rung change.
- A dimension that is "Not yet" for most learners at a stage is a brief problem, not a learner problem → look for the missing rung.
- A gate criterion nobody can evidence as written → rewrite the criterion's wording, not its bar.
- "Strong" patterns that recur show where the brief is behind the learners → raise the anchor, or move the content earlier.
