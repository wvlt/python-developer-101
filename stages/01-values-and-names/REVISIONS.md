# Revisions — Stage 1

Rung-level change log for this stage. Every change to a rung, exercise, hidden case, gate wording, entry condition or contract is recorded here with the feedback that caused it. Stage-level changes are ADRs in `docs/decisions/` and are only referenced here. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Rung-numbered** (2026-11-04, v0.4): ten rungs `s01-r0`–`s01-r9` in six parts, each with a Run/See/Say Check; 29 exercises with 57 visible tests and 63 hidden cases (`eval/threshold.json`: 57 of 63); eight break-lab snippets; reference solutions pass every case in CI. Not yet verified by a learner run.

## Log

- 2026-11-04 · s01-r0–r9 · Stage created (v0.4). Decisions recorded for the next reviser:
  - Exercises are whole programs over `input()`/`print()` (ADR-004). The input-reading lines are *given* above the marker from rung 1, including `int(input())`, before `int()` (r2) and names (r3) are taught; the brief says so and tells the learner to treat each name as the number it holds. Alternative considered: fixed-output exercises for r1 with no input, rejected because hidden cases could not vary.
  - Rung order is numbers → types → names (not numbers → names → types) so that `type()` and `input()`-is-text arrive before the learner writes their first assignment; the given lines make the dependency harmless.
  - `split()` is mentioned at r5 with a one-sentence note that lists are stage 3; no exercise requires it.
  - The receipt (r9) has exactly three items because loops are stage 2; the hidden cases include a zero quantity and a price that rounds. A hidden case whose total depended on float rounding order (0.1 × 10 + 0.005) was removed before publication because two correct programs could differ; replaced with 0.01.
  - Threshold 57/63 (90 %): six hidden failures allowed, which is two to three exercises entirely wrong.
  - Visible test IDs are `rMeK-a`, `-b`; the brief's `-k rMe` filters depend on this shape (a plain `-k r1` also matched ids ending in `1`).
- 2026-11-04 · s01-r5 · Learner read-through (v1.0.0): stage 2 rung 4 assumes `isdigit` and stage 2's Contract lists it under `s01-r5`, but rung 5 never showed it. Two prompt lines and one sentence added; Provides updated. Step change.

## Reference run

Pending: every code block executed on the pins by a maintainer at s01 verification; hidden tests against `solutions/` pass in CI from v0.4. At v1.0.0 the prompt examples in rungs 1–7 (arithmetic, conversions, slicing, methods, f-string specs, truthiness, `is`) were evaluated on CPython 3.13 and all matched the brief; the visible-test counts per rung (`8, 8, 8, 8, 10, 6, 8, 1`) and the first-run `57 failed` were confirmed.
