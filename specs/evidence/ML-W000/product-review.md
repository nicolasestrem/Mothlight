# ML-W000 — Independent product-contract review

Recorded: **2026-10-17**. Reviewer: `/root/agent_observatory_design`. Integration owner: `/root`. Product author: `/root/mothlight_contract_review`.

## Reviewed scope

The reviewer independently read the root instruction chain, numbered specifications, historical intake, decision log, data registry and UI reference. The focus was the useful public slice, origin-local private correspondence, independent origins, private event collection, failure/recovery behavior, attribution and work/acceptance traceability. The reviewer made no edits and ran no runtime tests.

Initial product-spec snapshot reported by the reviewer:

```text
866fa6e94387e6c427d90e476ec32ea9f160e336e4a20836182fd042b003e243
```

This hash identifies the reviewed draft, not the final corrected baseline.

## Round one findings

| Finding | Correction | Disposition |
|---|---|---|
| Manifest artifact wording could require a self-hash cycle. | Hash exported payloads; exclude the manifest's own bytes/digest; preserve common snapshot identity. | [ML-P003](../../06_PATCH_PLAN.md#ml-p003) |
| Storage pressure did not define early eviction or unsent-event behavior. | Permit bounded, accounted loss of non-protected events; preserve protected thread/audit state and independent public reads. | [ML-P004](../../06_PATCH_PLAN.md#ml-p004) |
| Deletion/expiry left recovery receipts and independent retry records underspecified. | Invalidate access/receipt/session; retain a finite retired-key horizon; define duplicate append behavior and durable deletion recovery. | [ML-P005](../../06_PATCH_PLAN.md#ml-p005) |
| Known-control classification had no explicit trusted source. | Require verified controls/operator action/reconciliation; untrusted visitor labels remain claims. | [ML-P006](../../06_PATCH_PLAN.md#ml-p006) |

The author separately identified the need to make deletion acknowledgement follow a durable independent deletion-journal record. That clarification was integrated with ML-P005. The integrating agent also clarified event-ID non-reuse after restore, occurrence versus collector receipt time, and private operator-location references.

## Focused round two

The reviewer re-read the changed requirements and acceptance rows. It identified one remaining phrase: ML-MAIL-004 broadly rejected all appends after closure, while ML-MAIL-003 allowed an authenticated duplicate retry to retrieve its prior result. The integration owner aligned the lifecycle text to reject **new** append operations and explicitly refer duplicate retries to ML-MAIL-003.

The reviewer then confirmed the corrected line and reported: **all four findings resolved; no residual material contradiction in the reviewed product contract.** The planned acceptance rows cover the corrected outcomes under the existing work IDs. No new platform or runtime claims were introduced by this review.

Final reviewed [03_MASTER_PRODUCTION_SPEC.md](../../03_MASTER_PRODUCTION_SPEC.md) SHA-256:

```text
bc609dee05d31d5415f2b88f9fc69fe97a3bc61e85bd237e1e41a3cf5a978f2a
```

The final source manifest should retain this exact product-spec digest. Other ledger/evidence files were finalized after this semantic review and are covered by the final structural check.

## Interpretation limits

The review found the corrected specification coherent enough for this starter. It does not establish that the software exists, that an origin is reachable, that a request has occurred, or that any visitor's identity or allowed scope is known. The complete controlled and live acceptance checks remain planned in `03` and the work table in `05`.
