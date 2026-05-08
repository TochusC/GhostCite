# RESEARCH.md — Research Content and Insights

> Core findings, key insights, academic judgments, and research gaps for GhostCite

---

## Research Questions

We seek systematic answers to three fundamental questions:

- **Q1 (Prevalence)**: How frequently do LLMs hallucinate citations across research domains?
- **Q2 (Contamination)**: To what extent have invalid citations entered published academic literature?
- **Q3 (Failure)**: Why do authors and reviewers fail to detect them?

---

## Key Findings

### 1. LLMs Are Unreliable for Citation Generation (Q1)

We benchmarked **13 state-of-the-art LLMs** (GPT-5, Claude-4, DeepSeek, Grok 4, Qwen-3, ERNIE, Hunyuan, and others) across **40 computer science research domains** aligned with arXiv CS subject classes. The experiment generated **375,440 citations** from **22,800 API interactions** (~\$800 total cost), of which **331,809 were successfully extracted** (88.38\% extraction rate) from **20,653 well-formed JSON outputs** (90.58\% format compliance).

**Hallucination rates span 14.23\% (DeepSeek) to 94.93\% (Hunyuan)** — a roughly 6.7$\times$ difference. All models hallucinate to some degree.

**Domain sensitivity is severe**: within the same model, hallucination rates vary by up to 51.39 percentage points across domains. Even the best-performing model (DeepSeek) reaches 52.5\% hallucination in some domains (e.g., OH) while achieving 2.6\% in others (e.g., CV). Average across models ranges from 28.80\% (Computation and Language) to 80.19\% (Digital Libraries).

**Temporal pattern**: LLMs preferentially hallucinate citations with recent publication years. Hallucination rates increase from 27.61\% (2000) to 98.75\% (2025), fitting an exponential curve with $R^2 = 0.94$.

**Stability analysis**: Valid citations are notably more stable (DeepSeek mean 0.58) vs. hallucinated (0.23). Well-known titles (NeRF, RAG, U-Net) recur across runs.

**LLMs cannot self-correct**: when prompted to validate citations, the 13 models achieved only **38\% average accuracy** — below random guessing (50\%). Only ERNIE exceeded 50\% (56\%), but did so by aggressively flagging valid citations as invalid (88\% false positive rate on valid citations).

> **Insight**: Citation hallucination is a fundamental limitation of LLMs' bibliographic knowledge, not an artifact of prompting strategy. Users cannot assume any "state-of-the-art" model is reliable for bibliographic tasks.

---

### 2. Ghost Citations Have Penetrated the Published Record (Q2)

We ethically collected **56,381 papers** from eight top-tier venues (NeurIPS, ICML, IJCAI, AAAI, IEEE S\&P, USENIX Security, ACM CCS, NDSS) spanning 2020–2025, selected by CSRankings. We extracted **2,199,409 citations** and verified them with CiteVerifier.

Of 2,530 flagged citations, manual verification classified:
- 490 (19.4\%) non-academic sources
- 1,301 (51.4\%) valid (confirmed through extensive manual search)
- **739 (29.2\%) invalid** — 136 metadata errors + 603 ghost citations

**1.07\% of papers (604/56,381) contain at least one invalid citation**: 133 papers (0.24\%) with metadata errors and 486 papers (0.86\%) with ghost citations (15 papers had both).

**2025 shows a dramatic inflection point**: invalid citation rates surged **80.9\%** over the 2020–2024 average (from 0.89\% to 1.61\%). This aligns temporally with the widespread adoption of autonomous AI agent workflows.

