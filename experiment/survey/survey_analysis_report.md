# Survey Analysis Report: Academic Writing, AI Tools & Citation Integrity

**Generated**: 2026-02-01

---

## 1. Executive Summary

This report summarizes results from two parallel surveys: the **Chinese survey** (n=79) and the **English survey** (n=18), for a total of **N=97** researchers.

### Key Findings

| Topic | Finding |
|-------|---------|
| **AI use** | **74 of 97 (76.3%)** use AI for research; 69/79 (Chinese) and 16/18 (English) use AI. |
| **Hallucination experience** | Among respondents who use LLMs to find references, **~41%** report encountering non-existent papers (“hallucinated citations”) **often** or **very often**. |
| **Verification behavior** | Among users of AI-generated or AI-recommended citations, **~78%** say they always or usually verify externally (e.g., Google Scholar/DBLP). |
| **Perceived severity** | **59.8%** consider hallucinated citations a **major problem** or **critical crisis** (35.1% chose “critical crisis”). |
| **Responsibility** | **73.2%** believe **authors** are primarily responsible for verifying citation authenticity. |
| **Automated tools** | **51.5%** strongly support conferences/journals deploying automated tools at submission to check DOIs and fake references. |
| **Risky behaviors** | ~**36%** have copy-pasted BibTeX without checking; ~**24%** have cited an AI-recommended paper without reading the full text. |

---

## 2. Sample and Demographics

### 2.1 Data Sources

- **Chinese survey** (chinese.md): 79 valid responses (after consent).
- **English survey** (CSV): 18 valid responses.
- **Total**: N=97.

### 2.2 Academic Position (combined, N=97)

| Position | Count | Percentage |
|----------|-------|------------|
| PhD Student | 33 | 34.0% |
| Master's Student | 19 | 19.6% |
| Faculty (Professor/Lecturer) | 17 | 17.5% |
| Undergraduate student | 15 | 15.5% |
| Postdoc | 6 | 6.2% |
| Researcher | 5 | 5.2% |
| Other | 2 | 2.1% |

### 2.3 Research Area (combined, N=97)

| Area | Count | Percentage |
|------|-------|------------|
| Other | 25 | 25.8% |
| AI & Machine Learning | 20 | 20.6% |
| Network Security | 19 | 19.6% |
| AI Security | 13 | 13.4% |
| System Security | 10 | 10.3% |
| Cryptography | 6 | 6.2% |
| Software Engineering | 4 | 4.1% |

### 2.4 Publication Experience (combined, N=97)

| Papers Published | Count | Percentage |
|------------------|-------|------------|
| 0 | 22 | 22.7% |
| 1-5 | 46 | 47.4% |
| 6-10 | 16 | 16.5% |
| 11-20 | 6 | 6.2% |
| 20+ | 7 | 7.2% |

### 2.5 Reviewer Experience (combined, N=97)

| Served as top-tier reviewer (last 3 years) | Count | Percentage |
|--------------------------------------------|-------|------------|
| No | 65 | 67.0% |
| Yes | 32 | 33.0% |

---

## 3. AI Tool Adoption and Usage

### 3.1 Do you use AI-powered tools for research? (combined, N=97)

| Response | Count | Percentage |
|----------|-------|------------|
| Yes | 74 | 76.3% |
| No | 13 | 13.4% |

*Note: ~10 respondents did not answer this item.*

### 3.2 Types of AI tools used (multi-select, among AI users)

| Type | Count | % of AI users |
|------|-------|----------------|
| General-purpose LLMs (e.g., ChatGPT, Claude, Gemini) | 74 | 100%* |
| Coding Assistants (e.g., GitHub Copilot, Cursor) | 38 | 39.2% |
| Academic search engines (e.g., Elicit, Semantic Scholar) | 7 | 7.2% |
| AI-powered reading tools (e.g., ChatPDF, Humata) | 7 | 7.2% |

*In the Chinese survey, 69 use AI and all 69 selected “General-purpose LLMs”; in the English survey, 16 of 18 use AI.*

### 3.3 Do you use AI for text polishing, grammar, or rephrasing? (combined, AI users)

