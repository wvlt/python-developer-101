# 13 — Revision protocol

How feedback becomes change, at the right granularity, with the cascade checked. Read [CONTEXT.md](../CONTEXT.md) first; this is the procedure that implements its "stages are stable, rungs are not" model.

## Vocabulary

- **Stage** — outcome + gate + contract. Numbered 0–10. Stable.
- **Rung** — one unit of instruction inside a stage. ID `sNN-rM`; insertions take a letter suffix (`s02-r4b`) so existing references stay valid. Renumbering happens only at a major curriculum version.
- **Exercise / case** — a rung has exercises (`rMeK`), each with visible tests and hidden cases (`sNN-rMeK-x`). Case IDs are stable; a retired case stays in the table marked retired.
- **Contract** — a stage's *Assumes* and *Provides* lists, in its brief. The dependency graph of the curriculum.
- **Cascade check** — when a stage's *Provides* changes, walking every later stage whose *Assumes* references the changed item and revising as needed.

## Three kinds of change

### 1. Rung change

The rung is unclear, too big, too small, assumes something not yet taught, teaches something already known, has a wrong time estimate, uses a term before its glossary stage, or is missing entirely. An exercise is ambiguous or a hidden case tests something the rung did not teach. The stage's outcome, gate threshold and *Provides* are unchanged.

**Procedure:** edit the brief, exercise or test; log in the stage's `REVISIONS.md` (date, rung or case ID, what changed, the feedback item that caused it); if a hidden case was added, bump `total` in `eval/threshold.json` and `pass` by the same amount; run `python scripts/eval.py --solutions NN`; done. No ADR, no cascade check beyond confirming *Provides* is unchanged. Patch version.

Most feedback is this kind. It should be fast: under an hour from feedback to merged change.

### 2. Contract change

A rung change that alters what the stage *Provides* (stage 2 now also teaches `zip(strict=True)`; stage 5's mini-project now logs to a file rather than stderr; stage 4 moves the debugger rung to stage 3). The stage's outcome and gate are the same, but a later stage's *Assumes* may now be wrong, or a later rung may now be redundant.

**Procedure:** make the rung change; update *Provides*; run the cascade check: for each later stage, grep its *Assumes* and its rungs for the changed item; revise or add a note; log in the originating stage's `REVISIONS.md` *and* in each downstream stage touched; update [docs/12](12-capability-map.md) if a competency moved. Minor version.

### 3. Stage change

A new stage, a removed stage, a changed outcome, a changed gate threshold, a change to the topic ladder (moving `sorted()` from stage 3 to stage 2), a changed tier or strand. Rare by design.

**Procedure:** ADR in `docs/decisions/` with the cohort data that justifies it (docs/11 table); update the syllabus, the capability map, the focus map, the board, and every brief touched; `CHANGELOG.md` entry. Major version if stages are renumbered; minor otherwise.

## Classifying feedback

| Feedback says | Kind | First response |
|---|---|---|
| "I did not understand rung 4" | rung | Ask what they expected; look for the term or concept introduced before its rung; add a worked example, not a paragraph |
| "Rung 4 assumed I knew X" | rung, or contract if X is a *Provides* of an earlier stage that does not deliver it | Check the earlier stage's rungs; if X is missing there, that is the change, not a definition here |
| "I already knew rung 4" | usually nothing; rung if ≥ 2 of 3 learners | Mark the rung as skippable with its Check still required |
| "Exercise r4e2 was ambiguous" | rung | Rewrite the task line and the example; add the ambiguous input as a visible test |
| "Hidden case s03-r4e2-c failed and I do not see why" | rung | Check whether the case tests the rung's concept or a neighbour's; move or retire the case |
| "Took 2× the estimate" | rung | Re-estimate first; split only if the feedback also shows a stall at a particular Check |
| "I could not read the error at rung 5" | rung | Add the error's bestiary entry to the rung's text; if the entry does not exist, add it |
| "Gate criterion could not be checked as written" | rung (wording) | Rewrite the criterion to name the artefact that proves it; the bar does not change |
| "I passed the hidden tests and still could not do the mini-project" | contract | The hidden cases are too close to the visible ones; add cases with different surface, same concept |
| "The installer screen looked different" | rung + pin | Update PINS.md and the platform note; reference run |
| "Wanted to know why" | rung | One sentence of motivation at the top of the rung; not a lecture |

## Rolling readiness

Briefs are rung-numbered one stage ahead of the cohort. Before the cohort reaches stage N:

1. Read stage N−1's `REVISIONS.md` and the feedback that produced it.
2. Rewrite stage N's build section as numbered rungs, each one concept and one working program, applying what N−1 taught about this cohort. Follow the part plan in [docs/17](17-focus-map.md) unless the feedback says otherwise.
3. Write the exercises, visible tests, hidden cases, solutions and break-lab; run `python scripts/eval.py --solutions NN`; set `threshold.json`; reconcile the threshold in the brief's Gate and in docs/01.
4. Confirm stage N's *Assumes* matches stage N−1's *Provides* exactly. Where it does not, that is a cascade item.
5. Replace part references with rung IDs in docs/12.
6. Run the reference run; record it in `REVISIONS.md`; mark the stage rung-numbered, then verified, on the board.

## Who may change what

- Anyone may propose any change by feedback or PR.
- Rung changes: one maintainer merges.
- Contract changes: one maintainer merges after the cascade check is recorded.
- Stage changes: ADR approved by two maintainers.

For a solo author, the roles collapse but the records do not: the `REVISIONS.md` entries, the cascade notes and the ADRs are what make the next revision safe.

## What to resist

- Adding a stage because a topic feels important. Find its rung.
- Lowering a threshold because learners struggle. Add rungs until they clear it; if the threshold is truly wrong, that is an ADR with the eval data.
- Defining a term early "so it is there when needed". It is noise until needed; the glossary stage is a rule.
- Rewriting a brief wholesale after one learner's feedback. Change the rungs the feedback touched; leave the rest for the next learner to confirm.
- Adding a hidden case that tests cleverness rather than the rung's concept.
- Letting `REVISIONS.md` go stale. A change with no log entry did not happen.
