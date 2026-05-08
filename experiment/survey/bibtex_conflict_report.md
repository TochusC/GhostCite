# Survey Analysis Report (Merged.csv)

## Data Summary
- Total rows after cleaning/consent: 97
- Conflict samples removed: 3
- Valid rows used for analysis: 94
- Answered both BibTeX questions: 97

## Key Findings
- AI tool usage: 75/86 (87.2%)
- Hallucination often/very often: 31/75 (41.3%)
- Always verify AI references: 65/75 (86.7%)
- Copy-paste BibTeX without checking (any): 39/94 (41.5%)
- Severity major/critical: 72/94 (76.6%)
- Support automated checks (Yes, absolutely): 66/94 (70.2%)
- BibTeX conflict rate: 3/97 (3.1%)

## Worth Highlighting
- Compare high AI adoption with verification behavior to assess risk exposure.
- Hallucination rates can be contrasted with "always verify" rates to quantify gaps.
- BibTeX conflict samples show potential self-report inconsistency worth qualitative follow-up.
- Severity perception vs support for automated tools signals policy readiness.

## Demographics
### Academic Position
- PhD Student: 32 (34.0%)
- Master's Student: 19 (20.2%)
- Faculty (Professor/Lecturer): 17 (18.1%)
- Undergraduate student: 13 (13.8%)
- Postdoc: 6 (6.4%)
- Researcher: 5 (5.3%)
- Other: 2 (2.1%)

### Research Area
- Other: 24 (25.5%)
- AI & Machine Learning: 20 (21.3%)
- Network Security: 18 (19.1%)
- AI Security: 13 (13.8%)
- System Security: 10 (10.6%)
- Cryptography: 5 (5.3%)
- Software Engineering: 4 (4.3%)

### Papers Published
- 1-5: 46 (48.9%)
- 6-10: 16 (17.0%)
- 0: 14 (14.9%)
- 20+: 12 (12.8%)
- 11-20: 6 (6.4%)

### Native English
- No: 89 (94.7%)
- Yes: 5 (5.3%)

### Reviewer Experience
- No: 62 (66.0%)
- Yes: 32 (34.0%)

## AI Tool Usage
### Use AI Tools for Research
- Yes: 75 (87.2%)
- No: 11 (12.8%)

### AI Tool Types (Multi-select)
- General-purpose LLMs (e.g., ChatGPT, Claude, Gemini): 75
- Coding Assistants (e.g., GitHub Copilot, Cursor): 41
- Academic search engines (e.g., Elicit, Semantic Scholar): 6
- AI-powered reading tools (e.g., ChatPDF, Humata): 6

### AI for Text Polishing
- Yes, for specific difficult paragraphs: 35 (46.7%)
- Yes, for almost every sentence: 22 (29.3%)
- Yes, but only for final proofreading: 17 (22.7%)
- No, I trust my own writing more: 1 (1.3%)

## Citation Integrity and Verification
### LLM Hallucination Frequency
- I do not use General LLMs for finding references: 25 (33.3%)
- Often (20-50%): 24 (32.0%)
- Occasionally (<20%): 16 (21.3%)
- Very Often (>50%): 7 (9.3%)
- Never: 3 (4.0%)

### Verify AI References Externally
- Always verify (100%): 58 (77.3%)
- Only if reading full text: 8 (10.7%)
- Yes, I verify 100% of them via Google Scholar/DBLP: 7 (9.3%)
- Only if suspicious: 1 (1.3%)
- I only verify if I need to read the full text: 1 (1.3%)

### Cited AI Suggestion Without Reading
- No, never: 62 (82.7%)
- Yes, once or twice: 8 (10.7%)
- Yes, often: 5 (6.7%)

### Verify Cited Claim Frequency
- Every single time: 48 (57.1%)
- Most of the time: 20 (23.8%)
- Only for critical claims: 14 (16.7%)
- Rarely: 2 (2.4%)