| Response | Count | Percentage |
|----------|-------|------------|
| Yes, for specific difficult paragraphs | 34 | 35.1% |
| Yes, for almost every sentence | 24 | 24.7% |
| Yes, but only for final proofreading | 15 | 15.5% |
| No, I trust my own writing more | 1 | 1.0% |

### 3.4 How do you use AI for citation-related tasks? (multi-select, combined)

| Usage | Count | Percentage |
|-------|-------|------------|
| None (do not use AI for citations) | 36 | 37.1% |
| Discovery (ask AI to recommend papers on a topic) | 23 | 23.7% |
| Formatting (convert to BibTeX, etc.) | 22 | 22.7% |
| Summarization (ask AI to summarize a paper to decide whether to cite) | 17 | 17.5% |
| Gap-filling (find a citation for a sentence) | 16 | 16.5% |
| Verification (ask AI if a specific paper exists) | 6 | 6.2% |

---

## 4. Hallucination Experience and Verification Behavior

### 4.1 When using a general LLM to find references, how often do you encounter “hallucinations” (non-existent papers)? (combined)

| Frequency | Count | Percentage |
|-----------|-------|------------|
| Often (20–50%) | 25 | 25.8% |
| Don't use LLMs for finding references | 19 | 19.6% |
| Occasionally (<20%) | 15 | 15.5% |
| Very Often (>50%) | 7 | 7.2% |
| Never | 4 | 4.1% |

