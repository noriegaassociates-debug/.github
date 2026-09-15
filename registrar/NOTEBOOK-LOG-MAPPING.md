# Notebook / Log Mapping Doctrine

**NMG MASTER REGISTRAR · Glassbox History Layer**

The notebook and log corpus is a first-class historical layer of the registrar. It exists to preserve development chronology, source aperture, analytical context, correction history, and the transition from exploratory research into registered source, architecture, license, dataset, patent, repository, model, measurement, or authority objects.

## Governing rule

A notebook or log is not automatically a validated source. It is a historical container whose contents may include source quotations, human analysis, engine output, provisional claims, corrections, links, code, diagrams, calculations, and later supersession records.

`NOTEBOOK / LOG != SOURCE AUTHORITY`

`ENGINE CONTRIBUTION != ORACLE`

`HISTORICAL VALUE != CURRENT VALIDITY`

## Required relationship model

Every material notebook/log entry should be capable of expressing:

`HISTORY EVENT -> NOTEBOOK / LOG -> SOURCE APERTURE -> ANALYTICAL STATE -> HUMAN DISPOSITION -> PROMOTION / SUPERSESSION EDGE`

A notebook may therefore link to one or more registrar objects without collapsing into them.

## Notebook classes

- `SOURCE-INGESTION-NOTEBOOK` — collects and organizes external sources.
- `ARCHITECTURE-NOTEBOOK` — develops NMG-authored architecture, boundaries, and integration logic.
- `PATENT-LINEAGE-NOTEBOOK` — preserves inventor/patent lineage and comparison history.
- `DATASET-NOTEBOOK` — records dataset discovery, schema, quality, transformations, and intended use.
- `VALIDATION-NOTEBOOK` — records tests, conflicts, uncertainty, corrections, and validation decisions.
- `ENGINE-INTERACTION-LOG` — preserves computational-engine contribution history.
- `PHYSICAL-MEASUREMENT-LOG` — records telemetry, calibration, measured state, and uncertainty.
- `GOVERNANCE-LOG` — records authority, license, EULA, service, standards, configuration, and compliance decisions.

A single notebook may carry multiple classes; class membership does not transfer authority between its contents.

## Mandatory notebook/log metadata

```yaml
notebook_or_log_id:
title:
classifications: []
created_at:
active_period:
status:
human_owner:

source_aperture: []
engine_contributors: []
engine_versions_if_known: []

related_history_batches: []
related_sources: []
related_repositories: []
related_licenses_or_eulas: []
related_datasets: []
related_patents: []
related_architectures: []
related_measurements: []
related_authorities: []

current_validation_state:
known_conflicts: []
supersedes: []
superseded_by: []

raw_record_location:
public_safe_summary:
notes:
```

## Log preservation rule

Original notebook and log states are retained. Corrections are appended through edges rather than destructive rewriting:

`ENTRY v1 -> CHALLENGE -> NEW SOURCE / TEST -> ENTRY v2 -> CURRENT DISPOSITION`

Where practical, timestamps, engine/provider identity, prompt/task context, source aperture, and human disposition should remain recoverable.

## Promotion rule

Notebook material is promoted only when the underlying object is separately registered:

- source material -> `SOURCE`
- patent material -> `PATENT`
- code/repository material -> `REPOSITORY` / `SOFTWARE`
- license terms -> `LICENSE` / `EULA`
- scientific dataset -> `DATASET`
- NMG-authored system definition -> `ARCHITECTURE`
- qualified transformer -> `N_TRANSFORMER`
- measured return -> `TELEMETRY` / `MEASUREMENT`
- validated physical assertion -> `PHYSICAL_EVENT`
- service or contracting right -> `AUTHORITY` / `SERVICE_CODE`

The notebook remains linked as historical provenance after promotion.

## Public / private boundary

Raw notebook URLs, engine conversation identifiers, local file paths, account-management pages, private repository locations, callback/session URLs, and unpublished research records remain in the controlled evidence vault unless intentionally released.

The public registrar should expose only the minimum chronology and provenance needed to understand lineage.

## Glassbox validation objective

The notebook/log system should allow a later reviewer to answer:

1. What question or problem was being investigated?
2. What sources were available at that time?
3. Which engine or tool participated, if any?
4. What conclusion or architecture was proposed?
5. What uncertainty or conflict existed?
6. What later evidence changed the record?
7. Which current registrar object inherited the result?

The value of the log is not that every historical statement was correct. The value is that the architecture remains reconstructable.

> **Preserve the path. Register the correction. Promote only the evidence that survives the gate.**
