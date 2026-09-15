# NMG Research Repository Map

**SYNTAX OS™ · EST. 1984**  
**Human-in-Command · Provenance-Preserved · Source-Grounded**

> **Registrar authority:** This repository map is subordinate to [`REGISTRAR.md`](./REGISTRAR.md). The map organizes research by function; the registrar governs identity, provenance, license / EULA, access, validation, lifecycle history, and future service-code / contracting mappings.

This map organizes the GitHub account by research function. It does **not** reassign authorship or ownership of upstream projects. Repositories marked by GitHub as forks remain attributable to their original maintainers, licenses, institutions, inventors, and scientific communities.

## Classification rule

| Class | Meaning |
|---|---|
| **NMG / NORIEGA RECORD** | NMG-authored or NMG-controlled architecture, integration, registry, or implementation record. |
| **UPSTREAM FORK / REFERENCE** | External software, standards, scientific tooling, or institutional source retained for study, interoperability, lineage, reproducibility, or comparison. |
| **SOURCE-ESTABLISHED** | Finding or capability supported by the cited upstream source. |
| **NMG ARCHITECTURAL INTEGRATION** | Noriega-authored wiring, synthesis, boundary definition, or system integration. |
| **COMPUTATIONAL MODEL** | Design, simulation, or proposed configuration not yet physically qualified. |
| **PHYSICALLY VERIFIED** | Reserved for records satisfying the applicable measurement, calibration, and validation gate. |

## Registrar binding

Every repository can be represented as a registrar object with its upstream owner, repository URL, version / commit, license, NMG use class, evidence state, related sources, service-access dependencies, and future approved-service mapping.

Historical repository records are not deleted solely because a fork is old, unused, superseded, or later found unsuitable. They remain part of the glassbox lineage and may be marked `HISTORICAL`, `SUPERSEDED`, `WITHDRAWN-FROM-USE`, or `INVALIDATED-BY-EVIDENCE` in the registrar.

Computational engines and engine-produced logs are treated the same way: preserved for historical validation, organized by lifecycle and provenance, but never treated as oracle authority.

## 1. VERITAS MINERALIS · Geoscience · Mineral State

Primary account anchors:

- `nc-veritas-repo` — NMG-controlled private source/deployment repository for NC-Veritas.
- `nc-localities` — interactive North Carolina localities, minerals, and gems.
- `EMIT-Data-Resources` — upstream NASA EMIT research/data-use reference.
- `emit-sds-l3` — upstream EMIT Level-3 processing reference.
- `gems-tools-pro` / `gems-tools-arcmap` — upstream USGS GeMS tooling.
- `spectral-dataset-RockSL` — upstream mineral spectral-library reference.
- `arcgis-python-api` and spatial-statistics examples — upstream geospatial analysis tooling.

Architectural boundary:

`PHYSICAL GEOLOGIC STATE -> SENSOR / SURVEY RETURN -> CALIBRATION -> REGISTERED MEASUREMENT -> MODEL / CLASSIFICATION -> HIC REVIEW`

## 2. N-VERITAS-MINERALIS-TRANSFORMER™

Canonical architecture specification is maintained in this `.github` repository under:

`architecture/N-VERITAS-MINERALIS-TRANSFORMER.md`

Required non-identity rule:

`SOURCE_PROVENANCE != CRYPTOGRAPHIC_INTEGRITY != SIMULATION_RESULT != TELEMETRY_RETURN != CALIBRATED_MEASUREMENT != PHYSICAL_EVENT`

No computational result is promoted into a physical-state claim without the applicable telemetry, calibration, provenance, uncertainty, and validation record.

## 3. Astronomical Observation · DESI · Physical-to-Digital Provenance

Upstream DESI references include:

- `desiutil`
- `desitarget`
- `desispec`
- `desimodules`
- `redrock`
- DESI tutorials and related source material

These repositories are upstream scientific/software references. Their presence in this account does not imply NMG authorship or DESI institutional authority.

Architectural lesson retained by NMG:

`PHYSICAL PHOTON FIELD -> INSTRUMENT -> RAW RETURN -> CALIBRATION -> CATALOG / INFERENCE -> DOWNSTREAM PHYSICAL TARGETING`

