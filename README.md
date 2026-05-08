# GhostCite

> A Large-Scale Analysis of Citation Validity in the Age of Large Language Models

---

## Project Overview

GhostCite investigates the emerging threat of "ghost citations" — fabricated or invalid citations produced by Large Language Models (LLMs) — and their penetration into the published scientific record.

We develop **CiteVerifier**, an open-source automated citation verification framework, and conduct a comprehensive three-pronged study:

1. **LLM Benchmark**: Evaluate 13 state-of-the-art LLMs across 40 research domains on citation generation (375,440 citations), finding hallucination rates of **14.23\%–94.93\%** with significant domain sensitivity.
2. **Archival Analysis**: Analyze **2.2 million citations** from **56,381 papers** (2020–2025) at 8 top-tier AI/ML and Security venues, confirming **1.07\%** of papers contain invalid citations with an **80.9\% surge in 2025**.
3. **User Study**: Survey 97 researchers (94 valid responses), revealing a critical "verification gap": **41.5\%** copy-paste BibTeX without checking, **76.7\%** of reviewers do not thoroughly check references, yet **70.2\%** strongly support automated checks.

**Current Status**: NDSS 2027 Under Review  
**Previous Target**: USENIX Security 2026

---

## Directory Structure

```
GhostCite/
├── INIT.md              # Workspace initialization workflow
├── README.md            # This file
├── RESEARCH.md          # Core findings, insights, and research gaps
├── PLAN.md              # Task plan and work steps
├── VERIFY.md            # Fact verification checklist
├── CHANGELOG.md         # Change log
├── CURRENT.md           # Current work status snapshot
├── reference/           # Research materials and references
│   ├── ndss_cfp.md      # NDSS Call for Papers summary
│   └── survey/          # Special topic verification documents
├── paper/               # Paper outputs
│   ├── usenix26/        # Original USENIX Security submission
│   └── ndss27/          # NDSS 2027 submission (current target)
│       ├── 0_0_main.tex           # Main document
│       ├── 0_abstract.tex         # Abstract
│       ├── section/               # Body sections (1_introduction–9_conclusion + ethics)
│       ├── appendix/              # Appendix sections
│       ├── table/                 # Tables (by section)
│       ├── figure/                # Figures (by section)
│       │   └── raw/               # Figure source files
│       ├── style/                 # IEEEtran.cls, ndss2026.tex
│       └── references.bib         # Bibliography
├── system/              # System implementation (CiteVerifier framework)
└── experiment/          # Experiment data and results
    ├── llm_benchmark/   # LLM citation generation benchmark
    ├── paper_audit/     # Archival analysis of published papers
    ├── survey/          # User survey data and analysis
    ├── citeverifier/    # CiteVerifier framework code
    └── user_study/      # Additional user study materials
```

---

## Current Status

### Completed ✅
- [x] Full paper draft completed (all 9 sections + ethics + appendix)
- [x] CiteVerifier framework implemented and validated
- [x] LLM benchmark experiment (13 models × 40 domains, 375K citations)
- [x] Archival analysis (56K papers, 2.2M citations, manual verification)
- [x] User survey (97 responses, 94 valid)
- [x] NDSS template configured (`paper/ndss27/`)
- [x] PDF compiles successfully
- [x] NDSS 2027 submission completed

### In Progress 🔄
- [ ] Under review at NDSS 2027

### Pending 📋
- [ ] Await reviewer decisions
- [ ] Prepare for potential Major/Minor Revision
- [ ] Prepare rebuttal materials if needed

---

## Key Contributions

1. **Technical baseline for citation verification.** We develop CiteVerifier, an open-source framework that verifies citations at scale, providing a replicable implementation example for researchers and future work.

2. **Comprehensive benchmark of LLM citation hallucination.** We evaluate 13 LLMs across 40 domains on 375,440 generated citations, revealing widespread citation hallucination across models and domains.

3. **Empirical analysis of published literature.** We analyze 2.2M citations from 56,381 papers (2020–2025), documenting the presence and increasing prevalence of invalid citations in the published literature.

4. **User study of researcher practices.** We survey 97 researchers across various roles and research domains, characterizing AI adoption rates, verification behaviors, and community attitudes toward citation validity and potential interventions.

---

## The Ghost Citation Lifecycle

Our studies map a four-stage "pollution pipeline":

1. **Generation** — LLMs synthesize plausible but non-existent references
2. **Adoption** — researchers copy without verification; superficial checks
3. **Review Failure** — trust-by-default norms; no automated flagging
4. **Publication & Propagation** — errors enter permanent record and are copied

> See [RESEARCH.md](RESEARCH.md) for detailed findings, insights, and recommendations.

---

## Quick Links

- [Research Notes](RESEARCH.md)
- [Task Plan](PLAN.md)
- [Verification Checklist](VERIFY.md)
- [NDSS CFP Summary](reference/ndss_cfp.md)
- [Main Paper](paper/ndss27/0_0_main.tex)

---

## NDSS-Specific Notes

| Aspect | Detail |
|--------|--------|
| Page limit | 13 pages (excluding ethics, references, appendix) |
| Template | IEEEtran.cls + ndss2026.tex |
| Review | Double-blind |
| Cycles | Summer / Fall (dual submission) |
| Revision | Minor / Major Revision possible |

---

*See [INIT.md](INIT.md) for the full workspace initialization workflow.*
