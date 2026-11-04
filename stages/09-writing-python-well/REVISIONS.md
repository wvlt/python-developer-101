# Revisions — Stage 9

Rung-level change log. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Outline** (2026-11-04, v0.4): eleven planned rungs `s09-r1`–`s09-r11` in parts A–G with time estimates; Contract, Gate IDs and kill criteria are binding. No Checks, exercises, visible tests, hidden cases, solutions or break-lab files yet. Rung-numbering happens one stage ahead of the first learner, after the previous stage's feedback is in, per [rolling readiness](../../docs/13-revision-protocol.md#rolling-readiness); at that point this file records the rung-numbered status, the actual hidden-case count and the reconciled threshold.

## Log

- 2026-11-04 · s09 · Outline created (v0.4) from the topic ladder and the part plan in [docs/17](../../docs/17-focus-map.md). Open items for the rung-numberer: three fixtures to build before rung-numbering: the 200-line script (r8), the stranger's pull-request branch in upstream (r10; capability-map gap 3), and the twelve-bug package (r11) with its answer key kept out of the learner's path; the gate's measure is the bug hunt plus `mypy`/`ruff`/coverage, so `scripts/eval.py` needs a mode that runs the learner's tests against the original and fixed packages; decide whether pre-commit is a rung or stays stretch (capability-map gap 2).
