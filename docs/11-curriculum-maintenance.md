# 11 — Curriculum maintenance

Python changes once a year and its tooling changes faster. A beginners' course rots at the installation step first: a download link moves, an installer gains a checkbox, an editor extension changes its welcome screen, and the first rung of stage 0 stops matching the learner's screen. This document is the design that keeps it matching.

## What is stable and what is not

**Stable (change rarely, with an ADR in `docs/decisions/`):**
- The learner profile and destination in `CONTEXT.md`.
- The stage outcomes, gates and contracts; the four tiers and four strands.
- The topic ladder: which concept lands at which stage.
- The gate structure and the universal checklist.
- The pedagogy and its evidence base.
- The conventions.
- The Programmer's Oath.

**Volatile (expected to change every cohort):**
- Rungs inside stages, per [13 — Revision protocol](13-revision-protocol.md); logged per stage in `REVISIONS.md`.
- Pins (`PINS.md`): Python patch version, every tool version, the editor and extension versions, download URLs, the public API endpoint.
- Platform notes in the stage 0 and stage 1 briefs (installer screens, PATH behaviour, `python` vs `python3`).
- Hidden test sets (cases may be added; retired cases keep their IDs).
- Reading-list items (swap, do not grow).
- Time estimates per rung (adjusted from the feedback table).

Briefs reference volatile things indirectly: "the Python installer from the link in PINS.md", "the current version of the editor". If you find a version number, download URL or product release name in a brief, that is a bug and [`scripts/check_pins.py`](../scripts/check_pins.py) should have caught it.

## `PINS.md`

The single place volatile identifiers live. Contains, per item: what it is, the exact version, the live source URL, the date verified, and any caveat (for example: the last Python 3.13 release with a binary installer; macOS installs `python3` not `python`). Also pins the fixture generator's seed and the public API used at stage 6.

A pin change is a PR that includes the Stage 0 reference run on the new pin and `python scripts/eval.py --solutions --all` green. No run, no pin.

## The identifier grep

CI runs `scripts/check_pins.py` on every PR. It fails if any brief, doc (other than this one and PINS.md itself), template, CONTEXT.md, README.md or AGENTS.md contains: a Python patch version; a tool name followed by a version; an extension version; a download or marketplace URL; or the public API's hostname. Allowed in: `PINS.md`, `docs/11-curriculum-maintenance.md`, `data/README.md`, `scripts/`, `.github/`, `.pre-commit-config.yaml`, `pyproject.toml`. If a brief genuinely needs to mention a version — it should not — the sentence goes in PINS.md and the brief links it.

## Reference run

Maintainers keep a record, in each stage's `REVISIONS.md`, of the most recent time every code block in that brief was executed on the current pins: date, platform, pins, outcome per rung, and what was changed as a result. Stage 0 is run on **both** macOS and Windows at every re-pin; it is the brief that touches the operating system most and the one a learner cannot recover from alone.

`solutions/` are the reference implementation for stages 1–9: CI runs the hidden tests against them on every PR, so a test that the solutions do not pass cannot merge, and a change to the harness that breaks a stage is visible immediately.

## Cadence

- **Every cohort start (or quarterly, whichever is sooner):** re-pin everything in PINS.md against live sources; run stage 0 end to end on macOS and Windows on a machine without Python installed; run stage 1 rung 0 (the uv/just/git install) the same way; run `python scripts/eval.py --solutions --all`; update reading-list availability; reread stages 0–2 as a learner against the worked-example rule in docs/03.
- **Every Python minor release (October):** decide whether to move the pin. The course moves to a new minor version when (a) the editor extension and every pinned tool support it, (b) a binary installer exists for macOS and Windows, and (c) the sibling courses have moved or will move in the same quarter. Record the decision in PINS.md's deprecation log. Features introduced by the new version are not added to briefs until the pin moves.
- **Every six months:** review the bestiary against the stage feedback: entries nobody hits any more are marked rare; new quiet failures from break-my-program reports are added with IDs. Review the tooling ramp against what junior developers are actually asked to use.
- **Annually:** review the stage structure against cohort data (below). Changing the structure requires an ADR with that data.

## Cohort data and how it changes the curriculum

Collected per learner per stage, from `PROGRESS.md`, `LEDGER.md`, eval run directories and the gate review forms:

| Signal | Source | Threshold | Change it triggers |
|---|---|---|---|
| Rung minutes vs estimate | PROGRESS.md | median > 1.5× estimate for ≥ 3 learners | Split the rung or fix the estimate (step change) |
| Rung *See* or *Say* failed | PROGRESS.md, gate review | ≥ 2 of 3 learners | Rung is broken: it produces the artefact without the understanding (step change) |
| Hidden case fails for most | eval runs | > 50 % of learners fail one case while passing its siblings | Either the case tests something untaught (fix the brief) or it is miswritten (fix the case) |
| Stage hours vs budget | LEDGER.md | median > 1.3× budget | Look for the rung that absorbs the time; consider moving content later |
| Gate first-attempt pass rate | gate reviews | < 60 % | The gate or the brief; compare against which `sNN-gK` fail |
| Kill criterion answered "always build it" | artefact cards | majority at a stage | The brief is not making the alternative visible; add a worked non-code solution |
| Break-lab prediction accuracy | journals | > 90 % correct before instruction | The break-lab is not surprising anyone; replace the snippet |

## Deprecation procedure

When a pinned thing goes away (an installer is pulled, an extension renamed, the public API changes):

1. Pin the replacement in PINS.md with the date and the reason in the deprecation log.
2. Re-run the affected stage's reference run; record it in `REVISIONS.md`.
3. If a brief's prose depended on the thing (an installer screen, a menu name), that is a step change in the brief, logged in `REVISIONS.md`.
4. If a contract depended on it (rare; a stage *Provides* "can call the public API"), follow the [contract-change procedure](13-revision-protocol.md).

## Ownership

- One maintainer owns PINS.md and the reference runs. Named in the board's maintainer view.
- Each stage has an owner for its `REVISIONS.md` and hidden tests; until there is a team, that is the same person.
- The bestiary accepts entries from anyone with a snippet.
- The learner owns their fork. Upstream never edits a learner's fork; feedback flows through issues and the stage-feedback template.

## Versioning

Curriculum semver: **major** for stage structure or contract renumbering; **minor** for contract changes and new stages' rung-numbering; **patch** for step changes and pin updates. Tags on `main`; `CHANGELOG.md` per version with the stages touched and the `REVISIONS.md` entries that back it.
