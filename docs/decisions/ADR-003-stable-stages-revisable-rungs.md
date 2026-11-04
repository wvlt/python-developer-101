# ADR-003 — Stable stages, revisable rungs, explicit contracts

- **Status:** accepted
- **Date:** 2026-11-04
- **Deciders:** curriculum author
- **Amends:** ADR-001 (adds the rung layer and contracts to the ten-stage structure)

## Context

The learner profile is sharp (programming 0/10) and the destination is concrete (junior developer, useful in week one, exit at the 7/10 the sibling courses assume). Two problems follow.

1. **Coverage.** A capability map built against the destination has to show every topic in the owner's ladder — `sorted()`, `lambda`, `zip`, context managers, `pickle`, and about a hundred others — delivered at a named rung and proven at a named gate. A stage-only structure cannot carry that trace.
2. **Revisability.** For an absolute beginner, the places where a brief assumes an unexplained word or an untaught concept are many and are only found by a learner stalling. Each fix is small — a sentence, a definition, a rung inserted — and must land without an ADR, while still being recorded so that later stages that assumed the old wording are checked.

## Options considered

### Option A — Stage-only granularity; revise briefs ad hoc

- Fast now; unrecorded later. A stage-1 fix to how variables are introduced could silently invalidate stage 3's aliasing break-lab. Rejected.

### Option B — Stages + rungs + contracts (chosen)

- Stages keep outcome, gate and position (stable; ADR to change). Each stage gains a **Contract** (Assumes / Provides) naming rung IDs. Rungs get IDs `sNN-rM`; insertions get letter suffixes; they change freely. Each stage directory gets a `REVISIONS.md`. A revision protocol classifies feedback into rung / contract / stage changes and defines the cascade check along contracts. A capability map traces every destination competency and every ladder topic to a rung. Briefs are rung-numbered one stage ahead of the learner.

### Option C — Fully rung-number all ten stages now

- Freezes the rung structure of stages 3–10 before any feedback from 0–2 exists. For a beginner course the feedback from the first three stages is precisely what determines rung size later. Rejected in favour of rolling readiness; outcomes, gates, contracts, break-labs and part-level build sections for 3–10 are fixed now, rungs later.

## Decision

Option B. Implemented in `CONTEXT.md`, `docs/12-capability-map.md`, `docs/13-revision-protocol.md`, `templates/STAGE_FEEDBACK.md`, Contract sections in all eleven briefs, `REVISIONS.md` in all eleven stage directories.

Two rules specific to this course are added to the revision protocol:

- **Vocabulary is a contract item.** A term first used in stage N is listed in the glossary with `[SN]` and counts as *Provided* by that stage. Using a term before its stage is a cascade bug, found by the read-through in the definition of done.
- **Exercises and their tests are rung content.** Adding, removing or reordering an exercise is a rung change; changing what a hidden test asserts is a rung change to the gate's *wording*, and changing the threshold N of M is a stage change.

## Consequences

- Feedback has a landing place below the stage, and a cascade path above it.
- Maintainers must keep contracts honest; a stale *Provides* is a bug with consequences.
- Stages 3–10 will be revised substantially before the learner reaches them; their `REVISIONS.md` says so.
- Revisit when the first learner completes stage 2: compare the rung changes made against the capability map and decide whether the stage boundaries still hold.

## Kill criteria for this decision

If three consecutive feedback rounds each require a *stage* change rather than rung changes, the stage boundaries are wrong and ADR-001 should be reopened.
