# 00 — Project intake

Intake date: **2026-10-17**. This is a historical provenance record, not the live task board. [CLAUDE.md](../CLAUDE.md) defines ownership of current facts and contracts.

## User inputs

| Source | User input (paraphrased) | Meaning carried forward |
|---|---|---|
| U01 | Asked what to build to attract escaped rogue test models. | Investigate unusual automated visitors, including the hypothesis of agents acting beyond a run's permissions. This is a research motivation, not evidence that such visitors are present. |
| U02 | Prefers self-hosting to Cloudflare-hosted properties, reasoning that a rogue agent would avoid them; suggested bare-metal hosting. | Use direct hosting without Cloudflare in the public HTTP path. A physical dedicated server has not been selected. |
| U03 | Has a cloud host and a self-hosted connection available and is willing to use both. | The two intended hosting environments are available according to the project owner; machine specifications and public reachability remain to be observed. |
| U04 | Can obtain a domain or dynamic DNS name through a registrar. | The registrar is available and is the planned naming arrangement. No actual hostname or DNS record has been supplied. |
| U05 | Chose Hermes bots and bot rooms for development discussion. | Hermes is the chosen environment for development brainstorming. Exact routes and model IDs remain unconfigured in this starter. |
| U06 | States that a large collection of data from data.gouv.fr was acquired legally and publicly under an approved access. | Accept the project owner's existing lawful public-data collection as an available project resource. Inventory actual files before choosing a service slice. The project uses the official portal spelling, `data.gouv.fr`, in its documentation. |
| U07 | Asked for a /specs/ directory for this project, following a specs-first method: one source of truth and accountability. | Create this governed specification starter using the [reference method](#reference-method). |

Earlier comments about model welfare, a German wiki, and model self-identification provide motivation. They do not establish a verified incident, a visitor's identity, a hosting requirement for model weights, or an inference lifecycle feature.

## Proposed design brought into this baseline

The earlier discussion proposed the working name **Mothlight**, the same useful content at two direct origins, source-linked HTML and structured extracts, an optional private data-request mailbox, and a private observatory. Proposed technical defaults included Caddy, a small application, SQLite for local event/metadata storage, and outbound private event batches from home to the cloud host.

The project owner welcomed the general design. This baseline makes the proposal concrete while keeping these defaults distinguishable from explicit user constraints. The [decision log](DECISION_LOG.md) records their authority and the [production spec](03_MASTER_PRODUCTION_SPEC.md) owns their behavior. No visitor arrival or deployment is established by the proposal.

The SVG and PNG schematics from the discussion are historical illustrations. They do not override a later corrected contract, and they are not prerequisites for reading these Markdown files.

## Reference method

Specs-first workflow adapted from the [reference repository](https://github.com/nicolasestrem/screensearch/tree/8cdef29381786537b1ccf4e9f6ec7bd1e65d11ad) (pinned revision `8cdef29381786537b1ccf4e9f6ec7bd1e65d11ad`, inspected 2026-10-17). Only transferable workflow was adopted: one shared instruction source, contract ownership, evidence before implementation, candid review, and Change / Why / Verification history. The reference's platform, model, and release requirements do not govern Mothlight.

## Deliberate adaptations

1. Current work status has one home in `05`; historical intake stays dated here.
2. Decision authority, implementation, verification, deployment, and research findings are distinct.
3. Clearly labeled fixtures are allowed; fabricated production success is not.
4. Same work unit means the same branch/PR through fixes and review iterations.
5. Open questions block only dependent work. Agents may resolve reversible details within the contract.
6. Globally scoped IDs survive corrections and archiving; completed history is preserved.
7. The exact corpus gets a data registry. Development model configuration is separate and is not a public-service dependency.
