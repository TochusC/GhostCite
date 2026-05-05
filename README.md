# GhostCite

> A Large-Scale Analysis of Citation Validity in the Age of Large Language Models

---

## Project Overview

GhostCite investigates the emerging threat of "ghost citations"—fabricated or invalid citations produced by Large Language Models (LLMs)—and their penetration into the published scientific record.

We develop **CiteVerifier**, an open-source automated citation verification framework, and conduct a comprehensive three-pronged study:

1. **LLM Benchmark**: Evaluate 13 state-of-the-art LLMs across 40 research domains on citation generation (375,440 citations), finding hallucination rates of **14.23%–94.93%** with significant domain sensitivity.
2. **Archival Analysis**: Analyze **2.2 million citations** from **56,381 papers** (2020–2025) at 8 top-tier AI/ML and Security venues, confirming **1.07%** of papers contain invalid citations with an **80.9% surge in 2025**.
3. **User Study**: Survey 94 researchers, revealing a critical "verification gap": **41.5%** copy-paste BibTeX without checking, **76.7%** of reviewers do not thoroughly check references, yet **70.2%** strongly support automated checks.

**Current Target**: NDSS 2027 (Network and Distributed System Security Symposium)  
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
│       ├── section/               # Body sections (1_introduction–9_conclusion)
│       ├── appendix/              # Appendix sections
│       ├── Tables/                # Tables (by section)
│       ├── Figures/               # Figures (by section)
│       ├── Tex/                   # Additional TeX snippets
│       ├── style/                 # IEEEtran.cls, ndss2026.tex
│       └── references.bib         # Bibliography
├── system/              # System implementation (CiteVerifier framework)
└── experiment/          # Experiment data and results
```

---

## Current Status

### Completed ✅
- [x] Full paper draft completed (all 9 sections + ethics + appendix)
- [x] CiteVerifier framework implemented and validated
- [x] LLM benchmark experiment (13 models × 40 domains, 375K citations)
- [x] Archival analysis (56K papers, 2.2M citations, manual verification)
- [x] User survey (94 valid responses)
- [x] NDSS template configured (`paper/ndss27/`)
- [x] PDF compiles successfully

### In Progress 🔄
- [ ] Adapt content emphasis for NDSS audience (systems/network security angle)
- [ ] Verify 13-page body limit (excluding ethics, references, appendix)
- [ ] Double-blind compliance check (author anonymization, third-person self-citations)

### Pending 📋
- [ ] Final page count verification
- [ ] Conflict-of-interest declaration
- [ ] Final proofread and consistency check
- [ ] Cover letter preparation

---

## Key Contributions

1. **CiteVerifier**: Open-source automated citation verification framework with cascaded multi-source retrieval and similarity-based classification.
2. **First large-scale LLM citation hallucination benchmark**: 13 models, 40 domains, quantitative hallucination rates and domain sensitivity analysis.
3. **Empirical measurement of published record contamination**: 2.2M citations analyzed, temporal trend showing 80.9% increase in 2025, evidence of error propagation.
4. **Behavioral analysis of verification failures**: Survey reveals gap between stated and actual verification practices across authors and reviewers.

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
