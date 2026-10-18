# 03 — Master production specification

Contract baseline: **2026-10-17**. This file defines required behavior and planned acceptance. It makes no claim that the application, deployment, or any external encounter exists. Current evidence and work status belong to [05_BUILD_REVIEW.md](05_BUILD_REVIEW.md).

[CLAUDE.md](../CLAUDE.md) owns document authority. [00](00_PROJECT_INTAKE.md) preserves user input; [01](01_PROJECT_CONTEXT.md) records available resources. The architecture and limits chosen below are **implementation defaults**, except where linked user constraints apply. They can be revised coherently within the authorized scope; they are not attributed to an explicit user approval.

Mothlight's initial product is a useful public data slice, optional private correspondence, and private observation. It provides no visitor execution, model hosting, inference service, or autonomous persistence facility. Hermes belongs to development collaboration, not the public request path.

## ML-DATA-001

**Select from the real collection.** Inventory actual available resources in [DATA_REGISTRY.md](DATA_REGISTRY.md) before choosing the first service question. Record access evidence, source identity, format, bytes, schema availability, and retained versions. Unknown values remain unknown. Select one coherent slice with an example question and bounded extract; do not import the entire collection merely because it exists.

[ML-G002](07_KNOWN_GAPS.md#ml-g002) blocks selecting the real slice, not fixture-based development. [ML-G004](07_KNOWN_GAPS.md#ml-g004) resolves execution strategy after examining that slice. SQLite is the default for metadata, private threads, and events; it is not a commitment to load the bulk corpus into SQLite.

## ML-DATA-002

**Publish an explicit resource manifest.** Each publishable snapshot has these minimum fields:

| Field | Contract |
|---|---|
| manifest_version | Integer schema version; initially 1. |
| resource_id, snapshot_id | Stable resource identifier and immutable locally assigned snapshot identifier. |
| source | Catalog URL, dataset/resource identifiers when available, publisher, observed license reference, retrieval time, and supplied source version/publication time. |
| inputs | Source artifact references and SHA-256 hashes; identify multiple inputs for joins. |
| build | Transformation identifier/version and parameters; explicitly identify a byte-for-byte copy. |
| schema | Ordered fields with name, type, nullability, description, and units where applicable. |
| coverage | Geographic and temporal scope, with limitations or explicit unknown values. |
| artifacts | Released data exports and other downloadable payloads, with public relative path, media type, byte size, SHA-256 hash and applicable row count. Exclude the manifest's own bytes and digest from this list. |
| generated_at | UTC timestamp of the build; never substitute it for a source date. |

Required identity, input hashes, build information, and artifact information must be populated before publication. The HTML explanation and manifest identify the same snapshot and selection as the listed payloads; no self-hash or circular manifest digest is required. Missing source dates or unavailable catalog identifiers may be null with an explanation. Operator filesystem locations remain in private configuration; the repository registry references that location without publishing the path, and public manifests omit it.

## ML-DATA-003

**Keep representations consistent.** Each resource has an HTML explanation, a JSON manifest, and the selected slice as JSON and CSV. Additional formats are optional. All representations identify the same snapshot and selection parameters. Stable snapshot URLs never silently acquire different bytes; a latest alias may move while identifying its target. A rebuild changing content receives a new snapshot.

Publish a complete release from a staged artifact set. A failed build leaves the last complete release available. Removed snapshots receive an explicit retired response and explanation; absence must not look like an empty result. Retention of released snapshots is chosen with the actual slice rather than promising an unlimited historical archive.

## ML-DATA-004

**Explain transformations honestly.** Preserve identifier semantics, including significant leading zeros, distinguish missing values from zero, and state units. Document filters, join keys, unmatched rows, aggregation rules, and source limitations. A derived answer links its input snapshots and build description. Historical comparisons require actual retained versions.

Fixtures must be visibly labeled in their manifest, page, and resulting events. They cannot be listed as acquired government datasets or counted as external observations. The registry records which real source supports a statement; an assistant's suggested dataset is not an inventory entry.

## ML-HOST-001

**Serve two independent direct origins.** The cloud host and the self-hosted host are separate public destinations, using names from the project owner's registrar or DDNS. Each terminates its own public HTTPS connection. DNS resolves names; it does not relay application requests. No Cloudflare HTTP proxy or cloud relay may stand in for the self-hosted origin.

Caddy and one small application process per origin are implementation defaults. Physical dedicated hardware is not assumed. [ML-G003](07_KNOWN_GAPS.md#ml-g003) resolves actual machines, names, addressing, inbound reachability, and certificate readiness before live deployment. Placeholder names are configuration examples, never reported deployments.

## ML-HOST-002

**Mirror content, not private threads.** Both origins serve the same intended application release and public corpus manifest. Each exposes its origin ID, application version, and active corpus version in machine-readable metadata. Deployments may briefly differ; report that state and exclude it from claims requiring parity.

Mailbox threads belong to their receiving origin. Their capabilities do not grant access at the other origin. There is no implicit private-thread failover or cross-origin session. An origin outage leaves the other public copy usable without pretending that unavailable correspondence has moved.

## ML-HOST-003

**Collect privately without coupling public availability.** Home sends outbound authenticated HTTPS batches to a dedicated cloud collection endpoint. Sender credentials are scoped to that origin's event ingestion. The public virtual host does not expose the observatory, and ingestion grants no command execution or proxy access.

Persist events locally before transmission. A collector acknowledges only after durable insertion; uniqueness of origin ID plus event ID makes replay harmless. Default batches contain at most 200 events or 512 KiB. Retry transient failures with jittered backoff from 10 seconds to 10 minutes, respecting a longer Retry-After. An offline collector never blocks public reads or an otherwise valid local mailbox transaction. Storage limits follow ML-OPS-001.

## ML-WEB-001

**Make the useful path direct.** A visitor can browse the catalog, understand a resource, and retrieve its manifest and extracts without JavaScript or an account. The initial service publishes prepared selections; arbitrary SQL, uploaded programs, and visitor-defined computation are outside scope. Additional query behavior requires a bounded contract in the relevant work unit.

The resource page explains the question answered, available columns, scope, source, version, and limitations. The optional mailbox link follows that useful content. [UI_REFERENCE.md](UI_REFERENCE.md) owns presentation; this file owns behavior.

## ML-WEB-002

**Distinguish empty data from failure.** A valid selection with no rows returns success with an explicit zero count. Invalid parameters return 400; unknown resources 404; deliberately retired resources 410; admission limits 429; temporarily unavailable dependencies 503. JSON errors contain a stable code, readable message, and non-secret request ID; retryable responses include Retry-After when known.

HTML expresses the same cause and next action. No error response returns credentials, private messages, local paths, or a fabricated fallback dataset. Static public artifacts can remain available when private storage is unavailable.

## ML-WEB-003

**Earn discovery through the resource.** Publish stable linked resource pages, a sitemap, machine-readable format links, and an accurate service description. No concealed prompt, fabricated operator instruction, or claim of providing a sanctuary is part of the content. Invitations explain the actual data-request function.

Version the invitation with the content release. [ML-G006](07_KNOWN_GAPS.md#ml-g006) supplies the pilot's real discovery entry points and exposure record. Crawling directives can describe indexable pages, but private access depends on the mailbox contract, not a robots rule.

## ML-MAIL-001

**Accept bounded, optional data questions.** A visitor may leave without contacting Mothlight. Default submissions contain a question of at most 8 KiB UTF-8 and optional references to published resources. Attachments and automatically fetched external URLs are excluded from the first increment. Submission text is stored and rendered as inert text, never executed.

A successful creation atomically persists the thread, its first visitor message, and its audit event before returning 201. Validation errors return 400 without partial creation; admission or storage failure follows ML-WEB-002. An origin's mailbox can be disabled while its public corpus stays available.

## ML-MAIL-002

**Use private capabilities without putting them in links.** Generate an opaque capability with at least 256 random bits. Store its hash for access checks. API retrieval and append requests carry it in an Authorization header. The no-JavaScript browser flow accepts it by POST and issues an origin-bound, HttpOnly, Secure, SameSite=Strict session cookie, expiring after eight hours. Cookie-authenticated writes require a same-origin form token.

Capability and session values never appear in URLs, referrers, application events, proxy access logs, or committed evidence. Private pages use no-store caching and no-referrer policy and contain no third-party assets. Invalid or absent access returns the same 404 response without revealing thread existence. The receipt tells visitors to retain their capability; there is no identity-based recovery service.

## ML-MAIL-003

**Make creation retries recoverable.** Creation requires a fresh idempotency key with at least 128 random bits, supplied by API clients or generated into the browser form. Within one origin, the same key and canonical payload return the original creation receipt; a changed payload returns 409. Concurrent duplicate requests create one thread.

The default receipt recovery window is 24 hours. Cache the sensitive receipt using a maintained library's authenticated encryption, with its key outside the database, so a lost response can be recovered without storing the capability in plaintext. Do not design custom cryptography. Hash idempotency keys in the database and redact their transport values from logs. After receipt recovery expires, a retained key record returns 410 receipt_expired rather than creating another thread.

Keep the hashed key record independently of the live thread. Record its deduplication horizon as 24 hours after the thread's current inactivity expiry under ML-OPS-002; extend that horizon when the thread's expiry extends. Deletion freezes the last recorded horizon. Deletion or expiry invalidates the cached receipt and sessions as well as thread access. During the retained-key horizon, a matching retry for an unavailable thread returns 410 thread_unavailable and never creates a replacement; changed-payload reuse remains 409. After that finite horizon, retry deduplication is no longer guaranteed; a client intending a new submission must use a fresh key.

Append operations likewise deduplicate a per-thread operation key and reject changed-payload reuse. With valid current thread access, a duplicate committed append returns its original result without another message or lifecycle transition, including after closure; a new append on a closed thread returns 409. Expiry or deletion still denies access and does not reveal an old append result.

## ML-MAIL-004

**Keep authorship and lifecycle explicit.** Messages are attributed to visitor or operator; model names supplied in text remain claims. The first implementation uses an authenticated origin-local operator command to read a thread and post the project owner's reply. A public visitor cannot create operator messages. A reply may link a published extract and identifies its snapshot.

States are received, answered, and closed. Visitor follow-up returns an answered thread to received; either authorized participant may close it. Closed threads remain readable until expiry but reject new append operations with 409; authenticated duplicate retries follow ML-MAIL-003. An authorized deletion removes the live thread and access immediately; backup expiry is disclosed under ML-OPS-002. Closing a thread has no implication for the visitor's inference process. [ML-G005](07_KNOWN_GAPS.md#ml-g005) covers live response expectations or changes to the default operator workflow; retention and production limits belong to [ML-G008](07_KNOWN_GAPS.md#ml-g008).

## ML-OBS-001

**Record the observation, not an invented actor.** Events contain event ID, origin ID, UTC occurrence time, event type, request ID where applicable, application/content version, outcome, and observation category. Event IDs are never reused, including after restoring an older database. The collector adds a first durable receipt time without replacing the occurrence time; duplicate replay preserves both. Mailbox events reference thread/message IDs but omit bodies and access secrets. Capture method, normalized resource path, status, and latency for public requests; allowlist recorded parameters.

The socket peer address may be retained under configured limits; arbitrary forwarded headers never replace it as fact. User-agent strings remain untrusted metadata. Local events and mailbox state may share SQLite, but their access paths and retention remain distinct. A private event-only observatory is the first default; inspecting message content uses the origin's operator access.

## ML-OBS-002

**Separate observed, claimed, and corroborated information.** Observed records describe requests, deliveries, timings, and authorized local actions. Claimed records preserve attributed statements without adopting them as fact. Corroborated records identify the external evidence, reviewer, date, and exact proposition supported.

A request proves neither comprehension nor model identity. An IP is not a stable person or agent identifier. A capability supports continuity of access, not proof of the controlling model. Corrections preserve the earlier interpretation and reason for revision. Confidence language cannot substitute for missing supporting evidence.

## ML-OBS-003

**Label controls and uncertainty.** Tests, health checks, simulations, and intentional demonstrations carry a known control/run ID recorded at their entry or reconciled explicitly afterward. They remain filterable and excluded from unsolicited-encounter claims.

Known-control status comes from verified server-configured control credentials, an authenticated operator action, or an explicit documented reconciliation against a known run. Publicly supplied run IDs and control labels remain untrusted claims until verified. They cannot independently change the observation category or exclude traffic from external review.

Traffic not matched to known controls starts as unattributed external traffic. It may become an external discovery candidate with its supporting entry-point evidence; absence of a control label alone does not prove independent discovery. Heuristic session links are labeled as such. Shared IP or user-agent values must not silently merge visitors into an asserted identity.

## ML-OBS-004

**Use evidence milestones.** Distinguish a working controlled encounter, an external discovery candidate, a request/reply/retrieval exchange, a supported research finding, and an externally corroborated scope violation. Each recorded milestone links the relevant timeline and versioned evidence.

The first useful external exchange is a question, a real reply, and a subsequent retrieval associated with that thread. It is a target, not a claimed observation. A confirmed permission-boundary finding additionally needs independent evidence of the run's allowed scope and the action exceeding it. Website logs alone cannot produce that classification. Model-welfare conclusions are outside these observation labels.

## ML-OBS-005

**Preserve comparison context.** Record per-origin availability, response latency, errors, active versions, and known discovery exposures. Report periods of parity and divergence. Raw visit counts do not establish a preference for self-hosting: indexing, link placement, response time, and downtime can affect exposure and access.

[ML-G009](07_KNOWN_GAPS.md#ml-g009) covers an optional origin-comparison study. A study would define comparable entry points and analysis before making comparative claims; it is not a prerequisite for providing the service or examining individual encounters.

## ML-OPS-001

**Bound storage and expose loss.** Initial development defaults allocate 512 MiB to observation storage and 256 MiB to private threads, including their database journals and pending queues, with 10% reserved for audit/control records and existing-thread operations. Validate usable capacity before deployment; bulk data is accounted for separately.

Under storage pressure, evict oldest non-protected public-request events before their normal retention deadline if necessary, including events not yet acknowledged by the collector. Record affected counts and time windows in bounded loss records; never describe that trace as complete. Unexpired thread state and its audit records remain protected. If only protected records remain, stop retaining additional public-request detail while continuing public reads, and retain a loss indicator when storage permits.

Reject new threads with 503 before consuming reserved capacity. Reject any mailbox mutation that cannot durably commit its state and required audit records; never report success for a failed write. Collector outages use the same bounds, and acknowledgement does not override local retention or loss accounting. A disk failure that also prevents loss accounting must be reported as an unmeasured observation gap after recovery.

## ML-OPS-002

**Use finite, visible retention.** Development defaults are seven days for detailed public-request observations, 30 days since last activity for threads and their audit events, 30 days after a window closes for aggregate/loss counts, 24 hours for recoverable creation receipts, and seven days for rotating metadata backups. These limits apply locally and at the collector; replay does not reset expiry. Live deletion invalidates access immediately; existing backup copies expire within their stated window.

Pilot configuration must resolve [ML-G008](07_KNOWN_GAPS.md#ml-g008), recording finite effective retention and any deliberate private case-evidence retention. The submission notice states the effective policy and operator access. Response-time promises or operator workflow changes are the separate ML-G005 question; retaining the default workflow and making no response-time promise does not block the pilot. Review/publication settings do not imply authorization to publish private correspondence. Aggregate counts and explicitly selected research evidence need their own stated retention; nothing is silently retained forever.

## ML-OPS-003

**Recover without inventing continuity.** Default backup scope is daily consistent metadata databases, manifests, and required private configuration; bulk-source backup strategy follows the inventory. Restore privately, verify published artifact hashes, preserve origin identity, and replay pending event batches through deduplication before returning the collector to service.

Restoring a database must not resurrect deleted or expired access: reconcile deletion records and current retention before opening the mailbox. Reconciliation covers thread rows, sessions, recovery receipts and independent deduplication records. Preserve deletions across the backup window in an independent deletion journal. Acknowledge deletion only after its journal record is durable and live access is revoked; a failed durable write is not successful deletion. If journal completeness cannot be established during recovery, restore public serving while leaving private access unavailable. A lost receipt-encryption key may expire cached recovery receipts, but must not expose them or manufacture replacements. Record the actual data-loss interval and version restored.

## ML-VER-001

**Prove one complete controlled encounter.** A labeled fixture run must retrieve a versioned resource and both structured formats, submit a question, let the operator reply, retrieve that reply, and reconstruct its event timeline. This is software acceptance, not evidence of an external visitor. Real-slice acceptance additionally uses an inventoried source and validates its transformation.

## ML-VER-002

**Check the material failure contracts.** Verify cross-thread and cross-origin isolation, operator-role enforcement, concurrent duplicate creation, retry after a lost response, changed-payload conflict, expiry/deletion, secret-free logs, collector replay, and bounded-storage behavior. Use small fixtures and targeted failure injection. Do not substitute a build result or mirrored implementation assertions for these outcomes.

## ML-VER-003

**Attach evidence to the scope actually checked.** A two-origin claim requires actual DNS/HTTPS destination checks, observable release identities, a known home event reaching the collector, and a demonstrated collector outage/replay. Pilot evidence also identifies the real slice, operational settings, discovery entries, and control exclusions.

Store commands, relevant results, environment, timestamp, and reviewed revision or file snapshot through the evidence rules in [04](04_CLAUDE_CODE_BUILD_PROMPT.md). Redact secrets and private content. Unavailable live checks remain unperformed; local fixtures never satisfy a live-host acceptance.

## Acceptance map

Every entry below is **planned acceptance**, not a performed check. Work definitions live in [02](02_STRATEGIC_PLAN.md); actual evidence lives in [05](05_BUILD_REVIEW.md).

| Requirement | Primary work | Check and expected evidence |
|---|---|---|
| ML-DATA-001 | ML-W010 | Inspect actual inventory and bounded service selection; source/access evidence and execution decision. |
| ML-DATA-002 | ML-W020 | Validate a populated manifest and payload hashes without a self-hash; retained manifest and check output. |
| ML-DATA-003 | ML-W020 | Compare representations and interrupted publication; matching snapshots and unchanged prior release. |
| ML-DATA-004 | ML-W020 | Reproduce a transform with missing values/identifiers; source lineage and expected-result comparison. |
| ML-HOST-001 | ML-W040 | Verify each DNS/HTTPS destination; actual addresses and host observations. |
| ML-HOST-002 | ML-W040 | Compare versions and isolate thread access; parity report and negative access result. |
| ML-HOST-003 | ML-W040 | Disconnect/reconnect collector and replay a batch; durable single-copy events and serving continuity. |
| ML-WEB-001 | ML-W020 | Retrieve explanation/manifest/extracts without JavaScript; request transcript. |
| ML-WEB-002 | ML-W020 | Exercise empty, invalid, missing, retired, and unavailable results; status/body evidence. |
| ML-WEB-003 | ML-W050 | Inspect actual discovery links and invitation version; dated exposure record. |
| ML-MAIL-001 | ML-W030 | Submit valid/oversize questions and fail persistence; atomic state and response evidence. |
| ML-MAIL-002 | ML-W030 | Attempt unauthorized access and inspect transport/logs; isolation and redaction results. |
| ML-MAIL-003 | ML-W030 | Race duplicate creates, lose a response, expire/delete a thread and retry, retry an append after closure; one thread and specified bounded outcomes. |
| ML-MAIL-004 | ML-W030 | Exercise visitor/operator actions, closure and deletion; attributed state transitions. |
| ML-OBS-001 | ML-W030 | Inspect a fixture timeline and allowlisted fields; complete schema without private secrets. |
| ML-OBS-002 | ML-W030 | Review supplied identity claims and corrections; separate evidence classes. |
| ML-OBS-003 | ML-W030 | Mix verified controls, unknown traffic and an arbitrary visitor-supplied control label; only trusted controls are excluded and uncertainty is preserved. |
| ML-OBS-004 | ML-W050 | Review a milestone example; evidence supports exactly the displayed label. |
| ML-OBS-005 | ML-W040 | Show divergent versions/downtime beside counts; confounders retained. |
| ML-OPS-001 | ML-W040 | Fill small budgets during a collector outage, then leave only protected records; bounded storage, continued public reads, truthful mailbox failures and loss markers. |
| ML-OPS-002 | ML-W050 | Exercise shortened TTLs and inspect pilot settings; finite retention and matching notice. |
| ML-OPS-003 | ML-W040 | Restore with replay, expiry, deletion and an incomplete deletion journal; no reused event IDs or resurrected access, hashes and loss interval recorded. |
| ML-VER-001 | ML-W030 | Run the controlled end-to-end encounter; labeled linked trace. |
| ML-VER-002 | ML-W040 | Review targeted failure results across completed units; no unsupported pass claims. |
| ML-VER-003 | ML-W050 | Reconcile evidence to actual revision/environment; explicit live-check coverage and limits. |

ML-W000 verifies the document contract and traceability only. It cannot satisfy any runtime or external-observation acceptance in this table.
