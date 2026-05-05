# INIT.md -- Workspace Initialization

> Any agent (human or AI) taking over a research project can follow this workflow to initialize the workspace.

---

## Root Directory Principle

**Only Meta documents (uppercase .md) in the root directory.** All other content goes into subfolders.

### Meta Documents

| File | Responsibility | For Whom |
|------|---------------|----------|
| `INIT.md` | Initialization workflow (this file) | First-time project taker |
| `README.md` | Project entry point | Anyone |
| `RESEARCH.md` | Research content and insights | Those who need to understand the research |
| `PLAN.md` | Task plan and work steps | Those who need to execute |
| `VERIFY.md` | Fact verification checklist | Those who need to check facts |
| `CHANGELOG.md` | Change log | Those who need to understand history |
| `CURRENT.md` | Current work status | Anyone needing quick status |

### Subfolders (created as needed)

| Subfolder | Content |
|-----------|---------|
| `reference/` | Original research materials, reference literature |
| `reference/survey/` | Special topic documents produced during verification |
| `template/` | NeurIPS 2026 template files |
| `paper/` | Paper output (modular LaTeX) |
| `system/` | System implementation (code, scripts, configs) |
| `experiment/` | Experiment data and results |

---

## Workflow Overview

```
Step 1 Understand materials --> Step 2 Build Meta docs --> Step 3 Verify facts
                                                              |
                                    Step 4 Execute (paper writing / system dev / experiments)
                                                              |
                                                        Step 5 Review & finalize
```

---

## Step 1: Understand Current State

Before doing anything, read all existing documents, reports, notes, and code in the workspace. If there are external reference materials, organize them into `reference/`.

**If the workspace already has content (files, paper frameworks, code, etc.), do not restructure directly. First report the current state to the user and ask for guidance before making adjustments.**

**Output**: No file output, but all subsequent documents depend on this understanding.

---

## Step 2: Build Meta Document System

Create in the following order. Each file has a single responsibility -- do not mix them.

### Creation Order

1. **README.md** -- What to do? Why? Where are the files? Current progress? Next steps?
2. **RESEARCH.md** -- Core findings, key insights, academic judgments, research gaps. No tasks or plans.
3. **PLAN.md** -- Task structure, output planning, work steps. No research insights, no fact verification.
4. **VERIFY.md** -- Pending questions + verified conclusions. See format specification below.
5. **CHANGELOG.md** -- Record changes by date.
6. **CURRENT.md** -- Current work status snapshot.

### VERIFY.md Format Specification

```markdown
# VERIFY.md -- Fact Verification Checklist

> Marking rules:
> - `[x]` Verified and passed
> - `[~]` Basically correct but with minor deviation (see notes)
> - `[!]` Incorrect, needs correction
> - `[?]` Cannot verify (no public source found)
>
> Each item should have a brief justification with source links below it.

## Category Name

- [x] **Fact description**
  > Brief evidence explanation.
  > - https://source-link

- [~] **Fact description**
  > Basically correct, but actually XXX not YYY.
  > - https://source-link

- [x] **Complex question** --> See `reference/survey/special_topic.md`
  > One-sentence conclusion.
  > - https://key-source-link
```

Most items can just have a brief conclusion + link. Only those with large information volume need separate `reference/survey/` documents.

---

## Step 3: Verify Facts

1. List pending questions in VERIFY.md (marked as `[ ]`)
2. Verify one by one via Web Search (can parallelize with sub-agents)
3. Fill in conclusions in VERIFY.md, update marks to `[x]` / `[~]` / `[!]`
4. Write detailed expansions into `reference/survey/` documents

---

## Step 4: Execute

Based on project type, execute core work. For this project (NeurIPS 2026 Position Paper), see paper workspace initialization below.

### Paper Workspace Initialization

#### Directory Structure

```
paper/neurips2026/
├── 0_0_package.tex         # Preamble: packages, macros, environment definitions
├── 0_0_main.tex            # Main document: documentclass, metadata, \input entries
├── 0_abstract.tex          # Abstract
├── 0_appendix.tex          # Appendix entry (\appendix + \input appendix/*)
├── references.bib          # Bibliography
├── section/                # Body sections: N_snake_case.tex
├── appendix/               # Appendix sections: N_snake_case.tex
├── table/                  # Tables: tab_name.tex
├── figure/                 # Figure .tex (\includegraphics + caption)
│   └── raw/                # Figure source files (.pdf, .png, .jpg)
├── listing/                # (Optional) Code/algorithms
└── style/                  # Format files: cls, bst, custom sty
```

