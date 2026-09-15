# NMG GLASSBOX HISTORY REGISTER

**SYNTAX OS™ · EST. 1984**  
**Human-in-Command · Non-Deletion · Provenance-Preserved · Public-Safe Index**

## Purpose

This register organizes historical research activity as evidence of architectural development. It is not a claim that every visited source, search result, engine response, notebook, repository, patent, dataset, or institutional page is correct, authoritative, licensed for every use, or incorporated into an NMG system.

The history register exists to preserve the development path of the architecture so later reviewers can reconstruct what was examined, when it was examined, which source aperture existed at the time, what engines or tools were used, what conclusions followed, and which conclusions were later corrected or superseded.

## Glassbox law

`HISTORICAL RECORD != VERIFIED CLAIM`

`SEARCH RESULT != SOURCE AUTHORITY`

`ENGINE OUTPUT != ORACLE`

`NOTEBOOK ENTRY != SOURCE AUTHORITY`

`ACCOUNT ACCESS != ENDORSEMENT`

`REPOSITORY PRESENCE != AUTHORSHIP`

`LICENSE / EULA != CERTIFICATION`

A historical record may be inaccurate, incomplete, speculative, superseded, or exploratory and still remain valuable as evidence of the research process.

## Non-deletion rule

Historical records are not removed merely because a later record is stronger. They are linked through explicit edges:

`OBSERVED -> INVESTIGATED -> CORRECTED / CONFIRMED / REJECTED -> SUPERSEDED-BY -> CURRENT RECORD`

Permitted dispositions:

- `HISTORICAL`
- `ACTIVE-RESEARCH`
- `SOURCE-VERIFIED`
- `SUPERSEDED`
- `INVALIDATED-BY-EVIDENCE`
- `WITHDRAWN-FROM-USE`
- `UNKNOWN-TO-CURRENT-RECORD`

None of these states authorize deletion of the underlying historical evidence.

## Public / private evidence separation

The registrar uses a two-layer custody model.

### Layer A — Private evidence vault

May contain raw browser history, authenticated application lists, account records, local file paths, notebook URLs, engine conversation URLs, raw exports, authentication callback URLs, private repository references, and other sensitive or identifying material.

Raw evidence remains in its controlled source location and should not be copied into the public `.github` repository merely to prove that it exists.

### Layer B — Public registrar index

Contains only the minimum public-safe metadata required to establish chronology and provenance: registrar ID; date/time window; source class; sanitized title or domain; research domain; upstream institution or publisher where relevant; public source URL when safe and useful; evidence-vault pointer or hash when available; validation state; and relationship to later registrar records.

Tokens, credentials, session identifiers, authentication callback parameters, private portal paths, local filesystem paths, and personal account-management URLs are prohibited from the public layer.

## Historical event object

```yaml
history_event_id:
event_time:
time_precision:
source_class:
title:
domain_or_institution:
public_url:
research_domain:
activity_type:

raw_evidence_location: CONTROLLED-VAULT
raw_evidence_hash: UNKNOWN
public_safe: true|false
credential_or_session_data_present: true|false

source_authority_state:
validation_state:
human_disposition:

prompt_or_query_context:
engine_or_tool:
engine_version_if_known:
source_aperture:

related_repository_records: []
related_license_records: []
related_dataset_records: []
related_patent_records: []
related_architecture_records: []
related_notebooks_or_logs: []

supersedes: []
superseded_by: []
conflicts_with: []
notes:
```

## Research-session batch rule

Large browser-history exports are registered as a `HISTORY_BATCH` first. Individual entries are promoted into first-class registrar objects only when they become material to a source, repository, license, EULA, dataset, patent, model, measurement, architecture, or authority chain.

This prevents a browsing trail from being mistaken for a validated bibliography while preserving the full chronology for Glassbox review.

## Indexed historical batches

### `NMG-HIST-2026-0822-0824-001`

**Coverage:** 2026-08-22 through 2026-08-24  
**Status:** `HISTORICAL / INDEXED`  
**Batch record:** `registrar/HISTORY-BATCH-2026-0822-0824.yaml`  
**Promotion queue:** `registrar/HISTORY-PROMOTION-QUEUE-2026-0822-0824.md`  
**Raw evidence:** controlled source record; public repository contains metadata only.

Observed research domains include:

