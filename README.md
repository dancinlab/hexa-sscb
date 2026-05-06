# hexa-sscb — Solid-State Circuit Breaker (HEXA-SSCB mk1)

> 600 ns DC fault interruption for 48 V / 100 A buses. SiC MOSFET + BCD 180 nm
> + Σ-Δ ADC + Cortex-M4, packaged as a 4-foundry SiP. **n=6 master identity**
> governs cutoff time (6×100 ns), foundry count (τ(6)=4), and BOM lattice
> (σ(6)=12) — every design knob answers to that arithmetic.
>
> **Status (2026-05-06):** mk1 design package frozen — paper + engineering
> pack + impact ladder (Mk.I → Mk.V). Silicon tape-out PLANNED.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Spec: mk1](https://img.shields.io/badge/spec-mk1-informational.svg)](core/sscb/spec.md)
[![Cutoff: 600 ns](https://img.shields.io/badge/cutoff-600ns-brightgreen.svg)](core/sscb/spec.md)
[![Foundries: 4](https://img.shields.io/badge/foundries-4_KR-blue.svg)](module/engineering_pack/README.md)
[![BOM: $35](https://img.shields.io/badge/BOM-%2435-yellow.svg)](module/engineering_pack/README.md)

> **Distribution**: GitHub canonical at <https://github.com/need-singularity/hexa-sscb>.
> Origin: extracted from `n6-architecture/domains/compute/sscb/` 2026-05-06.

---

## What is hexa-sscb?

`hexa-sscb` is a **solid-state DC circuit breaker** that interrupts a 48 V / 100 A
bus fault in **600 ns** — roughly 48,000× faster than a 30 ms electromechanical
breaker, with no contact-arc plasma column, and a Bill-of-Materials that
maps cleanly onto **four Korean foundry deliverables**:

1. **SiC MOSFET die** — main interrupter (Power Cube 7 / DBHi-Tek)
2. **BCD 180 nm gate driver** — DongbuHiTek / SK Key Foundry
3. **Σ-Δ ADC + comparator** — MagnaChip
4. **Cortex-M4 MCU + firmware** — SK Hynix system-IC line

The n=6 lattice is not decorative. It is the **falsification budget**:
- cutoff_ns ≡ 6 × 100 ns
- foundry_count ≡ τ(6) = 4
- bom_lines ≡ σ(6) = 12
- redundancy_depth ≡ φ(6) + τ(6) = 6

Every parameter in [`core/sscb/spec.md`](core/sscb/spec.md) is independently
falsifiable on the test bench (see §11 ACCEPTANCE in the engineering pack).

---

## Repository layout

```
hexa-sscb/
├── README.md                          ← this file (public landing)
├── README.ai.md                       ← AI-native handoff (raw 271)
├── LICENSE                            ← Apache-2.0
├── core/
│   └── sscb/
│       ├── spec.md                    ← inaugural paper (387 lines)
│       ├── domain.md                  ← full domain doc (1320 lines, §1–§22)
│       └── doc/                       ← per-feature deep dives
├── module/
│   ├── engineering_pack/
│   │   └── README.md                  ← 754-line build package (BOM/PCB/firmware/test)
│   └── impact/
│       └── README.md                  ← Mk.I → Mk.V impact ladder (§21+§22)
├── .own                              ← project-local SSOT (mk2 own_v1) — invariants + roles + directives
├── verify/                           ← invariant audit (Python stdlib)
├── build/                            ← pandoc PDF rebuild
├── tests/                            ← pytest acceptance scaffold
└── doc/
    ├── archive/                       ← Korean predecessor + paper backup
    └── lineage/                       ← origin manifest + commit refs
```

The `core/<feature>/` + `module/<feature>/` + `README.ai.md` triplet follows
**hive raw.mk2 arch.001** (collapsed from raw 270 / 271 / 272 / 273) — the
canonical core-hierarchy pattern enforced across the n6-architecture sister
repositories.

---

## Module inventory

| Module | What it is | Lines |
|---|---|---|
| [`core/sscb/spec.md`](core/sscb/spec.md) | Inaugural paper — n=6 lattice, COMPARE table, ASCII bars, §1-§22 | 387 |
| [`core/sscb/domain.md`](core/sscb/domain.md) | Full domain doc — exec summary, system reqs, architecture, circuit, PCB, firmware, mechanical, manufacturing, test, BOM, vendor, acceptance, appendix, IMPACT | 1320 |
| [`module/engineering_pack/`](module/engineering_pack/README.md) | Hand-off build package — every number derivable, every claim falsifiable, stdlib-only Python verification appendix | 754 |
| [`module/impact/`](module/impact/README.md) | §21 IMPACT ladder Mk.I → Mk.V (2026 → 2030) + §22 reduction to two practical questions | 200 |
| [`module/firmware/`](module/firmware/README.md) | STM32F4 reference firmware (CMSIS-only, host cross-compile) — engineering_pack §5 / domain.md §13 materialized | code |
| [`verify/`](verify/) | Runnable invariant audit — domain.md §7 11-subsection physics check + cross-document n=6 consistency + BOM σ(6)=12 lattice reduction | code |
| [`build/`](build/) | Pandoc Makefile + xeCJK LaTeX template — rebuilds the three KakaoTalk-shared PDFs from the .md sources | code |
| [`tests/`](tests/) | pytest scaffold for §16 T-1..T-10 + §19 A-1..A-10 acceptance — bench-only items skipped with reason, doc-bench-independent items auto-run | code |

---

## Build & verify

```bash
python3 verify/sscb_verify.py        # 10/10 PASS expected (exit 0)
python3 verify/cross_doc_audit.py    # n=6 consistency across spec/domain/engineering_pack/impact
python3 verify/bom_lattice.py        # σ(6)=12 BOM reconciliation, total ≤ $35
make -C build all                    # rebuild 3 PDFs (requires pandoc + xelatex + CJK font)
make -C module/firmware all          # cross-compile firmware.elf (requires arm-none-eabi-gcc)
pytest tests/ -v                     # acceptance scaffold; bench-only items skip with reason
```

---

## Architecture (one-line)

```
   48V DC bus ─┬─ SiC MOSFET ── load
               │     ▲
       Σ-Δ ADC │     │ gate
       (500kHz)│     │ (BCD 180nm driver)
               │     │
               └─► Cortex-M4 ─── 600 ns IRQ cutoff
                    │
                    └─ firmware = §13 in engineering_pack
```

Six 100 ns slices: **sense (1) · compute (2) · drive (2) · channel collapse (1).**
Each slice is independently bench-falsifiable.

---

## Caveats

- **mk1 is paper-frozen, not silicon-frozen.** Tape-out is PLANNED, not RELEASED.
  Numbers in [`core/sscb/spec.md`](core/sscb/spec.md) are SPICE-derived plus
  vendor datasheet composition; physical bring-up will refine them.
- **Single-direction (DC) only.** Bidirectional cutoff is a **Mk.II** target
  ([`module/impact/README.md`](module/impact/README.md) §21.mk2).
- **Auto re-close is manual on mk1.** Mk.II adds firmware auto-reclosure with
  fault-class discrimination.
- **GaN complement + AI cutoff prediction is Mk.V** (planned 2030-06-01).

---

## Lineage

This repository is a **forensic extraction** from the n6-architecture
monorepo. See [`doc/lineage/origin.md`](doc/lineage/origin.md) for the exact
commits and source paths each file was pulled from. Two of the four source
markdowns were recovered from a deletion commit (`a489a368`, 2026-04-21).

License: Apache-2.0.
