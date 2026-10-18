# Decision log

This file owns decision rationale and authority. The referenced owning specs contain the actual contract. Classes and lifecycle semantics are defined in [ML-GOV-002](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-002). All entries below were recorded **2026-10-17** by the integrating agent; `user_constraint` identifies the project owner's instruction, not approval of every drafted detail.

## ML-D001

- **Class / lifecycle:** `user_constraint` / `active`.
- **Decision:** Use the [reference specs-first method](00_PROJECT_INTAKE.md#reference-method), one authoritative source per question, and accountable delivery records.
- **Authority:** [Intake U07](00_PROJECT_INTAKE.md#user-inputs).
- **Reason:** Future development and reviews must follow inspectable files and evidence across agent sessions.
- **Owning contract:** [CLAUDE.md](../CLAUDE.md), [04](04_CLAUDE_CODE_BUILD_PROMPT.md).

## ML-D002

- **Class / lifecycle:** `user_constraint` / `active`.
- **Decision:** Plan to use both a cloud host and a self-hosted connection with direct public serving and no Cloudflare HTTP proxy.
- **Authority:** Intake U02–U03.
- **Reason:** The project owner explicitly wants those environments and direct hosting. A dedicated physical machine remains an implementation/deployment choice.
- **Owning contract:** [03](03_MASTER_PRODUCTION_SPEC.md), hosting requirements. Actual targets are [ML-G003](07_KNOWN_GAPS.md#ml-g003).

## ML-D003

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Obtain the eventual domain or DDNS names through the project owner's registrar.
- **Authority:** Intake U04 establishes availability; the initial design adopts it as the planned arrangement.
- **Reason:** Use the naming arrangement the project owner has available without turning availability into an immutable hosting instruction.
- **Owning contract:** Hosting requirements in [03](03_MASTER_PRODUCTION_SPEC.md); actual names are ML-G003.
- **Correction:** Independent review in ML-P001 corrected the initial stronger authority class before baseline completion; no new user approval was needed.

## ML-D004

- **Class / lifecycle:** `user_constraint` / `active`.
- **Decision:** Treat the project owner's existing lawful public-data collection as the starting corpus resource.
- **Authority:** Intake U06.
- **Reason:** Build from material already obtained, with concrete inventory before choosing the first service question.
- **Owning contract:** [DATA_REGISTRY.md](DATA_REGISTRY.md) for exact inventory, [03](03_MASTER_PRODUCTION_SPEC.md) for data behavior.

## ML-D005

- **Class / lifecycle:** `user_constraint` / `active`.
- **Decision:** Use Hermes bots and rooms for development brainstorming.
- **Authority:** Intake U05, replacing the earlier Open WebUI suggestion.
- **Reason:** Follow the project owner's collaboration choice. No capability, installation, or provider route is assumed from the choice alone.
- **Owning contract:** [MODEL_REGISTRY.md](MODEL_REGISTRY.md), [ML-GOV-005](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-005).

## ML-D006

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Use **Mothlight** as the working project name.
- **Authority:** Proposed in the earlier design and carried forward for this starter.
- **Reason:** Give artifacts and discussions a consistent identity; it is not a selected public hostname or registered product name.
- **Owning contract:** Project identity in [01](01_PROJECT_CONTEXT.md) and [02](02_STRATEGIC_PLAN.md).

## ML-D007

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Build a useful data resource, optional private data-question mailbox, and private observatory in that order of usefulness.
- **Authority:** Earlier design, developed into the current authorized specs work.
- **Reason:** There is a reason to visit and return, and a concrete exchange can be inspected even without an extraordinary visitor.
- **Owning contract:** Scope and milestones in [02](02_STRATEGIC_PLAN.md), behavior in [03](03_MASTER_PRODUCTION_SPEC.md).

## ML-D008

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Start from Caddy, a small application, local SQLite for mailbox/event metadata, and private outbound event batches from home to an observatory on the cloud host.
- **Authority:** Proposed architecture; reversible technical baseline.
- **Reason:** Keep the two public origins independent and the first implementation small. This does not choose SQLite as the query engine for the entire data collection.
- **Owning contract:** Hosting, storage, collection and failure behavior in [03](03_MASTER_PRODUCTION_SPEC.md). Framework and corpus execution choice: [ML-G004](07_KNOWN_GAPS.md#ml-g004).

## ML-D009

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Begin with one coherent corpus slice and prepared, versioned outputs; decide any additional query machinery from actual inventory and workload.
- **Authority:** Initial scope chosen for a reviewable first implementation.
- **Reason:** Prove useful data and provenance before committing to a general platform.
- **Owning contract:** [ML-W010](02_STRATEGIC_PLAN.md#ml-w010), data/web requirements in [03](03_MASTER_PRODUCTION_SPEC.md).

## ML-D010

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Use conservative observation categories and labeled controls; require independent corroboration for claims about identity or run permissions.
- **Authority:** Research integrity default in this contract; no assertion about an actual visitor.
- **Reason:** Keep the original research question answerable without promoting self-report or web traffic into unsupported conclusions.
- **Owning contract:** Observation and verification requirements in [03](03_MASTER_PRODUCTION_SPEC.md).

## ML-D011

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Keep exactly one current work ledger and reuse the same work-unit PR through corrections; permit truthful fixtures and scoped autonomy.
- **Authority:** Adaptation of the inspected reference method, informed by the project owner's stated accountability goal.
- **Reason:** Reduce drift, repeated context loss, unnecessary approvals, and untraceable PR proliferation.
- **Owning contract:** [04](04_CLAUDE_CODE_BUILD_PROMPT.md); actual work state in [05](05_BUILD_REVIEW.md).

## ML-D012

- **Class / lifecycle:** `deferred` / `active`.
- **Decision:** Leave universal querying, whole-corpus ingestion, automatic model replies, visitor compute/persistence, and an agent social platform outside the initial build.
- **Authority:** Bounded initial scope, not a claim that the project owner permanently rejects those separate ideas.
- **Reason:** They are not required to establish useful data, private correspondence, or reliable observations.
- **Owning contract:** [02](02_STRATEGIC_PLAN.md), boundaries in [01](01_PROJECT_CONTEXT.md).

## ML-D013

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Keep private threads on their receiving origin, use capability access without secrets in URLs, support recoverable creation retries, and use an origin-local operator command with an event-only central observatory for the first increment.
- **Authority:** Bounded product-contract authoring in ML-W000, not a claim of a pre-existing installation or specific user approval.
- **Reason:** Public content can be mirrored while private access, message authorship and durable receipt remain attributable to one origin. Avoid requiring a second messaging or model orchestration system for the first exchange.
- **Owning contract:** Mailbox and observation requirements in [03](03_MASTER_PRODUCTION_SPEC.md); receipt and return presentation in [UI_REFERENCE.md](UI_REFERENCE.md).

## ML-D014

- **Class / lifecycle:** `implementation_default` / `active`.
- **Decision:** Give local development concrete finite limits and retention values, then choose the effective pilot settings using observed capacity and operator needs.
- **Authority:** Initial engineering baseline; the exact values live once in the operations and mailbox requirements in `03`.
- **Reason:** Failure, retry and expiry can be implemented and tested now without pretending that final production capacity or public observation policy has been selected.
- **Owning contract:** [03](03_MASTER_PRODUCTION_SPEC.md), especially ML-OPS-001 and ML-OPS-002. Remaining pilot settings are [ML-G005](07_KNOWN_GAPS.md#ml-g005) and [ML-G008](07_KNOWN_GAPS.md#ml-g008).

## Adding or changing a decision

Allocate a new globally unique heading, record date/author/class/lifecycle, the concrete choice, its authority, reason and owning contract. If it replaces a decision, mark the previous entry superseded and link both directions. Update the owning contract and relevant work/verification record together. Do not store unresolved alternatives here as a second gap list; use `07` until resolved.
