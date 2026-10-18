# 04 — Shared build prompt

Applies to every implementing and reviewing agent. Use role names rather than provider-specific instructions. [CLAUDE.md](../CLAUDE.md) owns the reading order and document authority map.

## ML-GOV-001

**Read the current contract before editing.** Follow the root reading order, inspect the actual repository/worktree, current work row, existing branch and PR, and applicable findings. State the bounded work unit and requirements being addressed. A chat summary is an input to reconcile, not an independent specification.

## ML-GOV-002

**Separate authority from delivery.** Decision records use these classes:

| Class | Meaning | Who may change it |
|---|---|---|
| `user_constraint` | Explicit instruction or established user choice, with an intake or subsequent instruction reference. | The project owner, or an agent applying the project owner's already given instruction. |
| `implementation_default` | A concrete, reversible baseline chosen within the authorized purpose; usable without a new approval ceremony. | Integration owner, with rationale and dependent spec updates. |
| `open` | Missing information or a consequential choice for a named dependency. | Named owner supplies evidence or the project owner resolves a product choice; record the result. |
| `deferred` | Deliberately outside the current scope or milestone. | Integration owner may schedule within existing authority; scope expansion needs the relevant user direction. |

A decision's lifecycle is `active` or `superseded`. Open dependencies themselves live in `07`, not a competing decision backlog. If a decision is superseded, retain its ID, rationale, date, and replacement link.

Only `05` owns current work state: `planned`, `in_progress`, `blocked`, `implemented`, `verified`, or `released`. `implemented` means artifacts exist; `verified` means the unit's stated acceptance was actually checked against the identified revision/snapshot; `released` additionally identifies the real release/deployment evidence. Each row separately states deployment as `not_applicable`, `not_deployed`, or `deployed`. Never use a document or fixture check to claim live deployment. Historical evidence remains dated when a newer change needs new verification.

Observation and attribution categories belong to `03`; a verified software unit is not a verified research finding.

## ML-GOV-003

**Make the contract change first.** For behavior changes, update the owning requirement and decision rationale before or in the same bounded change as implementation. Link requirement IDs from the work record and PR. Preserve IDs; update the canonical home instead of copying rules into prompts, code comments, or a second roadmap.

For a silent reversible internal detail, choose a reasonable implementation and record it in the owning spec or work pass as appropriate. For a consequential unanswered product decision, add a scoped gap and continue unaffected work. For a contradiction, record a patch item, resolve it from existing authority where possible, and stop only the dependent behavior until it is coherent. Explain the specific missing answer if a user question is necessary.

## ML-GOV-004

**Keep one branch and PR for one work unit.** Before creating either, search the actual repository for the unit's branch/PR and inspect its status. Reuse the same open PR for additional commits, review fixes, and agent handoffs. A genuinely separate unit or an explicit stacked dependency may have a new PR; record its base and dependency. A closed or merged predecessor requires a recorded continuation relationship, not reuse of a closed review as though it were open.

Use feature branches. Do not force-push shared history, discard others' changes, or bypass review by committing directly to the default branch. A missing repository destination blocks remote attachment, not local specs work. Do not invent a PR URL or create a repository under an assumed name or visibility.

## ML-GOV-005

**Give parallel work clear ownership.** Each active work unit has one integration owner. Delegate only bounded tasks with disjoint file ownership, or read-only review. Shared contracts are integrated by that owner. A handoff includes the work ID, current revision/snapshot, files touched, commands actually run, open findings, and next bounded action.

Hermes rooms are a discussion surface. Bots may propose and critique; they do not silently rewrite authority through consensus or model-name claims. Actual provider configuration belongs in `MODEL_REGISTRY.md`. Do not send messages to people or publish encounters unless the project owner has authorized that action.

## ML-GOV-006

**Verify the real acceptance, and preserve the evidence.** Store exact commands, exit codes, relevant output, timestamp, environment/fixture label, and reviewed commit or file manifest under `specs/evidence/<work-id>/`. Link a readable summary from `05`; remove secrets and private visitor content before committing evidence, and state any redaction. Evidence for a different revision is historical, not proof of the changed path.

Use small meaningful tests for contract risks: snapshot consistency, mailbox isolation, retries, collection replay, and control labeling. Clearly labeled fixtures, fakes, and simulations are allowed for tests; do not turn them into production behavior or external-visitor evidence. A build succeeding does not prove a mailbox exchange or two-origin deployment. Mark unavailable live checks explicitly and continue independent verification.

For a docs-only unit, check links, ID coverage, source ownership, open-question scoping, and independent coherence. Do not invent runtime tests when no runtime exists. `python3 scripts/check_specs.py` is a structural check; semantic review is separate.

## ML-GOV-007

**Review the same increment independently.** Request a fresh reviewer when a meaningful contract or implementation increment is ready. Provide its scope, revision/snapshot and evidence; ask for concrete conflicts, omissions, or regressions. Reconcile actionable findings in `06`, fix within the same work unit, and record disposition.

Use at most two review rounds for that bounded increment before reporting a material unresolved blocker with its evidence. This limit does not turn a failed acceptance into a pass. Avoid endless stylistic loops; verified unaffected work may proceed.

If the repository has automatic PR reviewers, let its configured triggers operate. Do not assume such automation is configured in a new repository. Do not routinely summon bots, post ritual merge warnings, or open another PR to get a fresh review. Merging or publishing follows existing user authorization and repository gates; an agent may not fabricate either.

## ML-GOV-008

**Leave an accountable record after every meaningful pass.** Update the current row and add a dated pass in `05` with:

- Work ID, integration owner and contributors/reviewers.
- Branch/PR and exact revision, or an honest portable snapshot identifier.
- Requirement IDs and acceptance evidence.
- **Implemented** — what artifacts/behavior now exist.
- **Skipped / deferred** — what was intentionally left and why.
- **Hallucinated / corrected** — unsupported assumptions discovered and corrected, or explicitly none found in this pass.
- **Broke / regressed** — observed regressions and disposition, or checks' relevant limits.
- **Still risky** — concrete residual uncertainty and affected acceptance.

Update `06` for real fixes, `07` for genuine remaining unknowns, and `08` with **Change / Why / Verification**. Do not add ceremonial empty entries on every command. Planned acceptance in `03` must never be reported as performed evidence in `05`.

## ML-GOV-009

**Preserve history and keep live files readable.** Use stable IDs: `ML-W` for work, `ML-D` for decisions, `ML-G` for gaps, `ML-P` for patches, and `ML-<AREA>-` for requirements. Definitions have an exact ID heading in their owning file. References link to that heading when useful. Do not recycle an ID after deletion, renaming, or a release.

Records are history-preserving: correct or supersede with an explanation, never silently rewrite the old reason or test outcome. Current status rows may change as work progresses. On a real tagged release, move completed dated log details to a versioned `specs/archive/` with their IDs and evidence links preserved. Retain an exact ID heading and a compact archive pointer in each owning live file; work IDs also retain one compact status row in `05`. This keeps references resolvable without making archived prose a competing live definition. Retain unresolved gaps in full. Do not manufacture a release solely to tidy the specs.

## Reusable work prompt

> Read `CLAUDE.md` and its mandatory files. Work on the specified `ML-W` unit. Inspect the existing branch/PR and reuse it. List the applicable requirement IDs, current evidence, and scoped gaps. Update the owning contract before changing behavior, implement only the authorized bounded scope, run meaningful checks, obtain independent review, and record the actual result in `05`–`08`. Continue reversible and independent work without repeated approval requests. Hand off the same unit with its exact revision/snapshot and remaining acceptance.
