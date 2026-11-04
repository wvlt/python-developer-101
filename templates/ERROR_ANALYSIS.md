# Error analysis — <artifact> — <date>

> Three-line summary first: what was measured, what was found, what was changed.

**Measured:** `<artifact>` on `<eval set>`, n=`<n>`, baseline pass `<value>` (CI `<range>`), run `evals/runs/<dir>`.
**Found:** `<count>` failures open-coded into `<k>` buckets; largest was `<bucket>` at `<count>` (`<pct>`%).
**Changed:** `<fix>`; pass now `<value>` (CI `<range>`), run `evals/runs/<dir>`.

## 1. Setup

- Artifact and commit:
- Eval set and version (case count, source mix: hand / assisted / production / synthetic):
- Models (agent, judge) and prompt versions:
- Runs per case (k):

## 2. Failure collection

Number of failures collected: `<n>` (minimum 50). Selection method: all failures / random sample of failures / stratified by tag.

## 3. Open coding

One sentence per failure, written *before* any attempt to categorise. Keep the full list in `reports/error-analysis-<date>-codes.jsonl` with fields `case_id`, `run`, `code`. Reproduce the first ten here so a reader can judge the coding quality:

| Case | Code (one sentence, what went wrong) |
|---|---|
| s0N-c012 | Agent called search with the user's full question instead of extracting the entity. |
| | |

## 4. Taxonomy

Clusters derived from the codes. Each bucket gets a short name, a definition, a count, the bestiary ID if one exists, and whether a new bestiary entry is proposed.

| Bucket | Definition | Count | % | Bestiary | Example case |
|---|---|---|---|---|---|
| B1 | | | | | |
| B2 | | | | | |
| B3 | | | | | |
| Other | | | | | |

Buckets become eval tags (`tag:B1-<name>`) so they can be tracked over time.

## 5. The fix

- Target bucket: B`<n>` (the largest, unless there is a stated reason to pick another).
- Hypothesis: why this bucket occurs.
- Change made (prompt version bump / tool change / guardrail / retrieval change / code), with the diff or link:
- Change made to the eval set, if any (new cases added for this bucket; IDs):

## 6. Re-measurement

| | Before | After | Δ |
|---|---|---|---|
| Overall pass rate (CI) | | | |
| Target bucket count | | | |
| Other buckets (any regression?) | | | |
| Cost per task | | | |
| p95 latency | | | |

State plainly whether the CIs overlap. If they do, the improvement is not demonstrated; say so and say what n would be needed.

## 7. Next bucket

Which bucket is now largest, and the hypothesis for it. This is the first line of the next error-analysis report.

## 8. Judge check (if an LLM judge was used)

Did the judge's verdict agree with your own reading on the failures you coded? Disagreements and what they imply for the rubric.
