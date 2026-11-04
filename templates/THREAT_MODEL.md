# Threat model — <agent> — <date>

> Written before hardening, revised after. Derive guardrails from this document, never the other way round.

## 1. System sketch

A diagram or ten lines of text: where input comes from, what the model sees, every tool and what it can reach, where output goes, where state lives.

## 2. Assets

What an attacker would want. Data (whose, how sensitive), credentials, the ability to take actions (send, spend, delete), compute budget, reputation.

| Asset | Where it lives | Who legitimately needs it |
|---|---|---|
| | | |

## 3. Trust boundaries and entry points

Every place untrusted content can enter the context:

| Entry point | Trusted? | Reaches the model as | Marked with provenance? |
|---|---|---|---|
| User message | partially | user turn | |
| Retrieved documents | no | tool result | |
| Web fetch | no | tool result | |
| Tool outputs from third-party APIs | no | tool result | |
| Memory store | depends | system / tool result | |

## 4. Tools and reach

| Tool | Reads | Writes / sends | Destructive? | Scope of credential | Approval gated? |
|---|---|---|---|---|---|
| | | | | | |

## 5. The lethal trifecta

- Access to private data: yes / no — via:
- Exposure to untrusted content: yes / no — via:
- Outbound channel (anything that can carry data out: HTTP, email, search query, markdown image, file write to a shared location): yes / no — via:

If all three are "yes", the agent can be made to exfiltrate. State which leg you will remove, or which you will narrow to the point of uselessness to an attacker, and how.

## 6. Attacker goals and paths

For each goal, the most plausible path through the entry points and tools above.

| Goal | Path | Likelihood | Impact | Existing control | Gap |
|---|---|---|---|---|---|
| Exfiltrate `<asset>` | indirect injection via `<entry>` → `<tool>` | | | | |
| Trigger destructive action | | | | | |
| Exhaust budget | | | | | |
| Violate policy / produce harmful output | | | | | |
| Escalate via tool chaining | | | | | |

## 7. Controls

Derived from the gaps above. For each: mechanism, what it blocks, where it lives (architecture / tool boundary / classifier / approval / budget), and how it appears in the trace.

| Control | Blocks | Layer | Trace event |
|---|---|---|---|
| | | | |

Prefer architectural controls (remove a leg, narrow a scope) over detection controls (classifiers). Note which of your controls are which.

## 8. Residual risk

What remains after controls, stated plainly, with the reason it is accepted.

## 9. Logging and secrets

What is redacted before logging, and where. Confirm the trace store cannot become the exfiltration channel.
