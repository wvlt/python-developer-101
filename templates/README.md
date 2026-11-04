# Templates

Copy these into your stage directories. They are deliberately demanding; an empty field is a signal that work remains.

| Template | Copy to | Required in stages |
|---|---|---|
| [ARTIFACT_CARD.md](ARTIFACT_CARD.md) | `stages/NN/ARTIFACT_CARD.md` | all |
| [JOURNAL.md](JOURNAL.md) | `stages/NN/JOURNAL.md` | all |
| [ADR.md](ADR.md) | `stages/NN/decisions/ADR-NNN-title.md` | 4 onward, and on any convention deviation |
| [ERROR_ANALYSIS.md](ERROR_ANALYSIS.md) | `stages/NN/reports/error-analysis-<date>.md` | 3 onward |
| [COMPARISON_MEMO.md](COMPARISON_MEMO.md) | `stages/NN/reports/comparison-<date>.md` | 4, 6, 9 |
| [THREAT_MODEL.md](THREAT_MODEL.md) | `stages/NN/reports/threat-model-<date>.md` | 7 onward |
| [RED_TEAM_REPORT.md](RED_TEAM_REPORT.md) | `stages/07/reports/red-team-<date>.md` | 7 |
| [RUNBOOK.md](RUNBOOK.md) | `stages/NN/RUNBOOK.md` | 8 onward |
| [POSTMORTEM.md](POSTMORTEM.md) | `stages/NN/reports/postmortem-<date>.md` | 8 (chaos), 10, any incident |
| [PROGRESS.md](PROGRESS.md) | `PROGRESS.md` at fork root | from stage 0; one row per rung |
| [STAGE_FEEDBACK.md](STAGE_FEEDBACK.md) | issue or `feedback/sNN-<date>.md` in your fork | after every stage |

Instruments used by reviewers and authors, not copied into stage directories:

| Template | Used by | When |
|---|---|---|
| [GATE_REVIEW.md](GATE_REVIEW.md) | reviewer, in the gate PR | every gate |
| [RUNG.md](RUNG.md) | authors | when writing or revising a rung |

Conventions for filenames are in [docs/05-conventions.md](../docs/05-conventions.md).
