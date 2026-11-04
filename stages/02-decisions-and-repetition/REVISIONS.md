# Revisions — Stage 2

Rung-level change log for this stage. Every change to a rung, exercise, hidden case, gate wording, entry condition or contract is recorded here with the feedback that caused it. Stage-level changes are ADRs in `docs/decisions/` and are only referenced here. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Rung-numbered** (2026-11-04, v0.4): eleven rungs `s02-r1`–`s02-r11` in three parts, each with a Run/See/Say Check; 26 exercises (one a planted bug, `r9b1`) with 54 visible tests and 62 hidden cases (`eval/threshold.json`: 56 of 62); nine break-lab snippets; reference solutions pass every case in CI. Not yet verified by a learner run.

## Log

- 2026-11-04 · s02-r1–r11 · Stage created (v0.4). Decisions recorded for the next reviser:
  - Rungs 7 (`enumerate`/`zip`) and 9 (planted bug) need a sequence of inputs of varying length; the given lines build it with a list comprehension (`[input() for _ in range(n)]`) and say that lists are stage 3. Alternative considered: `enumerate` over a string only, rejected because hidden cases could not vary meaningfully. If feedback shows the given line confuses, the fallback is to move r7 to the start of stage 3.
  - The planted bug `r9b1` carries two faults on purpose: a shadowed `max` (loud to `ruff`, A001) and a running best started at 0 (quiet; caught only by the all-negative test). The brief uses the pair to say what a linter can and cannot see. `ruff`'s `A` rule set was enabled in `pyproject.toml` for this.
  - Break-lab 09 (the infinite loop) exits before the loop so that `just break 02` cannot hang; the learner reads it instead of running it.
  - The game (r11) takes the secret as its first input so tests can play it; the stretch adds `random`.
  - Threshold 56/62 (90 %).
  - `zip(strict=True)` is taught as the default; a hidden case for r7e2 has equal lengths only, because unequal lengths with `strict=True` raise and the exercise shape (stdout comparison) cannot express "raises" until stage 5. Noted as a gap for the s05 reviser: add a case there that expects the `ValueError`.

## Reference run

Pending: every code block executed on the pins by a maintainer at s02 verification; hidden tests against `solutions/` pass in CI from v0.4.