### Primary Metadata Source
- Google Scholar "Cite" button: 61 (72.6%)
- Direct export from publisher: 15 (17.9%)
- Copy from other papers: 4 (4.8%)
- Direct export from publisher (IEEE/ACM): 4 (4.8%)

## Severity and Responsibility
### Severity of Hallucinated Citations
- Critical crisis: 42 (44.7%)
- Major problem: 30 (31.9%)
- Minor nuisance: 22 (23.4%)

### Responsibility for Citation Authenticity
- Authors: 86 (91.5%)
- Reviewers: 3 (3.2%)
- Publishers: 2 (2.1%)
- AI tool developers: 2 (2.1%)
- Publishers (Editorial check): 1 (1.1%)

### Support for Automated Checks
- Yes, absolutely: 66 (70.2%)
- Maybe: 25 (26.6%)
- No: 3 (3.2%)

### Peer Review Effectiveness
- Not very effective: 62 (66.0%)
- Somewhat effective: 22 (23.4%)
- Ineffective: 8 (8.5%)
- Very effective: 2 (2.1%)

## Reviewer Behavior
### Reviewer Checks Reference Section
- Yes, skimming: 18 (60.0%)
- Yes, carefully: 7 (23.3%)
- No: 5 (16.7%)

### Reviewer Focus Areas (Multi-select)
- Missing key related work: 28
- Correctness of metadata (Year, Venue): 10
- Existence of the papers: 10
- Self-citation abuse: 5

### Reaction to One Incorrect Citation
- Mention in minor comments: 61 (64.9%)
- Ask for major revision: 15 (16.0%)
- Mention it in minor comments: 14 (14.9%)
- Reject the paper: 4 (4.3%)

### Reaction to Multiple Incorrect Citations
- Reject immediately (Ethical concern): 56 (59.6%)
- Ask for explanation: 38 (40.4%)

## BibTeX Consistency Check
- Rule: Strongly agree on verifying every BibTeX field AND Yes, often on copy-pasting without checking.
- Conflict samples: 3 (3.1%)

## Question Number Mapping (Overview Order)
| Q# | Question |
|---|---|
| Q1 | What is your current academic position? |
| Q2 | Which research area best describes your work? |
| Q3 | How many peer-reviewed papers have you published in your career? |
| Q4 | Have you served as a reviewer for top-tier conferences (e.g., USENIX Sec, CCS, S&P, CVPR, NeurIPS) in the last 3 years? |
| Q5 | Which stage of paper writing do you find most time-consuming? (Select up to 2).1 |
| Q6 | How do you typically search for related work?.1 |
| Q7 | Do you use AI-powered tools for research?.1 |
| Q8 | Which types of AI-powered tools do you use for research? (Select all that apply).1 |
| Q9 | Do you use AI tools specifically for text polishing, grammar checking, or rephrasing?.1 |
| Q10 | Specifically regarding CITATIONS, how do you use AI tools? (Select all that apply).1 |
| Q11 | When asking a General LLM (e.g., ChatGPT) to find references, how often do you encounter "hallucinations" (non-existent papers)?.1 |
| Q12 | If an AI tool provides a perfect-looking reference (Title, Author, Year, Venue all look correct), do you still verify it externally?.1 |
| Q13 | Have you ever cited a paper suggested by AI without reading the full text of that paper?.1 |
| Q14 | To what extent do you agree: "AI tools have made it easier to generate 'Related Work' sections, but harder to ensure citation accuracy.".1 |
| Q15 | What is your strategy when an AI tool generates a citation with a broken link or DOI?.1 |
| Q16 | When adding a citation to your paper, what is your primary source of metadata (title, year, venue)?.1 |
| Q17 | How often do you verify that a cited paper actually contains the claim you are attributing to it?.1 |
| Q18 | If you cannot find the full text of a paper (e.g., paywalled or offline), do you still cite it based on its abstract or title?.1 |
| Q19 | To what extent do you agree: "There is pressure to include a high number of references to make the paper look more scholarly.".1 |
| Q20 | When reviewing a paper, do you explicitly check the Reference section? |
| Q21 | What are you looking for when checking references? (Select all that apply) |
| Q22 | Have you ever clicked on a DOI link in a submission's bibliography to verify the paper exists? |
| Q23 | Have you ever suspected a submission contained fake or hallucinated references? |
| Q24 | If you see a citation to a "Preprint" or "ArXiv" paper, do you verify if it has been published in a peer-reviewed venue? |
| Q25 | How do you handle citations to non-English papers in a submission? |
| Q26 | To what extent do you agree: "The accuracy of the bibliography is as important as the accuracy of the experimental results." |
| Q27 | Do you believe the current peer review process is effective at catching metadata errors in references? |
| Q28 | How serious of an issue do you consider "hallucinated citations" (non-existent papers) in the era of AI? |
| Q29 | Who is primarily responsible for verifying the authenticity of cited references? |
| Q30 | Should conferences deploy automated tools to check for broken DOIs or fake references upon submission? |
| Q31 | To what extent do you agree: "It is acceptable to cite a paper based on AI summarization without reading the original text." |
| Q32 | Have you ever seen a reference list where the author names were clearly scrambled or incorrect (e.g., order reversed)? |
| Q33 | Have you ever seen a reference where the title existed but the venue/year was completely wrong? |
| Q34 | Do you think it is acceptable to cite a "Technical Report" if a peer-reviewed version exists? |
| Q35 | What is your reaction if you find one incorrect citation (e.g., wrong year) in a paper you are reviewing? |
| Q36 | What is your reaction if you find multiple (e.g., >5) incorrect or fake citations? |
| Q37 | If you encounter a suspicious or clearly fake reference in a published paper, do you report it? |
| Q38 | Have you ever copy-pasted a BibTeX entry from the internet without checking its content? |
| Q39 | To what extent do you agree: "I meticulously verify every single field (volume, issue, page numbers) of every BibTeX entry I import, ensuring 100% accuracy before submission." |
| Q40 | Do you use tools like "Semantic Scholar" or "ResearchRabbit" to build your bibliography? |

