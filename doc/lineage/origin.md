# Origin & lineage

This repository was extracted from the **canon** monorepo on
**2026-05-06**. This document records the exact upstream commits and paths
each file was pulled from, so that any change in this repo can be traced
back to (or propagated upstream to) the source-of-truth.

> **2026-05-06 (post-extraction)**: repository renamed `sscb` → `hexa-sscb`
> on GitHub and locally. Upstream path `canon/domains/compute/sscb/`
> and the local `core/sscb/` directory keep their original names — they are
> the n=6 lattice identity reference and must remain 1:1 with the upstream
> SSOT for sync purposes. Only the repo root and public-facing self-references
> were renamed.

## Upstream

- Repo: `canon` (local working copy at `~/core/canon`)
- Branch: `main`
- Extraction date: 2026-05-06
- Extractor: forensic recovery — two of four source markdowns were resurrected
  from a deletion commit's parent (see below).

## File-by-file provenance

| This repo | Upstream path | Commit pulled from | Notes |
|---|---|---|---|
| `core/sscb/spec.md` | `papers/sscb-mk1-2026-05-04.md` | working tree (HEAD `b0a45476`) | The inaugural paper (commit `cffa7e21`, Apr 2026). |
| `core/sscb/domain.md` | `domains/compute/sscb/sscb.md` | working tree (HEAD `b0a45476`) | Full domain doc, currently 1320 lines. Last substantive content commit: `068e84da` (§21 IMPACT reverse-chronological restructure). |
| `module/engineering_pack/README.md` | `domains/compute/sscb/sscb_engineering_pack_bak.md` | parent of `a489a368` (deletion commit, Apr 21 2026) | **Recovered from history.** Removed by commit `a489a368` ("English-only public landing header") which deleted both `_bak.md` files. |
| `module/impact/README.md` | `domains/compute/sscb/sscb.md` §21 IMPACT + §22 | working tree (HEAD `b0a45476`) | Extracted as a free-standing module from `domain.md` lines 1121–end. |
| `.own` (replaces deleted `ai-native/CLAUDE.md`) | `domains/compute/sscb/CLAUDE.md` | parent of `ea1bfc97` (purge commit) | `ai-native/CLAUDE.md` was first **recovered from history** (purged by commit `ea1bfc97` "AG10: purge CLAUDE.md + .claude/settings.json — hexa-only harness"), then **deleted again on 2026-05-06** per user directive ("claude.md 금지 → .own 활용"). Agent-scope content reorganized into project-root `.own` (hive raw.mk2 own_v1 schema). |
| `doc/archive/sscb_mk1_predecessor_korean.md` | `domains/compute/sscb/sscb_bak.md` | parent of `a489a368` | **Recovered from history.** Korean-language predecessor of the current `domain.md`. Preserved verbatim. |
| `doc/archive/sscb_mk1_paper_2026-05-04.md.bak` | `raw_archive/2026-05-04T/papers/sscb-mk1-2026-05-04.md.bak` | working tree | Paper backup snapshot. Preserved verbatim. |

## Key commits in upstream sscb history

| Commit | Date | Subject |
|---|---|---|
| `22cc76fd` | early mk1 | sscb mk1 domain + mk-∞ singularity breakthrough spec |
| `8cf9e811` | mid | sscb mk1 §7 operability re-verification + Mk.II smash/free |
| `04265a06` | mid | sscb/hexa-ufo @paper validation (0 violations) |
| `068e84da` | 2026-04-18 | §21 IMPACT reverse-chronological + `<details>` collapse |
| `cffa7e21` | 2026-05-04 | sscb mk1 inaugural paper landed |
| `a489a368` | 2026-04-21 | docs(readme): English-only — **deleted both `_bak.md` files** |
| `ea1bfc97` | post | purge CLAUDE.md (hexa-only harness) |
| `b0a45476` | 2026-05-05 | layout refactor `docs/ flat → <feature>/doc/ feature-grouped` |

## What was searched for and not found

- **Binary PDFs** (`sscb_mk1.pdf`, `sscb_mk1_engineering_pack.pdf`,
  `sscb_mk1_impact.pdf`) referenced as 986 KB / 1.2 MB / 404 KB shared via
  KakaoTalk with expiration ~2026-05-01. **No git history** in canon,
  contact, papers, nexus, secret, save, or raw-archive-temp-clone contains
  any `sscb*.pdf` blob. **No on-disk copies** found anywhere under `~/core` or
  `~/Downloads` / `~/Desktop`. The Markdown sources in this repo are the
  pre-PDF originals; PDFs can be regenerated via pandoc if needed.

## Re-derivation policy

If you change a file in `core/sscb/` here and want to push it upstream:

1. Reproduce the change in `canon/domains/compute/sscb/sscb.md`.
2. If the change is in `module/impact/`, propagate to `sscb.md` §21–§22.
3. `module/engineering_pack/` has no live upstream path (it was deleted in
   `a489a368`); upstream recovery requires re-introducing the file to
   `canon` first.

If you change a file in `doc/archive/`, **stop** — those are immutable
snapshots and must not be edited.
