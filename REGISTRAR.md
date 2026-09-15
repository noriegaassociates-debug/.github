# NMG MASTER REGISTRAR

**SYNTAX OS™ · EST. 1984**  
**Human-in-Command · Glassbox History · Provenance-Preserved · No-Endorsement Architecture**

## 1. Purpose

This registrar is the canonical organizing structure for NMG research, repositories, licenses / EULAs, source records, service-access authorities, validation records, and future service-approved code mappings.

The registrar is not an endorsement registry and it does not convert access, a fork, a citation, an accepted EULA, a government account, a software license, or a service approval into institutional sponsorship, certification, ownership, deployment authority, or scientific validation.

The long-term direction is:

`SOURCE / LICENSE / REPOSITORY / ACCESS RECORD -> PROVENANCE REGISTRATION -> VALIDATION STATE -> APPROVED SERVICE / CODE BOUNDARY -> ORGANIZATIONAL AUTHORITY MAPPING`

A later SAM / contract / service-code mapping may be attached only when the underlying authority is actually established. Until then the field remains `UNASSIGNED` or `PENDING-AUTHORITY`.

## 2. Glassbox historical rule

The historical record is retained to validate how the architecture was formed, challenged, corrected, and refined.

**Logs are not deleted merely because they are early, incomplete, superseded, incorrect, or produced by a computational engine. They are organized, classified, linked, and—when necessary—superseded by a stronger record.**

Computational engines are not oracles. Engine output is evidence of an interaction and an analytical state at a point in time; it is not automatically evidence that the underlying proposition is true.

Canonical rule:

`ENGINE OUTPUT != SOURCE AUTHORITY != CALIBRATED MEASUREMENT != PHYSICAL EVENT != HUMAN AUTHORITY`

Historical entries may therefore carry both their original content and a later correction / supersession edge without destroying the earlier record.

## 3. Non-deletion / supersession doctrine

Every registrar entry shall use one of these lifecycle states:

- `ACTIVE`
- `HISTORICAL`
- `SUPERSEDED`
- `WITHDRAWN-FROM-USE`
- `INVALIDATED-BY-EVIDENCE`
- `UNKNOWN-TO-CURRENT-RECORD`

`SUPERSEDED`, `WITHDRAWN-FROM-USE`, and `INVALIDATED-BY-EVIDENCE` do **not** mean erased. The prior record remains visible with the reason, date, authority, and successor record.

A correction requires a new edge:

`PRIOR RECORD -> CORRECTION / CONTRARY EVIDENCE -> CURRENT RECORD`

## 4. Registrar object classes

| Class | Purpose |
|---|---|
| `SOURCE` | Paper, patent, standard, dataset, institutional record, historical record, website, manual, or other source. |
| `REPOSITORY` | GitHub or other source-code / document repository. |
| `LICENSE` | Open-source, commercial, government, institutional, contractual, or other legal-use authority. |
| `EULA` | Accepted end-user / data-use agreement tied to a service or dataset. |
| `SERVICE_ACCESS` | Account-associated access to a platform, API, application, archive, data service, or computing environment. |
| `DATASET` | Registered dataset or data-product lineage. |
| `PATENT` | Patent / application / legal-status record. |
| `SOFTWARE` | Specific software package, version, module, or executable artifact. |
| `MODEL` | Computational or analytical model. |
| `MEASUREMENT` | Calibrated measurement record. |
| `TELEMETRY` | Instrument or system return. |
| `PHYSICAL_EVENT` | Physical-world event or state assertion. |
| `ARCHITECTURE` | NMG-authored architecture or bounded integration record. |
| `N_TRANSFORMER` | Specifically qualified N-TRANSFORMER™ class with physical boundary, telemetry, record, lineage, and authority requirements. |
| `SERVICE_CODE` | Future approved code / service mapping associated with an established organizational or contracting authority. |
| `AUTHORITY` | Human, contractual, regulatory, institutional, license, or other bounded authority record. |

## 5. Mandatory registrar fields

Each entry shall preserve at minimum:

```yaml
registrar_id:
object_class:
title:
canonical_name:
status:
created_at:
observed_at:
registered_at:

source_or_origin:
upstream_author_or_institution:
repository_url:
upstream_repository_url:
version_or_commit:

license_or_eula:
license_identifier:
license_text_location:
legal_use_authority:
accepted_or_effective_date:

service_provider:
service_name:
account_context:
access_scope:
service_environment:
service_approval_state:

sam_mapping: UNASSIGNED
service_code: UNASSIGNED
contract_or_award_authority: UNASSIGNED

validation_state:
validation_methodology:
known_uncertainty:
prohibited_claims:

source_provenance:
cryptographic_integrity:
telemetry_return:
calibrated_measurement:
physical_event:

engine_contributors:
human_authority:

supersedes:
superseded_by:
conflicts_with:
related_records:
notes:
```

