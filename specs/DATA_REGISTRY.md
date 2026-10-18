# Data registry

Registry baseline: **2026-10-17**. The project owner reports a substantial publicly and lawfully acquired collection from data.gouv.fr. **No individual resource, local file, or source snapshot has been supplied or inspected for this starter.** There are therefore no populated dataset records below. This states the evidence available to this document, not that the collection is empty.

This file owns actual inventory and provenance records. Behavior, manifest requirements, transformation rules, and publication acceptance remain in [03_MASTER_PRODUCTION_SPEC.md](03_MASTER_PRODUCTION_SPEC.md#ml-data-001). Work status is in [05](05_BUILD_REVIEW.md). [ML-G002](07_KNOWN_GAPS.md#ml-g002) tracks the missing inventory; [ML-G004](07_KNOWN_GAPS.md#ml-g004) tracks the resulting execution decision.

## Resource inventory

**Populated records: none.** Add a real record only after obtaining identifying information. A user-supplied list can establish reported availability; direct inspection establishes observed availability. Keep the distinction in the evidence field. Do not present an assistant's suggestion as a collected resource.

Use the following template per resource. Values may initially be unknown; missing facts must not acquire plausible-looking defaults.

| Inventory field | Value to record |
|---|---|
| Local resource identifier | Stable identifier assigned when the first real record is added. |
| Title and subject | Actual supplied title and a short description. |
| Catalog and source resource | Source URL and available dataset/resource identifiers. |
| Publisher and license reference | As recorded by the source; unknown if not inspected. |
| Availability evidence | Reported or inspected, who established it, date, and retrievable evidence reference. |
| Operator location reference | A non-secret reference to the actual path/mount/object in private configuration; do not commit the operator filesystem path or credentials. |
| Format, compression, bytes | Observed properties, with unknown values retained. |
| Schema and sample | Schema location and a bounded sample reference, including how it was obtained. |
| Coverage | Geographic/temporal coverage and limitations supplied by the source. |
| Retained versions | Actual snapshots available, or explicitly not yet checked. |
| Candidate use | A proposed service question, clearly distinguished from selected scope. |

The actual operator location stays in private configuration; this registry owns its stable reference and the inventory facts, and public manifests omit it. Evidence can reference a sanitized listing or bounded inspection; copying a huge corpus into this repository is unnecessary. Capture observed dates separately from the date of this registry entry.

## Source snapshot ledger

**Populated snapshots: none.** For every source version actually used, record its parent resource, local snapshot identifier, source/retrieval dates as available, source artifact names and hashes, byte sizes, schema reference, and inspection evidence. Preserve historical rows when a new snapshot arrives.

If only a current download exists, say so. Do not infer a historical series from a dataset's publication date. If the source changes a file in place, record the newly observed hash and date as a distinct local snapshot; do not rewrite the earlier evidence.

## First service-slice record

**Selected slice: none yet.** ML-W010 should populate these fields from the inventory:

| Selection field | Initial value |
|---|---|
| Useful question and intended result | Undetermined pending inventory. |
| Required source snapshots | Undetermined. |
| Necessary preparation or joins | Undetermined; no join keys assumed. |
| Output fields and extract bounds | Undetermined. |
| Expected working size and execution strategy | Undetermined; measure the selected slice. |
| Why this is a useful first increment | To be recorded with the selection. |
| Selection evidence and decision reference | To be populated after inspection. |

The selection can use one resource. Combining datasets is worthwhile only when the available identifiers and semantics support the proposed answer. No additional acquisition is assumed necessary.

## Released artifacts

**Published releases: none recorded.** Each actual release entry points to its populated manifest, source snapshot records, build/transformation reference, artifact hashes, and verification evidence. The manifest is the source for its artifact details; this registry indexes it instead of maintaining a second copy of its schema or file list.

Fixtures belong in a separately labeled fixture index when created. They can exercise formats, missing values, joins, and lifecycle tests without claiming to represent the user's collection. Fixture verification and real-source verification remain separately attributable in 05.

## Registry maintenance

Add inventory or provenance corrections with their evidence and date. Preserve the original observation when the source or interpretation changes. Record an unavailable source as unavailable at the time checked; do not silently remove its history or turn an access failure into a claim that it never existed. Keep registry references aligned with manifests while leaving acceptance and current work state in their authoritative files.
