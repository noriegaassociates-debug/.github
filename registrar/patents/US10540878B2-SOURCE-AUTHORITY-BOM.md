# US10540878B2 — Source-Authority Hardware BOM

**DUAL MODAL™ · EST. 2022**

## Authority rule

`PATENT-DISCLOSED HARDWARE != DUAL MODAL ARCHITECTURAL SYNTHESIS`

The BOM preserves the patent/family disclosure as upstream authority. RC-10…RC-24 assignments are intentionally marked **PENDING-DUAL-MODAL-MAPPING** unless an existing DUAL MODAL record explicitly assigns the row.

| Patent Figure/Ref. | Hardware / Sensor | Physical mechanism / native interface | Measurand / state | Patent-disclosed function | RC Cell | DUAL MODAL role | Authority tier |
|---|---|---|---|---|---|---|---|
| Fig.2 / 110 | EFAN device 110 | Integrated edge sensing + cable/DBS/TV/radio + POTS/cellular/RF | Multiple physical/environmental parameters | Local collection, processing, threshold/trend evaluation, host feedback | PENDING-DUAL-MODAL-MAPPING | Edge sensing/local decision substrate | DIRECT PATENT DISCLOSURE |
| Fig.3 / 1101 | Receiver/antenna 1101 | RF/broadcast reception | Inbound messages/control | Receives messages/control commands | PENDING-DUAL-MODAL-MAPPING | Inbound communications aperture | DIRECT PATENT DISCLOSURE |
| Fig.3 / 1104 | Sensor devices 1104 | Analog/digital physical sensing; wired/wireless | Radiation, chemicals, smoke, temperature, acceleration, light, pressure, etc. | Local environmental/physical monitoring | PENDING-DUAL-MODAL-MAPPING | Sensor fabric | DIRECT PATENT DISCLOSURE |
| Fig.3 / 1106 | Nonvolatile storage 1106 | Persistent local storage | Sensor history, filters, messages | Accumulation/temporary storage | PENDING-DUAL-MODAL-MAPPING | Local evidence/history store | DIRECT PATENT DISCLOSURE |
| Fig.3 / 1108 | Microprocessor 1108 | Digital processing/control | Sensor data, messages, thresholds | Data-flow control, alert monitoring, header evaluation, storage/forwarding | PENDING-DUAL-MODAL-MAPPING | Local processing/threshold logic | DIRECT PATENT DISCLOSURE |
| Fig.2-5 / 115 | Backchannel 115 | POTS/cellular/RF | Processed sensor data, ACKs | Return path to host | PENDING-DUAL-MODAL-MAPPING | Remote feedback path | DIRECT PATENT DISCLOSURE |
| Fig.4 / 202 | Front-end receiver 202 | RF-to-digital conversion | Broadcast signal | Converts cable/DBS signal to bitstream | PENDING-DUAL-MODAL-MAPPING | Acquisition/conversion | DIRECT PATENT DISCLOSURE |
| Fig.4-5 / 210 | NWR receiver 210 | 162-MHz NWR RF reception | Emergency broadcast | Redundant emergency-alert source | PENDING-DUAL-MODAL-MAPPING | Redundant alert channel | DIRECT PATENT DISCLOSURE |
| Fig.5 / 225 | GPS receiver 225 | Satellite positioning | Device position | Location filtering and host position reporting | PENDING-DUAL-MODAL-MAPPING | Geospatial identity support | DIRECT PATENT DISCLOSURE |
| Fig.6 / 319 | Secure microprocessor 319 | Protected processing | Protected descrambling/control state | Secure processing support | PENDING-DUAL-MODAL-MAPPING | Secure processing boundary | DIRECT PATENT DISCLOSURE |
| Fig.6 / 324 | Power source / UPS 324 | Power conversion + backup | Supply state | Resilient device power | PENDING-DUAL-MODAL-MAPPING | Power resilience | DIRECT PATENT DISCLOSURE |
| Fig.6 / 325 | ROM 325 | Read-only memory | Fixed data/programs | Fixed program/data storage | PENDING-DUAL-MODAL-MAPPING | Reference logic store | DIRECT PATENT DISCLOSURE |
| Fig.6 / 326 | FLASH 326 | Reprogrammable NVM | Firmware/data | Operator-updatable storage | PENDING-DUAL-MODAL-MAPPING | Mutable firmware/config store | DIRECT PATENT DISCLOSURE |
| Fig.6 / 327 | NVRAM 327 | Persistent writable memory | Settings/state | Retains settings across power cycles | PENDING-DUAL-MODAL-MAPPING | Persistent state | DIRECT PATENT DISCLOSURE |
| Fig.6 / 328 | RAM 328 | Volatile memory | Runtime data | Temporary application/system storage | PENDING-DUAL-MODAL-MAPPING | Runtime state | DIRECT PATENT DISCLOSURE |
| Fig.6 / 329 | CPU 329 | General digital processing | System data | Primary STB processor | PENDING-DUAL-MODAL-MAPPING | Host processor substrate | DIRECT PATENT DISCLOSURE |
| Fig.6 / 331 | Hard drive 331 | Long-term storage | Audio/video/data/history | Long-term local storage | PENDING-DUAL-MODAL-MAPPING | Long-duration evidence/data | DIRECT PATENT DISCLOSURE |
| Fig.6 / 333 | Internal sensor array 333 | Multi-sensor array | Multiple environmental states | Internal multi-parameter sensing | PENDING-DUAL-MODAL-MAPPING | Multi-sensor fabric | DIRECT PATENT DISCLOSURE |
| Fig.6 / 335 | Fan-driven sampling system 335 | Forced-air sample transport | Airborne signatures | Exposes sensor array to sample stream | PENDING-DUAL-MODAL-MAPPING | Environmental sample acquisition | DIRECT PATENT DISCLOSURE |
| Fig.6 / 340 | I/O ports 340 | Electrical/digital I/O | External sensor/device signals | Expansion attachment points | PENDING-DUAL-MODAL-MAPPING | Expansion interface | DIRECT PATENT DISCLOSURE |
| Fig.6 / 350 | Interfaces 350 | Wired/wireless protocols | External sensor/device data | Remote/surface-mounted sensor connectivity | PENDING-DUAL-MODAL-MAPPING | Interface boundary | DIRECT PATENT DISCLOSURE |
| Patent narrative | Figaro SnO₂ chemiresistors | Heated metal-oxide resistance change | Gas/VOC concentration | Chemical/gas sensing | PENDING-DUAL-MODAL-MAPPING | Chemical sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Cyranose 320 array | Polymer-composite resistance pattern | Vapor mixture / smellprint | Multi-vapor signature detection | PENDING-DUAL-MODAL-MAPPING | Chemical-pattern sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Sandia chemiresistors | Chemically selective resistance change | Chemical/vapor analytes | Chemical signature detection | PENDING-DUAL-MODAL-MAPPING | Chemical sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | GaAs SAW sensors | Surface-acoustic-wave perturbation | Adsorbed mass / vapor analyte | Chemical sensing via acoustic response | PENDING-DUAL-MODAL-MAPPING | Acoustic chemical sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Silicon FPW devices | Flexural plate-wave perturbation | Chemical/biological mass loading | Sensitive mass/analyte detection | PENDING-DUAL-MODAL-MAPPING | Acoustic/mass sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | ORNL cantilever biochips | Micromechanical deflection/resonance | Bio/chemical binding | Bio/chemical detection | PENDING-DUAL-MODAL-MAPPING | Micromechanical biosensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Liquid-crystal biosensors | Optical/orientational response | Biological/chemical analytes | Biohazard/analyte indication | PENDING-DUAL-MODAL-MAPPING | Optical biosensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | PNNL scintillating fibers | Radiation-to-light conversion | Neutron/radiation flux | Radiation sensing | PENDING-DUAL-MODAL-MAPPING | Radiation sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Sandia/NMRC RadFETs | Radiation-induced threshold shift | Dose / coarse spectrum | Radiation dosimetry | PENDING-DUAL-MODAL-MAPPING | Dosimetry | DIRECT PATENT DISCLOSURE |
| Patent narrative | LLNL Ge spectroscopy | Energy-resolved Ge detection | Radiation energy signature | Isotope/element identification | PENDING-DUAL-MODAL-MAPPING | Radiation spectroscopy | DIRECT PATENT DISCLOSURE |
| Patent narrative | SINTEF 387-strip silicon microstrip | Charge pulses in silicon strips | Particle strike / position | Low-level radiation + strike localization | PENDING-DUAL-MODAL-MAPPING | Spatial radiation sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Sandia COMRAD CdZnTe | Semiconductor pulse-height spectroscopy | Gamma/radiation energy | Radiation spectral discrimination | PENDING-DUAL-MODAL-MAPPING | Solid-state spectroscopy | DIRECT PATENT DISCLOSURE |
| Patent narrative | Amorphous-silicon neutron/dose sensors | Radiation-induced charge | Neutron / dose | Radiation monitoring | PENDING-DUAL-MODAL-MAPPING | Radiation sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Entran / TI acceleration sensors | Inertial acceleration transduction | Acceleration/shock | Explosion/earthquake/impact detection | PENDING-DUAL-MODAL-MAPPING | Inertial sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Platinum RTDs | Temperature-dependent resistance | Temperature | Local thermal measurement | PENDING-DUAL-MODAL-MAPPING | Thermal sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Infrared pyrometers | Thermal-radiation sensing | Non-contact temperature | Remote thermal measurement | PENDING-DUAL-MODAL-MAPPING | Non-contact thermal sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | Micromachined silicon pressure sensors | MEMS pressure transduction | Pressure/barometric pressure | Pressure measurement | PENDING-DUAL-MODAL-MAPPING | Pressure sensing | DIRECT PATENT DISCLOSURE |
| Patent narrative | AlN/SiC/GaN/InGaN UV emitters/detectors | Wide-bandgap optoelectronics | UV optical state | UV emission/detection | PENDING-DUAL-MODAL-MAPPING | UV optical sensing | DIRECT PATENT DISCLOSURE |
| Fig.8 / logic | Local threshold + historical trend logic | Local digital comparison/trend processing | Magnitude/rate-of-change/threshold | Local decision before escalation | PENDING-DUAL-MODAL-MAPPING | Evidence screening | DIRECT PATENT DISCLOSURE |
| Patent narrative | Multi-sensor fusion / covariance | Cross-sensor relationship processing | Related measurements | Trend, relationship, threshold comparison | PENDING-DUAL-MODAL-MAPPING | Sensor fusion | DIRECT PATENT DISCLOSURE |
| Fig.8 / alert | Local speaker alert | Electroacoustic actuation | Alert state | Local warning before upstream escalation | PENDING-DUAL-MODAL-MAPPING | Local fail-fast notification | DIRECT PATENT DISCLOSURE |
| Fig.8 / host | Host feedback / neighboring-device polling | Remote query/correlation loop | Regional sensor context | Analyze event, request data, poll nearby nodes, support human intervention | PENDING-DUAL-MODAL-MAPPING | Remote corroboration | DIRECT PATENT DISCLOSURE |
| Security narrative | GPS / ID / time cross-reference | Message-header provenance cross-check | Identity/location/time | Transmission validation / anti-unauthorized-access support | PENDING-DUAL-MODAL-MAPPING | Provenance support | DIRECT PATENT DISCLOSURE |
| Communications narrative | ACK / fallback paths | Acknowledgment + POTS/cellular/RF alternatives | Delivery/communications state | Delivery assurance and alternate return paths | PENDING-DUAL-MODAL-MAPPING | Communications resilience | DIRECT PATENT DISCLOSURE |

## Downstream-only DUAL MODAL elements

| Element | Authority |
|---|---|
| RC-10…RC-24 assignment | DUAL MODAL architectural mapping |
| Z_k evidence tuple | DUAL MODAL architectural formalization |
| NExUS motherboard partition | DUAL MODAL / NExUS synthesis |
| Dual-engine isolation / arbiter | DUAL MODAL / NExUS synthesis |

## Governing chain

`PHYSICAL PARAMETER -> SENSOR -> LOCAL PROCESSING -> THRESHOLD/TREND/CORRELATION -> LOCAL ALERT -> HOST FEEDBACK`

The patent source establishes the substrate. DUAL MODAL may map, formalize, partition, and govern that substrate, but does not retroactively become the source authority for the disclosed hardware.