*Among those who use LLMs to find references (excluding “Don't use LLMs”), ~**41%** chose “Often” or “Very Often”.*

### 4.2 If an AI gives you a perfect-looking reference, do you still verify it externally? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| Always verify (including “verify 100% via Google Scholar/DBLP”) | 64 | 66.0%* |
| Only if reading full text | 8 | 8.2% |
| Only if suspicious | 1 | 1.0% |
| I do not use General LLMs for finding references | 6 | 6.2% |
| Trust AI | 0 | 0.0% |

*Combines “Always verify” with equivalent phrasing such as “Yes, I verify 100% of them via Google Scholar/DBLP”.*

### 4.3 Have you ever cited an AI-recommended paper without reading the full text? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No, never | 58 | 59.8% |
| Yes, once or twice | 10 | 10.3% |
| Yes, often | 6 | 6.2% |

*~**23.7%** have at least once cited an AI-recommended paper without reading the full text.*

---

## 5. Citation Practices (Author Perspective)

### 5.1 When adding a citation, what is your primary source of metadata (title, year, venue)? (combined)

| Source | Count | Percentage |
|--------|-------|------------|
| Google Scholar "Cite" button | 62 | 63.9% |
| Direct export from publisher (IEEE/ACM) | 23 | 23.7% |
| I assume the paper exists and try to find it manually | 6 | 6.2% |
| Copy from other papers | 4 | 4.1% |
| Other (keep citation but remove DOI, assume hallucination and discard, etc.) | 2 | 2.1% |
| AI-generated | 0 | 0.0% |

### 5.2 How often do you verify that a cited paper actually contains the claim you attribute to it? (combined)

| Frequency | Count | Percentage |
|-----------|-------|------------|
| Every single time | 52 | 53.6% |
| Most of the time | 22 | 22.7% |
| Only for critical claims | 13 | 13.4% |
| Rarely | 2 | 2.1% |

### 5.3 If you cannot find the full text (paywalled or offline), do you still cite based on abstract or title? (Chinese n=79)

| Response | Count | Percentage |
|----------|-------|------------|
| No, never | 43 | 54.43% |
| Yes, if necessary | 33 | 41.77% |
| Yes, often | 3 | 3.80% |

### 5.4 Agreement: “There is pressure to include more references to make the paper look more scholarly.” (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| Somewhat agree | 31 | 32.0% |
| Neutral | 24 | 24.7% |
| Somewhat disagree | 16 | 16.5% |
| Strongly disagree | 12 | 12.4% |
| Strongly agree | 6 | 6.2% |

---

## 6. Perceptions of Hallucinated Citations and Responsibility

### 6.1 Agreement: “AI tools have made it easier to write Related Work but harder to ensure citation accuracy.” (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| Somewhat agree | 26 | 26.8% |
| Strongly agree | 23 | 23.7% |
| Neutral | 11 | 11.3% |
| Somewhat disagree | 11 | 11.3% |
| Strongly disagree | 3 | 3.1% |

### 6.2 Strategy when an AI-generated citation has a broken link or invalid DOI (combined)

| Strategy | Count | Percentage |
|----------|-------|------------|
| I assume the paper exists and try to find it manually | 45 | 46.4%* |
| I assume the paper is a hallucination and discard it | 23 | 23.7% |
| I ask the AI to provide a different link | 5 | 5.2% |
| I keep the citation but remove the DOI | 1 | 1.0% |

*Combines “Try to find manually” with equivalent English phrasing.*

### 6.3 How serious is “hallucinated citations” (non-existent papers) in the AI era? (combined, this question only)

| Severity | Count | Percentage |
|----------|-------|------------|
| Critical crisis | 34 | 35.1% |
| Major problem | 24 | 24.7% |
| Minor nuisance | 20 | 20.6% |
| Not a problem | 1 | 1.0% |

**59.8% combined consider it a “Major problem” or “Critical crisis”.**

### 6.4 Who is primarily responsible for verifying citation authenticity? (combined, this question only)

| Party | Count | Percentage |
|-------|-------|------------|
| Authors | 71 | 73.2% |
| Reviewers | 3 | 3.1% |
| Publishers (Editorial check) | 3 | 3.1% |
| AI tool developers | 2 | 2.1% |

### 6.5 Should conferences deploy automated tools at submission to check DOIs and fake references? (combined, this question only)

| Response | Count | Percentage |
|----------|-------|------------|
| Yes, absolutely | 50 | 51.5% |
| Maybe | 24 | 24.7% |
| No | 5 | 5.2% |

### 6.6 Agreement: “It is acceptable to cite a paper based on AI summarization without reading the original.” (combined, this question only)

| Response | Count | Percentage |
|----------|-------|------------|
| Somewhat disagree | 27 | 27.8% |
| Strongly disagree | 24 | 24.7% |
| Neutral | 17 | 17.5% |
| Somewhat agree | 9 | 9.3% |
| Strongly agree | 2 | 2.1% |

*~**52.5%** disagree or strongly disagree.*

---

## 7. Reviewer Perspective (reviewers only)

### 7.1 When reviewing, do you explicitly check the Reference section? (combined, reviewers n≈22–32)

| Response | Count | Percentage |
|----------|-------|------------|
| Yes, skimming | 14 | 14.4% |
| Yes, carefully | 5 | 5.2% |
| No | 3 | 3.1% |

### 7.2 What do you look for when checking references? (multi-select)

| Focus | Count | Percentage |
|-------|-------|------------|
| Missing key related work | 20 | 20.6% |
| Correctness of metadata (Year, Venue) | 8 | 8.2% |
| Existence of the papers | 6 | 6.2% |
| Self-citation abuse | 3 | 3.1% |

### 7.3 Have you ever clicked a DOI in a submission to verify the paper exists? (combined)

| Frequency | Count | Percentage |
|-----------|-------|------------|
| Occasionally | 9 | 9.3% |
| Rarely | 7 | 7.2% |
| Never | 6 | 6.2% |
| Frequently | 0 | 0.0% |

### 7.4 Have you ever suspected a submission contained fake or hallucinated references? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No | 18 | 18.6% |
| Yes | 4 | 4.1% |

### 7.5 Reaction to finding **one** incorrect citation (e.g., wrong year) (combined)

| Reaction | Count | Percentage |
|----------|-------|------------|
| Mention in minor comments | 68 | 70.1% |
| Ask for major revision | 12 | 12.4% |
| Reject the paper | 4 | 4.1% |
| Ignore | 0 | 0.0% |

### 7.6 Reaction to finding **multiple** (e.g., >5) incorrect or fake citations (combined)

| Reaction | Count | Percentage |
|----------|-------|------------|
| Reject immediately (Ethical concern) | 45 | 46.4% |
| Ask for explanation | 34 | 35.1% |
| Mention it in minor comments | 14 | 14.4% |
| Ask for major revision | 3 | 3.1% |
| Reject the paper | 1 | 1.0% |
| Consider innocent mistake | 0 | 0.0% |

### 7.7 If you find a suspicious or clearly fake reference in a **published** paper, do you report it? (multi-select, combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No, I would verify it privately but take no action | 34 | 35.1% |
| Yes, I would contact the PC Chairs or Journal Editors | 30 | 30.9% |
| Yes, I would contact the authors directly | 24 | 24.7% |
| No, I would ignore it | 6 | 6.2% |

---

## 8. Risky Behaviors and Edge Cases

### 8.1 Have you ever copy-pasted a BibTeX entry from the internet without checking its content? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No, never | 44 | 45.4% |
| Yes, rarely | 23 | 23.7% |
| Yes, often | 12 | 12.4% |

*~**35.1%** have at least once copy-pasted BibTeX without checking.*

### 8.2 Have you seen a reference list where author names were clearly wrong (e.g., order reversed)? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No | 60 | 61.9% |
| Yes | 37 | 38.1% |

### 8.3 Have you seen a reference where the title existed but the venue/year was completely wrong? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| No | 55 | 56.7% |
| Yes | 42 | 43.3% |

### 8.4 Is it acceptable to cite a “Technical Report” if a peer-reviewed version exists? (combined)

| Response | Count | Percentage |
|----------|-------|------------|
| Yes | 72 | 74.2% |
| No | 25 | 25.8% |

### 8.5 Agreement: “I meticulously verify every field (volume, issue, page numbers) of every BibTeX entry I import, ensuring 100% accuracy before submission.” (combined, this question only)

| Response | Count | Percentage |
|----------|-------|------------|
| Strongly agree | 23 | 23.7% |
| Somewhat agree | 24 | 24.7% |
| Neutral | 23 | 23.7% |
| Somewhat disagree | 6 | 6.2% |
| Strongly disagree | 3 | 3.1% |

### 8.6 Do you use tools like Semantic Scholar or ResearchRabbit to build your bibliography? (combined, this question only)

| Response | Count | Percentage |
|----------|-------|------------|
| No | 61 | 62.9% |
| Yes | 18 | 18.6% |

---

## 9. Additional Findings (from chinese.md, Chinese n=79)

### 9.1 Bibliography accuracy is as important as experimental results

- **Strongly agree**: 44 (55.7%)
- **Somewhat agree**: 22 (27.85%)
- **Neutral**: 10 (12.66%)
- **Somewhat disagree**: 3 (3.8%)

### 9.2 Is the current peer review process effective at catching reference metadata errors?

- **Not very effective**: 53 (67.09%)
- **Somewhat effective**: 19 (24.05%)
- **Ineffective**: 6 (7.59%)
- **Very effective**: 1 (1.27%)

*Most respondents consider current review insufficient for catching citation errors.*

---

## 10. Generated Figures

Figures used in this report are in the `figs/` directory:

- `ai_tool_usage.pdf`: AI tool usage
- `citation_practices.pdf`: Citation practices
- `demo_papers.pdf`: Publication experience
- `demo_position.pdf`: Position distribution
- `demo_research_area.pdf`: Research area
- `demo_reviewer.pdf`: Reviewer experience
- `hallucination_verification.pdf`: Hallucination and verification
- `reviewer_reactions.pdf`: Reviewer reactions
- `severity_responsibility.pdf`: Severity and responsibility
- `survey_dashboard.pdf`: Survey overview

---

## 11. Data and Report Notes

- **Chinese survey** statistics are from `chinese.md` (79 valid responses).
- **English survey** raw data are from `Survey on Academic Writing Workflows, AI Tools, and Citation Integrity.csv` (18 responses).
- **Combined statistics** were cleaned so that each question keeps only its correct response options; earlier automated merging had misassigned some options across questions, and this report recalculates percentages using the correct option sets (base N=97 or item-specific valid N).
- Some items are multi-select or shown only to “AI users” or “reviewers”; the base or item name is noted in the tables where relevant.

*This report was reorganized from the original questionnaire results.*
