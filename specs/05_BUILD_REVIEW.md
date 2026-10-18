# 05 — Build review

**This is the sole current work and verification ledger.** Work scope and acceptance are defined in [02](02_STRATEGIC_PLAN.md) and the owning requirements. Status meanings are defined in [ML-GOV-002](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-002).

## Current work state

As of **2026-10-17**. This starter has no identified Git remote, branch or PR; references below use a portable file snapshot until [ML-G001](07_KNOWN_GAPS.md#ml-g001) is resolved.

| Work | State | Deployment | Integration owner | Evidence / dependency |
|---|---|---|---|---|
| ML-W000 | verified | not_applicable | Integrating agent for this pass | [Structural evidence](evidence/ML-W000/verification.txt), [governance review](evidence/ML-W000/governance-review.md), [product review](evidence/ML-W000/product-review.md), [source snapshot](evidence/ML-W000/source-manifest.sha256). Portable specs only. |
| ML-W010 | planned | not_applicable | Implementing agent, assignment pending | Actual corpus input in ML-G002; execution choice ML-G004. |
| ML-W020 | planned | not_deployed | Implementing agent, assignment pending | ML-W010 real slice and runtime selection. |
| ML-W030 | planned | not_deployed | Implementing agent, assignment pending | ML-W020 behavior; any unresolved mailbox detail ML-G005. |
| ML-W040 | planned | not_deployed | Implementing agent, assignment pending | ML-W030; targets/reachability ML-G003; operational settings ML-G008. |
| ML-W050 | planned | not_deployed | Implementing agent, assignment pending | ML-W040; discovery ML-G006; pilot settings ML-G008. |

## Bootstrap authoring pass — 2026-10-17 — historical

- **Work:** ML-W000.
- **Integration owner:** `/root`, the integrating assistant in this session.
- **Contributors:** independent method reviewer; independent Mothlight scope reviewer; bounded product-contract author and checker author.
- **Branch / PR:** Not attached to a remote repository. No commit, PR, deployment or runtime execution is claimed.
- **Revision / evidence:** To be recorded after this pass's checks and review finish.
- **Requirements:** The ML-GOV requirements in `04`; product requirements are drafted for future work, not claimed as runtime verification.
- **Implemented:** Shared root instruction chain, numbered document ownership, historical intake, strategy, decisions, scoped gap records, development registry and PR template. Product contracts and structural checker are being integrated.
- **Skipped / deferred:** Repository attachment awaits an actual destination; corpus inspection, runtime implementation, DNS/server configuration and public pilot belong to later work units.
- **Hallucinated / corrected:** Proposed stack choices are recorded as defaults instead of being attributed to explicit user approval. No concrete dataset identity or model route has been invented.
- **Broke / regressed:** No application runtime exists in this starter to regress. Documentation integration and structural verification are still pending in this historical pass entry until its completion record is added.
- **Still risky:** The initial corpus and network targets are unobserved. The usefulness of a chosen slice, runtime behavior and live research outcomes require their own evidence.

## Bootstrap completion — 2026-10-17

- **Work:** ML-W000; specification acceptance only.
- **Integration owner:** `/root`.
- **Contributors:** `/root/mothlight_contract_review` authored `03`, UI reference and data registry after an initial scope review; `/root/screen_method_review` analyzed the reference method and authored the structural checker.
- **Independent document reviewers:** `/root/screen_method_review` for governed workflow/traceability; `/root/agent_observatory_design` for the product contract. Neither is represented as a separately configured Hermes provider or a real visitor. The checker author's temporary smoke checks are identified separately from independent document review.
- **Branch / PR:** Portable project folder; no remote destination, branch, commit or PR has been invented. ML-G001 remains open for attachment.
- **Reviewed revision / evidence:** The [source manifest](evidence/ML-W000/source-manifest.sha256) hashes the governed root/spec files, PR template, ignore rules and checker. Evidence files are excluded from that source digest set to avoid self-reference; the ZIP contains the reports. The product review records its exact final `03` hash. [Verification output](evidence/ML-W000/verification.txt) records actual commands, exit codes, timestamps and environment.
- **Requirements / acceptance:** All nine ML-GOV requirements are represented in the starter and work workflow. All 25 production and four UI requirements have a primary work unit, planned check and expected evidence. Structural consistency and independent semantic review are the acceptance for this documentation unit; future runtime requirements remain unperformed.
- **Implemented:** The `00`–`08` method, one authority map and current work table, user/default decision distinctions, scoped gaps, six planned work units, product/UI/data contracts, development model registry, PR reuse rule/template, structural checker and review/evidence records.
- **Skipped / deferred:** Remote attachment, corpus inspection, runtime selection/implementation, server provisioning, DNS, Hermes configuration and the public pilot remain their named future dependencies. No dataset or production fixture was created.
- **Hallucinated / corrected:** Registrar availability was initially classified too strongly; corrected in ML-P001. Overlapping operator/retention questions were separated in ML-P002. Product review corrected the manifest self-hash ambiguity, eviction policy, deletion/retry semantics and trusted-control classification in ML-P003 through ML-P006. The final broad append-rejection phrase was aligned during focused follow-up.
- **Broke / regressed:** No running application was changed. All observed document findings were resolved in the same work unit; the final checker validates the delivered structural references. No undocumented runtime pass is implied.
- **Still risky:** Useful output depends on the actual corpus; protocol correctness needs implementation tests; home reachability and two-origin behavior need live checks; a research finding needs actual evidence. These are explicitly planned acceptance, not failures concealed by a docs pass.

## Future pass format

Follow [ML-GOV-008](04_CLAUDE_CODE_BUILD_PROMPT.md#ml-gov-008). Keep current state in the table and append dated evidence rather than overwriting an earlier failed or incomplete check. For a changed revision, state which prior evidence still applies and which acceptance must be rerun.
