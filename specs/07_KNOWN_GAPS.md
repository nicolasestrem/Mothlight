# 07 — Known gaps

This file owns unknowns, deferrals and manual prerequisites. It is not a second work-status board; see [05](05_BUILD_REVIEW.md). Gap states are `open`, `resolved`, or `deferred`. Every gap names the exact dependent acceptance and the work that can continue. Dates below are recorded dates, not invented deadlines.

## ML-G001

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Which repository is the Mothlight destination, and is there an existing branch/PR or instruction set to reconcile?
- **Owner:** The project owner supplies the destination; integrating agent checks it and attaches the starter.
- **Needed by:** First remote commit or PR.
- **Blocks:** Repository attachment and truthful remote revision/PR references.
- **Can continue:** All portable specs work, review, local prototypes and structural validation. Do not create a guessed repository or use the method reference as the destination.
- **Resolution evidence:** Actual repository URL, existing instructions/history inspected, and branch/PR recorded in `05`.

## ML-G002

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Which actual files/resources form the first coherent, useful data slice, and what question should they answer?
- **Owner:** The project owner supplies a corpus location or inventory; implementing agent inspects it and proposes the smallest useful slice.
- **Needed by:** ML-W010 acceptance, before real-data acceptance in ML-W020.
- **Blocks:** Claims about actual datasets, their volume, usable join keys, historical comparisons, and real corpus output.
- **Can continue:** Manifest/schema design, labeled fixtures, public interface scaffolding and mailbox protocol implementation.
- **Resolution evidence:** Populated [DATA_REGISTRY.md](DATA_REGISTRY.md), observed schema/hashes/counts, selected service question and available snapshots. Existing approval and lawful collection are accepted premises, not a repeated approval task.

## ML-G003

- **State / recorded:** `open` / 2026-10-17.
- **Question:** What are the two actual machines, names and inbound network paths?
- **Owner:** The project owner supplies target access/names; implementing agent performs scoped deployment checks once targets are identified.
- **Needed by:** Live deployment acceptance in ML-W040.
- **Blocks:** Real DNS/DDNS, certificates, external reachability, measured capacity and a live two-origin claim.
- **Can continue:** Configuration templates, local independent-origin simulations, private batch protocol and recovery checks.
- **Resolution evidence:** Observed operating systems/capacity, separate hostnames and destinations, actual IPv4/IPv6 reachability, DDNS behavior if used, and direct HTTPS checks. If a home connection cannot accept traffic, record that finding and choose a compatible plan with the project owner; do not silently proxy the home endpoint through the cloud host.

## ML-G004

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Which application framework, export build method, and corpus query/storage approach fit the inspected first slice?
- **Owner:** Implementing agent; integration owner records the choice and rationale within scope.
- **Needed by:** ML-W010 technical choice and production runtime scaffold in ML-W020.
- **Blocks:** Frozen runtime dependency versions, real serving commands, performance/capacity claims, and corpus engine/schema commitments.
- **Can continue:** Behavior contracts, fixtures and interface prototypes. This is ordinarily a reversible implementation choice, not an automatic request for user approval.
- **Resolution evidence:** Inventory-based choice, alternatives/tradeoff briefly recorded, current primary documentation checked when selecting changing software, owning `03` sections and runnable verification commands updated.

## ML-G005

- **State / recorded:** `open` / 2026-10-17.
- **Question:** What checking routine and response expectations will the project owner use for live data questions, and does the project owner want any change to the initial operator command workflow?
- **Owner:** The project owner supplies operational preferences when needed; implementing agent keeps the documented command workflow as the default.
- **Needed by:** Any advertised response-time promise or operator workflow change; review the live routine during ML-W050 readiness.
- **Blocks:** Only those promises or changes. The existing mailbox fields, size, capability/session, retry and operator-command defaults in `03` are sufficient for ML-W030's local controlled encounter.
- **Can continue:** Full contracted lifecycle, negative access checks, text/extract replies and labeled controlled encounters. A pilot can retain the default workflow and state that no response time is promised.
- **Resolution evidence:** The actual operator routine and any selected response promise/workflow change recorded in its owning `03` section; user-facing copy in the UI reference. Effective production retention, admission limits, capacity and notice values belong to ML-G008.

## ML-G006

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Which legitimate public entry points will make the resource findable, and which exposures are intentionally seeded?
- **Owner:** The project owner for publication choices; implementing agent prepares a concrete discoverability plan and exposure record.
- **Needed by:** ML-W050 discovery acceptance.
- **Blocks:** Public pilot exposure claims and assertions of independent discovery.
- **Can continue:** Useful content, sitemap/link structure, versioned invitations and local tests.
- **Resolution evidence:** Selected entry points, actual publish/link timestamps, origin destinations, content/invitation versions and known demonstration traffic. Preparing the plan does not itself authorize contacting people or publishing an encounter.

## ML-G007

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Which actual Hermes release, rooms, provider routes and model IDs will be configured for development?
- **Owner:** The project owner for accounts/room destination; development integration owner for observed configuration.
- **Needed by:** A real shared bot-room session or automated development integration.
- **Blocks:** Claims that a particular model or multi-bot setup is running.
- **Can continue:** All Mothlight public-service development and specifications; no runtime LLM is required.
- **Resolution evidence:** [MODEL_REGISTRY.md](MODEL_REGISTRY.md) populated from actual configuration and a labeled smoke exchange; secrets retained outside the repository.

## ML-G008

- **State / recorded:** `open` / 2026-10-17.
- **Question:** What production retention, storage/admission bounds, observation notice and private research review/export settings will the pilot use?
- **Owner:** Implementing agent proposes operational values from observed capacity; the project owner owns research/publication choices.
- **Needed by:** ML-W040 storage/recovery tuning and ML-W050 admission of public pilot traffic.
- **Blocks:** Final production observation/retention configuration and any publication of private encounter material.
- **Can continue:** Local contract checks with declared test settings, evidence packet design and private operator review.
- **Resolution evidence:** Actual settings recorded once in `03`, clear public notice in the interface contract, capacity/recovery checks, and a defined private review procedure. No blanket inference of permission to publish a conversation.

## ML-G009

- **State / recorded:** `open` / 2026-10-17.
- **Question:** Is comparing visitor behavior by hosting origin a primary study, and which exposure/availability controls would make that comparison interpretable?
- **Owner:** The project owner for research priority; research reviewer for the proposed design.
- **Needed by:** Any host-preference claim, not basic pilot launch.
- **Blocks:** Interpreting traffic count differences as a preference for self-hosted versus cloud-hosted infrastructure.
- **Can continue:** Both direct origins, operational comparisons with uptime/latency/errors, useful exchanges and conservative encounter review.
- **Resolution evidence:** Stated hypothesis, observation period, comparable version/exposure information, controls/confounders and bounded analysis method. A negative or inconclusive result is permitted.

## Resolving or deferring a gap

Preserve the original ID and recorded question. Add the answer, source, resolution date and dependent contract/work links; change state to `resolved` or explain a bounded `deferred` scope. Move actual behavior into its owning spec and observed task state into `05`. New information may reopen a gap with a dated explanation; never conceal the earlier resolution.
