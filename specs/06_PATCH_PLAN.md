# 06 — Patch plan

Record concrete defects, contradictions and ordered corrections here. Missing input belongs in [07](07_KNOWN_GAPS.md); current work state belongs in [05](05_BUILD_REVIEW.md). Patch states are `open`, `in_progress`, `fixed`, or `deferred`; a fix requires an actual disposition and evidence.

## Bootstrap review scope

The ML-W000 baseline received structural and independent semantic review. The six observed findings below were corrected and their focused follow-ups completed. Current work/evidence remains in [05](05_BUILD_REVIEW.md). A resolved documentation queue is not evidence that a runtime works.

## ML-P001

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P3, authority attribution in ML-W000.
- **Finding / source:** Independent governance reviewer `/root/screen_method_review` found that registrar availability in intake U04 had been promoted into an immutable `user_constraint` in ML-D003.
- **Owner:** Integrating agent.
- **Fix:** Reclassified the planned registrar arrangement as an `implementation_default`, preserved the actual availability statement and recorded the correction in the decision log. Aligned intake/context wording.
- **Verification:** Owning text inspected after correction; final structural and focused review evidence is linked from `05`. This correction did not require another user permission request.

## ML-P002

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P3, gap scoping in ML-W000.
- **Finding / source:** Independent governance reviewer `/root/screen_method_review` found overlapping mailbox workflow and production retention questions in ML-G005 / ML-G008, despite completed local defaults in `03`.
- **Owner:** Integrating agent.
- **Fix:** Narrowed ML-G005 to the operator routine, response expectations and any requested workflow change. ML-G008 owns effective production retention, capacity/admission, notice and review settings. Clarified that the existing defaults support the local controlled encounter and that no response-time promise is required for a pilot.
- **Verification:** Corresponding `03` references and gap dependencies reconciled; final structural and focused review evidence is linked from `05`.

## Patch record fields

See also the product review fixes below. Each is a correction to the specification, not a claim that its planned runtime check has run.

## ML-P003

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P2, manifest implementability in ML-W000.
- **Finding / source:** Independent product reviewer `/root/agent_observatory_design` confirmed the integrating agent's concern that ML-DATA-002 could require the manifest to list its own hash.
- **Owner:** Integrating agent.
- **Fix:** Limited the artifact list to exported payloads, excluded the manifest's own bytes/digest, and retained common snapshot/selection identity across HTML, manifest and exports.
- **Verification:** Required acceptance wording updated; focused document review and final structural evidence are linked from `05`. No build or hash-validation runtime is claimed.

## ML-P004

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P2, bounded observation/collector behavior in ML-W000.
- **Finding / source:** Independent product reviewer `/root/agent_observatory_design` confirmed that ML-OPS-001 did not define eviction eligibility before normal TTL or collector acknowledgement.
- **Owner:** Integrating agent.
- **Fix:** Explicit pressure eviction of non-protected events, including unsent ones; bounded loss records; protected thread/audit state; continued public reads; rejection of mailbox writes that cannot commit. Related collection clarification preserves original occurrence/receipt times and forbids event-ID reuse after restore.
- **Verification:** Small-budget/outage acceptance now names these outcomes; focused review and final structural evidence are linked from `05`. This is a corrected failure contract, not a performed outage test.

## ML-P005

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P2, mailbox lifecycle/recovery in ML-W000.
- **Finding / source:** Independent product reviewer `/root/agent_observatory_design` identified missing receipt invalidation and independent retry-key retention on deletion/expiry. Product author `/root/mothlight_contract_review` also requested durable deletion-journal ordering before acknowledgement.
- **Owner:** Integrating agent.
- **Fix:** Added an explicit finite deduplication horizon, retired-key behavior, invalidation of sessions/receipts, duplicate append behavior after closure, and restore reconciliation. Successful deletion requires durable journal evidence plus revoked live access.
- **Focused follow-up:** Reviewer found one broad “reject append” phrase remaining in ML-MAIL-004; aligned it to reject only new operations, preserving authenticated duplicate-result retrieval under ML-MAIL-003.
- **Verification:** Lifecycle/recovery acceptance updated and reviewed as a contract; actual concurrency, deletion and restore tests remain future runtime work recorded in `03`.

## ML-P006

- **State / observed:** `fixed` / 2026-10-17.
- **Severity / work:** P2, trustworthy observation categories in ML-W000.
- **Finding / source:** Independent product reviewer `/root/agent_observatory_design` found that ML-OBS-003 did not define the trusted source of a known-control label.
- **Owner:** Integrating agent.
- **Fix:** Required verified control credentials, authenticated operator action or documented reconciliation. Public labels remain claims and cannot remove a visit from external review. Added that negative case to planned acceptance.
- **Verification:** Focused document review and final structural evidence are linked from `05`; no real traffic classification has been performed.

## Adding the next patch

Each concrete item gets an exact ID heading, observed date, severity/affected acceptance, finding and source, integration owner, owning requirement or conflicting sections, bounded fix, state and verification reference. Preserve the original finding when adding its resolution. Fix review feedback on the existing work-unit branch/PR.