Each transition retains its own source authority and validation boundary.

## 4. Metrology · Calibration · Traceability

Reference repositories include:

- `rmellipse` — NIST digital traceability / metrological records.
- `Metrology` — NIST metrology software reference.
- `AFM-Staircase` — NIST z-piezo AFM calibration reference.
- `STMems_Standard_C_drivers` — sensor-driver reference.
- `TimingDashboard` and `gr-timing_utils` — timing / PTP / GNU Radio timing references.

NMG rule: a recorded value is not a qualified measurement unless its instrument, calibration state, uncertainty, timing, geometry, and provenance are recoverable.

## 5. Materials · Atomistic · Carbon · Photonics

Reference repositories include:

- `AtomisticSimulation`
- `ComputationalMethods`
- `LEGO-xtal`
- `Graphene-topology`
- `Nanotube-Nucleation`
- `Machine_Vision_Carbon_Nanomaterial_Identification`
- `mpb` — MIT Photonic Bands
- `OpenILT` / `Neural-Lithography`
- chemical-vapor-deposition modeling references

These are source/reference repositories unless a separate NMG record explicitly defines an N- transformation boundary.

## 6. Energy · Nuclear · Grid · Resilient Infrastructure

Reference repositories include:

- `armi` — upstream TerraPower ARMI framework.
- `moose` — upstream Idaho National Laboratory multiphysics framework.
- `reactor` — Transatomic reactor documentation archive.
- `grid-data-models`
- `CIMHub`
- `distribution-system-model-calibration`
- `GenX.jl`
- `resstock`
- `dreams`
- `Taxonomy_Feeders`

These remain upstream tools and research references. NMG architecture must separately identify any authored mechanical, control, telemetry, governance, or transformer contribution.

## 7. Security · Governance · Compliance · Provenance

Reference repositories include:

- `OSCAL` / `oscal-content` / `liboscal-java`
- `content` — ComplianceAsCode material
- NIST 800-series tooling and identity references
- GSA acquisition-regulation repositories
- `vc-data-model`, `vc-recognized-entities`, and related W3C VC material
- `hpc_data_integrity_code`

These support standards mapping, evidence structure, compliance research, and provenance design. They do not by themselves certify NMG systems.

## 8. Post-Quantum Cryptography · Integrity

Reference repositories include:

- `crystals-kyber-js`
- `crystals-kyber-javascript`
- `liboqs-python`
- `mlkem-native`
- `SP800-90B_EntropyAssessment`
- `phc-winner-argon2`

Cryptographic integrity is one evidentiary domain. A valid signature or hash proves integrity/authenticity properties of a record; it does **not** independently prove the physical truth of the underlying event.

## 9. Communications · Timing · Networked Systems

Reference repositories include:

- `open5gs` / `open5gs-nms`
- `O-RAN-Testbed-Automation`
- `gr-satellites`
- `gr-timing_utils`
- `TimingDashboard`
- `Massive-MIMO-ISAC-A-Unified-Tensor-Approach-for-Channel-and-Target-Parameter-Estimation`
- `minimod` / `smb`

Any NMG operational integration must identify its exact physical boundary, interface, timing authority, telemetry path, failure mode, and Human-in-Command authorization boundary.

## 10. Computational / Architectural Intelligence Tooling

Reference repositories include:

- `python-genai`
- `gemini-cli`
- `Automodel`
- `WeKnora`
- `TruthfulQA`
- `LoRA`
- `document-intake-accelerator`

These are computational tools or upstream references. They are advisory components unless an NMG architecture explicitly assigns a bounded role. They do not receive independent physical authority.

## Governing lineage doctrine

NMG records shall preserve the following order:

`UPSTREAM SOURCE / INVENTOR / INSTITUTION -> SOURCE-SUPPORTED CAPABILITY -> NMG ARCHITECTURAL INTEGRATION -> VALIDATION STATE -> AUTHORIZED USE BOUNDARY`

Forking, mirroring, cataloging, integrating, or citing an external repository does not transfer ownership, authorship, institutional endorsement, certification, deployment status, or scientific authority.

> **Correspondence without collapse. Integration without identity. Transformation without loss of provenance.**
