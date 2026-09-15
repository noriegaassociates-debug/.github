# NMG Glassbox History Dataset

This directory defines the canonical construction rule for the historical-event dataset.

## Governing rule

The history dataset is generated directly from the working browser-history export files. It is not reconstructed from memory, narrative summaries, engine interpretations, or manually selected examples.

`WORKING FILE -> DETERMINISTIC EXTRACTION -> ROW-LEVEL HISTORY DATASET -> REVIEW / PROMOTION`

Narrative files such as `HISTORY-BATCH-*.yaml`, research summaries, notebook mappings, or promotion queues are derivative indexes. They may point into the dataset, but they do not create events and may not alter the underlying chronology.

## Canonical row

Each extracted event preserves the source location and exact export content:

- event ID
- source file and SHA-256
- source timestamp line number
- source link line number
- date and local time
- exact displayed title
- exact Markdown URL
- displayed domain
- tooltip, when present
- exact raw Markdown link line

Mechanical convenience fields such as normalized URL, parsed hostname, and hostname-family class are explicitly derived fields. They are not source-authority or validation judgments.

## Validation posture

Every row begins:

`validation_state = HISTORY_EVENT_UNVALIDATED`

`promotion_state = NOT_PROMOTED`

A row's presence proves that the event occurs in the supplied working history export. It does not prove the truth of the visited page, the correctness of an engine response, ownership, endorsement, license scope, scientific validity, or operational authority.

## Current canonical extraction

`NMG-GLASSBOX-HISTORY-2026-0822-0826-001`

- Coverage: 2026-08-22 through 2026-08-26
- Extracted event rows: 2,067
- Aug 22: 325
- Aug 23: 145
- Aug 24: 583
- Aug 25: 601
- Aug 26: 413

See `MANIFEST-2026-08-22_2026-08-26.json` for source-file hashes and deterministic extraction rules.

## Glassbox preservation

`HISTORY EVENT != VERIFIED CLAIM`

`ENGINE OUTPUT != ORACLE`

`VISIT != ENDORSEMENT`

`REPOSITORY VIEW != AUTHORSHIP`

`SOURCE DISCOVERY != LICENSE AUTHORITY`

Corrections and stronger evidence are represented through disposition and supersession links. The originating history row remains part of the Glassbox record.
