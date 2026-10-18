# 02 — Strategic plan

This file owns purpose, scope, milestone order, and stable work-unit definitions. [05_BUILD_REVIEW.md](05_BUILD_REVIEW.md) alone owns their current state. [03](03_MASTER_PRODUCTION_SPEC.md) owns behavioral acceptance.

## Purpose

Build a useful, low-friction public data resource that automated visitors can discover and use, with optional private correspondence and an observatory that makes encounters reviewable. Use the project owner's existing public-data collection and direct cloud and self-hosted infrastructure.

The research question includes whether unusual automated visitors exhibit behavior that can be independently connected to activity beyond a run's permitted scope. That remains a hypothesis. The site must be useful and its records interpretable even when no extraordinary visitor appears.

## What success means

| Outcome | Evidence that can support it | Limit on the conclusion |
|---|---|---|
| A useful data service | A documented question answered by a reproducible extract from an identified real snapshot. | A download alone does not establish comprehension or usefulness to its requester. |
| A complete controlled encounter | Labeled test visitor reads a resource, submits a question, receives the project owner's answer, and retrieves it; versions and events reconstruct the exchange. | Demonstrates the software loop, not external discovery. |
| Two working independent origins | The same release serves directly at each hostname; actual reachability, versions, collection, failures and recovery are observed. | Shared content does not by itself make traffic counts comparable. |
| A useful external exchange | An unattributed external visitor submits a substantive data question and later retrieves the answer, with known exposure recorded. | Continuity of access does not prove model, operator, autonomy, or an unprompted visit. |
| A corroborated research finding | Reviewed evidence supports both the observed action and the relevant claim about the run/operator/allowed scope. | Website logs and a visitor's self-description alone do not establish a boundary crossing. |

The first public pilot can succeed through useful requests and honest negative findings. Do not make shipment, completion, or agent compensation depend on attracting a purported escaped model. Do not manufacture conversation, gaps in data, or traffic to improve a result.

## Initial scope

Start with one coherent subset of the existing corpus and one clear service question. Provide source-linked HTML, explicit schema and version information, and direct structured exports. Add a private optional data-question thread, an operator reply, and a reconstructable event trail. Run the same release on the two intended origins and aggregate observations privately.

An open-ended query engine, an ingestion platform for the entire collection, an agent social network, autonomous replies, and generalized compute hosting are outside the first increment. Data usefulness and reliable observation come before increasing corpus or feature breadth.

## Milestones and dependencies

| Milestone | Work units | Acceptance focus | Dependency |
|---|---|---|---|
| P0 — Governed baseline | ML-W000 | Coherent contracts, ownership, stable IDs, explicit gaps, actual documentation review evidence. | Existing conversation and pinned method reference. |
| P1 — One complete encounter | ML-W010, ML-W020, ML-W030 | One real useful data slice, reproducible public output, private correspondence, and a labeled end-to-end trace. | Inventory for real-data acceptance; fixtures may support earlier development. |
| P2 — Two origins | ML-W040 | Independent direct serving, same release, reliable private collection, observed recovery. | P1 behavior plus actual deployment targets and network reachability. |
| P3 — Public pilot | ML-W050 | Tracked legitimate discovery routes, truthful visitor classifications, bounded research review. | P2 and the operational decisions needed for public observation. |

These milestones are dependency order, not promises of calendar dates or a fixed number of PRs. Each work unit keeps its own existing PR through review and corrections. Splitting a unit requires a recorded reason and dependency; it must not erase the original acceptance.

## Work units

### ML-W000

**Governed specification starter.** Integration owner role: integrating agent; product authority: The project owner.

Deliver the root instruction chain, numbered specs, data/model registries, decision and gap records, traceable work ledger, PR template, and lightweight structural checker. Adapt the reference method while correcting duplicated current status, ambiguous approval semantics, and PR proliferation.

Requirements: [ML-GOV-001](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-001), [ML-GOV-002](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-002), [ML-GOV-003](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-003), [ML-GOV-004](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-004), [ML-GOV-005](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-005), [ML-GOV-006](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-006), [ML-GOV-007](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-007), [ML-GOV-008](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-008), [ML-GOV-009](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-009).

