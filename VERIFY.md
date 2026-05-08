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

## Citation Verification (Full Bibliographic Audit)

> **Methodology**: All 52 unique citations appearing in the paper body were extracted and cross-checked against `references.bib`. Each citation was verified via Web Search for bibliographic accuracy (existence, authors, title, year, venue, pages, DOI/URL) and assessed for positional appropriateness (whether the cited work supports the claim at that location).

### Critical Issues — Fixed

- [x] **zoteroforum2018ghost** ~~(was `[!]`)~~ — **FIXED: Removed from paper and `references.bib`**
  > The Zotero Forums post was a misattribution (technical support about orphaned Word citation fields, not fabricated academic references). All three occurrences in `section/1_introduction.tex` and `section/2_background.tex` were removed; the orphaned bib entry was also deleted from `references.bib`.
  > - Fixed in commit 2026-05-05

- [x] **risko2016cognitive** ~~(was `[!]`)~~ — **FIXED: Removed commented-out line**
  > The citation only appeared in a commented-out LaTeX line (`%`) in `section/7_survey_results.tex` with no bib entry. The entire commented line was deleted.
  > - Fixed in commit 2026-05-05

### Critical Issues — Remaining

> None.

### Verified Citations — Minor Deviations

- [~] **bai2023qwen** (Appears in: section/3_methodology.tex)
  > The arXiv preprint arXiv:2309.16609 exists and is the original Qwen Technical Report (2023). However, it covers the original Qwen model, not the Qwen3-Flash variant used in the paper. A Qwen3-specific citation would be more accurate.
  > - https://arxiv.org/abs/2309.16609

- [~] **ieee2025ai-policy** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > The IEEE policy page exists and is correct, but `year = 2025` may represent an access/verification date rather than the original publication year. The policy was already visible in citations from 2023. Consider updating the year or adding a note.
  > - https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/#ai-generated-content

- [~] **levenshtein1966binary** (Appears in: section/1_introduction.tex, section/3_methodology.tex)
  > Paper exists. Deviation: `@inproceedings` should be `@article`; `pages = {707--710}` is missing from the bib entry.
  > - https://nymity.ch/sybilhunting/pdf/Levenshtein1966a.pdf

- [~] **lipton2018troubling** (Appears in: section/2_background.tex)
  > Paper exists. Deviation: The bib year is 2018, but the *Queue* journal publication date was February 2019 (arXiv preprint was July 2018). For a journal citation, year should be 2019.
  > - https://doi.org/10.1145/3317287.3328534

- [~] **maslej2025artificial** (Appears in: section/4_experiment.tex)
  > Report exists (AI Index Report 2025). Appropriateness is loose: it provides general background on AI trends but does not specifically establish the pre-LLM/post-LLM temporal split (2020–2022 vs. 2023–2025). The periodization is the authors' own methodological choice.
  > - https://arxiv.org/abs/2504.07139

- [x] **mitchell2023detectgpt** ~~(was `[~]`)~~ — **FIXED: Description corrected**
  > Paper exists (ICML 2023). ~~Deviation: The citing paper characterizes DetectGPT as "text writing-style analysis," but DetectGPT is actually a zero-shot detection method based on probability curvature.~~ **Fixed:** Text in `section/2_background.tex` changed to "zero-shot detection based on probability curvature."
  > - https://proceedings.mlr.press/v202/mitchell23a.html

- [~] **schloegel2025confusing** (Appears in: section/1_introduction.tex, section/ethics.tex)
  > Paper exists (USENIX Security 2025). Deviation: Missing `booktitle` field (required for `@inproceedings`); URL points to the presentation page rather than the paper PDF.
  > - https://www.usenix.org/conference/usenixsecurity25/presentation/schloegel

- [~] **scrapingdog** (Appears in: section/3_methodology.tex)
  > URL reachable. Deviation: `journal = {Scrape.do}` is inappropriate—this is a competitor's comparison blog post, not a journal. Citing the official ScrapingDog documentation would be more neutral.
  > - https://scrape.do/compare/scrapingdog-vs-scrapedo/

- [~] **simkin2003read** (Appears in: section/1_introduction.tex, section/3_methodology.tex)
  > Paper exists. Deviation: `month = {01}` is incorrect (issue is vol. 14, no. 3, not January); `pages` field is empty; journal abbreviated as `Complex Syst.` instead of `Complex Systems`.
  > - https://doi.org/10.25088/ComplexSystems.14.3.269

