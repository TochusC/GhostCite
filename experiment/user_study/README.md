# User Study Artifacts

This directory contains materials and analysis from the user study investigating how researchers and reviewers interact with citations, verify references, and perceive citation integrity issues.

## Contents

### Study Data & Results

#### `statistics.csv`
Aggregated statistical summary of user study responses.

**Includes:**
- Response counts per question
- Demographic breakdowns (career stage, research area, publication experience)
- Aggregate percentages for key questions
- Confidence intervals / margin of error
- Missing data indicators

**Key Metrics:**
- Total valid responses: 94 (after quality filtering)
- Demographic distribution
- Response rates per question
- Data quality indicators

#### `bibtex_conflict_invalid_rows.csv`
Records of participants with conflicting responses (reverse-coded validation questions).

**Columns:**
- `participant_id`: Anonymized participant identifier
- `conflict_type`: Type of conflict detected
- `question_pair`: Which paired items conflicted
- `decision`: Whether response was retained or removed
- `notes`: Reason for inclusion/exclusion decision

**Purpose:** Transparency in data cleaning and quality control; excludes n=3 responses per paper.

### Analysis & Reporting

#### `user_study_analysis.ipynb`
Comprehensive Jupyter notebook analyzing user study findings.

**Analyzes:**
- AI adoption rates and tool usage patterns
- Citation verification behaviors (gap between claimed and actual verification)
- Hallucination exposure and reporter experience
- Perceived severity of citation integrity issues
- Responsibility attribution (authors vs. reviewers vs. publishers)
- Support for automated solutions
- Reviewer perspectives on citation errors

**To run:**
```bash
jupyter notebook user_study_analysis.ipynb
```

#### `bibtex_conflict_report.md`
Detailed report of data quality procedures and quality assurance findings.

**Includes:**
- Survey design and pilot testing
- Inclusion/exclusion criteria
- Conflict detection methodology
- Final sample composition
- Response patterns and outlier analysis
- Limitations and potential biases

### Survey Materials

#### Survey Questions (in main paper appendix)
Complete survey instrument with:
- Question text (exact wording)
- Response options
- Question numbering and ordering
- Estimated completion time
- Instructions to participants

*Full survey text available in paper appendix.*

## Methodology Summary

### Participant Recruitment
- Open call to computer science researchers
- Distributed via academic mailing lists and social media
- No compensation offered
- Informed consent obtained before survey

### Inclusion Criteria
- Active in academic research (any career stage)
- Published or submitted at least one paper
- English fluency
- Completed all data quality check questions

### Quality Control
- Reverse-coded paired BibTeX verification items
- Removed 3 responses (n=3) with conflicting answers
- Final n=94 valid responses
- No missing data exclusions (all participants completed all questions)

### Sample Composition

By career stage:
- PhD students: ~35%
- Postdocs / Early career: ~25%
- Mid-career faculty: ~25%
- Senior faculty: ~15%

By research area:
- Systems security: ~30%
- Network security: ~15%
- Software security: ~18%
- ML/Privacy: ~20%
- Other areas: ~17%

## Key Findings

### AI Adoption
- **87.2%** (75/86) of respondents use AI-powered tools for research
- **46.7%** use AI for "specific difficult paragraphs"
- **29.3%** use AI for "almost every sentence"
- **22.7%** use AI only for "final proofreading"

### Citation Verification Gap
- **86.7%** claim to "always verify" AI-generated references
- **41.5%** copy-paste BibTeX without checking
- **17.3%** cite AI-suggested papers without reading them
- **Reviewers:** 76.7% do not thoroughly check references

### Hallucination Exposure
- **41.3%** report encountering hallucinated citations "often" or "very often"
- **74.5%** perceive peer review as ineffective at catching errors
- **80%** of reviewers never suspect fake/hallucinated references

### Perceived Severity & Support
- **76.6%** consider hallucinated citations a "major problem" or "critical crisis"
- **91.5%** attribute responsibility for citations to authors
- **70.2%** strongly support automated DOI/citation checking in submission systems
- **26.6%** respond "maybe" to automated solutions

## Dependencies

```bash
pip install pandas numpy jupyter matplotlib seaborn scipy
```

## Reproduction

1. **Load and explore data**:
   ```python
   import pandas as pd
   stats = pd.read_csv('statistics.csv')
   conflicts = pd.read_csv('bibtex_conflict_invalid_rows.csv')
   ```

2. **Run analysis notebook**:
   ```bash
   jupyter notebook user_study_analysis.ipynb
   ```

3. **Generate visualizations**:
   All figures and tables are produced via the notebook

## Data Availability & Privacy

- All identifiable information removed
- Participants assigned anonymous IDs
- No demographic identifiers that could enable re-identification
- Institutional affiliations not stored with responses
- Available upon request (survey data) or as part of this OSF project

## Ethical Considerations

- Study approved by institutional review board (if required)
- Informed consent obtained from all participants
- Participation was voluntary
- No deception used in study design
- Data stored securely with access restrictions

## Files Reference

- `requirements.txt` - Python dependencies
- `codebook.md` - Survey item codebook and answer encodings
- `raw_responses_anonymized.csv` - Complete response dataset (if available)

## Limitations

- Self-reported behavior may not reflect actual practice
- English-language speakers; results may not generalize globally
- Computer security researchers may not represent all STEM fields
- Voluntary participation may introduce selection bias
- Cross-sectional design; cannot infer causality

## Contact & Questions

For instrument details, recruitment procedures, or analysis methodology, see the main paper's "Survey Findings" section (Section 7) and Appendix on survey details.
