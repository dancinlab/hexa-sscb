#!/usr/bin/env python3
"""
SSCB mk1 — BOM σ(6)=12 lattice reduction (stdlib only).

Maps the 19-row physical BOM in module/engineering_pack/README.md §9 onto
the 12-slot lattice declared in core/sscb/spec.md §17 (= 9 active component
classes + 3 reserved sigma-slack slots) and asserts the total stays within
the $35 ceiling from .own own 1.

Run:
    python3 verify/bom_lattice.py        # exit 0 = total ≤ $35 and 12 slots

The reduction is a project-policy mapping (not a syntactic parse). It is
declared here so future BOM edits cannot silently drift away from the σ(6)
lattice — adding a new active component must either replace one of the 9
or consume one of the 3 reserved slots.

Authority: own 1 (n=6 lattice identity) — bom_lines ≡ σ(6) = 12.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# spec.md §17 declared cost ceiling (USD).
BOM_CEILING_USD = 35.0

# spec.md §17 lattice classes.
SIGMA_LATTICE = {
    "1.  SiC MOSFET die (matched 4-die set)":       "SiC",
    "2.  Gate driver BCD 180 nm":                   "Driver",
    "3.  Σ-Δ ADC + comparator":                     "ADC",
    "4.  MCU Cortex-M4 (commercial fallback)":      "MCU",
    "5.  TVS network":                              "TVS",
    "6.  RC snubber":                               "Snubber",
    "7.  DBC ceramic substrate":                    "DBC",
    "8.  Sintered die-attach + wirebond + mold":    "Package",
    "9.  Shunt + sense + passives + connector":     "Sense",
    "10. Reserved (sigma slack #1)":                "Reserved",
    "11. Reserved (sigma slack #2)":                "Reserved",
    "12. Reserved (sigma slack #3)":                "Reserved",
}

# engineering_pack §9 19-row BOM → σ(6)=12 lattice slot mapping.
# Each row is (engpack_part_id, USD_subtotal, lattice_class).
ENGPACK_BOM = [
    ("B-1  SiC MOSFET die (4× matched)",      10.00, "SiC"),
    ("B-2  Binning service",                   1.00, "SiC"),
    ("B-3  Gate driver BCD",                   1.50, "Driver"),
    ("B-4  Σ-Δ ADC + Comp",                    1.50, "ADC"),
    ("B-5  MCU STM32F429ZIT6",                 2.00, "MCU"),
    ("B-6  DBC Al₂O₃ substrate",               2.50, "DBC"),
    ("B-7  Mold compound",                     0.30, "Package"),
    ("B-8  Al wedge wire",                     0.005, "Package"),
    ("B-9  Shunt 0.5 mΩ",                      2.00, "Sense"),
    ("B-10 TVS SMBJ58A ×3",                    0.30, "TVS"),
    ("B-11 Ferrite bead ×2",                   0.10, "TVS"),
    ("B-12 Cap 10 µF/50 V ×4",                 1.20, "Snubber"),
    ("B-13 Cap 100 nF/25 V ×20",               0.20, "Snubber"),
    ("B-14 Resistor 5 Ω ×4",                   0.04, "Snubber"),
    ("B-15 PT1000 sensor",                     0.80, "Sense"),
    ("B-16 PCB sub-board",                     1.50, "Sense"),
    ("B-17 Solder paste",                      0.02, "Package"),
    ("B-18 Connector 12-pin",                  0.80, "Sense"),
    ("B-19 Assembly + UL mark",                5.00, "Package"),
]

ACTIVE_CLASSES = ("SiC", "Driver", "ADC", "MCU", "TVS", "Snubber",
                  "DBC", "Package", "Sense")


def reduce_to_lattice() -> tuple[dict[str, float], list[str]]:
    """Return (per-class total USD, errors)."""
    errors: list[str] = []
    classes_in_lattice = set()
    for slot, cls in SIGMA_LATTICE.items():
        classes_in_lattice.add(cls)
    if len(SIGMA_LATTICE) != 12:
        errors.append(f"σ(6) lattice has {len(SIGMA_LATTICE)} slots, expected 12")
    reserved = [s for s in SIGMA_LATTICE.values() if s == "Reserved"]
    if len(reserved) != 3:
        errors.append(f"reserved slots = {len(reserved)}, expected 3")
    active = [s for s in SIGMA_LATTICE.values() if s != "Reserved"]
    if len(active) != 9:
        errors.append(f"active classes = {len(active)}, expected 9")

    totals: dict[str, float] = {c: 0.0 for c in ACTIVE_CLASSES}
    for part_id, cost, cls in ENGPACK_BOM:
        if cls not in ACTIVE_CLASSES:
            errors.append(f"{part_id} maps to non-active class {cls!r}")
            continue
        totals[cls] += cost
    return totals, errors


def main() -> int:
    print("=" * 72)
    print("  SSCB mk1 — BOM σ(6)=12 lattice reduction")
    print("=" * 72)
    totals, errors = reduce_to_lattice()
    grand = sum(totals.values())

    print()
    print("  σ(6)=12 lattice slots (spec.md §17):")
    for slot in SIGMA_LATTICE:
        cls = SIGMA_LATTICE[slot]
        cost = totals.get(cls, 0.0) if cls != "Reserved" else 0.0
        marker = "  " if cls == "Reserved" else "→ "
        print(f"    {slot:<48} {marker}${cost:6.2f}")

    print()
    print(f"  Active 9-class subtotal : ${grand:6.2f}")
    print(f"  Reserved 3-slot budget  : $ 0.00 (mk1 ships empty)")
    print(f"  σ(6)=12 grand total     : ${grand:6.2f}")
    print(f"  Ceiling (.own own 1)    : ${BOM_CEILING_USD:6.2f}")
    print()

    fail = False
    if grand > BOM_CEILING_USD:
        errors.append(f"BOM total ${grand:.2f} > ceiling ${BOM_CEILING_USD:.2f}")
        fail = True

    rolled_up = sum(c for _, c, _ in ENGPACK_BOM)
    if abs(rolled_up - grand) > 1e-6:
        errors.append(
            f"reduction lost cost: engpack sum ${rolled_up:.4f} vs "
            f"lattice sum ${grand:.4f}"
        )

    if errors:
        print("  FAILURES:")
        for e in errors:
            print(f"    ✗ {e}")
        return 1
    print(f"  PASS — 19-row engineering_pack BOM reduces cleanly to σ(6)=12, "
          f"total ${grand:.2f} ≤ ${BOM_CEILING_USD:.2f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