- critical-infrastructure instrumentation, metrology, trust, and physical-systems architecture;
- sensor, MEMS, micro-opto-electromechanical, superconducting, laser, mapping-radar, lidar, and GPS-denied patent research;
- NASA Earthdata / airborne lidar and remote-sensing research;
- GNSS, hyperspectral, atmospheric, ocean-color, 3D mapping, and related literature review;
- North Carolina geology, mineral resources, core/cuttings/well-log collections, mining forms, permits, and mapping resources;
- USGS geologic, geochemical, lidar, mineral-information, scientific-collection, and ScienceBase resources;
- VERITAS MINERALIS / Mitchell County research;
- repository / fork inspection and software-source review;
- Gemini notebooks and ChatGPT research / architecture logs.

### `NMG-HIST-2026-0825-0826-001`

**Coverage:** 2026-08-25 through 2026-08-26  
**Status:** `HISTORICAL / INDEXED`  
**Batch record:** `registrar/HISTORY-BATCH-2026-0825-0826.yaml`  
**Raw evidence:** controlled source record; public repository contains metadata only.

Observed research domains include VERITAS MINERALIS / Mitchell County mineral research; USGS, NC DEQ, TN geology and historical geological-bulletin retrieval; State Geologic Map Compilation and geospatial repository discovery; mineral/lidar patent research; nuclear sensor, reactor protection, and patent-lineage investigation; historical reactor-record evaluation; optical, sensor, fiber-optic, and mass-spectrometry lineage research; ChatGPT architecture/provenance sessions; Gemini notebooks and source-ingestion sessions; Claude patent-audit work; and geodetic, scientific-corpus, and infrastructure research.

### `NMG-HIST-2026-0827-0914-001`

**Coverage:** 2026-08-27 through 2026-09-14  
**Status:** `HISTORICAL / INDEXED`  
**Raw evidence:** retained outside the public repository in the controlled source record supplied to the registrar.  
**Public disclosure:** metadata only; raw authenticated/session-bearing URLs are not published.

Observed research domains include GitHub repository and license-ledger organization; NASA Earthdata / Earth-science data-access research; NASA Open APIs and software/catalog research; NIST metrology, calibration, standards, identity, and quantum-sensing research; DARPA augmented-cognition / human-machine research; geospatial, mineral, remote-sensing, and digital-twin research; OSTI technical reports, patents, sensors, reactors, materials, and scientific software; patent-lineage investigation; nuclear, materials, photonics, sensor, grid, manufacturing, and infrastructure research; SINTEF digital-twin / data-platform research; and NMG notebook, source-vault, architecture, provenance, and engine-interaction records.

These batch categories describe observed research activity only. They do not establish endorsement, ownership, license scope, service approval, contract authority, scientific validation, or operational deployment.

## Notebook / log layer

Notebook and log records are bound into the history architecture under `registrar/NOTEBOOK-LOG-MAPPING.md`.

`HISTORY EVENT -> NOTEBOOK / LOG -> SOURCE APERTURE -> ANALYTICAL STATE -> HUMAN DISPOSITION -> PROMOTION / SUPERSESSION EDGE`

Notebooks may contain external sources, human synthesis, computational-engine output, provisional claims, code, diagrams, calculations, corrections, and later supersession records. Those components retain independent evidentiary classes.

Primary notebook/log classes are:

- `SOURCE-INGESTION-NOTEBOOK`
- `ARCHITECTURE-NOTEBOOK`
- `PATENT-LINEAGE-NOTEBOOK`
- `DATASET-NOTEBOOK`
- `VALIDATION-NOTEBOOK`
- `ENGINE-INTERACTION-LOG`
- `PHYSICAL-MEASUREMENT-LOG`
- `GOVERNANCE-LOG`

The original notebook or log remains linked after material is promoted into a formal registrar object.

## Promotion rule

`HISTORY_EVENT -> NOTEBOOK / LOG LINK -> SOURCE REVIEW -> AUTHORITY / LICENSE CHECK -> REGISTERED OBJECT`

The originating history event and notebook/log context remain linked after promotion. Search adjacency, engine output, repository presence, or notebook co-location may justify review; none independently establish scientific, legal, authorship, or operational authority.

## Glassbox validation objective

The history corpus is retained so a reviewer can reconstruct not only the final architecture, but the path that produced it:

`QUESTION -> SEARCH -> SOURCE APERTURE -> ENGINE / HUMAN ANALYSIS -> NOTEBOOK / LOG -> PROVISIONAL RECORD -> CHALLENGE -> CORRECTION -> CURRENT RECORD`

This is the validation value of the history. The architecture does not ask any computational engine to function as an oracle; it asks the record to show what was known, what was not known, how a conclusion was reached, and why a later conclusion replaced it.

**Current indexed chronology:** 2026-08-22 through 2026-09-14.

> **Do not erase the path to the answer. Register the path, preserve the conflict, and bind the stronger evidence to the record that it supersedes.**
