# Mothlight

A useful public data resource and a private observatory for studying automated visits and follow-up exchanges.

The research motivation includes unusual agent behavior and possible activity outside an agent run's authorized scope. Findings must distinguish observed actions, visitor claims, and independently corroborated facts. The useful public service is the foundation of the experiment.

## Start here

Read [CLAUDE.md](CLAUDE.md) for the shared instructions and authoritative document map. Agents enter through [AGENTS.md](AGENTS.md). The numbered [project plan](specs/02_STRATEGIC_PLAN.md) and [production contract](specs/03_MASTER_PRODUCTION_SPEC.md) define the build; [05_BUILD_REVIEW.md](specs/05_BUILD_REVIEW.md) reports its current state.

This starter adapts the [reference method](specs/00_PROJECT_INTAKE.md#reference-method). Historical schematics and chat discussions are supporting illustrations; the documents identified in `CLAUDE.md` own the contract.

## Check the specification structure

From the project root, with Python 3.10 or newer:

```sh
python3 scripts/check_specs.py
```

The check validates document links, stable ID references, and work-table coverage. It does not establish runtime correctness, deployment, visitor identity, or user approval. Runtime commands will be recorded when a runtime is selected and implemented.

## Attach this starter to a repository

Keep this folder's contents at the Mothlight repository root so `/specs/`, the shared instruction files, and the PR template retain their relative paths. When attaching it to an existing project, read that repository's instructions and reconcile any existing specs and open PR first. Preserve its history and accepted contracts; do not overwrite them mechanically. Record the real repository and branch in the work ledger.