- [~] **vaswani2017attention** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Paper exists (NeurIPS 2017). Deviation: Missing page numbers (5998–6008).
  > - https://papers.nips.cc/paper/7181-attention-is-all-you-need

- [~] **zhang2025siren** (Appears in: section/2_background.tex)
  > Paper exists (*Computational Linguistics*, 2025). Deviation: Bib lists `pages = {1--46}` and omits `volume = {51}`, `number = {4}`. Actual published pages are 1373–1418.
  > - https://doi.org/10.1162/coli_a_16

### Verified Citations — Fully Correct

- [x] **ISO690_2021** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > ISO 690:2021 exists with exact title, published by ISO in 2021 (4th edition). URL resolves correctly. Appropriately cited for bibliographic format heterogeneity.
  > - https://www.iso.org/standard/72642.html

- [x] **arxivCSClasses** (Appears in: section/1_introduction.tex, section/4_experiment.tex)
  > The arXiv CS archive page is reachable and enumerates the computer-science subject classes. Appropriately cited as the source for the 40-domain taxonomy.
  > - https://arxiv.org/archive/cs

- [x] **bailey2012menlo** (Appears in: section/1_introduction.tex, section/ethics.tex)
  > Verified in *IEEE Security & Privacy*, vol. 10, no. 2, pp. 71–75, 2012. DOI 10.1109/MSP.2012.52. Appropriately cited for ethical principles in ICT/security research.
  > - https://doi.org/10.1109/MSP.2012.52

- [x] **baker2016reproducibility** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified in *Nature* 533(7604):452–454, 2016. DOI 10.1038/533452a. Appropriately cited as a landmark meta-science study on reproducibility.
  > - https://doi.org/10.1038/533452a

- [x] **bender2021dangers** (Appears in: section/2_background.tex)
  > Verified in FAccT 2021, pp. 610–623. DOI 10.1145/3442188.3445922. Appropriately cited for the "stochastic parrots" thesis about LLMs privileging form over truth.
  > - https://doi.org/10.1145/3442188.3445922

- [x] **bengio2003neural** (Appears in: section/2_background.tex)
  > Verified in *JMLR* vol. 3, pp. 1137–1155, 2003. Appropriately cited as the theoretical basis for autoregressive token prediction in LLMs.
  > - https://www.jmlr.org/papers/v3/bengio03a.html

- [x] **chairs2025iclr** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: ICLR blog post published 19 Nov 2025 at the exact URL. Appropriately cited for conference policy responses to AI-generated content.
  > - https://blog.iclr.cc/2025/11/19/iclr-2026-response-to-llm-generated-papers-and-reviews/

- [x] **consultmu2026ghost** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: Blog post hosted at given URL, discusses fabricated references in generative AI outputs. Appropriately cited to define "ghost references."
  > - https://www.consultmu.co.uk/ghost-references-cause-many-genai-errors/

- [x] **cotton2024chatting** (Appears in: section/2_background.tex)
  > Verified in *Innovations in Education and Teaching International*, vol. 61, no. 2, pp. 228–239, 2024. DOI 10.1080/14703297.2023.2190148. Appropriately cited for academic-integrity challenges with ChatGPT.
  > - https://doi.org/10.1080/14703297.2023.2190148

- [x] **csrankings** (Appears in: section/1_introduction.tex, section/4_experiment.tex)
  > Verified: CSRankings is maintained by Emery Berger at https://csrankings.org. Appropriately cited to justify venue selection.
  > - https://csrankings.org

- [x] **dwivedi2023so** (Appears in: section/2_background.tex)
  > Verified in *International Journal of Information Management*, Vol. 71, article 102642, 2023. DOI 10.1016/j.ijinfomgt.2023.102642. Appropriately cited for generative AI proliferation in research.
  > - https://www.sciencedirect.com/science/article/pii/S0268401223000233

- [x] **fister2016toward** (Appears in: section/2_background.tex)
  > Verified in *Frontiers in Physics*, Vol. 4, article 49, 2016. DOI 10.3389/fphy.2016.00049. Appropriately cited for citation manipulation practices.
  > - https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2016.00049/full

- [x] **gptzero2025nips** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: URL reachable. Report titled "GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers," dated Jan 2026. Appropriately cited.
  > - https://gptzero.me/news/neurips/

