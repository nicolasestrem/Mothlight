# 08 — AI-assisted change history

Preserve dated **Change / Why / Verification** records here. [05](05_BUILD_REVIEW.md) owns current work status. Completed records can be archived only under the history-preserving rules in [ML-GOV-009](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-009).

## 2026-10-18 — ML-W000 — Trim reference mentions

- **Change:** Replaced verbose references to the method source with links to [00](00_PROJECT_INTAKE.md#reference-method); condensed that section to one link; removed personal/familiar phrasing.
- **Why:** The reference is background provenance, not contract content; one canonical link is enough.
- **Verification:** `python scripts/check_specs.py` (see PR).

## 2026-10-17 — ML-W000 — Baseline authoring

- **Change:** Started the Mothlight specification tree, shared agent entry points, numbered ownership model, intake, strategy, decision/gap records, work ledger and PR template. Product contracts and a structural checker are being integrated in the same unit.
- **Why:** The project owner requested the reference method for specs-first development, one source of truth and accountability. The pinned reference is `8cdef29381786537b1ccf4e9f6ec7bd1e65d11ad`; workflow rationale and provenance are in [00](00_PROJECT_INTAKE.md).
- **Verification:** Reference intake and independent method/scope reviews completed. Artifact acceptance is not claimed in this historical authoring entry; the completion record will identify actual checker output, review dispositions and final file snapshot.
- **Authority / scope:** Authorized specification work. User constraints are separated from implementation defaults in [DECISION_LOG.md](DECISION_LOG.md). No runtime, dataset import, remote PR or deployment is represented as completed by this entry.

## 2026-10-17 — ML-W000 — Reviewed specification starter

- **Author / integration owner:** `/root`.
- **Change:** Completed the governed Mothlight baseline with 38 stable requirements across workflow, product and interface contracts; six work units; 14 decision records; nine scoped gaps; six preserved review findings; canonical data/model registries; a PR template; and a standard-library structural checker. Added source and review evidence with a reproducible file snapshot.
- **Why:** Establish the requested specs-first contract before implementation, preserve the research purpose and available resources, and make future agent work accountable to exact requirements and observed results. Defaults are concrete but revisable; unknown corpus and host facts remain explicit.
- **Corrections:** ML-P001 through ML-P006 document actual attribution, gap, manifest, storage, lifecycle and control-label findings and their fixes. Retained the final closed-thread retry wording correction from focused review.
- **Verification:** [Governance review](evidence/ML-W000/governance-review.md) and [product review](evidence/ML-W000/product-review.md) completed with their findings resolved. [Actual structural/manifest check output](evidence/ML-W000/verification.txt) and [source hashes](evidence/ML-W000/source-manifest.sha256) identify the delivered snapshot. The full product contract has the same final hash confirmed by its independent reviewer.
- **Scope limit:** This is a verified specification starter. Application, corpus, deployment and external-encounter acceptance remain planned in `03` and their work rows in `05`.

## New record format

Date, work ID and author/integration owner; **Change** with affected owning requirements; **Why** with decision or finding; **Verification** with exact revision/snapshot and evidence links; remaining acceptance if relevant. Correct an earlier statement with a dated correction, not silent history replacement.