## All Questions (Full Statistics)
### What is your current academic position?
- Responses: 94 | Unique: 7 | Multi-select: False
- PhD Student: 32 (34.0%)
- Master's Student: 19 (20.2%)
- Faculty (Professor/Lecturer): 17 (18.1%)
- Undergraduate student: 13 (13.8%)
- Postdoc: 6 (6.4%)
- Researcher: 5 (5.3%)
- Other: 2 (2.1%)

### Which research area best describes your work?
- Responses: 114 | Unique: 7 | Multi-select: True
- Other: 24 (21.1%)
- AI: 20 (17.5%)
- Machine Learning: 20 (17.5%)
- Network Security: 18 (15.8%)
- AI Security: 13 (11.4%)
- System Security: 10 (8.8%)
- Cryptography: 5 (4.4%)
- Software Engineering: 4 (3.5%)

### How many peer-reviewed papers have you published in your career?
- Responses: 94 | Unique: 5 | Multi-select: False
- 1-5: 46 (48.9%)
- 6-10: 16 (17.0%)
- 0: 14 (14.9%)
- 20+: 12 (12.8%)
- 11-20: 6 (6.4%)

### Is English your native language?
- Responses: 94 | Unique: 2 | Multi-select: False
- No: 89 (94.7%)
- Yes: 5 (5.3%)

### Have you served as a reviewer for top-tier conferences (e.g., USENIX Sec, CCS, S&P, CVPR, NeurIPS) in the last 3 years?
- Responses: 94 | Unique: 2 | Multi-select: False
- No: 62 (66.0%)
- Yes: 32 (34.0%)

### Which stage of paper writing do you find most time-consuming? (Select up to 2).1
- Responses: 175 | Unique: 20 | Multi-select: True
- Conceptualization: 62 (35.4%)
- Writing the Introduction: 36 (20.6%)
- Literature Search: 24 (13.7%)
- Review: 24 (13.7%)
- Technical Description: 24 (13.7%)
- Formatting References: 5 (2.9%)

