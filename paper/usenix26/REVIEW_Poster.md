SP2026 Posters Paper #61 Reviews and Comments
===========================================================================
Paper #61 Poster: GHOSTCITE: A Large-Scale Analysis of Citation Validity in
the Age of Large Language Models


Review #61A
===========================================================================

Overall merit
-------------
3. Weak accept

Reviewer expertise
------------------
3. Knowledgeable

Poster summary
--------------
This poster studies ghost citations in LLM assisted academic writing and presents a verification pipeline, an LLM benchmark, an archival analysis of published papers, and a user survey. The core claim is that invalid citations are already appearing in top venues and are increasing over time.

Strengths
---------
This study is very important, and the poster combines three complementary components: system design, empirical measurement, and human factors. The main findings are concrete and easy to locate, especially the benchmark results and the increase in invalid citation rate.

Weaknesses
----------
The poster is visually crowded and too text heavy for a poster, which makes the tables, heatmap, and detailed claims hard to read at normal viewing distance. It also has multiple presentation errors and inconsistencies, including misspellings such as “Validality,” “Acadmic,” “Emprical,” and “Tittle,” which weaken credibility.

Comments for authors
--------------------
The work addresses a real problem and the study design is stronger than a typical poster. However, the poster needs a cleanup: reduce text, enlarge the key figures, and fix the spelling and formatting errors so the main message can be understood quickly.

The strongest part is the breadth of evidence across the benchmark, archival analysis, and survey. I recommend clarifying the distinction between metadata errors and fully fabricated citations more prominently, since that distinction is essential to the claim.



Review #61B
===========================================================================

Overall merit
-------------
3. Weak accept

Reviewer expertise
------------------
2. Some familiarity

Poster summary
--------------
Invalid citations (referring to non-existent works, not just typos) are a threat to the scientific community. While it is commonly hypothesized that LLMs are increasing the prevalence of such invalid citations (denoted ghost citations), the prevalence and impact of this is not yet well-understood. Along these lines, the poster develops CITEVERIFIER, a technique to measure ghost citations, overcoming various obstacles like inconsistent citation formats, benign citation typos, and scalability. CITEVERIFIER is experimentally evaluated on LLM-generated citations, as well as recent AI and security papers from top-tier venues.

Strengths
---------
* Relevant problem
* Narrative was easy to follow

Weaknesses
----------
* Citations deemed legitimate by CITEVERIFIER are not scrutizined in the experimental evaluation (only those flagged as invalid)

Comments for authors
--------------------
The takeaways are not too interesting. It is unsurprising that there is a recent spike in ghost citations, and the takeaways (that authors too often trust LLM citations without verifying, and that reviewers don't verify citations) are intuitively obvious. However, despite this, it is good to ground our intuition with empirical observation rather than assuming it is correct, and the experiments are indeed novel. Further, while the results may be unsurprising to me, they could probably spur some interesting discussion at a poster session. Also, the scale of the work is impressive.

To me, the most interesting results are (1) error propagation and (2) the gap between 86.7% of users claiming to "always verify" citations and 41.5% claiming to copy-paste without checking. I would focus more on these in the poster.

As I noted above, it is a weakness that citations deemed legitimate are not scrutinized. I can intuitively believe that citations deemed legitimate are more likely to be correctly classified than those flagged as illegitimate, but it would be better to have some empirical analysis.



Comment @A1 by Zuyao Xu <xuzuyao@mail.nankai.edu.cn> (Author)
---------------------------------------------------------------------------
We sincerely thank reviewers for their constructive feedback. 
We have carefully addressed concerns and revised the poster accordingly.

**1. Poster presentation and content refinement (Reviewer A & B)**

We have significantly reduced the text throughout the poster, enlarged key figures and tables, and improved the overall layout to ensure readability at a normal viewing distance. We have also carefully proofread the entire poster and corrected all spelling and formatting errors.

**2. False negative analysis of CiteVerifier (Reviewer B)**

We have added a manual validation study to evaluate both sides of CiteVerifier's classifications. Specifically, we manually checked two random samples (400 valid, 400 invalid). Valid accuracy was 100%, and invalid accuracy was 98% (392/400); the remaining 8 cases were non-paper sources (4), out-of-domain works (1), or poorly indexed items (3). These results suggest relatively low false positive rates and confirm the high precision of the verification pipeline.

**3. Emphasis on key findings (Reviewer B)**

We have restructured the poster to give greater visual prominence to these results, placing them in larger, more central positions. By shifting emphasis toward these more novel findings, we believe the revised version better highlights the non-obvious contributions of our work.

We thank the reviewers again for their time and helpful feedback.


Comment @A2 by Administrator
---------------------------------------------------------------------------
The changes look great. Congratulations and thanks for your hard work.