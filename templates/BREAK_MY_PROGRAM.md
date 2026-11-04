# Break my program — <program> — <date>

> One peer tries, for an hour, to make another's program fail — loud or quiet — using only the README and the command line. Protocol in [docs/10](../docs/10-instructor-guide.md#break-my-program-protocol). Required at stage 10; recommended at every mini-project from stage 5. Solo learners do it themselves the next day on a fresh clone.

## Scope (agreed before starting)

- **Owner:** · **Breaker:** · **Date:** · **Duration:** `<minutes>`
- **Program and commit:**
- **What the breaker may read:** README, `--help` output, the fixture files. Not the source, not the tests, not `FAILURE_REVIEW.md`.
- **In scope:** any input through the program's documented interface (arguments, files it reads, `input()`, environment variables).
- **Out of scope:** editing the source; deleting files the program did not create.

## Breaker's plan (written before running anything)

Five inputs I expect to break it, and why, from the [quiet failures list](../docs/07-failure-bestiary.md#q--the-quiet-failures-the-risk-model) and the [standard inputs](FAILURE_REVIEW.md).

| # | Input | Expected failure | Bestiary guess |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Findings

One row per unexpected behaviour. Quiet findings (wrong output, no error) count double. "Expected" is what a reasonable user would want.

| # | Exact input / command | Observed | Expected | Loud / quiet | Bestiary | Severity (wrong answer / crash / data loss / annoyance) |
|---|---|---|---|---|---|---|
| F1 | | | | | | |
| F2 | | | | | | |

Attempts that did **not** break it (so the owner knows what is already covered):

- 

## Owner's response (before the next session)

For every finding: a test that fails on the commit above and passes after the fix; the fix; or a reasoned disagreement.

| Finding | Test (file and name) | Fix (commit) | Or: why this is not a bug |
|---|---|---|---|
| F1 | | | |
| F2 | | | |

Fixes that removed an input surface rather than handling it (for example: the program no longer accepts a path to a pickle file) are noted as such; removing is often the stronger fix.

## Comparison with the failure review

| | Count | Findings |
|---|---|---|
| Anticipated in `FAILURE_REVIEW.md` and prevented (breaker failed to break it) | | |
| Anticipated and not prevented | | |
| Not anticipated | | |

The third row is the lesson. Each entry becomes a row in the failure review, a test, and — if it fits no bestiary entry — a proposed entry with a snippet.

## Post-mortem

Required at stage 10, in [`POSTMORTEM.md`](POSTMORTEM.md). Link it here.

## Swap

Date and link of the session where roles were reversed.