### How do you typically search for related work?.1
- Responses: 203 | Unique: 15 | Multi-select: True
- Keyword search on Google Scholar/DBLP: 68 (33.5%)
- Following citations from other papers: 62 (30.5%)
- Browsing conference proceedings: 40 (19.7%)
- Using AI-powered tools (e.g., ChatGPT, Connected Papers): 33 (16.3%)

### Do you use AI-powered tools for research?.1
- Responses: 86 | Unique: 2 | Multi-select: False
- Yes: 75 (87.2%)
- No: 11 (12.8%)

### Which types of AI-powered tools do you use for research? (Select all that apply).1
- Responses: 128 | Unique: 8 | Multi-select: True
- General-purpose LLMs (e.g., ChatGPT, Claude, Gemini): 75 (58.6%)
- Coding Assistants (e.g., GitHub Copilot, Cursor): 41 (32.0%)
- Academic search engines (e.g., Elicit, Semantic Scholar): 6 (4.7%)
- AI-powered reading tools (e.g., ChatPDF, Humata): 6 (4.7%)

### Do you use AI tools specifically for text polishing, grammar checking, or rephrasing?.1
- Responses: 75 | Unique: 4 | Multi-select: False
- Yes, for specific difficult paragraphs: 35 (46.7%)
- Yes, for almost every sentence: 22 (29.3%)
- Yes, but only for final proofreading: 17 (22.7%)
- No, I trust my own writing more: 1 (1.3%)

### Specifically regarding CITATIONS, how do you use AI tools? (Select all that apply).1
- Responses: 117 | Unique: 19 | Multi-select: True
- None: I do not use AI tools for citation-related tasks (Please do not select other options if this is checked): 35 (29.9%)
- Formatting: Converting references into specific formats (e.g., BibTeX): 23 (19.7%)
- Discovery: Asking AI to recommend papers on a specific topic: 23 (19.7%)
- Summarization: Asking AI to summarize a paper to decide whether to cite it: 15 (12.8%)
- Gap Filling: "I need a citation for this statement, please find one.": 15 (12.8%)
- Verification: Asking AI if a specific paper exists: 6 (5.1%)

### When asking a General LLM (e.g., ChatGPT) to find references, how often do you encounter "hallucinations" (non-existent papers)?.1
- Responses: 75 | Unique: 5 | Multi-select: False
- I do not use General LLMs for finding references: 25 (33.3%)
- Often (20-50%): 24 (32.0%)
- Occasionally (<20%): 16 (21.3%)
- Very Often (>50%): 7 (9.3%)
- Never: 3 (4.0%)

### If an AI tool provides a perfect-looking reference (Title, Author, Year, Venue all look correct), do you still verify it externally?.1
- Responses: 75 | Unique: 5 | Multi-select: False
- Always verify (100%): 58 (77.3%)
- Only if reading full text: 8 (10.7%)
- Yes, I verify 100% of them via Google Scholar/DBLP: 7 (9.3%)
- Only if suspicious: 1 (1.3%)
- I only verify if I need to read the full text: 1 (1.3%)

### Have you ever cited a paper suggested by AI without reading the full text of that paper?.1
- Responses: 75 | Unique: 3 | Multi-select: False
- No, never: 62 (82.7%)
- Yes, once or twice: 8 (10.7%)
- Yes, often: 5 (6.7%)

### To what extent do you agree: "AI tools have made it easier to generate 'Related Work' sections, but harder to ensure citation accuracy.".1
- Responses: 75 | Unique: 5 | Multi-select: False
- Somewhat agree: 28 (37.3%)
- Strongly agree: 24 (32.0%)
- Neutral: 11 (14.7%)
- Somewhat disagree: 9 (12.0%)
- Strongly disagree: 3 (4.0%)

### What is your strategy when an AI tool generates a citation with a broken link or DOI?.1
- Responses: 75 | Unique: 4 | Multi-select: False
- I assume the paper exists and try to find it manually: 45 (60.0%)
- I assume the paper is a hallucination and discard it immediately: 24 (32.0%)
- I ask the AI to provide a different link: 4 (5.3%)
- I keep the citation but remove the DOI: 2 (2.7%)

