# ADR-004 — Exercises are small programs that read input and print; tests are written by the course until stage 6

- **Status:** accepted
- **Date:** 2026-11-04
- **Deciders:** curriculum author
- **Amends:** ADR-001 (fixes how the Measure strand works for a learner who cannot yet write a function)

## Context

The Measure strand means tests. Every rung from stage 1 carries four to eight micro-exercises with tests the learner runs; every gate runs a hidden set. But functions are stage 4 and classes are stage 7. In stages 1–3 the learner knows only: a file, `print`, `input`, variables, expressions, and (from stage 2) `if` and loops. The exercise and test format must work with exactly that vocabulary and no more — "no concept appears in code before it is introduced" applies to exercise stubs and visible tests as much as to worked examples.

A second constraint: hidden tests must be able to run the learner's solution on inputs the visible tests did not show, or they measure nothing the visible tests did not.

## Options considered

### Option A — Fill-in-the-function from stage 1

- Each exercise is a `def` stub; tests import and call it.
- Requires `def`, parameters and `return` in stage 1, three stages before functions are taught. Rejected on the no-concept-before-its-rung rule.

### Option B — Exercises are whole programs that read `input()` and `print()`; tests run them as subprocesses with chosen stdin (chosen, stages 1–3)

- Each exercise is a file `exercises/rMeK_name.py` with a two-line header saying what it must do, the `input()` lines already written, and a marker *your code below this line*. The learner runs it by hand (`uv run exercises/r4e3_last_character.py`, types a word, sees the answer) exactly as they ran `hello.py` in stage 0. Tests feed stdin and compare stdout. Hidden tests feed different stdin.
- Uses only stage-0 vocabulary. The exercise *is* a program, which is the course's definition of the core object. Hidden inputs are natural. Planted-bug exercises are the same shape with a bug already in the file.
- Cost: a subprocess per test case (~50 ms each); a stage's hidden set of ~60 cases runs in a few seconds.

### Option C — Exercises assign named variables; tests import the module and inspect them

- Avoids subprocesses, but hidden tests cannot vary the input without the learner knowing about module globals and injection, and output-by-print — the thing stage 0 taught — is not what is checked. Rejected.

### Option D — Learner writes their own tests from stage 1

- Writing a test needs `def`, `assert` and an import; and a beginner who writes the test and the solution tests their misconception twice. Rejected until the learner has functions (stage 4) and has read tests for five stages; they write their first at stage 6 and are measured on coverage at stage 9.

## Decision

Option B for stages 1–3. From stage 4, exercises become fill-in-the-function (stubs with a docstring and `...`), and tests import them; from stage 7, fill-in-the-class. Tests are written by the course through stage 5; the learner writes their own from stage 6 (rung in the brief), alongside the course's hidden set which continues to gate every stage.

Mechanics, fixed in docs/05 and docs/15:

- `stages/NN-name/exercises/` — the stubs; the learner edits them in place in their fork.
- `stages/NN-name/tests/` — visible tests, run by `just test NN`; data-driven tables of `(exercise, stdin, expected stdout)`.
- `stages/NN-name/eval/` — hidden tests, run by `just eval NN`, which writes `eval/runs/<timestamp>-<sha>/summary.json` with pass counts per exercise and the IDs of failing cases, and prints a table. Case IDs are `sNN-rMeK-x` and are stable.
- `stages/NN-name/solutions/` — reference solutions. The learner opens one only after the rung's Check, and `AGENTS.md` forbids an assistant from reading them aloud.
- `stages/NN-name/breaklab/` — the predict-then-run snippets, run by `just break NN`.
- "Hidden" means the harness reports IDs and counts, not assertions, and the convention that the learner does not open `eval/` before the gate. The files are in a public repository; the course relies on the learner's interest in their own fluency, says so plainly in docs/06, and asks the Say questions at the gate, which cannot be looked up.

## Consequences

- Stage 1–3 tests are honest to what the learner knows, and the first time the learner sees `def` is in a worked example, not a test file.
- The subprocess runner is one small shared module (`course/runner.py`) plus a root `conftest.py`; a beginner never reads it.
- Hidden sets must be authored with inputs that differ from the visible ones in kind (empty input, negative numbers, unicode, trailing spaces) or they add nothing; the authoring guide lists the required variations.
- Revisit at stage 4 readiness: if feedback shows learners confused by the switch from programs to functions-under-test, add a bridging rung (`s04-r1b`) that tests one function both ways.

## Kill criteria for this decision

If learners routinely pass the visible tests and fail the hidden set by more than 30%, the visible tests are teaching the test rather than the concept, and the format — not the threshold — must change.