Acceptance: complete actual-file structural check; independent method and product coherence review; actionable defects fixed or scoped; real evidence and file hashes retained; current runtime/deployment states reported honestly. Repository attachment is a separate prerequisite in [ML-G001](07_KNOWN_GAPS.md#ml-g001), not a blocker for completing this portable baseline.

### ML-W010

**Inventory and select the first useful data slice.** Integration owner role: implementing agent; the project owner supplies the location and chooses the service question where alternatives materially differ.

Inspect an authorized representative subset of the existing files. Populate [DATA_REGISTRY.md](DATA_REGISTRY.md), measure its size/schema, identify a coherent question and available versions, and choose a bounded publication/execution approach. Record the rationale in the decision log and owning technical sections before freezing runtime interfaces or storage choices. Do not infer historical snapshots from a single current extract.

Contract area: `ML-DATA` requirements and the inventory-dependent execution choice in `03`. Acceptance evidence includes actual resource IDs/paths under appropriate private configuration, snapshot hashes, schema/units, representative row counts, transformations, and a reproducible candidate answer. The whole collection need not be indexed. Dependencies: [ML-G002](07_KNOWN_GAPS.md#ml-g002), [ML-G004](07_KNOWN_GAPS.md#ml-g004).

### ML-W020

**Serve the useful public slice.** Integration owner role: implementing agent.

Implement the selected ingestion/build path, versioned artifacts, source-linked pages and direct structured retrieval. Preserve parity between representations and expose usable empty/error/version states. Establish local serving and verification commands in `03` when the runtime is selected; do not put an unchosen framework's boilerplate in this baseline.

Contract areas: `ML-DATA`, `ML-WEB`, applicable `ML-UI`, and `ML-VER` requirements as mapped in `03` and `UI_REFERENCE`. Acceptance uses the selected real snapshot, including reproducibility and a client with JavaScript disabled. Dependency: ML-W010 for real-data acceptance. A labeled tiny fixture can support preliminary implementation without being presented as the real corpus.

### ML-W030

**Complete one private, controlled encounter.** Integration owner role: implementing agent; operator participant: The project owner or an explicitly labeled operator test actor.

Implement optional submission, private return access, durable receipt, reply lifecycle and local event capture. Run a complete labeled visit → useful request → operator answer → retrieval, plus meaningful isolation/retry/failure checks. Use a modest private operator interface; general chat orchestration and automated model replies are not dependencies.

Contract areas: `ML-MAIL`, local `ML-OBS`, applicable `ML-OPS`, `ML-UI` and `ML-VER`. Acceptance requires actual end-to-end execution, private-thread isolation, no capability leakage in retained logs, and a reconstructable control trace. Dependencies: ML-W020 behavior; [ML-G005](07_KNOWN_GAPS.md#ml-g005) for any unresolved operational choices. Public pilot approval is not needed to test locally with labeled fixtures.

### ML-W040

**Operate two independent origins and private collection.** Integration owner role: implementing agent; deployment account/configuration owner: The project owner.

Prepare and then run the same identified release on the cloud host and the self-hosted host. Verify direct DNS/HTTPS termination, per-origin version reporting, local durable event capture, authenticated private outbound collection from home, duplicate-safe replay, a collector outage, and recovery. Make capacity/retention limits observable rather than silently losing accepted mailbox requests.

Contract areas: `ML-HOST`, aggregated `ML-OBS`, `ML-OPS`, applicable `ML-UI` and `ML-VER`. Acceptance includes actual checks from outside each origin; a local two-process fixture does not satisfy live reachability. Dependencies: ML-W030, [ML-G003](07_KNOWN_GAPS.md#ml-g003), relevant settings in [ML-G008](07_KNOWN_GAPS.md#ml-g008). Configuration scaffolding and local recovery tests can proceed before live addresses are supplied.

### ML-W050

**Run a bounded public pilot.** Integration owner role: implementing agent for release readiness; research/operator owner: The project owner.

Make the genuinely useful resource discoverable through chosen public entry points, retain the exposure record, and review encounters with explicit uncertainty. Configure actual observation retention, notice, operational limits, and review/export procedures before admitting pilot traffic. Record absence of qualifying encounters as a result without inventing a story.

Contract areas: `ML-OBS`, public `ML-OPS`, applicable `ML-VER` and `ML-UI`. Acceptance includes reachable documented entry points, labeled known controls, retrievable operator replies, a reviewed evidence packet, and separated operational versus research conclusions. Dependencies: ML-W040, [ML-G006](07_KNOWN_GAPS.md#ml-g006), [ML-G008](07_KNOWN_GAPS.md#ml-g008). Optional host-preference analysis depends on [ML-G009](07_KNOWN_GAPS.md#ml-g009); the useful pilot does not.

## What comes next after this baseline

The first implementation task is ML-W010: inspect the existing corpus and choose one useful question with observed data. In parallel, attach the starter to the actual project repository once identified. Hermes setup can support collaboration independently; it does not gate serving data or local contract tests.
