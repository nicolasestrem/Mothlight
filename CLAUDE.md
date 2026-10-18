# Mothlight — shared repository instructions

These instructions apply to every human and coding agent. The filename does not assign authority to a particular model. `AGENTS.md` is a pointer to this file, not a second instruction set.

## Start every work session

1. Read this file and [01 — Project context](specs/01_PROJECT_CONTEXT.md).
2. Read [02 — Strategic plan](specs/02_STRATEGIC_PLAN.md) and [03 — Master production spec](specs/03_MASTER_PRODUCTION_SPEC.md).
3. Read [04 — Shared build prompt](specs/04_CLAUDE_CODE_BUILD_PROMPT.md) in full.
4. Read the current work table and relevant pass in [05 — Build review](specs/05_BUILD_REVIEW.md), then the relevant entries in [06 — Patch plan](specs/06_PATCH_PLAN.md) and [07 — Known gaps](specs/07_KNOWN_GAPS.md).
5. Read [UI_REFERENCE.md](specs/UI_REFERENCE.md) for interface work; [DATA_REGISTRY.md](specs/DATA_REGISTRY.md) for corpus work; [MODEL_REGISTRY.md](specs/MODEL_REGISTRY.md) for development bot configuration. Consult [00 — Intake](specs/00_PROJECT_INTAKE.md) and [DECISION_LOG.md](specs/DECISION_LOG.md) for provenance.

Do not rely on a previous chat, memory summary, bot-room consensus, diagram, or an earlier read when the repository has changed. Inspect the current branch, work unit, and existing PR before editing. For a portable copy without Git metadata, say so and identify the delivered file snapshot instead.

## One authoritative home for each question

| Question | Authoritative file |
|---|---|
| What did the project owner originally say, and what was only proposed? | [00_PROJECT_INTAKE.md](specs/00_PROJECT_INTAKE.md), dated historical intake |
| What infrastructure, data, and constraints are presently known? | [01_PROJECT_CONTEXT.md](specs/01_PROJECT_CONTEXT.md) |
| Why build this, in which scope and order? | [02_STRATEGIC_PLAN.md](specs/02_STRATEGIC_PLAN.md) |
| What must the product do, including failure and acceptance behavior? | [03_MASTER_PRODUCTION_SPEC.md](specs/03_MASTER_PRODUCTION_SPEC.md) |
| How do public and private interfaces present that behavior? | [UI_REFERENCE.md](specs/UI_REFERENCE.md) |
| Which real data resources and snapshots are available? | [DATA_REGISTRY.md](specs/DATA_REGISTRY.md) |
| Which provider routes and models are configured for development? | [MODEL_REGISTRY.md](specs/MODEL_REGISTRY.md) |
| How must an agent implement, review, verify, and hand over work? | [04_CLAUDE_CODE_BUILD_PROMPT.md](specs/04_CLAUDE_CODE_BUILD_PROMPT.md) |
| What is the current work status and what was actually checked? | [05_BUILD_REVIEW.md](specs/05_BUILD_REVIEW.md) |
| Which concrete defects or contradictions need a patch? | [06_PATCH_PLAN.md](specs/06_PATCH_PLAN.md) |
| What is unknown or deferred, who owns it, and what does it block? | [07_KNOWN_GAPS.md](specs/07_KNOWN_GAPS.md) |
| Why was a decision made and what is its authority? | [DECISION_LOG.md](specs/DECISION_LOG.md); behavior itself stays in its owning spec |
| What changed, why, and with which evidence? | [08_CHANGELOG_AI.md](specs/08_CHANGELOG_AI.md) |

This table owns document responsibilities. Other files link here rather than maintaining competing maps. `05` alone owns current implementation/verification/deployment status; historical pass entries elsewhere are dated observations. `02` owns the work plan, not a second live task board.

## Contract precedence and change authority

Current explicit user instructions and already established authorization take precedence over repository guidance. Record a durable instruction in its owning spec when it changes the contract. Do not claim the project owner approved an agent's proposal merely because it appears in this repository.

Use [the decision classes in 04](specs/04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-002). Accepted user constraints persist until the user changes them. Recorded implementation defaults can be changed by the integration owner within the authorized scope, with a reason and dependent contract updates. An unknown blocks only the work that needs its answer. Resolve reversible internal choices autonomously; continue independent work. Do not invent missing dataset, deployment, or identity facts.

If two authoritative documents conflict, log the concrete conflict in `06`, correct the owning document when the answer is already supported, and update references. When a consequential product decision really lacks authority, ask one focused question after completing unaffected work. Do not repeatedly request an approval already provided.

## Accountability without parallel truth

Every meaningful work unit has one stable `ML-W` ID in `02`, one current status row in `05`, an identified integration owner, and acceptance evidence tied to the reviewed revision or file snapshot. Reuse its branch and PR for corrections. Read the complete operating rules in `04`; do not create additional agent-specific rulebooks.

Development bot rooms produce proposals and review findings. The integration owner promotes accepted changes into the owning files. A conversation by itself does not modify a contract or verify a feature.