- [x] **gptzero2026iclr** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: URL reachable. Report documents 50+ hallucinations in ICLR 2026 submissions, published Dec 2025. Appropriately cited.
  > - https://gptzero.me/news/iclr-2026/

- [x] **greenberg2009how** (Appears in: section/2_background.tex)
  > Verified in *BMJ* 2009;339:b2680. DOI 10.1136/bmj.b2680. Appropriately cited for citation distortions creating false authority.
  > - https://doi.org/10.1136/bmj.b2680

- [x] **grobid-client-python** (Appears in: section/3_methodology.tex)
  > Verified: GitHub repository exists at given URL, maintained by Patrice Lopez and Luca Foppiano. Appropriately cited for GROBID parser usage.
  > - https://github.com/kermitt2/grobid-client-python

- [x] **huang2023survey** (Appears in: section/2_background.tex)
  > Verified: arXiv:2311.05232, 2023 (later published in *ACM TOIS*, 2025). Appropriately cited as a major LLM hallucination survey.
  > - https://arxiv.org/abs/2311.05232

- [x] **ioannidis2005most** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified in *PLoS Medicine*, 2(8):e124, 2005. PMID 16060722. Appropriately cited as a landmark meta-science paper.
  > - https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124

- [x] **ji2023survey** (Appears in: section/2_background.tex)
  > Verified in *ACM Computing Surveys*, 55(12):1-38, 2023. Appropriately cited as a comprehensive hallucination survey.
  > - https://dl.acm.org/doi/10.1145/3571730

- [x] **kaplan1965norms** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified in *American Documentation*, 16(3):179-184, 1965. DOI 10.1002/asi.5090160305. Appropriately cited for citation norms.
  > - https://ideas.repec.org/a/bla/amedoc/v16y1965i3p179-184.html

- [x] **kirchenbauer2023watermark** (Appears in: section/2_background.tex)
  > Verified in ICML 2023, pp. 17061–17084. Appropriately cited as a watermarking detection method.
  > - https://proceedings.mlr.press/v202/kirchenbauer23a.html

- [x] **lee2025impact** (Appears in: section/2_background.tex)
  > Verified in CHI 2025. DOI 10.1145/3706598.3713778. Appropriately cited for self-reported verification behavior among knowledge workers.
  > - https://doi.org/10.1145/3706598.3713778

- [x] **li2023halueval** (Appears in: section/2_background.tex)
  > Verified: arXiv:2305.11747. Appropriately cited as a hallucination evaluation benchmark.
  > - https://arxiv.org/abs/2305.11747

- [x] **lin2022truthfulqa** (Appears in: section/2_background.tex)
  > Verified in ACL 2022, pp. 3214–3252. Appropriately cited as a factuality benchmark.
  > - https://aclanthology.org/2022.acl-long.229/

- [x] **lund2023chatgpt** (Appears in: section/2_background.tex)
  > Verified in *JASIST*, Vol. 74, No. 5, pp. 570–581, 2023. DOI 10.1002/asi.24750. Appropriately cited for ChatGPT in scholarly publishing.
  > - https://doi.org/10.1002/asi.24750

- [x] **merton1973sociology** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: University of Chicago Press, 1973. Appropriately cited as the canonical source for scientific citation norms.
  > - https://press.uchicago.edu/ucp/books/book/chicago/S/bo5984499.html

- [x] **nature2023tools** (Appears in: section/2_background.tex)
  > Verified in *Nature* Vol. 613, No. 7945, p. 612, 2023. DOI 10.1038/d41586-023-00191-1. Appropriately cited for Nature's AI usage ground rules.
  > - https://doi.org/10.1038/d41586-023-00191-1

- [x] **newman2001structure** (Appears in: section/2_background.tex)
  > Verified in *PNAS* 98(2):404–409, 2001. DOI 10.1073/pnas.98.2.404. Appropriately cited for citation graph foundations.
  > - https://doi.org/10.1073/pnas.98.2.404

- [x] **oladokun2025hallucitation** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified in *Journal of Web Librarianship* 19(1):62–92, 2025. DOI 10.1080/19322909.2025.2482093. Appropriately cited for hallucinated citations in ChatGPT outputs.
  > - https://doi.org/10.1080/19322909.2025.2482093

