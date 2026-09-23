# US3550002A — SOURCE-AUTHORITY COMMUNICATION / SYNCHRONIZATION BOM

This record separates the physical and signal-processing architecture directly disclosed in US3550002A from any later DUAL MODAL™ synthesis.

## Authority law

`PATENT-DISCLOSED PULSAR SYNCHRONIZATION != DUAL MODAL™ ARCHITECTURAL MAPPING != MODERN CRYPTOGRAPHY`

| Patent Ref. | Asset / Function | Physical / Signal Mechanism | Native Interface | Patent-Disclosed Function | DUAL MODAL™ Interpretation | Authority Tier |
|---|---|---|---|---|---|---|
| 1 / 2 or 10 / 11 | Steerable receiving antennas | Radio-frequency collection from extraterrestrial source | RF feed to receiver | Simultaneously observe selected pulsar at separated sites | Shared external physical-reference aperture | DIRECT PATENT DISCLOSURE |
| 14 / 15 | Receivers | RF reception / downconversion | Antenna input -> electrical signal output | Receive pulsar emissions at remote sites | Reference-signal acquisition | DIRECT PATENT DISCLOSURE |
| 16 / 17 | Amplifiers | Electrical amplification | Receiver output -> control signal | Amplify pulsar timing pulses for oscillator control | Reference conditioning | DIRECT PATENT DISCLOSURE |
| 20 / 21 | Local free-running oscillators | Local periodic electrical oscillation | Control input from pulsar-derived error signal | Maintain local phase/timing coherence against pulsar | Local clock / phase state disciplined by external source | DIRECT PATENT DISCLOSURE |
| 22 | Phase / position processing | Phase comparison and downstream computation | Receiver/oscillator phase data | Processes phase differences to obtain position plot | Correlation / reconstruction stage | DIRECT PATENT DISCLOSURE |
| Pulse counters / multiplying circuits | Clock-rate conversion | Integer pulse-rate multiplication/division | Pulsar pulse input -> local clock pulses | Derive clock signals while retaining source stability | Derived-timebase generation | DIRECT PATENT DISCLOSURE |
| 30 | Transmitting station | Source-side communication node | Message + pulsar reference inputs | Encodes and transmits information using pulsar reference | Reference-bound transmitting node | DIRECT PATENT DISCLOSURE |
| 31 | Tracking antenna | Pulsar RF observation | RF -> mixer/reference chain | Observes selected pulsar at transmitter site | Source-side reference aperture | DIRECT PATENT DISCLOSURE |
| 34 | Message source | Information-signal generation | Electrical/baseband signal | Supplies message S(t) | Information payload | DIRECT PATENT DISCLOSURE |
| 35 | Mixer | Signal combination / modulation | Pulsar f1(t) + message S(t) | Encodes/masks message using pulsar signal | Physical-reference keyed signal combination | DIRECT PATENT DISCLOSURE |
| 36 | Transmitter | RF transmission | Encoded signal input -> RF output | Radiates encoded message | Communications egress | DIRECT PATENT DISCLOSURE |
| 37 | Transmit antenna | Electromagnetic radiation | RF feed | Sends encoded signal toward remote station | RF egress aperture | DIRECT PATENT DISCLOSURE |
| 40 | Receiving station | Remote communication node | Received RF + local pulsar reference | Receives and decodes pulsar-referenced signal | Remote correlation node | DIRECT PATENT DISCLOSURE |
| 41 | Tracking antenna | Independent observation of same pulsar | RF -> local reference chain | Generates local f2(t) reference at receiving site | Independent witness of common physical source | DIRECT PATENT DISCLOSURE |
| 43 | Amplifier | Pulsar-reference amplification | Tracking antenna -> correlation detector | Conditions remote pulsar signal | Local reference conditioning | DIRECT PATENT DISCLOSURE |
| 44 | Correlation detector | Cross-correlation processing | Encoded signal + local pulsar signal | Correlates received waveform with f2(t) to recover message | Cross-site physical-reference correlation | DIRECT PATENT DISCLOSURE |
| 46 | Receive antenna | RF collection of transmitted signal | RF input -> detector chain | Receives encoded terrestrial signal | Communications ingress aperture | DIRECT PATENT DISCLOSURE |
| Delay compensation | Time-delay correction | Compensating signal delay | Reference path before correlator | Corrects finite propagation-time difference between stations | Time-alignment boundary | DIRECT PATENT DISCLOSURE |

## Patent-disclosed synchronization chain

[
	ext{PULSAR}
ightarrow
	ext{RF OBSERVATION}
ightarrow
	ext{RECEIVER / AMPLIFIER}
ightarrow
	ext{LOCAL OSCILLATOR CORRECTION}
ightarrow
	ext{DISTRIBUTED PHASE / TIME COHERENCE}
]

## Patent-disclosed communication chain

[
	ext{MESSAGE }S(t)
+
	ext{PULSAR REFERENCE }f_1(t)
ightarrow
	ext{ENCODED TRANSMISSION}
ightarrow
	ext{REMOTE SIGNAL}
+
	ext{INDEPENDENT PULSAR REFERENCE }f_2(t)
ightarrow
	ext{CORRELATION}
ightarrow
	ext{RECOVERED MESSAGE}
]

## Source-authority boundary

The patent supplies:
- a naturally occurring extraterrestrial reference;
- simultaneous observation by geographically separated nodes;
- local oscillator disciplining;
- interferometric phase coherence;
- local clock derivation;
- pulsar-referenced message encoding;
- independent remote observation of the same source;
- correlation-based recovery;
- propagation-delay compensation.

It does **not** supply:
- DUAL MODAL™ RC cells;
- (Z_k) evidence tuples;
- NExUS motherboard partitioning;
- modern cryptographic authentication;
- Human-in-Command governance;
- current military deployment claims.

The appropriate lineage relation is:

[
oxed{
	ext{EXTERNAL PHYSICAL REFERENCE}
ightarrow
	ext{LOCAL OBSERVATION}
ightarrow
	ext{LOCAL STATE DISCIPLINE}
ightarrow
	ext{CROSS-NODE CORRELATION}
}
]

Any later DUAL MODAL™ mapping must remain a downstream architectural layer.
