# Revisions — Stage 5

Rung-level change log. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Outline** (2026-11-04, v0.4): eleven planned rungs `s05-r1`–`s05-r11` in parts A–E with time estimates; Contract, Gate IDs and kill criteria are binding. No Checks, exercises, visible tests, hidden cases, solutions or break-lab files yet. Rung-numbering happens one stage ahead of the first learner, after the previous stage's feedback is in, per [rolling readiness](../../docs/13-revision-protocol.md#rolling-readiness); at that point this file records the rung-numbered status, the actual hidden-case count and the reconciled threshold.

## Log

- 2026-11-04 · s05 · Outline created (v0.4) from the topic ladder and the part plan in [docs/17](../../docs/17-focus-map.md). Open items for the rung-numberer: tests use `tmp_path` copies of `data/library/` including `broken/`; the pickle demonstration (r7) must be a file that opens a harmless program (the calculator) and be shown, not run blind; a hidden case should expect `ValueError` from `zip(strict=True)` (gap noted in s02 REVISIONS); an environment-variable hidden case closes capability-map gap 1.
