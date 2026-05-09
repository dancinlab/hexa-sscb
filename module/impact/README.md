## §21 IMPACT per Mk (what changes — three tiers, per version)

> Every Mk uses a strict 3-tier structure: ① what changes immediately (demonstration) / ② derived effects (causal) / ③ what does not change (candid).
> Every mkN except mk1 must link the previous-version document (GitHub blob / compare URL).

### §21.mk5 — Mk.V GaN complement + AI (v1.0, 2030-06-01, PLANNED)

<details open>
<summary>📎 <a href="https://github.com/n6-arch/canon/compare/sscb-mk4-v1.0...sscb-mk5-v1.0">mk4 → mk5 diff</a> · <a href="https://github.com/n6-arch/canon/blob/sscb-mk4-v1.0/domains/compute/sscb/sscb.md">prev mk4 blob</a> · PLANNED · 2030-06-01</summary>

📎 **Previous version**: [mk4 (sscb-mk4-v1.0)](https://github.com/n6-arch/canon/blob/sscb-mk4-v1.0/domains/compute/sscb/sscb.md)
📎 **git diff**: [mk4 → mk5](https://github.com/n6-arch/canon/compare/sscb-mk4-v1.0...sscb-mk5-v1.0)
📎 **status**: PLANNED

#### ① What changes immediately (vs mk4, planned)

| Axis | mk4 | mk5 planned |
|---|---|---|
| Voltage / current | 1500 V / 500 A | **3000 V / 1000 A** |
| Cutoff time | 300 ns | **200 ns** (≈ n×33) |
| Topology | SiC 4-die parallel | **SiC + GaN HEMT complement** (ultra-fast turnoff) |
| Intelligence | simple overcurrent trip | **AI pre-fault prediction** (anomaly-pattern detection) |

#### ② Derived effects (mk5 → Mk-∞)

```
mk5 GaN complement + AI -> domestic HVDC long-distance transmission breaker
                       -> TinyML on-die standardization (Samsung 40 nm NPU)
                       -> Mk-∞ singularity (EDiP embedding + 4Q single die)
```

#### ③ What does not change (candid)

- ✗ mk5 still a discrete SiP (EDiP embedding is Mk-∞)
- ✗ BOM $300 — not mass market (industrial only)
- ✗ TinyML false-positive risk — human oversight required

</details>

### §21.mk4 — Mk.IV 100 % domestic sourcing (v1.0, 2029-06-01, PLANNED)

<details>
<summary>📎 <a href="https://github.com/n6-arch/canon/compare/sscb-mk3-v1.0...sscb-mk4-v1.0">mk3 → mk4 diff</a> · <a href="https://github.com/n6-arch/canon/blob/sscb-mk3-v1.0/domains/compute/sscb/sscb.md">prev mk3 blob</a> · PLANNED · 2029-06-01</summary>

📎 **Previous version**: [mk3 (sscb-mk3-v1.0)](https://github.com/n6-arch/canon/blob/sscb-mk3-v1.0/domains/compute/sscb/sscb.md)
📎 **git diff**: [mk3 → mk4](https://github.com/n6-arch/canon/compare/sscb-mk3-v1.0...sscb-mk4-v1.0)
📎 **status**: PLANNED

#### ① What changes immediately (vs mk3, planned)

| Axis | mk3 | mk4 planned |
|---|---|---|
| Voltage / current | 800 V / 300 A | **1500 V / 500 A** |
| Cutoff time | 400 ns | **300 ns** |
| SiC domestic sourcing | partial (matched binning) | **100 % domestic** (YesPower open MPW matured) |
| Market | data center | **industrial / solar DC string** |

#### ② Derived effects (mk4 → mk5)

```
mk4 1500 V -> KEPCO transmission-distribution pilot
           -> solar inverter power-disconnect standardization
           -> GaN HEMT complement integration prep -> mk5
```

#### ③ What does not change (candid)

- ✗ mk4 unit cost $150 — premium over mechanical
- ✗ above 3000 V still Wolfspeed/Infineon exclusive
- ✗ no AI predictive trip yet (mk5)

</details>

### §21.mk3 — Mk.III HVDC data center (v1.0, 2028-06-01, PLANNED)

<details>
<summary>📎 <a href="https://github.com/n6-arch/canon/compare/sscb-mk2-v1.0...sscb-mk3-v1.0">mk2 → mk3 diff</a> · <a href="https://github.com/n6-arch/canon/blob/sscb-mk2-v1.0/domains/compute/sscb/sscb.md">prev mk2 blob</a> · PLANNED · 2028-06-01</summary>

📎 **Previous version**: [mk2 (sscb-mk2-v1.0)](https://github.com/n6-arch/canon/blob/sscb-mk2-v1.0/domains/compute/sscb/sscb.md)
📎 **git diff**: [mk2 → mk3](https://github.com/n6-arch/canon/compare/sscb-mk2-v1.0...sscb-mk3-v1.0)
📎 **status**: PLANNED

#### ① What changes immediately (vs mk2, planned)

| Axis | mk2 | mk3 planned |
|---|---|---|
| Voltage / current | 400 V / 200 A | **800 V HVDC / 300 A** |
| Cutoff time | 500 ns | **400 ns** |
| Wafer | 6-inch SiC | **8-inch SiC** transition |
| Bonding | Cu clip | confirmed (lifetime ×3) |

#### ② Derived effects (mk3 → mk4)

```
mk3 800 V -> AI-server-rack direct HVDC market entry
          -> YesPower 8-inch SiC line maturing
          -> foundation for mk4 1500 V full-domestic
```

#### ③ What does not change (candid)

- ✗ solar-string 1500 V not yet reached
- ✗ not yet in transmission-distribution tens-of-kV range
- ✗ no GaN complement yet (awaiting mk5)

</details>

### §21.mk2 — Mk.II (v1.0, 2027-06-01, PLANNED)

<details>
<summary>📎 <a href="https://github.com/n6-arch/canon/compare/sscb-mk1-v1.0...sscb-mk2-v1.0">mk1 → mk2 diff</a> · <a href="https://github.com/n6-arch/canon/blob/sscb-mk1-v1.0/domains/compute/sscb/sscb.md">prev mk1 blob</a> · PLANNED · 2027-06-01</summary>

📎 **Previous version**: [mk1 (sscb-mk1-v1.0)](https://github.com/n6-arch/canon/blob/sscb-mk1-v1.0/domains/compute/sscb/sscb.md)
📎 **git diff**: [mk1 → mk2](https://github.com/n6-arch/canon/compare/sscb-mk1-v1.0...sscb-mk2-v1.0)
📎 **status**: PLANNED (tag unreleased)

#### ① What changes immediately (vs mk1, planned)

| Axis | mk1 | mk2 planned |
|---|---|---|
| Voltage / current | 48 V unidirectional / 100 A | **400 V bidirectional / 200 A** (8× power) |
| Cutoff time | 600 ns | **500 ns** (1.2×) |
| Reclose | manual | **auto-reclose** (firmware auto-reclose) |
| Bonding | Al wedge | **Cu clip** (lifetime ×3) |

#### ② Derived effects (mk2 → mk3)

```
mk2 bidirectional -> enters data-center 48 V -> 400 V HVDC transition
                  -> EV onboard breaker PoC
                  -> Cu clip process established -> mk3 HVDC 800 V foundation
```

#### ③ What does not change (candid)

- ✗ single-phase AC market still mechanical
- ✗ not yet at HVDC beyond 1500 V (awaits mk4)
- ✗ no > 5 kA short-circuit capacity (mk3 extension)

</details>

### §21.mk1 — what changes (v1.0, 2026-04-18)

<details>
<summary>📎 <a href="https://github.com/n6-arch/canon/releases/tag/sscb-mk1-v1.0">sscb-mk1-v1.0 release</a> · <a href="https://github.com/n6-arch/canon/blob/sscb-mk1-v1.0/domains/compute/sscb/sscb.md">mk1 blob</a> · RELEASED · 2026-04-18</summary>

📎 **git tag**: `sscb-mk1-v1.0`
📎 **release**: [sscb-mk1-v1.0 release](https://github.com/n6-arch/canon/releases/tag/sscb-mk1-v1.0)
📎 **First version** — no prior version (prev_link not required).

#### ① What changes immediately (demonstration, vs existing market)

| Axis | Existing | after mk1 |
|---|---|---|
| 48 V DC breaker | Wolfspeed $80–150 (US-dependent) | **domestic $32** (4× cheaper) + 100 % domestic supply chain |
| Cutoff speed | mechanical 10–50 ms, I²t=250 kJ @ 5 kA | **600 ns** (16,000× faster), I²t=15 J |
| YesPower utilization | low MPW | first customer for regular custom runs |
| 4-fab MPW cooperation | each in isolation | first simultaneous kick-off demonstration |

#### ② Derived effects (mk1 → Mk-∞ two-stage rocket)

```
mk1 ships -> YesPower gains conviction -> opens custom mask line (🛸10 promotion)
          -> Samsung 40 nm NPU-MCU channel secured -> TinyML on-die
          -> AT&S EDiP shipbuilding-semiconductor fusion -> 1500 V DC breaker
          = data-center / EV HVDC · domestic-defense DC distribution
```

#### ③ What does not change (candid)

- ✗ residential AC distribution-panel breaker market (unchanged)
- ✗ not a Wolfspeed replacement (large / high-voltage still overseas)
- ✗ not price-competitive ($32 > mechanical contactor $5–10)
- ✗ mk1 alone does not change the energy paradigm

**Key point**: mk1 is not a technical breakthrough; it is an **ecosystem-connection demonstration**. Its value is that fabs, investors, and the government see "this works" with their own eyes — and at that moment the path toward Mk-∞ opens.

</details>

## §22 Reduction to two practical questions

The full mk1–mk5 roadmap reduces to the following two questions.

### Question 1: will YesPower open a custom line?

→ **mk1 1 k-unit order is the answer.** By 2026 Q4, ship 100 EA prototypes and request a regular custom run.
   Once YesPower recognizes this customer as "regular", they open the line. Capacity secured from mk2 onward.

### Question 2: when the government / Hyundai / Hanwha ask "do you have a domestic DC breaker?", can you answer "yes"?

→ **mk1 certification (UL 489B + KC) is the answer.** Certifications obtained by the end of 2026 Q4.
   The evidence of "yes" is at least 1 k mk1 units procured, the certificates, and a field-test report.

The **12-month playbook** that answers both questions is the §8–§20 engineering package. mk1 alone does not
change the paradigm, but once both questions are answered the path to Mk-∞ opens.

---

*End of document. 22 sections total. §1–§7 brief + §8–§20 engineering + §21–§22 impact.
 canonical paper — single-.md unified convention (@paper preset=canonical_full).*
