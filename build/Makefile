# SSCB mk1 — pandoc PDF rebuild
#
# Regenerates the three PDFs originally shared via KakaoTalk
# (sscb_mk1.pdf / sscb_mk1_engineering_pack.pdf / sscb_mk1_impact.pdf,
# binaries lost — see doc/lineage/origin.md "What was searched for and not
# found"). The .md sources in this repo are the pre-PDF originals.
#
# Usage:
#   make -C build check   # verify pandoc + xelatex available
#   make -C build all     # build all three PDFs
#   make -C build clean   # remove build artifacts
#
# Generated PDFs land in build/out/ and are .gitignore'd via the project
# root .gitignore (*.pdf rule).

ROOT     := ..
OUT      := out
PANDOC   := pandoc
HEADER   := header.tex

PANDOC_FLAGS := \
  --pdf-engine=xelatex \
  --include-in-header=$(HEADER) \
  --variable=geometry:a4paper,margin=25mm \
  --variable=fontsize:11pt \
  --variable=colorlinks:true \
  --variable=linkcolor:black \
  --variable=urlcolor:blue \
  --syntax-highlighting=tango \
  --toc \
  --toc-depth=2

PDFS := \
  $(OUT)/sscb_mk1.pdf \
  $(OUT)/sscb_mk1_engineering_pack.pdf \
  $(OUT)/sscb_mk1_impact.pdf

.PHONY: all clean check
all: $(PDFS)

$(OUT):
	mkdir -p $(OUT)

$(OUT)/sscb_mk1.pdf: $(ROOT)/core/sscb/spec.md $(HEADER) | $(OUT)
	$(PANDOC) $(PANDOC_FLAGS) \
	  --metadata=title:"HEXA-SSCB mk1 — Inaugural Paper" \
	  --metadata=date:"2026-05-04" \
	  -o $@ $<

$(OUT)/sscb_mk1_engineering_pack.pdf: $(ROOT)/module/engineering_pack/README.md $(HEADER) | $(OUT)
	$(PANDOC) $(PANDOC_FLAGS) \
	  --metadata=title:"HEXA-SSCB mk1 — Engineering Pack" \
	  --metadata=date:"2026-05-06" \
	  -o $@ $<

$(OUT)/sscb_mk1_impact.pdf: $(ROOT)/module/impact/README.md $(HEADER) | $(OUT)
	$(PANDOC) $(PANDOC_FLAGS) \
	  --metadata=title:"HEXA-SSCB mk1 — IMPACT Ladder (Mk.I → Mk.V)" \
	  --metadata=date:"2026-05-06" \
	  -o $@ $<

clean:
	rm -rf $(OUT)

check:
	@command -v $(PANDOC)  >/dev/null 2>&1 || { echo "MISSING: pandoc";  exit 1; }
	@command -v xelatex    >/dev/null 2>&1 || { echo "MISSING: xelatex"; exit 1; }
	@$(PANDOC) --version | head -1
	@xelatex --version | head -1
	@echo "OK: build toolchain ready"