### When adding a citation to your paper, what is your primary source of metadata (title, year, venue)?.1
- Responses: 84 | Unique: 4 | Multi-select: False
- Google Scholar "Cite" button: 61 (72.6%)
- Direct export from publisher: 15 (17.9%)
- Copy from other papers: 4 (4.8%)
- Direct export from publisher (IEEE/ACM): 4 (4.8%)

### How often do you verify that a cited paper actually contains the claim you are attributing to it?.1
- Responses: 84 | Unique: 4 | Multi-select: False
- Every single time: 48 (57.1%)
- Most of the time: 20 (23.8%)
- Only for critical claims: 14 (16.7%)
- Rarely: 2 (2.4%)

### If you cannot find the full text of a paper (e.g., paywalled or offline), do you still cite it based on its abstract or title?.1
- Responses: 84 | Unique: 3 | Multi-select: False
- No, never: 46 (54.8%)
- Yes, if necessary: 35 (41.7%)
- Yes, often: 3 (3.6%)

### To what extent do you agree: "There is pressure to include a high number of references to make the paper look more scholarly.".1
- Responses: 84 | Unique: 5 | Multi-select: False
- Somewhat agree: 31 (36.9%)
- Neutral: 21 (25.0%)
- Somewhat disagree: 17 (20.2%)
- Strongly disagree: 10 (11.9%)
- Strongly agree: 5 (6.0%)

### When reviewing a paper, do you explicitly check the Reference section?
- Responses: 30 | Unique: 3 | Multi-select: False
- Yes, skimming: 18 (60.0%)
- Yes, carefully: 7 (23.3%)
- No: 5 (16.7%)

### What are you looking for when checking references? (Select all that apply)
- Responses: 53 | Unique: 12 | Multi-select: True
- Missing key related work: 28 (52.8%)
- Correctness of metadata (Year, Venue): 10 (18.9%)
- Existence of the papers: 10 (18.9%)
- Self-citation abuse: 5 (9.4%)

### Have you ever clicked on a DOI link in a submission's bibliography to verify the paper exists?
- Responses: 30 | Unique: 4 | Multi-select: False
- Occasionally: 13 (43.3%)
- Rarely: 9 (30.0%)
- Never: 6 (20.0%)
- Frequently: 2 (6.7%)

### Have you ever suspected a submission contained fake or hallucinated references?
- Responses: 30 | Unique: 2 | Multi-select: False
- No: 24 (80.0%)
- Yes: 6 (20.0%)

### If you see a citation to a "Preprint" or "ArXiv" paper, do you verify if it has been published in a peer-reviewed venue?
- Responses: 30 | Unique: 3 | Multi-select: False
- Sometimes: 15 (50.0%)
- No: 9 (30.0%)
- Always: 6 (20.0%)

### How do you handle citations to non-English papers in a submission?
- Responses: 30 | Unique: 4 | Multi-select: False
- I check them using translation tools: 10 (33.3%)
- I ignore them: 10 (33.3%)
- I assume they are valid: 9 (30.0%)
- I ask the authors to clarify: 1 (3.3%)

### To what extent do you agree: "The accuracy of the bibliography is as important as the accuracy of the experimental results."
- Responses: 94 | Unique: 4 | Multi-select: False
- Strongly agree: 52 (55.3%)
- Somewhat agree: 29 (30.9%)
- Neutral: 10 (10.6%)
- Somewhat disagree: 3 (3.2%)

### Do you believe the current peer review process is effective at catching metadata errors in references?
- Responses: 94 | Unique: 4 | Multi-select: False
- Not very effective: 62 (66.0%)
- Somewhat effective: 22 (23.4%)
- Ineffective: 8 (8.5%)
- Very effective: 2 (2.1%)

