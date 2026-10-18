# UI reference

This file owns presentation for the behavior in [03_MASTER_PRODUCTION_SPEC.md](03_MASTER_PRODUCTION_SPEC.md). It is an initial interface contract, not a finished visual design or deployed screenshot. Mothlight is a working name; there is no required brand system. Current status belongs to [05](05_BUILD_REVIEW.md).

## ML-UI-001

**Present a small, useful catalog.** The public home page names the service, states the actual subject of its selected collection, and links its resources. Each resource page follows this reading order: question answered; concise scope and limitations; source and source date; snapshot; fields/units; download choices; optional data request.

Use descriptive links such as Download CSV and Read manifest, with format and file size when known. Display unknown source dates explicitly rather than substituting a fresh build date. Explain whether a link points to an immutable snapshot or the current selection. A fixture or example label appears near the title and download controls, not only in a footer. No invented visit counts, scientific findings, datasets, or live status decoration.

## ML-UI-002

**Keep core interaction accessible and simple.** Use semantic headings, native links and forms, visible keyboard focus, associated field labels, sufficient contrast, and text that remains usable at a 320-pixel viewport and at increased browser text size. Long tables may scroll within a labeled region; the whole page must not require horizontal scrolling.

Catalog navigation, data retrieval, submission, and private-thread access work without JavaScript. JavaScript may improve convenience but cannot be the only way to obtain a capability receipt, understand an error, or read a reply. Status is expressed in text, not color alone. Keep public pages free of unnecessary animation, conversation theatrics, or model-persona branding.

## ML-UI-003

**Explain the mailbox at the moment it matters.** Before submission, show the question limit, optional resource references, effective retention, and that the project owner can read and answer the private thread. Do not promise a response time before it has been established under [ML-G005](07_KNOWN_GAPS.md#ml-g005).

The successful receipt prominently displays the private capability with plain-text instructions to retain it and identifies the origin where it works. Public resources have two copies; private threads always return to their original host. The capability is not a shareable URL. A separate POST form opens a thread from it; never encourage pasting it into a query string. Copy convenience is optional. Private pages display visitor and operator authorship, timestamps, resource versions, and state.

Validation preserves safe user input and explains the correction. Rate, storage, expired-receipt, and unavailable-origin messages reflect the statuses in 03. Closure and deletion controls state their distinct effect before the action. The private page contains no public search, directory of other threads, or speculative label identifying a visitor as a particular model.

## ML-UI-004

**Make the observatory readable evidence.** Its default view is private to the operator and shows origin, time range, active versions, availability, event loss, and control exclusion. An encounter view orders requests and mailbox lifecycle events chronologically and distinguishes observed facts, attributed claims, and external corroboration.

Unknown identity remains visibly unknown. Heuristic links and incomplete traces are marked at the relevant event. Success milestones display their supporting evidence or say target/example. A raw count chart includes the context required by ML-OBS-005. The first observatory links to an origin-local operator workflow for message inspection; it does not imply that private message bodies were centrally collected. Publication is not a default action or an assumed permission.

## Planned interface acceptance

| Requirement | Work | Check and expected evidence |
|---|---|---|
| ML-UI-001 | ML-W020 | Inspect a real-slice page against its manifest; matching source/version/format information. |
| ML-UI-002 | ML-W020 | Exercise keyboard and no-JavaScript retrieval, narrow viewport and enlarged text; concise observations and screenshots where useful. |
| ML-UI-003 | ML-W030 | Complete no-JavaScript submission, receipt, opening, reply and failure paths; secret-redacted interaction record. |
| ML-UI-004 | ML-W040 | Review a labeled mixed-traffic fixture with downtime/loss and claims; accurate labels and evidence links. |

These are planned checks. Record their actual results against the checked revision in 05; writing this reference is not interface verification.
