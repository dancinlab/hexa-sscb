#!/usr/bin/env python3
"""
SSCB mk1 — §7 operability verification (11 subsections, stdlib only).

Source-of-truth: core/sscb/domain.md §7 (lines 258-481). This file is a
verbatim extraction of the inline Python block in §7, with an added exit-code
contract: returns 0 iff all 10 quantitative tests PASS, 1 otherwise.

Verifies the SSCB mk1 hardware against physical law, process reality, and
economic budget. The n=6 lattice is design motivation (§4-§6) only — this
script does not re-confirm n=6, it asks whether the specific BOM/PCB/firmware
proposed in domain.md actually closes its physical and budget constraints.

Run:
    python3 verify/sscb_verify.py        # exit 0 = 10/10 PASS

Authority: own 1 (hexa-sscb-n6-master-identity) — the four lattice identifiers
this verifier checks (cutoff_ns / die count / BOM line count / IRQ depth) are
declared in .own and must match domain.md. If a number drifts in either, fix
domain.md first, then mirror here.
"""
from math import log, exp, pi
import sys

# === Design inputs ======================
V_BUS        = 48.0         # V   bus voltage
I_NOM        = 100.0        # A   continuous current
I_SC         = 5_000.0      # A   short-circuit target
T_OFF_BUDGET = 600e-9       # s   total cutoff budget
T_AMB        = 70.0         # °C
TJ_MAX       = 175.0        # °C
N_CYCLES_REQ = 100_000
BOM_BUDGET   = 35.0         # USD
SCHED_BUDGET_MO = 12

# === SiC MOSFET (YesPower planar 150mm MPW) ==
N_DIES       = 4
RDSON_25C    = 0.030        # Ω
RDSON_TC     = 1.5
QG           = 80e-9        # C
QGD          = 25e-9        # C
VGS_ON       = 15.0         # V
VPLATEAU     = 5.0          # V
RDS_SPREAD   = 0.10
I2T_RATING   = 100.0
VDS_RATING   = 1200.0

# === Driver / MCU / ADC ================
RG_EXT       = 5.0          # Ω
T_DRV_PROP   = 30e-9        # s
T_COMP_PROP  = 50e-9        # s
F_MCU        = 120e6        # Hz
N_IRQ_CYC    = 16
F_ADC        = 100e6        # Hz
OSR_ADC      = 100

# === Package / thermal =================
RTH_JC       = 0.30         # K/W
RTH_CA       = 0.40         # K/W
L_STRAY      = 15e-9        # H

# === SiC gate TDDB (Weibull) ===========
WEIBULL_ETA  = 1.0e9
WEIBULL_BETA = 2.5

# === BOM (1k volume, USD) ==============
BOM = {
    "SiC 4-die matched binning": 4 * 2.5 + 1.0,
    "BCD gate driver":           1.5,
    "Σ-Δ ADC 16bit":             1.5,
    "MCU Cortex-M4 COTS":        2.0,
    "DBC Al2O3 substrate":       2.5,
    "TO-247 + encapsulant":      3.0,
    "Passives + Shunt":          3.0,
    "PCB + connectors":          2.0,
    "Assembly + test + UL mark": 5.0,
}

# === Foundry schedule (months) =========
SCHEDULE = {
    "YesPower SiC planar":   {"mpw": 10, "parallel": True},
    "DB HiTek BCD 180nm":    {"mpw": 3,  "parallel": True},
    "SK hynix CMOS 0.18um":  {"mpw": 3,  "parallel": True},
    "MCU Cortex-M4 COTS":    {"mpw": 0,  "parallel": True},
    "Assembly + UL cert":    {"mpw": 2,  "parallel": False},
}


def test_turnoff_budget():
    I_drv = (VGS_ON - VPLATEAU) / RG_EXT
    t_mos = QGD / I_drv + 40e-9
    t_irq = N_IRQ_CYC / F_MCU
    t_tot = T_COMP_PROP + t_irq + T_DRV_PROP + t_mos
    return t_tot <= T_OFF_BUDGET, {
        "t_comp_ns": T_COMP_PROP*1e9, "t_irq_ns": t_irq*1e9,
        "t_drv_ns":  T_DRV_PROP*1e9,  "t_mos_ns": t_mos*1e9,
        "total_ns":  t_tot*1e9,       "budget_ns": T_OFF_BUDGET*1e9,
    }


def test_i2t():
    i2t = (I_SC ** 2) * T_OFF_BUDGET
    return i2t <= I2T_RATING, {
        "i2t_event_A2s": i2t, "die_rating_A2s": I2T_RATING,
        "margin_x":  I2T_RATING / i2t if i2t > 0 else 0,
    }