Fields that do not apply remain explicit as `N/A`, `UNKNOWN`, or `UNASSIGNED`; they are not silently omitted.

## 6. Validation labels

The registrar uses these labels without promotion across categories:

- `SOURCE-ESTABLISHED`
- `NMG ARCHITECTURAL INTEGRATION`
- `COMPUTATIONAL MODEL`
- `TELEMETRY-RETURN`
- `CALIBRATED MEASUREMENT`
- `PHYSICALLY VERIFIED`
- `LEGAL / LICENSE AUTHORITY VERIFIED`
- `SERVICE ACCESS RECORDED`
- `SERVICE APPROVAL VERIFIED`

A repository license can establish legal-use conditions for code while proving nothing about the physical truth of a scientific claim. A service-access record can establish account access while proving nothing about endorsement, contracting status, or agency approval of NMG architecture.

## 7. Repository registration rule

For each repository record, preserve:

`UPSTREAM OWNER -> UPSTREAM REPOSITORY -> FORK / MIRROR / NMG REPOSITORY -> LICENSE -> COMMIT / VERSION -> NMG USE CLASS -> VALIDATION / SERVICE BOUNDARY`

Required `NMG USE CLASS` values:

- `UPSTREAM-REFERENCE`
- `SOURCE-LIBRARY`
- `INTEROPERABILITY-DEPENDENCY`
- `REPRODUCIBILITY-DEPENDENCY`
- `NMG-AUTHORED`
- `NMG-INTEGRATION`
- `SERVICE-CANDIDATE`
- `SERVICE-APPROVED` *(only when separately evidenced)*

Forking, starring, cloning, mirroring, cataloging, or integrating does not transfer authorship, ownership, endorsement, certification, or institutional authority.

## 8. License / EULA / service-access rule

License and access records are first-class registrar objects.

For each EULA or service access, record the provider, service / application name, environment (`LOCAL`, `DEV`, `TEST`, `SIT`, `UAT`, `STAGING`, `PROD`, or other), account context, acceptance / approval evidence, scope, restrictions, and source record.

An accepted EULA means only that the recorded terms were accepted for the associated service / data context. An approved application in an identity system means only that the account has the recorded application relationship or grant. Neither is treated as institutional endorsement of NMG, its architectures, or its claims.

## 9. Government / institutional source boundary

Government, university, standards-body, laboratory, and commercial records retain their original authority.

Canonical rule:

`ACCESS != ENDORSEMENT`

`LICENSE != CERTIFICATION`

`FORK != AUTHORSHIP`

`ACCOUNT != CONTRACT`

`SERVICE APPROVAL != SCIENTIFIC VALIDATION`

`SCIENTIFIC SOURCE != NMG ARCHITECTURE`

Graph integration may connect these objects but may not merge their authority domains.

## 10. Glassbox engine register

Each computational-engine contribution must be loggable with:

- engine / provider identity;
- model or system version when known;
- source aperture available to the engine;
- prompt / task or interaction identifier;
- output record;
- uncertainty / conflict notes;
- whether the output was later corrected or superseded;
- human disposition;
- downstream records that used it.

The purpose is reproducibility and historical validation of the architecture, not oracle status.

## 11. Physical-return rule

Where a registrar chain reaches an operational physical system, a command or software output is not treated as proof that a physical state changed.

`COMMAND -> AUTHORIZED TRANSITION -> PHYSICAL RETURN -> RE-MEASUREMENT -> REGISTERED RESULT`

No service or software is promoted to an operational N-TRANSFORMER™ boundary without the required physical transformer, telemetry, controlled repository, lineage, validation, and Human-in-Command authority.

## 12. Current build phase

Current status: **REGISTRAR STRUCTURE BUILD-OUT**.

The immediate objective is to organize and register the existing corpus without deleting historical material. Repository, source, license, EULA, access, and notebook records can be entered now. SAM / contracting / service-code mappings remain future authority fields until the relevant evidence is registered.

> **Challenge requires provenance. Correction requires evidence. Supersession requires a stronger record. History remains part of the glassbox.**
