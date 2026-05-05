# VERIFY.md — Fact Verification Checklist

> Marking rules:
> - `[x]` Verified and passed
> - `[~]` Basically correct but with minor deviation (see notes)
> - `[!]` Incorrect, needs correction
> - `[?]` Cannot verify (no public source found)
>
> Each item should have a brief justification with source links below it.

---

## NDSS Submission Requirements

- [x] **Page limit is 13 pages excluding ethics, references, and appendix**
  > Confirmed in NDSS 2026 CFP.
  > - https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/

- [x] **Double-blind review required**
  > Author names and affiliations must not appear. Prior work cited in third person.
  > - https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/

- [x] **US Letter paper size (not A4)**
  > Two-column layout, Times font 10pt+, 11pt+ line spacing.
  > - https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/

- [x] **Dual submission cycles (Summer/Fall)**
  > Each author limited to 6 submissions per cycle, 12 total.
  > - https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/

- [x] **Major Revision option available**
  > Unlike USENIX's binary decision, NDSS offers Minor/Major Revision.
  > - https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/

---

## Paper Content — Core Claims

### LLM Benchmark Claims

- [x] **13 LLMs evaluated**
  > Verified against experimental logs and API call records. Models include GPT-5, Claude-4, DeepSeek, Grok 4, Qwen-3, ERNIE, Hunyuan, and others.
  > - See `paper/ndss27/section/5_llm_results.tex`, Table `tab:model_validity`

- [x] **375,440 citations generated from 22,800 API interactions**
  > Verified against experiment logs. 331,809 successfully extracted (88.38% extraction rate) from 20,653 well-formed JSON outputs.
  > - See `paper/ndss27/section/5_llm_results.tex`

- [x] **Hallucination rates: 14.23% (DeepSeek) to 94.93% (Hunyuan)**
  > Verified against classified output data. DeepSeek is best-performing; Hunyuan is worst.
  > - See `paper/ndss27/section/5_llm_results.tex`, Table `tab:model_validity`

- [x] **40 research domains aligned with arXiv CS subject classes**
  > Domain list matches arXiv CS classification. See Appendix `app:domain_codes`.
  > - https://arxiv.org/category_taxonomy

- [x] **Domain sensitivity: 51.39 percentage point spread across domains**
  > Average hallucination rates range from 28.80% (Computation and Language) to 80.19% (Digital Libraries).
  > - See `paper/ndss27/Tables/Sec5_LLM/domain_sensitivity.tex`

- [x] **LLM-as-judge accuracy: 38% average (below random guessing)**
  > Each of 13 models judged 100 citations (50 valid, 50 invalid). ERNIE highest at 56% but with 88% false positive rate on valid citations.
  > - See `paper/ndss27/section/5_llm_results.tex`, Table `tab:judge_accuracy`

- [x] **Temporal pattern: hallucination rates increase with publication year (R² = 0.94)**
  > Exponential fit to year-vs-hallucination count data. Valid citations show different distribution.
  > - See `paper/ndss27/section/5_llm_results.tex`, Figure `fig:temporal_distribution_barplot`

### Archival Analysis Claims

- [x] **56,381 papers from 8 venues (2020–2025)**
  > Venue counts: NeurIPS (20,387), AAAI (13,821), ICML (11,192), IJCAI (5,535), USENIX (1,915), CCS (1,756), S&P (1,073), NDSS (702). Total = 56,381.
  > - See `paper/ndss27/section/6_paper_results.tex`, Table `tab:collected_papers` (Appendix)

- [x] **2,199,409 citations extracted**
  > Verified against CiteVerifier output logs.
  > - See `paper/ndss27/section/6_paper_results.tex`

- [x] **604 papers (1.07%) contain at least one invalid citation**
  > 2,530 flagged → 739 confirmed invalid (136 metadata errors + 603 ghost citations) → 604 unique papers. 15 papers had both types.
  > - See `paper/ndss27/section/6_paper_results.tex`

- [x] **80.9% increase in 2025 over 2020–2024 average**
  > 2020–2024 average: 0.89%; 2025: 1.61%. Increase = (1.61 - 0.89) / 0.89 = 80.9%.
  > - See `paper/ndss27/section/6_paper_results.tex`, Figure `fig:papers_with_invalid_citations_timetrend`

- [x] **Repeated invalid citation appears in 16 independent papers**
  > "AugMix" erroneous title traced to OpenReview's cite button. Appears across AAAI, IJCAI, and NeurIPS.
  > - See `paper/ndss27/section/6_paper_results.tex`, Case Study 5

- [x] **NDSS has highest proportion of papers with invalid citations (2.56%)**
  > Among the 8 venues, NDSS shows the highest rate by proportion, though absolute count is lower due to smaller volume.
  > - See `paper/ndss27/section/6_paper_results.tex`, Table `tab:invalid_by_venue`

### Survey Claims

- [x] **97 responses, 94 valid (3 removed for inconsistency)**
  > Paired reverse-worded items flagged 3 inconsistent responses. Remaining 94 analyzed.
  > - See `paper/ndss27/section/7_survey_results.tex`

- [x] **87.2% use AI tools for research (n=86)**
  > Self-reported AI tool usage among respondents who answered the question.
  > - See `paper/ndss27/section/7_survey_results.tex`, Figure `fig:survey_key_questions`

- [x] **41.5% copy-paste BibTeX without checking**
  > Behavioral item in survey. 39 of 94 respondents admitted to this practice.
  > - See `paper/ndss27/section/7_survey_results.tex`

- [x] **76.7% of reviewers do not thoroughly check references (n=30)**
  > Self-reported reviewer behavior. 23 of 30 reviewers admitted not thoroughly checking.
  > - See `paper/ndss27/section/7_survey_results.tex`

- [x] **80.0% of reviewers never suspect fake citations (n=30)**
  > 24 of 30 reviewers reported never suspecting fabricated references in submissions.
  > - See `paper/ndss27/section/7_survey_results.tex`

- [x] **70.2% strongly support automated checks**
  > 66 of 94 respondents strongly support deploying automated DOI/reference checking in submission systems. Only 3.2% (3/94) oppose.
  > - See `paper/ndss27/section/7_survey_results.tex`

### CiteVerifier Framework Claims

- [x] **Manual validation: 100% valid accuracy, 98% invalid accuracy**
  > Spot-check of 400 valid + 400 invalid samples. 8 false positives were non-paper sources, out-of-domain works, or poorly indexed items.
  > - See `paper/ndss27/section/5_llm_results.tex`

- [x] **Threshold θ = 0.9 validated empirically**
  > Only 0.4% of real-paper citations fall at or below 0.9; 50.3% of LLM-generated citations do. See CDF analysis.
  > - See `paper/ndss27/section/3_methodology.tex`, Figure `fig:llm_papers_similarity_ecdf`

---

## Formatting Verification

- [ ] **PDF compiles without errors**
  > To be verified after final adaptation pass.

- [ ] **Page count ≤ 13 pages (body only)**
  > To be verified after content trimming.

- [ ] **All cross-references work**
  > To be verified after final compilation.

- [ ] **Figures readable in grayscale**
  > NDSS requires black-and-white print clarity. To be verified.

---

*Last updated: 2026-05-04*
