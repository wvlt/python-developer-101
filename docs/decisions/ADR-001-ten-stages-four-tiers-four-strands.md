# ADR-001 — Ten gated stages in four tiers, four strands, with Observe renamed Inspect

- **Status:** accepted
- **Date:** 2026-11-04
- **Deciders:** curriculum author (sole maintainer)

## Context

The curriculum must take a person who has never written a line of code to a junior Python developer who is useful in week one on a tier-1 team: fluent, tested, tool-literate, able to read tracebacks and other people's code, and able to say when not to write code. The structural question is the number and grouping of instructional units, and how the cross-cutting habits (testing, debugging, reading failures) are placed.

Constraints: ~15 weeks at 8–10 h/week (about 140 h); zero cost; must work for a solo learner and a cohort; the exit level must match the entry level the sibling courses assume. The sibling course [AI Agents 101](https://github.com/wvlt/ai-agents-101) fixes the shape (tiers, stages, strands, rungs, contracts, board) so that the three courses are one product; deviating is possible but must be argued.

The owner supplied a topic ladder of eleven stages (0–10). The question this ADR answers is whether that count and grouping is right for *this* learner, and whether the four strands carry over unchanged.

## Options considered

### Option A — Five stages (one per syntax family: values, control flow, collections, functions, objects)

- Description: fewer, bigger stages of ~28 h each, gates three to four weeks apart.
- Evidence: Bloom's mastery learning and Ericsson's deliberate practice both depend on short feedback loops; a beginner's misconception about `=` or about aliasing compounds for three weeks before a gate catches it. Cognitive-load research argues for small, worked steps for novices; 28-hour stages invite the "big project" brief that a novice cannot start.
- Consequence: fewer gates, slower correction of misconceptions, weaker portfolio granularity.

### Option B — Ten gated stages plus an ungated two-hour stage 0, in four tiers, four strands (chosen)

- Description: each stage = one working program with tests + one gate, ~12–14 h, about 1.5 weeks. Tiers group stages into a narrative the learner can hold: **A — Talking to the machine** (the computer does exactly what you said; s00–s03), **B — Structure** (functions, errors and files, modules and tests; s04–s06), **C — Objects** (s07–s08), **D — Craft** (s09–s10). Strands spiral through every stage so testing, debugging and reading failures are habits, not late modules.
- Evidence: Bloom (frequent gates); Ericsson (short feedback); Cowan (~4 chunks → four tiers, four strands); Bruner (spiral); Kapur (productive failure before instruction); Sweller (worked examples for novices). Detail in docs/03.
- Consequence: ten portfolio programs; a mini-project per stage; tests from stage 1; the break-lab in every stage.

### Option C — Twenty stages (one per topic: strings, lists, dicts, sets, comprehensions, …)

- Description: topic granularity, ~7 h each.
- Evidence: a 7-hour stage is too small to carry a program that combines concepts, and combination is where beginners fail; twenty gates is review overhead without feedback benefit; the learner loses the thread. Topic granularity is preserved *inside* stages as rungs, which is where it belongs.
- Consequence: a syllabus, not a ladder.

### On the owner's ladder specifically

The eleven-stage topic ladder was checked against three tests: (1) does each stage end in a program that combines its concepts? (2) does each stage's *Assumes* follow from the previous *Provides* without a gap? (3) is any stage over 16 h for this learner? All three pass. Stage 5 (errors, files, pickle, datetime, argparse, logging) is the widest; it stays one stage because every item is "the outside world touching your program", and splitting it would separate exceptions from the file I/O that produces them. Its budget is 14 h. Stage 10 is 20 h because the capstone, post-mortem, peer session and teach-back are four artefacts.

## Decision

Option B, on the owner's ladder, with two adaptations:

1. **The Observe strand is renamed Inspect.** In the agents course "observe" meant watching a remote system through traces. Here the learner looks *inside their own running program* — the REPL, `print`, f-string debugging, the debugger's inspect pane, `logging`, `timeit`, the profiler. "Inspect" is the verb the debugger uses and the verb a reviewer uses; "observe" suggests watching from outside. The habit sentence becomes *never ship a program you cannot see inside*. The stage rubric dimension is renamed accordingly.
2. **Measure means tests, written by the course until stage 6.** A beginner cannot write a test at stage 1 but can run one and watch it go from red to green. The eval harness (`just eval`) runs a hidden set against the learner's solutions and writes a run directory with pass counts per exercise; gate thresholds are "≥ N of M hidden tests". From stage 6 the learner writes tests, and from stage 9 measures coverage. Detail in [ADR-004](ADR-004-exercises-as-programs-tests-by-the-course.md).

## Why not the others

A: gates too sparse for a learner whose misconceptions form in the first hour. C: topics are not capabilities; a stage must end in a program that combines them.

## Consequences

- Easier: portfolio clarity; a mini-project per stage; one place (stage 3, collections) where the aliasing lesson lands before functions complicate it.
- Harder: ten gates and ~100 exercises per tier is real authoring load; mitigated by rolling readiness (rung-number one stage ahead) and by data-driven tests.
- Revisit if: a stage exceeds its budget by > 50% for two learners (split it), or a first-attempt pass rate > 95% (merge or advance it). See docs/11.

## Kill criteria for this decision

If learners cannot say which tier they are in and why, the tier framing has failed and the structure should be rethought rather than relabelled.
