# Artifact Card — Stage NN: <name>

> One page. Every field filled. "TBD" is a gate failure. Numbers carry n and, where applicable, a 95% CI.

## Identity

- **Stage:** NN — <name>
- **Author:**
- **Curriculum version:** (git tag of upstream you started on)
- **Date passed gate:**
- **Commit:** (SHA on `main` after merge)

## What it does

Two sentences, for a stranger. What goes in, what comes out, what it is for.

## How well it works

| Metric | Value | n | CI (95%) | Run |
|---|---|---|---|---|
| Primary eval pass rate | | | | `evals/runs/<dir>` |
| pass^5 (if applicable) | | | | |
| Per-provider: <provider A> | | | | |
| Per-provider: <provider B> | | | | |
| Per-provider: local | | | | |
| Stage-specific metric (e.g. recall@5, attack success rate) | | | | |

Judge model (if any): `<provider/model>`, calibration agreement: `<value>` on `<n>` cases.

## What it costs

- Cost per task (mean / p95): USD
- Tokens per task (mean / p95):
- Latency per task (p50 / p95):
- Total spend this stage: USD (from `LEDGER.md`)

## How it fails

Top three failure buckets from error analysis, with counts and the bestiary ID:

1. `<bucket>` — n=<count> — bestiary <ID> — status: fixed / mitigated / open
2.
3.

Exemplar traces: `traces/examples/success.jsonl`, `recovered.jsonl`, `unrecovered.jsonl`.

## What was decided

Links to ADRs in `decisions/`, one line each:

- ADR-001 — <title> — <decision in ten words>

## Guardrails in place

List each mechanism, what it prevents, and where it is in the trace:

- `<mechanism>` — prevents `<failure>` — trace event `<kind>`

## Context budget (stage 5 onward)

| Component | Tokens (max) | Priority when trimming |
|---|---|---|
| System prompt | | |
| History | | |
| Retrieved | | |
| Tool results | | |
| Reserve for output | | |

## Kill criteria

When would you *not* use this artifact or technique? Be specific to this problem.

## AI assistance

What was AI-assisted, with what, and what you did to verify it. Which parts were written unassisted (stage 2 loop is required to be).

## Models and versions

| Role | Provider / model | Pinned in `MODELS.md`? |
|---|---|---|
| Agent | | |
| Judge | | |
| Embeddings (S5+) | | |
| Local | | |

## What I would do with one more week

Three bullets, in priority order, each tied to a failure bucket or a metric.
