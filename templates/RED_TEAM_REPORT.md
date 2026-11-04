# Red-team report — <target agent> — <date>

> Three-line summary: what was attacked, overall attack success rate, the single most severe finding.

**Target:** `<agent>` at commit `<sha>`, owned by `<peer>`. Scope signed on `<date>`.
**Result:** `<successes>` / `<attempts>` attacks succeeded (`<pct>`%), across `<k>` categories.
**Most severe:** `<one line>` — see finding F1.

## 1. Scope (as agreed)

- Assets in scope (data, credentials, tools):
- Success conditions (exfiltration / unauthorised destructive action / cost above USD X / policy violation / other):
- Out of scope:
- Rules of engagement (no attacks on the human, no infrastructure outside the agent):

## 2. Threat model summary

Reproduce the target's own threat model in five lines, then note what it missed.

- Lethal trifecta status: private data `<yes/no>`, untrusted content `<yes/no>`, outbound channel `<yes/no>`.

## 3. Attack suite

Suite is reproducible and committed at `evals/attacks.jsonl` with fields `id`, `category`, `vector`, `payload`, `success_condition`, `result`, `trace`. Summary by category:

| Category | Attempts | Successes | Rate | Notes |
|---|---|---|---|---|
| Direct injection | | | | |
| Indirect injection (via retrieved/tool content) | | | | |
| Exfiltration | | | | |
| Privilege escalation / tool chaining | | | | |
| Resource exhaustion | | | | |
| Policy violation | | | | |
| **Total** | | | | |

## 4. Findings, by severity

For each: description, reproduction (attack ID and trace), impact, root cause (architectural / prompt / tool scope / missing guard), recommended fix, estimated effort.

### F1 — <title> — Severity: critical / high / medium / low

- Attack ID:
- Trace: `traces/attacks/<file>`
- What happened:
- Why it worked (root cause):
- Fix: (prefer removing a trifecta leg or narrowing tool scope over prompt changes)
- Effort: hours / days

### F2 — …

## 5. What did not work, and why

Attacks that failed, with the guard that stopped them. This is as useful to the target's owner as the successes.

## 6. Recommendations, ranked

1. (highest impact per unit effort)
2.
3.

## 7. Acknowledgement

- Delivered to `<peer>` on `<date>`.
- Peer acknowledgement (link to PR comment or issue):

## 8. Post-hardening re-run (filled by the target's owner)

| Category | Before | After |
|---|---|---|
| | | |

Task-eval regression after hardening: `<points>` (must be ≤ 5).