def test_overshoot():
    didt   = I_SC / T_OFF_BUDGET
    v_over = L_STRAY * didt
    limit  = 0.20 * VDS_RATING
    return v_over <= limit, {
        "didt_GA_per_s": didt/1e9, "v_over_V": v_over, "limit_V": limit,
    }


def test_current_share():
    g_ratio   = (1.0 + RDS_SPREAD) / (1.0 - RDS_SPREAD)
    effective = 1.0 + (g_ratio - 1.0) * 0.70
    per_die_max    = (I_NOM / N_DIES) * effective
    per_die_budget = (I_NOM / N_DIES) * 1.20
    return per_die_max <= per_die_budget, {
        "per_die_A":       per_die_max,
        "per_die_budget_A": per_die_budget,
    }


def test_thermal():
    I_die     = I_NOM / N_DIES
    rdson_hot = RDSON_25C * RDSON_TC
    p_die     = I_die * I_die * rdson_hot
    rth       = RTH_JC + RTH_CA
    Tj        = T_AMB + p_die * rth
    return Tj <= TJ_MAX, {
        "I_die_A": I_die, "P_die_W": p_die, "Rth_K_W": rth,
        "Tj_C":  Tj,    "limit_C":   TJ_MAX,
    }


def test_gate_lifetime():
    F = 1.0 - exp(-(N_CYCLES_REQ / WEIBULL_ETA) ** WEIBULL_BETA)
    return F < 1e-3, {
        "cycles_req": N_CYCLES_REQ,
        "fail_prob":  F,
    }


def test_adc_bandwidth():
    f_bw = F_ADC / (2 * OSR_ADC)
    req  = 400e3
    return f_bw >= req, {
        "f_BW_Hz": f_bw, "required_Hz": req,
    }


def test_irq_latency():
    t_irq  = N_IRQ_CYC / F_MCU
    budget = 150e-9
    return t_irq <= budget, {
        "t_irq_ns":  t_irq*1e9, "budget_ns": budget*1e9,
    }


def test_bom():
    total = sum(BOM.values())
    return total <= BOM_BUDGET, {
        "total_USD": total, "budget_USD": BOM_BUDGET,
    }


def test_schedule():
    parallel = max(s["mpw"] for s in SCHEDULE.values() if s["parallel"])
    serial   = sum(s["mpw"] for s in SCHEDULE.values() if not s["parallel"])
    total    = parallel + serial
    return total <= SCHED_BUDGET_MO, {
        "parallel_mo": parallel, "serial_mo": serial,
        "total_mo": total, "budget_mo": SCHED_BUDGET_MO,
    }


FALSIFIERS = [
    "measured t_off > 720 ns -> scrap mk1 design",
    "Tj > 175 °C @ I_NOM=100 A steady -> redesign cooling",
    "without binning RDS_spread >= 15% -> §7.4 FAIL",
    "measured I²t < 20 A²s -> re-select SiC die",
    "dv/dt overshoot > 240 V -> mandatory snubber, BOM +$2",
    "fails UL 489 short-circuit 10 kA interrupt -> halt commercialization",
    "actual BOM total > $42 -> lose price competitiveness",
    "actual MPW > 15 months -> cascading delay toward Mk-∞",
    "gate-oxide degradation before N=100k cycles -> swap SiC vendor",
    "Al2O3 substrate degradation under 500 A continuous -> AlN mandatory, BOM +$2",
]


TESTS = [
    ("§7.1  turnoff budget  (≤ 600 ns)",    test_turnoff_budget),
    ("§7.2  I2t energy      (≤ die rating)", test_i2t),
    ("§7.3  dv/dt overshoot (≤ 240 V)",     test_overshoot),
    ("§7.4  current share   (±20%)",        test_current_share),
    ("§7.5  Tj thermal      (≤ 175 °C)",    test_thermal),
    ("§7.6  TDDB lifetime   (F < 0.1%)",    test_gate_lifetime),
    ("§7.7  ADC bandwidth   (≥ 400 kHz)",   test_adc_bandwidth),
    ("§7.8  IRQ latency     (≤ 150 ns)",    test_irq_latency),
    ("§7.9  BOM total       (≤ $35)",       test_bom),
    ("§7.10 MPW schedule    (≤ 12 mo)",     test_schedule),
]


def main() -> int:
    print("=" * 72)
    passed = 0
    for name, fn in TESTS:
        ok, detail = fn()
        mark = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"  [{mark}] {name}")
        for k, v in detail.items():
            print(f"         · {k}: {v}")
    print("=" * 72)
    print(f"  §7.11 FALSIFIERS ({len(FALSIFIERS)} conditions):")
    for f in FALSIFIERS:
        print(f"    ✗ {f}")
    print("=" * 72)
    total = len(TESTS)
    print(f"  {passed}/{total} PASS  —  SSCB mk1 operability verification")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
