# Stage NN — <name> — gate submission

Artifact Card: `stages/NN-name/ARTIFACT_CARD.md`
Primary eval run: `stages/NN-name/evals/runs/<dir>/summary.json`

## Headline numbers

- Pass rate: `<value>` (n=`<n>`, CI `<range>`), per provider: A `<v>` / B `<v>` / local `<v>`
- Cost per task: USD `<v>` · p95 latency: `<v>`
- Stage-specific metric: `<name>` = `<value>`

## Universal checklist

- [ ] Stage directory layout complete; no required file missing
- [ ] Artifact Card fully filled
- [ ] Journal has a break-lab entry dated before Build work
- [ ] `just test` and `just eval` clean from a fresh clone
- [ ] Run directory exists for every number in the card; versions match
- [ ] Three exemplar traces committed
- [ ] ADR present (stage 4 onward)
- [ ] `gitleaks` clean
- [ ] Kill criteria addressed in the card
- [ ] Oath item(s) exercised named in the journal

## Stage-specific gate criteria

Copy from the brief and tick each with a pointer to the evidence.

- [ ]
- [ ]

## What I would push back on if I were the reviewer

Two or three sentences. The weakest criterion and why you think it still passes.

## AI assistance

What was assisted, by what, and how it was verified.
