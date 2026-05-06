# hexa-sscb — AI-native handoff

> Conformance: hive raw 271 (readme-ai-native-mandate). This file is the
> canonical entry point for AI agents (Claude / Hexa / etc.) operating
> on this repository. Human entry point is [`README.md`](README.md).

## Identity

- **Name**: `hexa-sscb` (Solid-State Circuit Breaker, HEXA-SSCB mk1)
- **Axis**: `compute`
- **n=6 lattice**:
  - cutoff_ns ≡ 6 × 100 ns = 600 ns
  - foundry_count ≡ τ(6) = 4
  - bom_lines ≡ σ(6) = 12
  - redundancy_depth ≡ φ(6) + τ(6) = 6
- **Parent (canonical SSOT)**: `n6-architecture/domains/compute/sscb/sscb.md`
- **Distribution**: `https://github.com/need-singularity/hexa-sscb` (public)

## Hierarchy (canonical pattern)

```
hexa-sscb/                   T0 (repo root)
├── core/sscb/               T1 (single-feature core)
│   ├── spec.md              ← paper (canonical short form)
│   └── domain.md            ← full domain spec (canonical long form)
├── module/                  T2 (per-module fan-out)
│   ├── engineering_pack/    ← build package (BOM / PCB / FW / test)
│   ├── impact/              ← Mk-ladder IMPACT (§21 + §22)
│   └── firmware/            ← STM32F4 reference (CMSIS-only)
├── verify/                  T0 (runnable invariant audit, stdlib Python)
├── build/                   T0 (pandoc PDF rebuild)
├── tests/                   T0 (pytest acceptance scaffold)
├── .own                     T0 (project-local SSOT, mk2 own_v1 — invariants + roles + directives)
└── doc/                     T0 (human-only archive + lineage)
```

Imports flow **T0 → T1 → T2** only. T2 modules MUST NOT import sibling T2
modules; cross-module references go through T1 (`core/sscb/`).

## Invariants (must not violate when editing)

1. **n=6 identity holds**: any change touching cutoff_ns / foundry_count /
   bom_lines / redundancy_depth must restate the 6-lattice equality.
2. **Falsifiability preserved**: every numeric claim in `core/sscb/spec.md`
   and `module/engineering_pack/README.md` must remain bench-falsifiable. Do
   not introduce derived numbers without showing the derivation.
3. **Korean-foundry-stack invariant**: BOM allocation across the four
   Korean foundries (SiC / BCD 180nm / Σ-Δ / Cortex-M4) is contractual. Do
   not silently substitute a Western foundry into the BOM.
4. **Mk-ladder monotonicity**: in `module/impact/README.md`, the Mk.I → Mk.V
   ladder must remain monotone in capability and in date. Do not insert a
   Mk.X regression below an existing Mk.

## Edit policy

- **Additive-only** at the doc layer. Do not rename, move, or delete files
  in `core/` / `module/` without updating `doc/lineage/origin.md` and adding
  a redirect note.
- **English primary** in commit messages and new prose; Korean predecessor
  in `doc/archive/` is preserved verbatim and not retranslated in place.
- Architectural changes (adding a new module, splitting `core/sscb/`) require
  updating this file's hierarchy diagram **before** the implementing PR.

## Common agent tasks

| Task | Where to look first |
|---|---|
| Add a new Mk variant | `module/impact/README.md` (then propagate to `core/sscb/domain.md` §21) |
| Tighten a cutoff-time number | `core/sscb/spec.md` §2 + `module/engineering_pack/README.md` §1 |
| Adjust BOM | `module/engineering_pack/README.md` §9, then verify σ(6)=12 still holds via `verify/bom_lattice.py` |
| Change firmware logic | `module/engineering_pack/README.md` §13, then mirror in `module/firmware/src/fault_handler.c` |
| Add acceptance test | `module/engineering_pack/README.md` §11 ACCEPTANCE, then add a `tests/test_acceptance.py` case |
| Run invariant check | `python3 verify/sscb_verify.py && python3 verify/cross_doc_audit.py` (exit 0 required) |
| Rebuild lost PDFs | `make -C build all` (regenerates 3 KakaoTalk-shared PDFs from .md) |
| Cross-compile firmware | `make -C module/firmware all` (host-only; target run requires STM32F429 + scope) |

## Lineage tag

This repo was extracted from `n6-architecture` on 2026-05-06.
Source commits: see [`doc/lineage/origin.md`](doc/lineage/origin.md).

The Korean-language predecessor and a 2026-05-04 paper backup are preserved
verbatim under `doc/archive/` for forensic continuity.