### How serious of an issue do you consider "hallucinated citations" (non-existent papers) in the era of AI?
- Responses: 94 | Unique: 3 | Multi-select: False
- Critical crisis: 42 (44.7%)
- Major problem: 30 (31.9%)
- Minor nuisance: 22 (23.4%)

### Who is primarily responsible for verifying the authenticity of cited references?
- Responses: 94 | Unique: 5 | Multi-select: False
- Authors: 86 (91.5%)
- Reviewers: 3 (3.2%)
- Publishers: 2 (2.1%)
- AI tool developers: 2 (2.1%)
- Publishers (Editorial check): 1 (1.1%)

### Should conferences deploy automated tools to check for broken DOIs or fake references upon submission?
- Responses: 94 | Unique: 3 | Multi-select: False
- Yes, absolutely: 66 (70.2%)
- Maybe: 25 (26.6%)
- No: 3 (3.2%)

### To what extent do you agree: "It is acceptable to cite a paper based on AI summarization without reading the original text."
- Responses: 94 | Unique: 5 | Multi-select: False
- Strongly disagree: 33 (35.1%)
- Somewhat disagree: 31 (33.0%)
- Neutral: 17 (18.1%)
- Somewhat agree: 12 (12.8%)
- Strongly agree: 1 (1.1%)

### Have you ever seen a reference list where the author names were clearly scrambled or incorrect (e.g., order reversed)?
- Responses: 94 | Unique: 2 | Multi-select: False
- No: 59 (62.8%)
- Yes: 35 (37.2%)

### Have you ever seen a reference where the title existed but the venue/year was completely wrong?
- Responses: 94 | Unique: 2 | Multi-select: False
- No: 50 (53.2%)
- Yes: 44 (46.8%)

### Do you think it is acceptable to cite a "Technical Report" if a peer-reviewed version exists?
- Responses: 94 | Unique: 2 | Multi-select: False
- Yes: 72 (76.6%)
- No: 22 (23.4%)

### What is your reaction if you find one incorrect citation (e.g., wrong year) in a paper you are reviewing?
- Responses: 94 | Unique: 4 | Multi-select: False
- Mention in minor comments: 61 (64.9%)
- Ask for major revision: 15 (16.0%)
- Mention it in minor comments: 14 (14.9%)
- Reject the paper: 4 (4.3%)

### What is your reaction if you find multiple (e.g., >5) incorrect or fake citations?
- Responses: 94 | Unique: 2 | Multi-select: False
- Reject immediately (Ethical concern): 56 (59.6%)
- Ask for explanation: 38 (40.4%)

### If you encounter a suspicious or clearly fake reference in a published paper, do you report it?
- Responses: 108 | Unique: 10 | Multi-select: True
- No, I would verify it privately but take no action: 40 (37.0%)
- Yes, I would contact the PC Chairs or Journal Editors: 36 (33.3%)
- Yes, I would contact the authors directly: 24 (22.2%)
- No, I would ignore it: 8 (7.4%)

### Have you ever copy-pasted a BibTeX entry from the internet without checking its content?
- Responses: 94 | Unique: 3 | Multi-select: False
- No, never: 55 (58.5%)
- Yes, rarely: 26 (27.7%)
- Yes, often: 13 (13.8%)

### To what extent do you agree: "I meticulously verify every single field (volume, issue, page numbers) of every BibTeX entry I import, ensuring 100% accuracy before submission."
- Responses: 94 | Unique: 5 | Multi-select: False
- Somewhat agree: 27 (28.7%)
- Strongly agree: 26 (27.7%)
- Neutral: 26 (27.7%)
- Somewhat disagree: 10 (10.6%)
- Strongly disagree: 5 (5.3%)

### Do you use tools like "Semantic Scholar" or "ResearchRabbit" to build your bibliography?
- Responses: 94 | Unique: 2 | Multi-select: False
- No: 78 (83.0%)
- Yes: 16 (17.0%)

