# CHANGELOG.md — Change Log

> Record changes by date. Reverse chronological order.

---

## 2026-05-08

### NDSS 2027 Submission

**Created by**: AI Assistant

**Changes**:

1. **Submitted to NDSS 2027**
   - Submission portal: NDSS 2027 (Summer cycle)
   - Paper: `paper/ndss27/0_0_main.pdf`
   - Status: Under Review

2. **Meta Documents Updated**
   - `README.md`: Current status updated to "Under Review at NDSS 2027"
   - `CURRENT.md`: Rewritten as post-submission snapshot with submission checklist
   - `PLAN.md`: All Phases 1–4 marked complete; Phase 5 added (Under Review / Awaiting Decision)
   - `VERIFY.md`: Formatting verification items marked complete
   - `RESEARCH.md`: Last updated timestamp refreshed

---

## 2026-05-05

### NDSS 适配与 USENIX 审稿意见回复（重大修订）

**创建者**：AI 助手

**背景**：本文在 USENIX Security 2026 被拒（Reviewer A: Weak Reject；Reviewer B: Reject）。本轮修改系统性回应两位审稿人的关切，同时适配 NDSS 2027 的投稿要求。

---

#### Reviewer A（Weak Reject）— 已回复项

| 审稿人意见 | 我们的修改 | 涉及文件 |
|-----------|-----------|---------|
| **"摘要和引言过长"** | 摘要从 9 行精简为紧凑的单段，删除过多具体数字。引言中的实验概述也做了删减（移除了 $800 成本、具体生成率、传播数据）。 | `0_abstract.tex`, `section/1_introduction.tex` |
| **"论文对安全领域的针对性关联不够强"** | 全文增加安全针对性论述：引言第 2 段补充威胁建模/漏洞分类影响；新增第 4 个研究空白（安全社区缺乏证据）；安全专属缓解建议（虚构攻击向量、错归属防御技术）；贡献 1 将幽灵引用定位为"研究诚信的系统性威胁，尤其在安全领域"。 | `section/1_introduction.tex`, `section/8_discussion.tex` |
| **"对研究者，我建议更进一步：引用前至少要读摘要"** | 讨论部分新增明确要求："我们敦促研究者在引用任何论文前，无论其来自 AI 工具还是传统检索，都应至少阅读摘要或直接来自来源的总结。" | `section/8_discussion.tex` |
| **实验 I 的外部有效性** | 在实验 I 新增"实验设置局限性"段落，承认大批量生成设计优先考虑内部有效性而非外部有效性。讨论/局限性中新增"LLM 基准测试的外部有效性"独立段落。 | `section/4_experiment.tex`, `section/8_discussion.tex` |
| **调查方法论：引导性/抽象问题、启动效应、社会期望偏差** | (a) 附录表格中全部 40 道调查问题标签从缩写扩展为完整措辞；(b) 在 `reference/survey/` 新增 Redmiles et al. (2017) 调查方法论最佳实践详细分析；(c) 局限性中新增"调查回答偏差"段落，承认社会期望偏差、人口学问题前置带来的启动效应、缺乏认知访谈/专家预测试。参考文献新增 Redmiles et al. (2017)。 | `table/Appendix/tab_survey_details_full.tex`, `section/8_discussion.tex`, `references.bib`, `reference/survey/` |

---

#### Reviewer B（Reject）— 已回复项

| 审稿人意见 | 我们的修改 | 涉及文件 |
|-----------|-----------|---------|
| **"S&P 相关性不明" / "为何聚焦如此多领域？"** | 同 Reviewer A 的安全相关性回应：全文加强安全框架。决策保留 40 领域结构（已由 arXiv CS 学科分类说明），而非将实验重构为仅限 S&P。 | `section/1_introduction.tex`, `section/8_discussion.tex` |
| **"实验设计未反映研究者真实使用方式"** | 同外部有效性回应。在局限性中明确承认结果为"受控下界，而非直接的真实世界估计值"。 | `section/4_experiment.tex`, `section/8_discussion.tex` |
| **"方法论描述不完整：调查分析和工具评估方法描述不足"** | (a) 实验 III 新增"数据分析"段落，说明描述性统计、开放式 Q59 的主题编码、以及配对反向措辞一致性检查（Q38/Q39）；(b) 实验 II 第 3 步新增 400 引用假阴性抽查的样本量估算理由（95% 置信区间，5% 误差范围）。 | `section/4_experiment.tex` |
| **"图 1 和图 3 难以解读"** | 尚未处理，待后续图表质量专项修改。 | — |

