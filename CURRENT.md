# CURRENT.md — Current Work Status

> Quick snapshot of current project state

---

## Status: Paper Draft Complete — NDSS Adaptation in Progress

**Target**: NDSS 2027 (Network and Distributed System Security Symposium)

**Previous Target**: USENIX Security 2026

**Paper Title**: GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models

---

## What's Done ✅

### Research & Writing
1. Full paper draft completed (all 9 sections + ethics + appendix)
2. CiteVerifier framework implemented and validated
3. LLM benchmark: 13 models × 40 domains, 375,440 citations generated and verified
4. Archival analysis: 56,381 papers, 2.2M citations, manual verification completed
5. User survey: 97 responses collected, 94 valid after consistency filtering
6. All figures, tables, and references prepared

### NDSS Setup
7. NDSS template configured (`paper/ndss27/` with IEEEtran.cls + ndss2026.tex)
8. Main document (`0_0_main.tex`) compiles to PDF
9. Double-blind author anonymization applied
10. Meta documents refreshed to reflect actual content

---

## What's In Progress 🔄

1. **NDSS content emphasis adjustment**
   - Strengthening systems/network security angle for NDSS audience
   - Ensuring clear connection to real-world scholarly infrastructure

2. **Page limit verification**
   - Confirming body ≤ 13 pages (excluding ethics, references, appendix)
   - Identifying trim targets if over limit

3. **Double-blind compliance final check**
   - Verifying all self-citations are in third person
   - Removing any identifying metadata from comments

---

## What's Next 📋 (Priority Order)

1. **Compile and check page count** — identify sections to condense if needed
2. **Grayscale figure check** — ensure all figures readable in B&W (NDSS requirement)
3. **Terminology consistency pass** — "ghost citation" / "hallucinated citation" / "fabricated citation"
4. **Reference integrity check** — all `\cite{}` resolve, IEEE format correct
5. **Final proofread** — grammar, transitions, abstract-body number alignment
6. **Conflict-of-interest declaration** — prepare for submission system
7. **Cover letter draft** — highlight NDSS relevance
8. **Monitor NDSS 2027 CFP** — update for any rule/format changes

---

## Key Deadlines

- **NDSS 2027 Summer Cycle**: Expected ~April 2027
- **NDSS 2027 Fall Cycle**: Expected ~August 2027

*Note: NDSS 2027 CFP not yet released. Using NDSS 2026 as reference baseline.*

---

## Quick Links

- [Main Paper](paper/ndss27/0_0_main.tex)
- [Task Plan](PLAN.md)
- [Research Notes](RESEARCH.md)
- [NDSS CFP](reference/ndss_cfp.md)

---

*Last updated: 2026-05-04*