### Any additional comments on the state of academic integrity and writing tools?
- Responses: 80 | Unique: 12 | Multi-select: False
- Free-text responses: 80
- (空): 61
- 无: 9
- 大模型极大的方便了科研以及论文写作，但是应该严重杜绝将大模型作为创作的机器，充当写作或辅助的工具我认为是可以的: 1
- NONE: 1
- 无。: 1
- 感谢问卷，有一些陋见想要一吐为快。我认为，在符合事实的前提下（即无幻觉、无错误），检测文本是否为AI撰写/生成，实际上是不太可能或者极度困难的。对抗AI内容生成检测的工具已经存在，可以通过一次润色，使得原有100%AI 生成的文本在主流检测器（例如GPTZero等）下都做到 0% AI generation判定。这导致任何作者都可以claim其内容无AI参与，即使他们的东西是100% AI 生成的（不可检测性），因此投稿过程中附上AI使用的声明只能对抗守序善良的作者。同时我认为，由幻觉导致的虚假参考文献问题不难解决。可以设计一个toolkit进行自动化检测（搜索+比对，我们实验室内就有该工具对所有bib进行投稿前检查，包括格式+正确性），AI Agent本身也可以调用这个toolkit进行自我审查，从而有效规避不合适的参考文献。虚假参考文献问题很可能只是昙花一现，随着技术发展很快会消失。: 1
- 新颖且的确存在现实问题（ai导致的论文写作错误）的调查角度，祝早日发表: 1
- 具体AI水论文: 1
- AI is cancer: 1
- In one of my papers, I used an AI tool to get two citations for a paragraph in my paper. Since the submission deadline was really close, I used those citations without verifying them. Later I understood that in one of them the name of the authors doesn't match the paper and fortunately I had time to fix the issue, but that was a good lesson for me to always verify the papers and their relevance.: 1
- Comment for updating this questionnaire and making the questions not required. For instance, the question about using AI for research, with yes and no answers, was difficult to address. While I use grammar tools, I do not use the likes of ChatGPT for referencing, but the AI for referencing/literature review questions was required. That forced me to come back to select no,  to answer the opinion questions. Meanwhile, I use Grammarly, but where it was put with the required information made it difficult.: 1
- I primarily use DBLP for citations and assume that they are correct. Regarding questions 2 and 3 on this page, I didn't encounter any issues because I never explicitly checked the reference. I only check them if I am particularly interested in them, for personal reasons or because they support major claims of the paper.: 1

### verify_norm
- Responses: 94 | Unique: 5 | Multi-select: False
- Somewhat agree: 27 (28.7%)
- Strongly agree: 26 (27.7%)
- Neutral: 26 (27.7%)
- Somewhat disagree: 10 (10.6%)
- Strongly disagree: 5 (5.3%)

### copy_norm
- Responses: 94 | Unique: 3 | Multi-select: False
- No, never: 55 (58.5%)
- Yes, rarely: 26 (27.7%)
- Yes, often: 13 (13.8%)

## Figures
- figs/profile_position.pdf
- figs/profile_area.pdf
- figs/profile_papers.pdf
- figs/profile_native_english.pdf
- figs/profile_reviewer.pdf
- figs/ai_use.pdf
- figs/ai_tool_types.pdf
- figs/ai_text_polish.pdf
- figs/citation_hallucination.pdf
- figs/citation_verify_external.pdf
- figs/citation_without_reading.pdf
- figs/citation_verify_claim.pdf
- figs/citation_metadata_source.pdf
- figs/issue_severity.pdf
- figs/issue_responsibility.pdf
- figs/issue_automated_tools.pdf
- figs/issue_peer_review.pdf
- figs/reviewer_check_refs.pdf
- figs/reviewer_focus.pdf
- figs/reviewer_reaction_one.pdf
- figs/reviewer_reaction_multi.pdf
- figs/bibtex_conflict_summary.pdf
- figs/bibtex_conflict_heatmap.pdf
- figs/bibtex_conflict_distributions.pdf

## Notes
- Invalid rows are exported to bibtex_conflict_invalid_rows.csv
- Auto plots for all questions are in figs/all_questions/