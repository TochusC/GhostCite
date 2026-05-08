# Archival Analysis Artifacts

This directory contains the analysis of invalid citations found in archived research papers across major computer science conferences.

## Contents

### `analysis.ipynb`
Jupyter notebook performing the empirical analysis of citation validity in published papers.

**Includes:**
- Data loading and preprocessing from archival sources
- Statistical analysis of invalid citations per venue and year
- Breakdown of citation categories and error patterns
- Visualization of trends in citation validity across different research areas
- Distribution analysis of invalid citation frequency

**To reproduce:**
```bash
jupyter notebook analysis.ipynb
```

### `summary.csv`
Aggregated statistical summary of the archival analysis results.

**Columns:**
- Conference/Venue name
- Analysis year/period
- Total papers analyzed
- Papers with at least one invalid citation
- Percentage of papers affected
- Categories of invalid citations found
- Error types and frequencies

## Data Sources

The analysis uses papers from major venues (USENIX Security, NDSS, ACM CCS, etc.) with full reference extraction and validation against authoritative databases (DBLP, CrossRef, arXiv).

## Key Findings

- Distribution of invalid citations across venues and time periods
- Correlation between venue and citation error rates
- Trend analysis showing citation validity patterns over time
- Identification of high-risk citation practices

## Data Privacy & Anonymization

**Important Note on Privacy Protection:**

While the analysis identifies papers containing invalid citations, the publicly released dataset does **not** include paper titles or author names. Instead, the dataset preserves only:
- Citation metadata (titles, authors, venues of the cited references)
- Statistical aggregations at the venue/time-period level
- Error patterns and invalid citation categories

This approach ensures that:
- Individual papers with quality issues cannot be directly identified from the dataset
- The analysis results serve educational purposes without unfairly targeting specific works
- Researchers can study citation validity patterns without accessing sensitive publication metadata

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib, seaborn
- Jupyter notebook

## Contact & Questions

For questions about artifact reconstruction or analysis methodology, refer to the main paper's "Archival Results" section.
