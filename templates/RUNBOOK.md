# Runbook — <service> — v<n>

> Written for a peer who has never seen the code and is reading this at 3 a.m. Short imperative steps. Every step says what you should see if it worked.
> Test: hand it to that peer in stage 8. If they cannot execute it, it is not done.

## Service facts

- URL:
- Health endpoint: `GET /healthz` → expect `200 {"status":"ok","version":"<sha>"}`
- Dashboard:
- Trace search:
- Logs:
- Deploy command / pipeline:
- Rollback command:
- Kill switch (stops all agent runs without a deploy):
- Owner / escalation:
- Model pins in effect: see `MODELS.md` at the deployed SHA

## Alerts and responses

### ALERT: Pass rate on sampled traffic below `<threshold>` for `<window>`

1. Open the dashboard; check whether the drop coincides with a deploy (prompt or code). Expect: a deploy marker near the drop, or none.
2. If a deploy: roll back. Expect: pass rate recovers within one window.
3. If no deploy: check model pin drift (provider changed the model behind an alias). Expect: eval run against the pinned ID vs the alias shows a difference.
4. Open five failing traces. Classify against the bestiary. Record IDs in the incident doc.
5. If cause is external (provider), switch to fallback provider via config. Expect: error rate drops; pass rate recovers to the fallback's known level.

### ALERT: Cost per task above `<threshold>` or total spend rate above `<threshold>`

1. Check step count per run on the dashboard. Expect: if a loop bug, p95 steps has jumped.
2. If loop bug: engage kill switch. Expect: new runs stop; in-flight runs hit max iterations and stop gracefully.
3. Identify the triggering input pattern from the most expensive traces.
4. Add a per-request budget guard or a case to the attack suite as appropriate; redeploy; release kill switch.

### ALERT: Provider error rate above `<threshold>`

1. Check provider status page.
2. If provider outage: switch to fallback provider via config. Expect: error rate recovers.
3. If not outage: check for 429s. Expect: if rate limited, backoff metrics rising. Reduce concurrency via config.

### ALERT: Tool error rate for `<tool>` above `<threshold>`

1. Call the tool directly with a known-good input. Expect: valid output matching its schema.
2. If upstream changed shape: circuit-break the tool (config) so the agent gets a structured "tool unavailable" observation rather than garbage.
3. Fix the adapter, redeploy, close the circuit.

### ALERT: Approval queue depth above `<threshold>` or approvals pending longer than `<window>`

1. A human is not responding to approval requests. Page the on-call approver.
2. If approvals are spurious (agent requesting destructive actions it should not attempt), engage kill switch and inspect traces.

### ALERT: p95 latency above `<threshold>`

1. Check whether provider latency or tool latency dominates (trace span breakdown).
2. Provider: switch or reduce output length via config. Tool: check upstream; circuit-break if needed.

## Chaos lab record

Each scenario must have been run and this table filled before the stage-8 gate.

| Scenario | Date | Detected by alert? | Time to detect | Handled by runbook step? | Notes |
|---|---|---|---|---|---|
| Provider outage | | | | | |
| Rate limit | | | | | |
| Model deprecation / alias drift | | | | | |
| Tool returns garbage | | | | | |
| Cost spike | | | | | |

## Routine

- Daily: read ten production traces, including every unrecovered failure. Ten minutes.
- Weekly: review the cost per task trend and the top failure buckets; add production failures to the eval set.
- On every prompt change: CI eval gate must pass; canary to 10% for one window before full rollout.