**Error propagation is real**: we identified "repeated invalid citations" appearing in up to **16 independent papers** (e.g., an erroneous "AugMix" title traced to OpenReview's cite button). Researchers copy citations from existing papers, compounding mistakes.

**Distribution is widespread**: invalid citations appear across all venues. While AI/ML venues have higher absolute counts (due to volume), the proportion is similar: 1.08\% (AI) vs. 1.01\% (Security). NDSS shows the highest proportion (2.56\% of papers).

**Clustering suggests AI-assisted generation**: 544 papers (88.7\%) contain a single invalid citation, while 68 (11.3\%) contain two or more, with one paper containing 9. Clusters of invalid citations are a stronger signal of systematic AI-assisted generation than isolated human errors.

> **Insight**: The published scientific record is already contaminated. The 2025 surge suggests we are at the beginning of an accelerating crisis, not observing a stable baseline.

---

### 3. Human Verification Mechanisms Systematically Fail (Q3)

We surveyed **97 researchers** (94 valid responses after removing 3 inconsistent samples) across career stages and research areas, recruited via social media and targeted emails to 300 randomly sampled authors and PC members.

**High AI adoption, low actual verification**: 87.2\% use AI-powered tools for research, and 86.7\% of AI users claim to "always verify" AI-generated citations. Yet behavioral data reveals:
- **41.5\%** copy-paste BibTeX without checking
- **17.3\%** cite AI-suggested papers without reading them
- **44.4\%** take no action when encountering suspicious references

**Reviewer trust-by-default norm**: among reviewers (n=30):
- **76.7\%** do not thoroughly check references
- **80.0\%** never suspect fake citations in submissions

**Peer review is viewed as ineffective**: 74.5\% rate peer review as "not very effective" or "ineffective" at catching citation errors.

**Severity perception**: 76.6\% consider it a "major problem" or "critical crisis" (44.7\% critical crisis, 31.9\% major problem).

**Responsibility attribution**: 91.5\% blame authors alone; only 3.2\% reviewers, 2.1\% publishers, 2.1\% AI developers.

**Community readiness for intervention**: despite the above, **70.2\%** strongly support deploying automated DOI/reference checking in submission systems, with only 3.2\% opposed.

> **Insight**: The problem persists not due to ignorance (76.6\% consider it a major problem or critical crisis), but due to systemic workflow gaps where verification is cognitively offloaded to trust-based assumptions.

---

## The Ghost Citation Lifecycle

Our three studies collectively map a "pollution pipeline" through which ghost citations propagate from LLM outputs to the permanent scientific record:

1. **Generation**: LLMs synthesize plausible-looking but non-existent citations from parametric memory, combining real author names, authentic venue titles, and domain-specific terminology into structurally valid but fabricated references.

2. **Adoption**: researchers trust and adopt AI outputs with superficial verification ("looks reasonable"). Cognitive offloading leads users to accept AI-generated citations without independent verification.

3. **Review Failure**: reviewers lack capacity and assume good faith; trust-by-default norms allow passage. Peer review operates on presumption of good faith, and submission systems do not flag potentially invalid references automatically.

4. **Publication & Propagation**: once published, errors enter bibliographic databases and are copied by subsequent researchers. Each subsequent citation makes the error harder to spot, creating a self-reinforcing cycle of contamination.

This self-reinforcing pipeline creates an **illusion of evidential support** while contaminating the citation graph with phantom nodes and invalid edges. If this continues, the community faces a choice: accept growing contamination or shift to universal verification and impose heavy burdens on every researcher.

---

## Research Gaps Addressed

1. **Scalable detection gap**: prior work highlighted risks but lacked automated verification at scale. CiteVerifier fills this with a cascaded, multi-source retrieval pipeline tolerant of format heterogeneity.
2. **Empirical measurement gap**: no prior work measured ghost citation prevalence in both LLM outputs *and* the published record at this scale.
3. **Behavioral explanation gap**: prior work did not explain *why* verification fails. Our survey identifies the verification gap, cognitive offloading, and trust-by-default norms as root causes.

---

## Academic Judgments

### Judgment 1: Ghost citations are a systemic threat, not a minor quality issue
The 2025 surge, error propagation across 16+ papers, and the verification gap collectively indicate that ghost citations threaten to shift the scholarly community from a presumption of trust to one of systematic skepticism — an unsustainable burden.

### Judgment 2: The problem requires coordinated multi-stakeholder intervention
No single fix suffices. Researchers must verify, venues must deploy automated checks, AI developers must ground outputs in retrieval, and the community must build shared infrastructure. Our survey shows 70.2\% community support for automated checks, indicating readiness.

### Judgment 3: Detection is a conservative lower bound
Our detected 1.07\% invalid citation rate is likely conservative. The threshold-based classifier ($\theta = 0.9$) may miss hallucinations that closely resemble real papers, and some legitimate but poorly indexed works may be misclassified. The true rate is likely higher.

---

## Recommendations by Stakeholder

### For Researchers
- Treat all AI-generated output as unverified until checked
- Use retrieval-grounded tools over purely generative ones
- Check each cited title in a trusted index; treat missing DOIs as red flags
- Never cite any paper without reading at least its abstract or a direct summary from the source

### For Conferences and Journal Organizers
- Integrate automated citation verification into submission pipelines (70.2\% strong support)
- Require structured reference metadata at submission
- Provide reviewers with compact citation-risk summaries
- Establish clear policies on AI-assisted citation generation

### For AI Tool Developers
- Ground citation outputs in retrieval from verified sources rather than pure generation
- Clearly distinguish retrieved from generated content
- Enforce structured outputs with evidence fields (DOI, URL, database identifier)
- Surface "not found" signals instead of fabricating metadata

### For the Research Community
- Develop shared verification infrastructure and norms for AI-assisted bibliography construction
- Invest in detection research and conduct regular measurement studies to track trends
- Build open validation APIs and benchmark datasets
- Standardize reporting so policies and tools can evolve with evidence

---

## Methodology Notes

- **CiteVerifier validation**: manual spot-check of 400 valid + 400 invalid samples confirmed 100\% valid accuracy and 98\% invalid accuracy (8 false positives were non-paper sources, out-of-domain works, or poorly indexed items).
- **Threshold calibration**: $\theta = 0.9$ was validated empirically using CDF of title similarity for real-paper citations (only 0.4\% fall at or below 0.9) vs. LLM-generated citations (50.3\% at or below 0.9).
- **Manual verification protocol**: 16-person team, independent review, expert double-check of all invalid classifications, approximately one month of effort.
- **Survey validity**: paired reverse-worded items flagged inconsistent responses; 3 of 97 were removed.

---

## Limitations

- **Online/CoT configuration limits**: online-search/chain-of-thought via third-party API flags may not activate vendors' full native toolchains.
- **Detection conservatism**: title-similarity only $\rightarrow$ conservative lower bound; may miss hallucinations resembling real papers; some legitimate but poorly indexed works may be misclassified.
- **External validity of LLM benchmark**: fixed-number citation generation per domain ensures fair cross-model comparison but differs from real-world use where citations are produced while drafting arguments.
- **Survey self-report bias**: social-desirability bias may cause over-reporting of diligence; high self-reported verification (86.7\%) alongside admitted risky practices (41.5\%) is suggestive of this bias.

---

*Last updated: 2026-05-08*
