# Revisions — Stage 6

Rung-level change log. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Outline** (2026-11-04, v0.4): ten planned rungs `s06-r1`–`s06-r10` in parts A–E with time estimates; Contract, Gate IDs and kill criteria are binding. No Checks, exercises, visible tests, hidden cases, solutions or break-lab files yet. Rung-numbering happens one stage ahead of the first learner, after the previous stage's feedback is in, per [rolling readiness](../../docs/13-revision-protocol.md#rolling-readiness); at that point this file records the rung-numbered status, the actual hidden-case count and the reconciled threshold.

## Log

- 2026-11-04 · s06 · Outline created (v0.4) from the topic ladder and the part plan in [docs/17](../../docs/17-focus-map.md). Open items for the rung-numberer: the mutation check in `just eval 06` (apply a planted bug to a copy of the learner's package and count failing learner tests) is new harness work for `scripts/eval.py`; the HTTP client rung (r6) must run offline in CI via `LIBRARY_OFFLINE=1` and the recorded sample; `pyproject.toml` already carries the two packages as the `s06` extra.
