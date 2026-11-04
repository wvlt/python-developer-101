# Comparison memo — <what is being compared> — <date>

> For stage 8 (inheritance vs composition), stage 9 (loop vs comprehension vs generator; list vs set vs dict), stage 10 (JSON vs pickle) and any time two designs are weighed. Feeds an ADR; does not replace it.

**Question:** <one sentence: what decision does this memo inform?>
**Answer:** <one sentence: which option, by how much, on what>.

## Setup

- Task: <what the code must do, in one sentence>
- Test set: `tests/<file>` at `<sha>`, n=`<n>` cases
- Input sizes measured: `<e.g. 400 loans; 40 000 loans>`
- Machine: <laptop model or "the course machine">; Python per `PINS.md`
- Held constant across options (tests, inputs, data):
- Varied across options:

## Results

| Option | Tests passing | Lines (no tests) | Time, n=`<small>` | Time, n=`<large>` | Peak memory (if measured) | Bestiary risks |
|---|---|---|---|---|---|---|
| A — | | | | | | |
| B — | | | | | | |
| C — | | | | | | |

Timing method: `timeit`, `<k>` repeats, best of `<k>` reported. Memory: `tracemalloc` peak, or "not measured".

## Reading the table

Which differences are large enough to matter for this program's actual input size? Which are inside run-to-run noise (state the noise: run it three times and report the spread)? A difference smaller than the spread is "not demonstrated", not "slightly faster".

## Qualitative

Things the table cannot show: how long it took to find a planted bug in each version (minutes, measured); how many places change if a field is added; whether a stage-4 learner could read it. One paragraph per option, evidence where possible.

## Recommendation

One option, one sentence, the single decisive reason. Then: what would make this recommendation wrong (an input size, a new requirement).

## What this memo did not test

Be explicit. Future you will want to know.
