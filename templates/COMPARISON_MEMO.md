# Comparison memo — <what is being compared> — <date>

> For stage 4 (patterns), stage 6 (frameworks), stage 9 (single vs multi) and any time two designs are weighed. Feeds an ADR; does not replace it.

**Question:** <one sentence: what decision does this memo inform?>
**Answer:** <one sentence: which option, by how much, on what>.

## Setup

- Task and eval set: `<cases.jsonl>` at `<sha>`, n=`<n>`, tags used:
- Providers: `<A>`, `<B>`, local `<C>`
- Runs per case (k):
- Judge (if any) and calibration:
- Held constant across options (tools, prompts where possible, model):
- Varied across options:

## Results

| Option | Pass rate (CI) | pass^k | Cost / task | p50 | p95 | New failure buckets | Removed failure buckets |
|---|---|---|---|---|---|---|---|
| A — | | | | | | | |
| B — | | | | | | | |
| C — | | | | | | | |

Per-provider breakdown (required from stage 4):

| Option | Provider A | Provider B | Local |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |

## Reading the table

Which differences are outside the confidence intervals? Which are not? Say it plainly. A result that looks better but whose CI overlaps the baseline is "not demonstrated", not "slightly better".

## Qualitative

Things the table cannot show: debuggability, operability, security surface, complexity for the next maintainer, lock-in. One paragraph per option, evidence where possible (e.g. "trace for option B spans 3 agents and took me 25 minutes to read vs 4 for option A").

## Recommendation

One option, one sentence, the single decisive reason. Then: what would make this recommendation wrong (a number or an event).

## What this memo did not test

Be explicit. Future you will want to know.
