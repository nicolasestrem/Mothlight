# ML-W000 — Reference and scope intake review

Recorded: **2026-10-17**. This is a historical review record, not a normative contract or a runtime test. The integrating agent consolidated the actual reports received from the two delegated reviewers named below.

## Reference method review

- **Reviewer:** `/root/screen_method_review`, read-only reference task.
- **Reference:** see [the intake](../../00_PROJECT_INTAKE.md#reference-method).
- **Reported complete reads:** AGENTS.md, CLAUDE.md, numbered specs 00–08, and MODEL_REGISTRY.md. The reviewer specifically confirmed all 1,875 lines of 03 and all 267 lines of 04. UI_REFERENCE.md was outside the governance-review scope.
- **Result:** Preserve the numbered ownership model, contract-before-build sequence, separate approval/implementation/verification/release states, candid build review, and Change / Why / Verification history.
- **Adaptations recommended:** One current status home; explicit PR reuse; truthful fixtures; scoped ambiguity handling; globally scoped IDs; history-preserving archive semantics.
- **Limits:** This reviewed a workflow reference. The reference's runtime rules and native tests were not applied to Mothlight, and the reviewer did not modify it.

The reference reviewer observed stale historical starting-state prose, overlapping roadmap authority, inconsistent live status, and a broad “never mock” instruction that conflicts with required test fixtures. These are reasons for the adaptations documented in [the intake](../../00_PROJECT_INTAKE.md#deliberate-adaptations), not defects asserted against a running Mothlight application.

## Mothlight scope review

- **Reviewer:** `/root/mothlight_contract_review`, independent conversation-scope task before product authoring.
- **Input:** The project owner's user messages and the earlier proposed Mothlight design.
- **Result:** Distinguish explicit user choices from proposed defaults. Carry forward direct cloud and self-hosted origins, the registrar option, the existing lawful public corpus, Hermes development rooms, and the requested specs method. Do not invent concrete datasets, exact model routes, machine facts, or a verified escaped visitor.
- **Contract recommendations:** Source/version provenance, useful non-JavaScript retrieval, private optional correspondence, independent origins and local durability, duplicate-safe collection, labeled controls, and separate observed/claimed/corroborated records.
- **Outcome interpretation:** A controlled encounter proves an exercised software loop. Unknown external traffic is a candidate, not proof of spontaneous discovery or identity. A claim about a run boundary needs evidence of both the action and the run's permitted scope.
- **Limits:** The reviewer later authored the bounded product contracts. This initial scope report is not presented as an independent review of those later files; final product coherence receives a separate reviewer.

## Checker development smoke evidence

Reported by `/root/screen_method_review` for its owned checker file. Temporary fixtures were separate from the evolving project and were not shipped as a runtime or test suite.

```text
VALID_FIXTURE=PASS
BROKEN_CONTRACT_DETECTION=PASS (8 targeted failures detected)
SYMLINK_ROOT_GUARD=PASS
PYTHON_COMPILE=PASS
ID_HEADING_LEVELS_2_TO_6=PASS
PYTHON_COMPILE=PASS
```

The integrating agent inspected the checker implementation. The completed package's actual checker command/output is recorded separately after integration. These reported smoke results do not prove semantic correctness or runtime acceptance.
