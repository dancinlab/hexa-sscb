# build — pandoc PDF rebuild

Regenerates the three PDFs originally shared via KakaoTalk:

| Output (`out/`) | Source `.md` |
|---|---|
| `sscb_mk1.pdf` (~986 KB) | `core/sscb/spec.md` |
| `sscb_mk1_engineering_pack.pdf` (~1.2 MB) | `module/engineering_pack/README.md` |
| `sscb_mk1_impact.pdf` (~404 KB) | `module/impact/README.md` |

Per [`doc/lineage/origin.md`](../doc/lineage/origin.md), the PDF binaries were
not recoverable from any git history or local disk — the `.md` sources in
this repo are the pre-PDF originals. PDFs are `.gitignore`'d so they never
end up tracked.

## Toolchain

- `pandoc` ≥ 3.0
- `xelatex` (TeX Live / MacTeX)
- A CJK-capable font: `Apple SD Gothic Neo` is the macOS default referenced
  by `template.tex`. On Linux substitute `Noto Sans CJK KR` and edit
  `setCJKmainfont` / `setCJKmonofont`.

### macOS

```bash
brew install pandoc
brew install --cask mactex     # ~5 GB; brings xelatex + xeCJK
```

### Linux (Debian/Ubuntu)

```bash
sudo apt install pandoc texlive-xetex texlive-lang-cjk fonts-noto-cjk
```

## Run

```bash
make -C build check     # prints pandoc + xelatex versions
make -C build all       # builds the 3 PDFs into build/out/
make -C build clean     # rm -rf build/out/
```

## Authority

This build target is one of the four code-permitted locations declared in
`.own` own 3 (`hexa-sscb-doc-first-code-scope`). Adding a new build target
(e.g. an HTML mirror) requires editing `.own` own 3 + the README inventory
before the implementing PR.
