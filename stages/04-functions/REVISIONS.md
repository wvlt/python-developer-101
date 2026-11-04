# Revisions — Stage 4

Rung-level change log. Protocol: [docs/13-revision-protocol.md](../../docs/13-revision-protocol.md).

## Status

**Outline** (2026-11-04, v0.4): eleven planned rungs `s04-r1`–`s04-r11` in parts A–G with time estimates; Contract, Gate IDs and kill criteria are binding. No Checks, exercises, visible tests, hidden cases, solutions or break-lab files yet. Rung-numbering happens one stage ahead of the first learner, after the previous stage's feedback is in, per [rolling readiness](../../docs/13-revision-protocol.md#rolling-readiness); at that point this file records the rung-numbered status, the actual hidden-case count and the reconciled threshold.

## Log

- 2026-11-04 · s04 · Outline created (v0.4) from the topic ladder and the part plan in [docs/17](../../docs/17-focus-map.md). Open items for the rung-numberer: the exercise shape changes here to function stubs (ADR-004), so `course/runner.py` gains an import-and-call path at rung-numbering; the debugger rung (r10) needs a provided buggy program; the catalogue (r11) depends on s03-r11's question set.
