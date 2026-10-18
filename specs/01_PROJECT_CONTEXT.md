# 01 — Project context

Context baseline: **2026-10-17**. Update this file when available resources or constraints change. Current work and verification status lives only in [05_BUILD_REVIEW.md](05_BUILD_REVIEW.md).

## Known resources and their evidence

| Resource | Known fact | Not yet established | Source |
|---|---|---|---|
| Hosting | The project owner has cloud hosting resources and a self-hosted connection and wants to use both. | Machines, operating systems, capacity, addresses, inbound reachability and credentials. | [Intake U03](00_PROJECT_INTAKE.md#user-inputs) |
| Naming | The project owner can arrange a domain or DDNS through the registrar. | Names, DNS records, TTLs, update mechanism and certificate readiness. | Intake U04 |
| Corpus | The project owner reports a substantial lawful public-data collection from data.gouv.fr. | Exact resources, local paths, size, schema, timestamps, hashes and retained historical snapshots. | Intake U06; inventory in [DATA_REGISTRY.md](DATA_REGISTRY.md) |
| Collaboration | The project owner chose Hermes bots and rooms. | Installed release, provider routes, exact models, room setup and available automation. | Intake U05; configuration in [MODEL_REGISTRY.md](MODEL_REGISTRY.md) |
| Project repository | The method reference is recorded in [00](00_PROJECT_INTAKE.md#reference-method). | A Mothlight remote repository has not been identified. This work can proceed as a portable starter. | Connected repository lookup on 2026-10-17; [ML-G001](07_KNOWN_GAPS.md#ml-g001) |

Unknown does not mean unavailable. Do not infer nonexistent datasets, unreachable home networking, or missing permission from absent configuration. Verify the particular dependency when its work unit needs it.

## Constraints that shape the design

- The public service uses direct origins without a Cloudflare HTTP proxy; the project owner's registrar is the planned naming arrangement. The authoritative networking contract is in [03](03_MASTER_PRODUCTION_SPEC.md).
- The cloud host and the self-hosted host are distinct public destinations. A private collection path must not silently turn the home endpoint into a cloud proxy.
- The existing corpus is the starting material. Inventory it and select a coherent useful subset before proposing additional acquisition or a generalized ingestion system.
- Development collaboration uses Hermes. Use role names in durable instructions and exact configured identities in the model registry; do not treat a model's conversational self-description as configuration evidence.
- Specs are the unique contract. Reviewable work, explicit ownership, and evidence are part of delivery, not a retrospective narrative.

## Interpretation discipline

The research motivation is legitimate to investigate as a hypothesis. Serving a request can establish a request, response, and timing; the resulting log does not itself establish a model's identity, consciousness, comprehension, autonomy, or a violation of its run's allowed scope. The [production spec](03_MASTER_PRODUCTION_SPEC.md) defines how to retain observations and separately record claims and corroboration.

The project does not assume that nearly all web visitors are agents. Human, crawler, operator-directed agent, control, and unattributed traffic remain possible. Classification follows evidence, including uncertainty.

## Scope boundaries

Mothlight provides useful public data, optional private data correspondence, and private review of observations. The initial scope excludes executing visitor-supplied instructions, offering visitor compute or autonomous persistence, hosting model weights, and designing an agent escape or inference termination mechanism. These are separate products, not dependencies of this service.

This baseline does not require an LLM in the public request path. Development bot credentials and conversations belong outside the public service and its data stores.
