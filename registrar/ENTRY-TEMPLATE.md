# NMG Registrar Entry Template

Use this template for each source, repository, license, EULA, service-access record, dataset, software artifact, patent, model, measurement, telemetry return, architecture, N-TRANSFORMER™ record, or future service-code mapping.

```yaml
registrar_id: NMG-REG-YYYY-NNNN
object_class:
title:
canonical_name:
status: ACTIVE
created_at:
observed_at:
registered_at:

# Origin / provenance
source_or_origin:
upstream_author_or_institution:
source_citation:
repository_url:
upstream_repository_url:
version_or_commit:
parent_record:

# Legal / use authority
license_or_eula:
license_identifier:
license_text_location:
legal_use_authority:
accepted_or_effective_date:
restrictions_or_conditions:

# Service / account boundary
service_provider:
service_name:
account_context:
access_scope:
service_environment:
service_approval_state:
service_access_evidence:

# Future contracting / service mapping
sam_mapping: UNASSIGNED
service_code: UNASSIGNED
contract_or_award_authority: UNASSIGNED
naics_or_psc_mapping: UNASSIGNED

# Evidence / validation
validation_state:
validation_methodology:
known_uncertainty:
prohibited_claims:
source_provenance:
cryptographic_integrity:
simulation_result:
telemetry_return:
calibrated_measurement:
physical_event:

# Architectural use
nmg_use_class:
nmg_architectural_integration:
physical_transformation_boundary:
controlled_repository_boundary:
required_telemetry:
human_authority:

# Glassbox engine history
engine_contributors:
engine_record_ids:
engine_output_status:
human_disposition:

# History / graph
supersedes:
superseded_by:
conflicts_with:
related_records:
change_reason:
notes:
```

## Rules

1. Do not delete a historical entry because it later proves incomplete, incorrect, or superseded. Change the lifecycle state and attach the successor / correction edge.
2. Do not use `SERVICE-APPROVED`, `PHYSICALLY VERIFIED`, or `LEGAL / LICENSE AUTHORITY VERIFIED` unless the relevant evidence is actually registered.
3. Keep `SOURCE`, `LICENSE`, `SERVICE_ACCESS`, `REPOSITORY`, `MODEL`, `MEASUREMENT`, `TELEMETRY`, and `PHYSICAL_EVENT` as separate objects even when they are linked.
4. Computational engines are advisory contributors. Their outputs remain part of the glassbox history but do not receive independent source or physical authority.
5. Government or institutional access, account relationships, EULAs, grants, repositories, and services shall never be represented as endorsement unless an independent record expressly establishes endorsement.
6. Empty authority fields remain `UNKNOWN`, `UNASSIGNED`, or `N/A`; do not infer them from adjacency in the graph.
