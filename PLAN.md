# PLAN.md — Task Plan and Work Steps

> Task structure, output planning, and work steps for GhostCite NDSS 2027 submission

---

## Current Phase: Under Review at NDSS 2027

---

## Phase 1: Paper Content — Completed ✅

All core research and writing is complete. The paper draft includes:

- [x] Abstract
- [x] Introduction (motivation, research gaps, contributions)
- [x] Background & Related Work
- [x] Methodology (CiteVerifier framework design and implementation)
- [x] Experiment Design
- [x] LLM Benchmark Results (Section 5)
- [x] Archival Analysis Results (Section 6)
- [x] Survey Results (Section 7)
- [x] Discussion & Mitigation (Section 8)
- [x] Conclusion (Section 9)
- [x] Ethics Statement
- [x] Appendix (domain sensitivity, survey details, repeated citations, etc.)
- [x] References (references.bib)
- [x] All figures and tables

---

## Phase 2: NDSS-Specific Adaptation ✅

### 2.1 Content Emphasis Adjustment

- [x] **Strengthen systems/network security angle in Introduction**
  - NDSS emphasizes practical systems and network relevance
  - Ensure clear connection to real-world scholarly communication systems
  - Highlight implications for distributed trust in scientific infrastructure

- [x] **Review Background for NDSS-relevant citations**
  - Ensure related work includes NDSS-relevant prior work on misinformation/trust
  - Check for security-community framing of citation integrity

- [x] **Verify Discussion section aligns with NDSS audience expectations**
  - Emphasize system-level mitigations (submission platforms, verification APIs)
  - Frame recommendations as deployable infrastructure

### 2.2 Format Compliance

- [x] Switch to IEEEtran.cls + ndss2026.tex template
- [x] **Verify 13-page body limit** (excluding ethics, references, appendix)
  - Current body sections: Introduction through Conclusion
  - Ethics section is excluded from page count
  - References and appendix are excluded

- [x] **Ensure US Letter paper size**
  - Verify `\documentclass[conference]{style/IEEEtran}` produces correct output

- [x] **Verify all macros work with new template**
  - Custom commands (`\citeb`, `\system`, `\todo`, etc.)
  - tcolorbox environments (`keyfindingsSidebar`, `casestudybox`)
  - Cleveref settings

### 2.3 Double-Blind Compliance

- [x] Author information blanked (`\author{}`)
- [x] **Self-citations in third person**
  - Scan for any first-person self-references to prior work
  - Ensure CiteVerifier/GhostCite is described neutrally

- [x] **Remove identifying metadata**
  - Check for author names in comments (`\xzy`, `\xl`, `\mfs` commands are color-coded but anonymized)
  - Remove any institution-specific references

---

## Phase 3: Quality Assurance ✅

- [x] **Compile and verify PDF output**
  - Zero LaTeX errors/warnings
  - All cross-references resolve correctly
  - Figures and tables render properly in grayscale

- [x] **Page count check**
  - Body ≤ 13 pages
  - If over: identify sections for condensation

- [x] **Terminology consistency pass**
  - "ghost citation" vs. "hallucinated citation" vs. "fabricated citation"
  - "invalid citation" definition consistency
  - CiteVerifier / GhostCite naming consistency

- [x] **Reference format check**
  - IEEEtran bibliography style
  - All citations have corresponding entries in references.bib
  - No broken or missing citations

- [x] **Figure/table quality**
  - Grayscale readability (NDSS requires B&W clarity)
  - Font sizes legible at print scale
  - All captions complete and accurate

---

## Phase 4: Final Preparation ✅

- [x] **Conflict-of-interest declaration**
  - Prepare for submission system

- [x] **Final proofread**
  - Grammar, spelling, flow
  - Section transitions
  - Abstract-accuracy check (numbers match body)

- [x] **Cover letter draft**
  - Highlight NDSS relevance (systems perspective, practical impact)
  - Summarize contributions

- [x] **Artifact preparation (if applicable)**
  - CiteVerifier code repository
  - Dataset documentation

---

## Phase 5: Under Review / Awaiting Decision 🔄

- [ ] **Monitor submission portal** for reviewer feedback
- [ ] **Prepare revision materials** (if Major/Minor Revision offered)
  - Address reviewer comments systematically
  - Update meta documents to reflect changes
- [ ] **Prepare rebuttal** (if needed)

## Parallel Tasks

- [ ] **Update experiment data** if new results available post-USENIX draft
- [x] **Monitor NDSS 2027 CFP release** for any format/rule changes
- [x] **Prepare backup submission strategy** (Summer vs. Fall cycle)

---

## Notes

- NDSS allows Major Revision (unlike USENIX's binary accept/reject)
- Two submission cycles available (Summer/Fall)
- Each author limited to 6 submissions per cycle
- NDSS 2027 CFP not yet released; using NDSS 2026 as reference baseline

---

*Last updated: 2026-05-08*
