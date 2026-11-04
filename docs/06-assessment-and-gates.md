# 06 — Assessment and gates

## Philosophy

Assessment here is not grading. It is the same question a colleague will ask on day one: *does it work, how do you know, and what happens on an input you did not think of?* A gate is a set of criteria you can check yourself, that a peer can check in twenty minutes, and that leave no room for "it seems fine."

Three principles:

1. **Criteria, not calendar.** You pass when the criteria are met. Time is advice.
2. **Hidden inputs, not visible ones.** Every gate runs tests whose inputs you have not seen. Passing the visible tests shows you can make a test green; passing the hidden set shows you understood the concept.
3. **Say it without notes.** Every gate asks three Say questions from the stage's rungs. They cannot be looked up in time and they are the part of the gate that a peer, a reviewer or an interviewer will actually ask.

## The eval harness

`just eval NN` runs the hidden test set in `stages/NN-name/eval/` against your `exercises/` (and `src/` from stage 6) and writes `eval/runs/<timestamp>-<sha>/summary.json`:

```json
{
  "stage": "s01", "target": "exercises", "timestamp": "…", "git_sha": "…",
  "n_total": 49, "n_pass": 46, "threshold": {"pass": 44, "total": 49}, "verdict": "pass",
  "per_exercise": {"r1e1": {"pass": 3, "total": 3, "failed": []}, "r4e3": {"pass": 1, "total": 3, "failed": ["s01-r4e3-b", "s01-r4e3-c"]}}
}
```

and prints the same as a table. Run it as often as you like; every run is a directory, and the one you cite in your Artefact Card is the one a reviewer reproduces.

**What "hidden" means.** The tests are in the repository; a public course cannot hide a file. The harness prints case IDs and counts, not assertions, and the convention is that you do not open `eval/` before the gate. The course relies on your interest in your own fluency, and on the Say questions, which cannot be looked up. If you open the hidden tests, the number on your card is not a measurement.

**Thresholds** are "≥ N of M", set so that one exercise can be entirely wrong and the stage still passes, but two cannot. They are in each brief's Gate and in `eval/threshold.json`; changing N or M is a stage change (ADR).

## The universal gate checklist

Every stage from 1, in addition to its specific criteria:

- [ ] **u1** Stage directory follows the [layout](05-conventions.md#stage-directory-layout); no required file missing.
- [ ] **u2** `ARTIFACT_CARD.md` fully filled for the mini-project; no field reads "TBD".
- [ ] **u3** `JOURNAL.md` has a dated break-lab entry with predictions written *before* the snippets were run, and the actual results beside them.
- [ ] **u4** `just test NN` passes and `just eval NN` meets the threshold from a fresh clone; the run directory cited in the card exists.
- [ ] **u5** Every rung's Run, See and Say are ticked in `PROGRESS.md` with minutes.
- [ ] **u6** git history has one commit per rung at least, with messages that say what changed (from stage 1, rung 8).
- [ ] **u7** `ruff check` is clean on `exercises/` and `src/` (from stage 2).
- [ ] **u8** Kill criteria for the stage addressed in the card: "when would you not write this?"
- [ ] **u9** Programmer's Oath item(s) exercised this stage named in the journal.
- [ ] **u10** AI-assistance field in the card is credible for the stage's policy (unassisted through stage 6; review only from stage 7).

## Per-stage gate criteria

Restated from the briefs with the reviewer's check in brackets. The exact IDs (`sNN-gK`) are in each brief.

**Stage 1** — ≥ 44/49 hidden [run `just eval 01`]; three Say questions from r1, r4, r7 [ask]; ≥ 5 commits [`git log --oneline`]; receipt formatter's output aligned to the column widths in the brief [run it].

**Stage 2** — ≥ 50/56 hidden; `ruff check` clean; fork on GitHub with ≥ 8 commits and Pages or `just site` showing `PROGRESS.md`; the game validates every input (reviewer types letters where numbers are expected); three Say questions.

**Stage 3** — ≥ 54/60 hidden on a held-out sample; aliasing Say question answered with a drawing or the sentence "two names, one object"; the catalogue answers the five questions in the brief on the held-out sample [reviewer runs it].

**Stage 4** — ≥ 54/60 hidden; every function has a docstring and type hints [script]; a debugger session journaled naming the variable watched and what it showed; the mutable-default Say question.

**Stage 5** — ≥ 54/60 hidden including the four broken-file cases; the program logs every skipped line with its line number [grep the log]; a long traceback read to its root and journaled; the pickle Say question ("why never unpickle untrusted data?").

**Stage 6** — ≥ 45/50 hidden; ≥ 15 learner-written tests of which ≥ 12 fail under the planted bug [`just eval 06` runs the mutation check]; one standard-library function replacing hand-written code, named in the card.

**Stage 7** — ≥ 45/50 hidden; the dataclass-vs-class Say question with an example of each; `__repr__` on every class is useful in the debugger [reviewer breaks in and looks].

**Stage 8** — ≥ 45/50 hidden; comparison memo on inheritance vs composition with test counts; the iterator-vs-iterable Say question; the context manager cleans up on error [reviewer raises inside the `with`].

**Stage 9** — ≥ 10/12 planted bugs found and fixed with a test each; `mypy --strict` clean; `ruff check` and `ruff format --check` clean; coverage ≥ 90 %; three `timeit` comparisons with before/after numbers; code-reading memo passes the artefact rubric.

**Stage 10** — see [capstone criteria](#capstone-criteria).

## Rubric for qualitative items

For memos, ADRs, reports and the teach-back, reviewers use a three-level rubric. Only the top level passes.

- **Pass:** every claim is supported by a number (tests, seconds, lines, cases) or a runnable example. Alternatives were considered and rejected for stated reasons. A stranger could act on it.
- **Revise:** direction is right; one or more claims unsupported; or alternatives not considered. Return with specific requests.
- **Redo:** adjectives in place of numbers; conclusion not connected to evidence; or the document could have been written without doing the work.

## Capstone criteria

A capstone passes when all of:

1. **Builds and runs.** `uv build` produces a wheel; `uv run library --help` lists the sub-commands; each sub-command has `--help`.
2. **Tested.** `just eval 10` ≥ threshold; the learner's own tests ≥ 40; coverage ≥ 90 %; `mypy --strict` and `ruff` clean.
3. **Persists.** Data round-trips through JSON to the fixture directory; the comparison memo against pickle has a table (size, speed, safety, readability) with numbers for the first two.
4. **Handles the outside world.** Every file read goes through one function that logs and skips bad lines; every user-facing error is a custom exception with a message a non-programmer could act on; no traceback reaches the user on any input the reviewer tries for ten minutes.
5. **Reviewed for quiet failures.** `FAILURE_REVIEW.md` written before building; each listed risk names the test or structure that prevents it.
6. **Broken by a peer.** The break-my-program session ran for ≥ 1 hour and found ≥ 1 finding; every finding has a test that fails on the old code and passes on the fix; the post-mortem is blameless and names mechanisms.
7. **Taught back.** One concept from each tier explained to a non-programmer in five minutes with a running example and a deliberate mistake; reviewer applies the rubric to the session.
8. **Handed off.** The AI Agents 101 Stage 0 brief read; every *Assumes* item in its Contract ticked as "I can do this" with a pointer to the rung here that taught it.
9. **Or:** a post-mortem concluding, with the reasons, that the library would be better served by a spreadsheet, plus the spreadsheet. This passes on equal terms.

## Portfolio

On completing stage 10, the learner's `main` branch is the portfolio: ten stage directories, each with exercises, a mini-project, a journal and a card; a capstone with tests, types and a README; a `PROGRESS.md` with every rung ticked and every stall noted; a `LEDGER.md` with real hours. Reviewers, employers and the learner's future self should be able to open any stage and understand, in twenty minutes, what was built, what it does on bad input, how it was tested and what was learned.

## Badges (optional, for cohorts)

Tie them to tiers, not stages:

- **Tier A — Reads the machine:** writes a program that runs, reads the error when it does not, and knows two names can point at one object.
- **Tier B — Shapes a program:** functions, errors handled, files read without crashing, a package with the learner's own tests.
- **Tier C — Thinks in objects:** classes that behave like Python's own.
- **Tier D — Craft:** typed, tested, measured, reviewed; and says "no program" when that is the answer.
