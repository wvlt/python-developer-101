# Post-mortem — <system or incident> — <date>

> Blameless. Specific. Written so that someone building a similar system next year avoids the same thing.
> Used for stage-8 chaos scenarios, any real incident, and the stage-10 capstone (where it is written regardless of whether anything went wrong).

## Summary

Three sentences: what the system is, what happened (or what was learned), what changed as a result.

## Timeline

For incidents. ISO timestamps. Include detection, diagnosis, mitigation, resolution. Note which alerts fired and which should have.

| Time | Event | Source (alert / human / trace) |
|---|---|---|
| | | |

Time to detect: · Time to mitigate: · Time to resolve:

## Impact

- Tasks affected (count, % of traffic):
- Users affected:
- Cost impact (USD):
- Any irreversible actions taken by the agent during the incident:

## Root cause

The mechanism, not the symptom. Reference bestiary IDs. If multiple contributing causes, list all and mark the one without which it would not have happened.

## What the evals missed

Which eval cases would have caught this before production? Why did they not exist? Add them now and link the IDs.

## What observability missed

Was the failure visible in traces? In metrics? Did an alert fire? If detection was by a human, what signal should have fired first?

## What went well

Specifically. The runbook step that worked, the guard that limited blast radius, the trace that made diagnosis fast.

## Action items

| Action | Owner | Due | Type (eval / guard / alert / runbook / architecture / process) | Done |
|---|---|---|---|---|
| | | | | |

## For capstones only: reflections

- What would you build differently from the start?
- Where did production disagree with the evals, and what does that say about the eval set?
- Was an agent the right choice? Answer with the numbers from your ADR and from production. If the answer is no, say so; that is a passing answer.
- What did this cost per task, and what would it cost at 10× load?
- What do you now believe about agents that you did not believe at stage 1?