- [x] **openrouter** (Appears in: section/4_experiment.tex)
  > Verified: https://openrouter.ai is operational. Appropriately cited for API aggregation platform.
  > - https://openrouter.ai

- [x] **redmiles2017survey** (Appears in: section/8_discussion.tex)
  > Verified: UMD Technical Report CS-TR-5055, 2017. Appropriately cited for social-desirability bias in self-reported surveys.
  > - https://drum.lib.umd.edu/items/683d78b0-a0e3-4fae-9c93-b75aae4ad11b

- [x] **rossow2012prudent** (Appears in: section/1_introduction.tex)
  > Verified in *2012 IEEE S&P*, pp. 65–79. DOI 10.1109/SP.2012.14. Appropriately cited as a landmark security meta-science paper.
  > - https://doi.org/10.1109/SP.2012.14

- [x] **sakai2026hallucitation** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: arXiv:2601.18724, 2026. Appropriately cited for ACL-focused hallucinated reference analysis.
  > - https://arxiv.org/abs/2601.18724

- [x] **shumailov2024ai** (Appears in: section/2_background.tex)
  > Verified in *Nature* 631(8022):755–759, 2024. DOI 10.1038/s41586-024-07566-y. Appropriately cited for model collapse when training on synthetic data.
  > - https://doi.org/10.1038/s41586-024-07566-y

- [x] **simkin2005stochastic** (Appears in: section/2_background.tex)
  > Verified in *Scientometrics* Vol. 62, No. 3, pp. 367–384, 2005. DOI 10.1007/s11192-005-0028-2. Appropriately cited for citation copying and error propagation.
  > - https://doi.org/10.1007/s11192-005-0028-2

- [x] **smith2006peer** (Appears in: section/2_background.tex)
  > Verified in *Journal of the Royal Society of Medicine* Vol. 99, No. 4, pp. 178–182, 2006. DOI 10.1177/014107680609900414. Appropriately cited for peer review flaws.
  > - https://doi.org/10.1177/014107680609900414

- [x] **sweetland1989errors** (Appears in: section/2_background.tex)
  > Verified in *The Library Quarterly* Vol. 59, No. 4, pp. 291–304, 1989. DOI 10.1086/602160. Appropriately cited as a classic study on bibliographic citation errors.
  > - https://doi.org/10.1086/602160

- [x] **tay2025why** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified: Substack post from Dec 2025 at given URL. Appropriately cited for ghost references in the LLM era.
  > - https://aarontay.substack.com/p/why-ghost-references-still-haunt

- [x] **thorp2023chatgpt** (Appears in: section/1_introduction.tex, section/2_background.tex)
  > Verified in *Science* Vol. 379, No. 6630, p. 313, 2023. DOI 10.1126/science.adg7879. Appropriately cited as a foundational policy statement on AI in publishing.
  > - https://doi.org/10.1126/science.adg7879

- [x] **wagstaff2012machine** (Appears in: section/2_background.tex)
  > Verified: arXiv:1206.4656, 2012. Appropriately cited for ML evaluation pitfalls.
  > - https://arxiv.org/abs/1206.4656

### Unreferenced Bib Entries (Orphaned)

The following 11 entries exist in `references.bib` but are **never cited** in the paper body. Consider removing them to keep the bibliography lean:

- `achiam2023gpt` — GPT-4 technical report
- `berger2019goto` — CSRankings goto statement critique
- `bommasani2021opportunities` — Foundation models opportunities and risks
- `chen2021evaluating` — Evaluating large language models
- `gao2023pal` — Program-aided language models
- `garfield1980citation` — Citation indexing history
- `liang2022holistic` — Holistic evaluation of language models (HELM)
- `liu2024deepseek` — DeepSeek-V3 technical report
- `nature2023ai` — Nature AI image generation policy
- `team2023gemini` — Gemini technical report
- `yan2024practical` — Practical attacker on LLM watermarking

---

## Formatting Verification

- [x] **PDF compiles without errors**
  > Verified before submission. Zero LaTeX errors/warnings.

- [x] **Page count ≤ 13 pages (body only)**
  > Verified before submission. Body fits within limit.

- [x] **All cross-references work**
  > Verified before submission. All references resolve correctly.

- [x] **Figures readable in grayscale**
  > Verified before submission. NDSS black-and-white print clarity confirmed.

---

*Last updated: 2026-05-08*