Create:
```bash
mkdir -p paper/neurips2026/{section,appendix,table,figure/raw,style}
```

#### Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Body section | `section/N_snake_case.tex` | `section/3_system_model.tex` |
| Appendix section | `appendix/N_snake_case.tex` | `appendix/2_domain_definitions.tex` |
| Table | `table/descriptive_name.tex` | `table/protocol_comparison.tex` |
| Figure | `figure/descriptive_name.tex` | `figure/architecture_overview.tex` |
| Listing | `listing/descriptive_name.tex` | `listing/discovery_flow.tex` |
| Label | `sec:`, `tab:`, `fig:`, `alg:`, `eq:`, `app:` | `\label{sec:eval-setup}` |

#### \input Path Convention

All `\input` paths are **relative to the paper root directory**, without `.tex` suffix:

```latex
\input{0_abstract}
\input{section/1_introduction}
\input{table/corpus_stats}
\input{figure/architecture_overview}
\input{listing/discovery_flow}
\input{0_appendix}           % internally \input{appendix/1_xxx}
```

#### Format File Search Path

Add at the top of `0_0_package.tex` so `\documentclass` and `\bibliographystyle` can find files in `style/`:

```latex
\makeatletter
\providecommand*\input@path{}
\g@addto@macro\input@path{{style/}}
\makeatother
```

### Writing

- Write body text based on RESEARCH.md insights and PLAN.md structure
- Each section can be written in parallel (but after writing, need to unify transitions and consistency)
- Web Search verification and paper writing can be parallel
- references.bib incrementally supplemented during writing
- After each batch: update PLAN.md checkboxes + CHANGELOG.md

---

## Step 5: Review & Finalize

1. **Incorporate verification results**: Check VERIFY.md and `reference/survey/`, add new findings to output
2. **Unify transitions**: Section transitions, terminology consistency, cross-references, front-back correspondence
3. **Update references**: Supplement or correct
4. **Compile/test**: Layout adjustments or system testing
5. **Update CHANGELOG.md**

---

## Meta Document Maintenance Rules

| Document | When to Update | Format Notes |
|----------|---------------|--------------|
| `README.md` | When project structure changes | Directory structure and progress checkboxes match reality |
| `RESEARCH.md` | New insight or design change | Each insight has its own heading, includes Why |
| `PLAN.md` | Task completed or plan changes | Phases + checkboxes, mark current phase |
| `VERIFY.md` | When fact claims change | `[x]`/`[~]`/`[!]`/`[?]` + justification quote blocks |
| `CHANGELOG.md` | **After every non-trivial change** | Date descending -> category -> file list |
| `INIT.md` | When workflow itself changes | Keep generic, no project-specific content |

### Maintenance Principles

- **Immediate update**: Update the corresponding Meta document right after completing a piece of work; do not batch at the end
- **Single responsibility**: Do not put insights in PLAN, tasks in RESEARCH, or verification in PLAN
- **Consistent with reality**: README directory structure, PLAN checkboxes must reflect actual state

---

## Workflow Conventions

### Read Before Write

Before starting any work, read the relevant existing documents. Read current content before modifying files. Do not act on assumptions.

### Root Only Has Meta

Root directory is the project's "control panel" -- only Meta documents. All content (materials, paper, code, data) goes into subfolders.

### Parallel Strategy

- Web Search verification and writing/development can be parallel (use sub-agents)
- Paper sections can be written in parallel, but after completion need unified transitions
- Independent subtasks should be parallel; dependent ones should be sequential

### Incremental Commit

- After each verifiable step, update CHANGELOG and corresponding checkboxes
- Do not wait until everything is done to record at once
- CHANGELOG is in reverse chronological order; each entry says what changed

### Modular

- Paper files must be split (section / table / figure / listing); do not write monolithic files
- Same for code; split by responsibility
- Main entry file (`0_0_main.tex` or `main.py`) only does orchestration; no substantive content

### Lean Verification

- VERIFY.md writes conclusions + links; one or two lines is enough
- Only those with large information volume needing detailed recording get `reference/survey/` documents
- Not every item needs a special topic document