---

#### 可信度提升（用户指出的核心问题）

| 问题 | 修改 | 文件 |
|-------|--------|-------|
| 无法验证的 "first" 声明 | 删除 "the first comprehensive study" → 改为 "a comprehensive study" | `0_abstract.tex`, `section/1_introduction.tex` |
| 过于绝对的措辞 | "confirming" → "finding"；"accelerating crisis" → "facilitate the penetration"；"We strongly argue" → "We argue"；"Our findings reveal" → "Our findings suggest" | `0_abstract.tex`, `section/1_introduction.tex`, `section/8_discussion.tex` |
| 摘要堆砌数字 | 从摘要中移除 7 个具体百分比，移至正文 | `0_abstract.tex` |
| 全文破折号 | 删除所有 em dash（`---`）及句中 en dash；保留范围短横线（如 2020--2025）作为标准学术格式 | 多文件 |

---

#### 结构性修改

| 修改 | 详情 |
|--------|--------|
| **目录命名统一** | `Figures/` → `figure/`，`Tables/` → `table/`，删除冗余 `Tex/` 目录；所有 `\input{}` 和 `\includegraphics{}` 路径更新 | `paper/ndss27/` |
| **表格移回正文** | TABLE VI (models_evaluated) → 第 4 节；TABLE IX (collected_papers) → 第 6 节；TABLE XII (repeated_citation_errors) → 第 6 节 | 多文件 |
| **删除跨模型重叠分析** | 删除附录子章节、图形文件及第 5 节中的重叠引用 | `appendix/`, `section/5_llm_results.tex` |
| **Keyfinding 盒子重排版** | 添加 `\faLightbulb` 图标 + 手动编号；标题栏显示 "Keyfinding 1: LLM 基准测试" | `0_0_main.tex`, `section/5_llm_results.tex`, `section/6_paper_results.tex` |
| **摘要格式** | 从多段合并为标准单段摘要 | `0_abstract.tex` |

---

#### 修改结果

- **页数**：25 页 → 24 页（精简 + 表格移动 + 删除重叠分析）
- **编译**：所有修改过程中零 LaTeX 错误
- **Git 提交**：15 次提交跟踪全部修改

---

## 2026-05-05

### Citation Fix Pass (Post-Audit)

**Created by**: AI Assistant

**Changes**:

1. **Removed `zoteroforum2018ghost`** — misappropriated citation
   - Deleted from `section/1_introduction.tex` (1 occurrence)
   - Deleted from `section/2_background.tex` (2 occurrences)
   - Rewrote sentence in `section/2_background.tex` to remove "online forums" claim (now reads "academic blogs")
   - Deleted orphaned entry from `references.bib`

2. **Removed `risko2016cognitive`** — dead commented-out citation
   - Deleted the commented-out line in `section/7_survey_results.tex`

3. **Corrected `mitchell2023detectgpt` description**
   - Changed "text writing-style analysis" → "zero-shot detection based on probability curvature" in `section/2_background.tex`

4. **Updated VERIFY.md**
   - Moved `zoteroforum2018ghost` and `risko2016cognitive` to "Critical Issues — Fixed"
   - Updated `mitchell2023detectgpt` to `[x]` with fix note

---

## 2026-05-05

### Full Citation Verification Audit

**Created by**: AI Assistant (5 parallel sub-agents)

**Changes**:

1. **VERIFY.md — Citation Verification Section**
   - Extracted all 52 unique citations from `paper/ndss27/section/*.tex`, `appendix/*.tex`, and `0_abstract.tex`
   - Cross-checked against `references.bib`; identified 1 citation missing from bib (`risko2016cognitive`) and 11 orphaned bib entries
   - Verified each citation via Web Search for bibliographic accuracy (existence, authors, title, year, venue, pages, DOI/URL)
   - Assessed positional appropriateness (whether cited work supports the claim at that location)
   - **2 Critical Issues flagged**:
     - `zoteroforum2018ghost` — misappropriated (Zotero Word support post cited as fabricated academic references)
     - `risko2016cognitive` — missing bib entry, appears only in commented-out LaTeX line
   - **11 Minor Deviations flagged**:
     - `bai2023qwen` — covers original Qwen, not Qwen3-Flash variant used
     - `ieee2025ai-policy` — year may be access date, not original publication year
     - `levenshtein1966binary` — wrong entry type, missing pages
     - `lipton2018troubling` — bib year should be 2019 (journal pub date)
     - `maslej2025artificial` — loose appropriateness for temporal split claim
     - `mitchell2023detectgpt` — technique mischaracterized as "writing-style analysis"
     - `schloegel2025confusing` — missing `booktitle`
     - `scrapingdog` — `journal` field inappropriate (competitor blog post)
     - `simkin2003read` — incorrect month, missing pages, abbreviated journal name
     - `vaswani2017attention` — missing page numbers
     - `zhang2025siren` — wrong pages, missing volume/number
   - **39 citations fully verified and correct**
   - Listed 11 unreferenced bib entries for potential cleanup

---

## 2026-05-04

### Meta Document Refresh

**Created by**: AI Assistant

**Changes**:

1. **README.md**
   - Rewrote to reflect actual GhostCite research content (LLM benchmark, archival analysis, user survey)
   - Updated directory structure to match `paper/ndss27/` layout
   - Added current status with completed/in-progress/pending tasks
   - Added key contributions summary
   - Updated target conference info (NDSS 2027)

2. **RESEARCH.md**
   - Filled in all placeholder sections with actual findings from the paper
   - Documented Q1/Q2/Q3 research questions and answers
   - Added key findings for LLM benchmark, archival analysis, and survey
   - Added Ghost Citation Lifecycle framework
   - Documented research gaps addressed
   - Added academic judgments
   - Added methodology notes (validation, threshold calibration, manual verification protocol)

3. **PLAN.md**
   - Restructured phases to reflect actual project state (paper is written; NDSS adaptation remains)
   - Phase 1: marked all content sections as completed
   - Phase 2: added NDSS-specific adaptation tasks (content emphasis, format compliance, double-blind)
   - Phase 3: added quality assurance checklist (compilation, page count, terminology, references, figures)
   - Phase 4: added final preparation tasks (conflict-of-interest, proofread, cover letter, artifact)

4. **VERIFY.md**
   - Retained NDSS submission requirement verifications
   - Added comprehensive "Paper Content — Core Claims" section
   - Organized claims by: LLM Benchmark, Archival Analysis, Survey, CiteVerifier Framework
   - Each claim includes brief justification and source reference within the paper

5. **CURRENT.md**
   - Updated to reflect actual paper completion status
   - Added concrete next steps for NDSS submission

---

## 2026-05-02

### Project Initialization

**Created by**: AI Assistant

**Changes**:

1. **Directory Structure**
   - Created `paper/usenix26/` - Original USENIX Security submission
   - Created `paper/ndss27/` - NDSS 2027 submission (new target)
   - Created `reference/` - Research materials
   - Created `reference/survey/` - Special topic documents

2. **File Organization**
   - Moved original paper files to `paper/usenix26/`
   - Downloaded NDSS template (IEEEtran.cls + ndss2026.tex)
   - Created NDSS main file: `paper/ndss27/0_0_main.tex`

3. **Meta Documents (Initial Skeletons)**
   - Created `README.md` - Project overview
   - Created `RESEARCH.md` - Research insights (placeholder)
   - Created `PLAN.md` - Task plan (placeholder)
   - Created `VERIFY.md` - Fact verification checklist (placeholder)
   - Created `CHANGELOG.md` - This file
   - Created `CURRENT.md` - Current status

4. **Reference Materials**
   - Created `reference/ndss_cfp.md` - NDSS Call for Papers summary
   - Documented key differences between USENIX and NDSS
   - Listed submission requirements and deadlines

---

## Notes

- Original paper was targeting USENIX Security 2026
- Now adapting for NDSS 2027 submission
- Key changes needed: page limit adjustment, systems/network focus strengthening
- Meta documents were refreshed on 2026-05-04 to reflect actual paper content

---
