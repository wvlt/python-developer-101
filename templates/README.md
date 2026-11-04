# Templates

Copy these into your stage directories. They are deliberately demanding; an empty field is a signal that work remains.

| Template | Copy to | Required in stages |
|---|---|---|
| [ARTIFACT_CARD.md](ARTIFACT_CARD.md) | `stages/NN/ARTIFACT_CARD.md` | 1 onward (the mini-project) |
| [JOURNAL.md](JOURNAL.md) | `stages/NN/JOURNAL.md` | all |
| [ADR.md](ADR.md) | `stages/NN/decisions/ADR-NNN-title.md` | 7 onward, and on any convention deviation |
| [COMPARISON_MEMO.md](COMPARISON_MEMO.md) | `stages/NN/reports/comparison-<date>.md` | 8, 9, 10 |
| [ERROR_ANALYSIS.md](ERROR_ANALYSIS.md) | `stages/NN/reports/error-analysis-<date>.md` | 9 (the planted-bug hunt) |
| [FAILURE_REVIEW.md](FAILURE_REVIEW.md) | `stages/NN/reports/failure-review-<date>.md` | 10; recommended 5 onward |
| [BREAK_MY_PROGRAM.md](BREAK_MY_PROGRAM.md) | `stages/NN/reports/break-my-program-<date>.md` | 10; recommended 5 onward |
| [POSTMORTEM.md](POSTMORTEM.md) | `stages/NN/reports/postmortem-<date>.md` | 10, and after any bug that reached someone |
| [PROJECT_README.md](PROJECT_README.md) | `stages/NN/src/README.md` or the capstone root | 6 onward |
| [PROGRESS.md](PROGRESS.md) | `PROGRESS.md` at fork root | from stage 0; one row per rung |
| [STAGE_FEEDBACK.md](STAGE_FEEDBACK.md) | issue or `feedback/sNN-<date>.md` in your fork | after every stage |

Instruments used by reviewers and authors, not copied into stage directories:

| Template | Used by | When |
|---|---|---|
| [GATE_REVIEW.md](GATE_REVIEW.md) | reviewer, in the gate PR | every gate |
| [RUNG.md](RUNG.md) | authors | when writing or revising a rung |

Conventions for filenames are in [docs/05-conventions.md](../docs/05-conventions.md).
