# ML-W000 — Independent governance review

Recorded: **2026-10-17**. Reviewer: `/root/screen_method_review`. Integration owner: `/root`.

## Reviewed scope

The reviewer read the completed root instructions, `00`–`08`, decision log, model/data registries, UI reference and PR template. This included the complete product spec for governance/traceability; a separate reviewer examines the product protocol. The reviewer authored only the structural checker, so this is an independent review of the governed documents, not an independent code review of its own checker.

## Round one findings and integration

| Finding | Severity | Review result | Integration disposition |
|---|---|---|---|
| Registrar availability was treated as a stronger instruction than intake U04 established. | P3 | Keep the planned arrangement, correct the authority class without asking the project owner again. | [ML-P001](../../06_PATCH_PLAN.md#ml-p001): reclassified ML-D003 as implementation_default and aligned source wording. |
| ML-G005 and ML-G008 overlapped after the completed mailbox contract supplied local defaults. | P3 | Narrow operator questions and give production retention/capacity/notice one home. | [ML-P002](../../06_PATCH_PLAN.md#ml-p002): split the questions and clarified which work can continue. |

The reviewer reported **no blocking governance finding**. The integrating agent retained the findings and corrections rather than deleting the original issue from the record.

## Coverage confirmed by the reviewer

- One root authority map and an AGENTS pointer.
- One current work ledger, with historical observations distinguished from live state.
- Six work definitions with exactly one valid current row each.
- All nine governance requirements assigned to ML-W000.
- All 25 production requirements and four UI requirements mapped to work, check and expected evidence.
- Scoped gaps that do not stop independent work because corpus, hosts or Hermes configuration are unknown.
- Explicit PR reuse, stacked dependencies, closed-PR continuation and integration ownership.
- Review and release rules that preserve existing user authorization.
- Archive semantics compatible with retained canonical ID headings and compact work rows.

## Observed draft check

The reviewer executed the package checker from `/tmp`, proving that root resolution does not depend on the caller's working directory. Reported exit code: **0**.

```text
Structural specs check: 18 documents; 129 local links; 65 definitions; 213 id references; 6 work rows
PASS. Structural only; runtime behavior and semantic acceptance are not assessed.
```

This output belongs to the draft present during that review. It predates later decision and evidence records; it is not represented as the final package count. Final acceptance uses the final integration check and snapshot linked from [05](../../05_BUILD_REVIEW.md).

## Focused follow-up — round two

The same independent reviewer re-read the corrected intake/context, ML-D003, ML-G005 / ML-G008, ML-MAIL-004 / ML-OPS-002 and the two dispositions. Reported result: **ML-P001 and ML-P002 resolved; no residual contradiction within that scope.** The reviewer also confirmed that ML-D013 / ML-D014 identify agent-authored defaults and refer to `03` for actual values.

This follow-up is a semantic document review. It does not claim runtime behavior, deployment or the final structural-check result. No governed files were edited by that reviewer.
