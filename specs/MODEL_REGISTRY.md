# Development model registry

This registry owns actual provider routes and exact model identifiers used for development collaboration. It does not identify public visitors and does not place an LLM in Mothlight's serving path.

## Chosen environment

The project owner chose **Hermes bots and rooms**: [ML-D005](DECISION_LOG.md#ml-d005). Exact installation, version, room identifiers and configured routes have not been inspected for this project. Open configuration dependency: [ML-G007](07_KNOWN_GAPS.md#ml-g007).

| Desired participant from the discussion | Durable role to assign per task | Actual configured provider route | Exact model ID / version | Evidence |
|---|---|---|---|---|
| OpenAI / ChatGPT | Implementation or integration, as assigned | Unrecorded | Unrecorded | No project configuration observed |
| Claude | Implementation or independent review, as assigned | Unrecorded | Unrecorded | No project configuration observed |
| DeepSeek | Implementation or independent review, as assigned | Unrecorded | Unrecorded | No project configuration observed |

These are desired participants, not a claim that three specific models are connected. Models may exchange roles. Durable instructions use **integration owner**, **implementer**, **independent reviewer**, **operator**, and **research reviewer**. Avoid permanent provider stereotypes or assumptions that every available model has the same permissions.

## Record a real configuration

For each configured bot, record a stable local bot ID, assigned task role, Hermes release/commit, provider base route without credentials, exact model identifier returned/configured, relevant tool permissions, context limits/settings actually selected, date, and a sanitized smoke-check reference. Treat aliases and provider-routed deployments as aliases until the underlying identity is independently known.

Keep API keys, personal account identifiers where unnecessary, room access secrets and raw private prompts outside the repository. A visitor saying “I am Claude” does not populate this registry. A development model's self-description does not override the configured route and provider evidence.

## Room-to-repository handoff

Use [ML-GOV-005](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-005): one integration owner promotes a reviewed proposal into the owning specs. Record the work ID, proposal rationale, selected decision and actual reviewer evidence. Do not turn a room transcript or a majority vote into a competing source of truth.
