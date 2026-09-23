# US2873303A — SOURCE-AUTHORITY PHOTOVOLTAIC BOM

This record separates the photovoltaic hardware and semiconductor physics directly disclosed in US2873303A from any later DUAL MODAL™ or N-TRANSFORMER™ architectural mapping.

## Authority law

`PATENT-DISCLOSED PHOTOVOLTAIC DEVICE != DUAL MODAL™ ARCHITECTURAL MAPPING != N-TRANSFORMER™ IDENTITY`

| Patent Ref. | Physical Asset | Physical Mechanism | Native Interface | Measurand / Energy Domain | Patent-Disclosed Function | DUAL MODAL™ Interpretation | Authority Tier |
|---|---|---|---|---|---|---|---|
| 1 | n-type AlSb region | Semiconductor majority/minority carrier transport | p-n junction + ohmic contact | Incident optical energy / carrier density | Forms one side of photovoltaic junction | Semiconductor conversion region | DIRECT PATENT DISCLOSURE |
| 2 | p-type AlSb region | Semiconductor majority/minority carrier transport | p-n junction + ohmic contact | Incident optical energy / carrier density | Forms complementary side of photovoltaic junction | Semiconductor conversion region | DIRECT PATENT DISCLOSURE |
| p-n interface | AlSb junction | Built-in electric field separates photogenerated carriers | Junction between regions 1 and 2 | Photogenerated electron-hole pairs | Converts absorbed optical energy into separated charge | Primary physical energy-conversion boundary | DIRECT PATENT DISCLOSURE |
| 3 | Light-receiving surface | Optical absorption into AlSb | Incident solar / visible radiation | Photon flux | Admits radiation to active semiconductor region | Optical-energy ingress boundary | DIRECT PATENT DISCLOSURE |
| 9 | Anti-reflecting coating | Optical impedance / reflection reduction | Optical surface coating | Incident light | Reduces reflection losses at receiving surface | Passive optical coupling optimization | DIRECT PATENT DISCLOSURE |
| 5 / 6 | Metal coatings / ohmic contacts | Low-resistance carrier extraction | Electrical contact to p/n regions | Photogenerated electrical current | Collects current from semiconductor regions | Electrical extraction boundary | DIRECT PATENT DISCLOSURE |
| 7 | External load resistance | Electrical power dissipation | Conductors 8 / 9 | Output voltage/current | Receives generated electrical power | External load boundary | DIRECT PATENT DISCLOSURE |
| Thickness constraint | Thin illuminated region | Minority-carrier diffusion before recombination | Semiconductor geometry | Minority-carrier diffusion length | Keeps illuminated region thinner than minority-carrier diffusion length | Geometry-to-carrier-collection constraint | DIRECT PATENT DISCLOSURE |
| Alternate Fig. 2 embodiment | Reversed illuminated polarity | Same junction physics with opposite illuminated layer orientation | Optical surface + junction | Photon flux / carrier generation | Allows n-type region to be the illuminated thin layer | Alternative source-disclosed geometry | DIRECT PATENT DISCLOSURE |

## Source-disclosed physical chain

[
oxed{
	ext{PHOTON FLUX}
ightarrow
	ext{AlSb ABSORPTION}
ightarrow
	ext{MINORITY-CARRIER GENERATION / TRANSPORT}
ightarrow
	ext{p-n JUNCTION SEPARATION}
ightarrow
	ext{OHMIC CONTACT EXTRACTION}
ightarrow
	ext{LOAD CURRENT}
}
]

The patent's important physical constraint is that the illuminated semiconductor portion be thinner than the minority-carrier diffusion length so photogenerated minority carriers can reach the junction before recombination.

## Source-authority boundary

The patent supplies:
- AlSb as the semiconductor material;
- p-type and n-type regions;
- p-n junction operation;
- illuminated thin-region geometry;
- anti-reflection coating;
- ohmic collection contacts;
- external load connection.

It does **not** supply:
- DUAL MODAL™ RC cells;
- (Z_k) evidence tuples;
- telemetry or digital supervisory control;
- Human-in-Command governance;
- NExUS partitioning;
- N-TRANSFORMER™ identity.

The appropriate lineage relation is:

[
	ext{OPTICAL ENERGY}
ightarrow
	ext{SEMICONDUCTOR PHYSICAL STATE}
ightarrow
	ext{CHARGE SEPARATION}
ightarrow
	ext{ELECTRICAL OUTPUT}
]

Any later DUAL MODAL™ or N-TRANSFORMER™ mapping must remain a downstream architectural layer.
