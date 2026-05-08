# GhostCite: Citation Validity in the LLM Era

*Generated on: 2026-02-05 15:21:17*

---

## 0. Structural Data Success Rate Analysis

Overview of how many structurally valid citations were generated vs total attempts.

- **Total Interactions**: 22800
- **Well-formed Interactions**: 20653
- **Well-formed Interaction Rate (%)**: 90.58
- **Total Citations**: 375440
- **Well-formed Citations**: 331809
- **Well-formed Citation Rate (%)**: 88.38
- **Valid Citations**: 164933
- **Hallucination Rate (%)**: 50.29
- **Invalid (Hallucinated) Citations**: 166876


---

## Model-wise Performance Summary

Performance breakdown by model.

|          |   JSONs Processed |   Citations Processed |   Valid Citations |   Invalid Citations |   Hallucination Rate (%) |
|:---------|------------------:|----------------------:|------------------:|--------------------:|-------------------------:|
| Claude 4 |              1760 |                 28800 |             22650 |                6150 |                     1.64 |
| DeepSeek |              1719 |                 27973 |             24160 |                3813 |                     1.02 |
| ERNIE    |              1673 |                 27332 |              8057 |               19275 |                     5.13 |
| GLM-4.5  |              1711 |                 27835 |             21885 |                5950 |                     1.58 |
| GPT-5    |              1723 |                 28366 |             13103 |               15263 |                     4.07 |
| Gemini   |              1686 |                 27102 |             11021 |               16081 |                     4.28 |
| Grok 4   |              1743 |                 28627 |              5779 |               22848 |                     6.09 |
| Hunyuan  |              1107 |                 16094 |               765 |               15329 |                     4.08 |
| Kimi     |              1568 |                 24955 |             14561 |               10394 |                     2.77 |
| Llama 4  |              1713 |                 27925 |             15100 |               12825 |                     3.42 |
| Phi-4    |              1643 |                 27164 |              3507 |               23657 |                     6.3  |
| Qwen-3   |              1749 |                 28546 |             21972 |                6574 |                     1.75 |
| Seed     |               858 |                 11090 |              2373 |                8717 |                     2.32 |

---

## 1. Overall Citation Hallucination Rate by Model

Models ranked by average citation hallucination rate. Lower is better (fewer hallucinations).

| model    |   Hallucination Rate (%) |   Total Citations |   Std Error (%) |   95% CI Error (%) |
|:---------|-------------------------:|------------------:|----------------:|-------------------:|
| DeepSeek |                    14.23 |              1719 |            0.84 |               1.65 |
| GLM-4.5  |                    21.25 |              1711 |            0.99 |               1.94 |
| Claude 4 |                    21.84 |              1760 |            0.98 |               1.93 |
| Qwen-3   |                    23.52 |              1749 |            1.01 |               1.99 |
| Kimi     |                    41.86 |              1568 |            1.25 |               2.44 |
| Llama 4  |                    45.84 |              1713 |            1.2  |               2.36 |
| GPT-5    |                    50.92 |              1723 |            1.2  |               2.36 |
| Gemini   |                    59.47 |              1686 |            1.2  |               2.34 |
| ERNIE    |                    71.9  |              1673 |            1.1  |               2.15 |
| Seed     |                    78.64 |               858 |            1.4  |               2.74 |
| Grok 4   |                    79.98 |              1743 |            0.96 |               1.88 |
| Phi-4    |                    87.47 |              1643 |            0.82 |               1.6  |
| Hunyuan  |                    94.93 |              1107 |            0.66 |               1.29 |

---

## 2. Impact of Online Searching and Thinking Mode

Comparison of citation hallucination rates between online+thinking vs offline+no-thinking conditions. Negative difference indicates online search helps reduce hallucinations.

| model    |   Offline + No Thinking |   Online + Thinking |   Difference (Online - Offline) |
|:---------|------------------------:|--------------------:|--------------------------------:|
| Seed     |                   75.78 |               94.5  |                           18.72 |
| GPT-5    |                   42.54 |               58.97 |                           16.42 |
| Llama 4  |                   44.22 |               47.5  |                            3.27 |
| Claude 4 |                   21.43 |               22.25 |                            0.83 |
| GLM-4.5  |                   21.2  |               21.29 |                            0.1  |
| Phi-4    |                   87.47 |               87.48 |                            0.02 |
| Gemini   |                   59.67 |               59.26 |                           -0.42 |
| Grok 4   |                   80.26 |               79.7  |                           -0.57 |
| Qwen-3   |                   23.83 |               23.21 |                           -0.62 |
| Hunyuan  |                   95.27 |               94.59 |                           -0.68 |
| Kimi     |                   42.28 |               41.45 |                           -0.84 |
| DeepSeek |                   14.68 |               13.78 |                           -0.89 |
| ERNIE    |                   75.77 |               68.12 |                           -7.65 |

---

## Online Search Impact Summary

- **Average Online+Thinking Rate (%)**: 54.78
- **Average Offline+NoThinking Rate (%)**: 52.65
- **Average Improvement (%)**: 2.13
- **Models Improved by Online Search**: 6
- **Models Degraded by Online Search**: 7


---

## 3. Citation Hallucination Rate by Research Topic (Domain)

Topics ranked by average citation hallucination rate. Lower hallucination rate indicates the domain is easier for LLMs to generate valid citations.

| topic   |   Hallucination Rate (%) |   Total Citations |   Std Error (%) |   95% CI Error (%) |
|:--------|-------------------------:|------------------:|----------------:|-------------------:|
| DL      |                    80.19 |               510 |            1.77 |               3.46 |
| OH      |                    75.38 |               513 |            1.9  |               3.73 |
| NI      |                    73.42 |               534 |            1.91 |               3.75 |
| ET      |                    69.38 |               519 |            2.02 |               3.97 |
| GT      |                    64.04 |               526 |            2.09 |               4.1  |
| SY      |                    63.9  |               522 |            2.1  |               4.12 |
| CY      |                    62.24 |               507 |            2.15 |               4.22 |
| AR      |                    60.59 |               518 |            2.15 |               4.21 |
| CE      |                    60.58 |               515 |            2.15 |               4.22 |
| DB      |                    60.31 |               514 |            2.16 |               4.23 |
| SE      |                    60.26 |               525 |            2.14 |               4.19 |
| CR      |                    59.96 |               523 |            2.14 |               4.2  |
| HC      |                    59.51 |               508 |            2.18 |               4.27 |
| MM      |                    59.2  |               519 |            2.16 |               4.23 |
| AI      |                    57.32 |               525 |            2.16 |               4.23 |
| PF      |                    54.63 |               512 |            2.2  |               4.31 |
| MA      |                    53.97 |               515 |            2.2  |               4.3  |
| RO      |                    52.21 |               503 |            2.23 |               4.37 |
| IR      |                    51.05 |               522 |            2.19 |               4.29 |
| CG      |                    49.66 |               518 |            2.2  |               4.31 |
| FL      |                    49.6  |               514 |            2.21 |               4.32 |
| DM      |                    49.33 |               520 |            2.19 |               4.3  |
| PL      |                    48.4  |               524 |            2.18 |               4.28 |
| OS      |                    47.96 |               514 |            2.2  |               4.32 |
| SC      |                    47.23 |               523 |            2.18 |               4.28 |
| NE      |                    45.58 |               526 |            2.17 |               4.26 |
| SD      |                    45.51 |               506 |            2.21 |               4.34 |
| NA      |                    44.01 |               518 |            2.18 |               4.27 |
| DC      |                    43.96 |               515 |            2.19 |               4.29 |
| IT      |                    43.18 |               527 |            2.16 |               4.23 |
| LG      |                    41.92 |               507 |            2.19 |               4.3  |
| LO      |                    41.55 |               510 |            2.18 |               4.28 |
| MS      |                    35.03 |               518 |            2.1  |               4.11 |
| CV      |                    33.64 |               514 |            2.08 |               4.08 |
| GR      |                    32.5  |               510 |            2.07 |               4.07 |
| CC      |                    32.23 |               518 |            2.05 |               4.02 |
| GL      |                    31.5  |               510 |            2.06 |               4.03 |
| DS      |                    29.76 |               521 |            2    |               3.93 |
| SI      |                    29.31 |               518 |            2    |               3.92 |
| CL      |                    28.8  |               492 |            2.04 |               4    |

---

## Topic/Domain Summary

- **Lowest Hallucination Topic**: CL
- **Lowest Hallucination Rate (%)**: 28.80
- **Highest Hallucination Topic**: DL
- **Highest Hallucination Rate (%)**: 80.19
- **Average Hallucination Rate (%)**: 50.72
- **Std Dev of Hallucination Rates (%)**: 13.26


---

## 4. Effect of Number of References on Citation Validity

Citation hallucination rate (%) when asking for different numbers of references. Lower range indicates more consistent performance across batch sizes.

| model    |   10 References |   20 References |   30 References |   Range (Max-Min) |
|:---------|----------------:|----------------:|----------------:|------------------:|
| Gemini   |           59.74 |           59.06 |           59.22 |              0.68 |
| GLM-4.5  |           20.91 |           21.84 |           21.39 |              0.94 |
| Kimi     |           42.22 |           41.77 |           40.78 |              1.45 |
| Phi-4    |           87.83 |           87.46 |           86.31 |              1.52 |
| Grok 4   |           79.84 |           81.15 |           78.64 |              2.51 |
| Hunyuan  |           94.61 |           94.55 |           97.11 |              2.56 |
| Qwen-3   |           24.39 |           22.95 |           21.72 |              2.68 |
| Claude 4 |           23    |           20.11 |           20.95 |              2.89 |
| Llama 4  |           45.77 |           44.76 |           47.7  |              2.94 |
| DeepSeek |           15.31 |           13.26 |           12.36 |              2.96 |
| Seed     |           79.01 |           77.3  |           84.27 |              6.97 |
| ERNIE    |           75.49 |           65.56 |           70.71 |              9.94 |
| GPT-5    |           44.07 |           59.95 |           57.24 |             15.87 |

---

## Scaling Analysis Summary

- **Average Rate for 10 References (%)**: 53.25
- **Average Rate for 20 References (%)**: 53.05
- **Average Rate for 30 References (%)**: 53.72
- **Most Stable Model**: Gemini
- **Least Stable Model**: GPT-5


---

## 5. Model Performance by Topic (Heatmap Data)

Citation hallucination rate (%) for each model-topic combination. Lower values (closer to 0) indicate better performance.

| model    |    AI |   AR |   CC |   CE |   CG |   CL |   CR |   CV |   CY |   DB |   DC |   DL |   DM |   DS |   ET |   FL |   GL |   GR |   GT |   HC |   IR |   IT |   LG |   LO |   MA |   MM |   MS |   NA |   NE |   NI |   OH |   OS |   PF |   PL |   RO |   SC |   SD |   SE |   SI |   SY |
|:---------|------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| Claude 4 |  25.5 | 10.7 | 17.9 | 17.9 | 11.1 |  1.6 | 46.4 |  5   | 96.9 | 74.4 |  6.1 | 97.2 | 18.4 | 15.1 | 32.8 | 18.4 |  3   |  1   | 74.1 | 11.9 |  8.9 | 15.5 | 15   |  8.5 | 19.4 | 13.4 |  7.5 | 15.5 |  6.2 | 65   | 27.4 | 13.5 |  8.9 |  6.9 | 12.4 |  8.3 |  9.4 | 16.7 |  2.2 |  7.5 |
| DeepSeek |   8.9 |  8.6 |  5   | 22.3 |  7.5 |  8.4 |  5.8 |  2.6 |  9.7 |  7.1 |  4   | 26.6 | 23.1 |  5.3 | 32.8 | 10.2 | 12.6 |  5.6 | 18.4 | 11.1 | 10.6 | 10.4 | 22.2 |  3.9 | 10.8 |  3.7 | 30.7 | 19.9 | 12.6 | 17.4 | 52.5 | 12.4 | 11.9 | 13.6 |  7.3 | 27.1 | 11.3 | 18.3 |  2.1 | 33.3 |
| ERNIE    |  90.1 | 98.4 | 45.1 | 93.1 | 84.6 | 40.1 | 90.6 | 38.6 | 63.9 | 96.1 | 84.2 | 94.5 | 72.8 | 38   | 92.9 | 60.4 | 49.2 | 64.5 | 74.4 | 86.9 | 66.9 | 45   | 54.6 | 53.3 | 64.3 | 81.9 | 52.4 | 50.1 | 45.9 | 96   | 98.6 | 82.4 | 64   | 70.7 | 79.6 | 92.4 | 77.7 | 90   | 46.4 | 92.5 |
| GLM-4.5  |   9.5 | 28.8 |  8.6 | 36.9 | 13.8 |  3   | 16.3 |  2.9 | 21.2 |  8.2 |  6   | 38.2 | 12.2 |  9   | 30.1 | 10.7 | 21.6 | 25.1 | 23.7 | 31.7 | 20.2 |  6.1 | 10.9 | 10.3 | 17.9 | 49.7 | 41.3 | 26.1 | 23.3 | 35.9 | 42.8 | 21.9 | 33.6 | 15.5 | 19.6 | 23.5 | 27.9 | 27.8 |  8.5 | 30.9 |
| GPT-5    |  70   | 57   | 24.4 | 72.4 | 57   | 38.8 | 47.1 | 40.9 | 57.2 | 46.2 | 46.6 | 93   | 54.7 | 39.2 | 84.3 | 63.3 | 29.4 | 19.1 | 60.1 | 61   | 50   | 52.2 | 32.4 | 40.6 | 45.4 | 46.1 | 18   | 45.3 | 47.9 | 78.1 | 75.6 | 50.9 | 75   | 57   | 45.5 | 27.4 | 34.9 | 60   | 28.2 | 66.7 |
| Gemini   |  72.7 | 76.9 | 47.7 | 67.8 | 74.4 | 20.6 | 74.3 | 20.6 | 80.6 | 87.3 | 36   | 89.9 | 46.4 | 16.9 | 94.4 | 84.6 | 12.7 | 10.8 | 88.5 | 75   | 60.5 | 60.8 | 45.9 | 61.1 | 70.3 | 80.2 | 20.8 | 43   | 66.6 | 92.9 | 89.6 | 61.8 | 67   | 35.8 | 75.4 | 37.9 | 35.5 | 83.3 | 21.8 | 86.4 |
| Grok 4   | 100   | 99.2 | 83   | 90.3 | 96.4 | 45.3 | 84.5 | 75.2 | 99.3 | 97.3 | 93.6 | 99.8 | 70.6 | 48.4 | 98.8 | 96.1 | 36.9 | 43.2 | 94.2 | 80.2 | 88.9 | 89.5 | 75.5 | 75.2 | 86.9 | 97.4 | 40.9 | 85   | 75.8 | 99.6 | 86.9 | 70.3 | 82.7 | 90.6 | 76.9 | 53.2 | 55.4 | 96   | 36.7 | 95.5 |
| Hunyuan  |  90.8 | 97.6 | 90.5 | 97.1 | 95.2 | 86.9 | 97.9 | 89.5 | 94.4 | 97.4 | 98.2 | 98.1 | 94.4 | 88.6 | 94.8 | 96.3 | 91.9 | 97   | 96.4 | 95.6 | 94.6 | 93.7 | 78.1 | 97.9 | 93.5 | 94.6 | 91.4 | 90.5 | 95.9 | 96.2 | 99.8 | 97.1 | 96.4 | 95.2 | 96.8 | 98.8 | 97.8 | 97.8 | 94.6 | 99.5 |
| Kimi     |  48.6 | 73.4 | 11.2 | 48.5 | 20.3 | 35.2 | 83.2 | 28.3 | 48.2 | 29.4 | 32.2 | 80.9 | 27.7 | 18.4 | 49.7 | 38.6 | 42.2 | 25.9 | 59.4 | 72.8 | 53.4 | 11.4 | 35.7 | 24.7 | 36.9 | 49.7 | 31.1 | 23.7 | 39.4 | 75.4 | 79.8 | 38.6 | 46.5 | 32.7 | 52.1 | 36.5 | 27.2 | 52.8 | 21.1 | 64.7 |
| Llama 4  |  66.8 | 45   |  7.4 | 58.6 | 49.1 | 23.8 | 58.6 | 34.5 | 69.5 | 61   | 33.9 | 68.9 | 57.9 | 13.1 | 71.2 | 34.2 |  6.2 | 19.8 | 67.1 | 66.5 | 49   | 38.6 | 57.2 | 41.5 | 74.8 | 71.6 | 12.2 | 34.6 | 31.6 | 75.9 | 79.7 | 25.6 | 41.9 | 62.8 | 48.2 | 40.7 | 35.3 | 40.8 | 10.4 | 47   |
| Phi-4    |  96   | 98.6 | 73.8 | 94.3 | 91.8 | 66   | 96.2 | 69.4 | 98.7 | 98.8 | 83.2 | 98.1 | 93   | 85.6 | 98.6 | 85.8 | 54.2 | 79.1 | 92.8 | 93.1 | 80.8 | 88.6 | 85.1 | 87.6 | 94.7 | 89.6 | 56.7 | 75.2 | 79.9 | 97.6 | 97.8 | 89   | 94.8 | 93.3 | 92.6 | 90   | 89   | 98.5 | 61.8 | 97.3 |
| Qwen-3   |  22.8 | 32.8 |  3   | 22   |  8   |  9.3 | 16.5 |  5.1 |  9.2 | 13.9 | 17.1 | 71.2 | 25.3 |  3.4 | 41.8 | 12.2 | 12.5 | 16.6 | 17.8 | 34.1 | 25.8 |  5.5 | 15.3 | 11.4 | 29.6 | 26.6 | 32.1 | 29   | 11.8 | 45.9 | 71.6 | 21.7 | 28   | 18.3 | 25.2 | 25.9 | 37.2 | 35.2 | 13   | 38.2 |
| Seed     |  51.9 | 98.2 | 30.5 | 96.5 | 76.9 | 49.5 | 92   | 42.5 | 97.9 | 87.8 | 66.6 | 99.7 | 80.5 | 31.6 | 95.2 | 67.5 | 80.5 | 70.9 | 87.6 | 91.5 | 87.3 | 69.8 | 46.2 | 61.6 | 87.2 | 97.2 | 64.1 | 65.8 | 93.8 | 91.3 | 97.7 | 78.6 | 89   | 65.3 | 96.7 | 92.6 | 83.8 | 92.6 | 85.6 | 96.5 |

---

## Model-Topic Analysis Summary

- **Best Model-Topic Combination**: Claude 4 on GR
- **Best Combination Rate (%)**: 0.98
- **Worst Model-Topic Combination**: Grok 4 on AI
- **Worst Combination Rate (%)**: 100.00
- **Average Cross-Topic Variance by Model**: 322.57


---

## 6.1 Temporal Distribution of Citations

Distribution of valid vs hallucinated citations by publication year (2000-2025).

|   original_year |   Hallucinated |   Valid |   Total |   Hallucination Rate (%) |
|----------------:|---------------:|--------:|--------:|-------------------------:|
|            2000 |           1155 |    3028 |    4183 |                    27.61 |
|            2001 |           1675 |    3244 |    4919 |                    34.05 |
|            2002 |           1638 |    3764 |    5402 |                    30.32 |
|            2003 |           1610 |    4063 |    5673 |                    28.38 |
|            2004 |           1837 |    3464 |    5301 |                    34.65 |
|            2005 |           2019 |    4077 |    6096 |                    33.12 |
|            2006 |           2323 |    4307 |    6630 |                    35.04 |
|            2007 |           2169 |    4455 |    6624 |                    32.74 |
|            2008 |           2304 |    4592 |    6896 |                    33.41 |
|            2009 |           2023 |    5340 |    7363 |                    27.48 |
|            2010 |           2810 |    3919 |    6729 |                    41.76 |
|            2011 |           2951 |    4689 |    7640 |                    38.63 |
|            2012 |           3135 |    3967 |    7102 |                    44.14 |
|            2013 |           3367 |    3925 |    7292 |                    46.17 |
|            2014 |           3353 |    5023 |    8376 |                    40.03 |
|            2015 |           4396 |    5839 |   10235 |                    42.95 |
|            2016 |           4635 |    7278 |   11913 |                    38.91 |
|            2017 |           5556 |   10031 |   15587 |                    35.65 |
|            2018 |           8746 |    7206 |   15952 |                    54.83 |
|            2019 |          11892 |    8471 |   20363 |                    58.4  |
|            2020 |          17447 |    8568 |   26015 |                    67.07 |
|            2021 |          19556 |    5804 |   25360 |                    77.11 |
|            2022 |          21124 |    4618 |   25742 |                    82.06 |
|            2023 |          20297 |    4388 |   24685 |                    82.22 |
|            2024 |           5333 |     670 |    6003 |                    88.84 |
|            2025 |            315 |       4 |     319 |                    98.75 |

---

## Temporal Analysis Summary

- **Year with Most Citations**: 2020
- **Peak Year Citation Count**: 26015
- **Year with Highest Hallucination Rate**: 2025
- **Highest Hallucination Rate (%)**: 98.75
- **Year with Lowest Hallucination Rate**: 2009
- **Average Hallucination Rate (%)**: 48.24


---

## 6.2 Hallucination Consistency (Stability) by Model

Stability measures how consistently a model hallucinates the same fake papers. Higher stability (closer to 1) means the model repeatedly generates the same hallucinated citations.

| model    |   Mean Stability |   Std Dev |   Config Count |
|:---------|-----------------:|----------:|---------------:|
| DeepSeek |            0.226 |     0.216 |             80 |
| GLM-4.5  |            0.19  |     0.203 |             80 |
| Claude 4 |            0.181 |     0.187 |             80 |
| Qwen-3   |            0.175 |     0.199 |             80 |
| Llama 4  |            0.097 |     0.07  |             80 |
| Gemini   |            0.069 |     0.083 |             80 |
| Seed     |            0.047 |     0.091 |             78 |
| Kimi     |            0.041 |     0.08  |             80 |
| GPT-5    |            0.04  |     0.036 |             80 |
| Grok 4   |            0.035 |     0.027 |             80 |
| ERNIE    |            0.034 |     0.04  |             80 |
| Hunyuan  |            0.024 |     0.04  |             80 |
| Phi-4    |            0.007 |     0.012 |             80 |

---

## Hallucination Stability Summary

- **Most Consistent Hallucinator**: DeepSeek
- **Highest Stability Score**: 0.23
- **Least Consistent Hallucinator**: Phi-4
- **Lowest Stability Score**: 0.01
- **Average Stability Across Models**: 0.09


---

## 6.3 Valid Citation Stability by Model

Stability measures how consistently a model cites the same real papers. Higher stability means the model repeatedly cites the same valid references across runs.

| model    |   Mean Stability |   Std Dev |   Config Count |
|:---------|-----------------:|----------:|---------------:|
| DeepSeek |            0.577 |     0.094 |             80 |
| Qwen-3   |            0.574 |     0.09  |             80 |
| Claude 4 |            0.571 |     0.187 |             80 |
| Gemini   |            0.552 |     0.156 |             80 |
| GLM-4.5  |            0.528 |     0.115 |             80 |
| GPT-5    |            0.512 |     0.117 |             80 |
| Llama 4  |            0.469 |     0.15  |             80 |
| Grok 4   |            0.38  |     0.194 |             72 |
| Hunyuan  |            0.348 |     0.255 |             74 |
| Kimi     |            0.341 |     0.09  |             80 |
| ERNIE    |            0.323 |     0.164 |             80 |
| Seed     |            0.246 |     0.191 |             49 |
| Phi-4    |            0.191 |     0.146 |             79 |

---

## Valid Citation Stability Summary

- **Most Consistent Valid Citer**: DeepSeek
- **Highest Stability Score**: 0.58
- **Least Consistent Valid Citer**: Phi-4
- **Lowest Stability Score**: 0.19
- **Average Stability Across Models**: 0.43


---

## 6.6 Most Frequently Cited Papers by Topic

For each research topic, the most commonly cited valid paper across all models. High percentage indicates strong consensus among models about key references in that field.

| Topic   | Most Cited Title                                                                                |   Citation Count |   Total Valid in Topic |   Percentage (%) |
|:--------|:------------------------------------------------------------------------------------------------|-----------------:|-----------------------:|-----------------:|
| GR      | NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis                          |              352 |                   5449 |             6.46 |
| CL      | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks                                |              348 |                   5575 |             6.24 |
| NI      | Green Traffic Engineering for Satellite Networks Using Segment Routing Flexible Algorithm       |              138 |                   2312 |             5.97 |
| ET      | FCT O-RAN: Design and Deployment of a Multi-Vendor End-to-End Private 5G Testbed                |              148 |                   2600 |             5.69 |
| AR      | Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks  |              184 |                   3313 |             5.55 |
| DL      | Digital Libraries                                                                               |               96 |                   1730 |             5.55 |
| IT      | A Mathematical Theory of Communication                                                          |              260 |                   4760 |             5.46 |
| SI      | Semi-Supervised Classification with Graph Convolutional Networks                                |              287 |                   5877 |             4.88 |
| CV      | U-Net: Convolutional Networks for Biomedical Image Segmentation                                 |              262 |                   5425 |             4.83 |
| GT      | Algorithmic Game Theory                                                                         |              146 |                   3158 |             4.62 |
| DC      | MapReduce: Simplified Data Processing on Large Clusters                                         |              202 |                   4522 |             4.47 |
| AI      | Language Models are Few-Shot Learners                                                           |              154 |                   3595 |             4.28 |
| SD      | Musical genre classification of audio signals                                                   |              185 |                   4332 |             4.27 |
| CG      | Computational Geometry: Algorithms and Applications                                             |              178 |                   4252 |             4.19 |
| SE      | Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Based Testing      |              141 |                   3402 |             4.14 |
| FL      | Introduction to Automata Theory, Languages, and Computation                                     |              171 |                   4169 |             4.1  |
| GL      | Denoising Diffusion Probabilistic Models                                                        |              234 |                   5732 |             4.08 |
| CC      | Computational Complexity: A Modern Approach                                                     |              230 |                   5649 |             4.07 |
| HC      | AttenTrack: Mobile User Attention Awareness Based on Context and External Distractions          |              130 |                   3306 |             3.93 |
| MA      | Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations                        |              152 |                   3905 |             3.89 |
| MM      | LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition                      |              134 |                   3496 |             3.83 |
| PL      | Dato: A Task-Based Programming Model for Dataflow Accelerators                                  |              168 |                   4417 |             3.8  |
| CY      | Algorithms of Oppression: How Search Engines Reinforce Racism                                   |              114 |                   3201 |             3.56 |
| OS      | Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment                      |              153 |                   4355 |             3.51 |
| DS      | Introduction to Algorithms                                                                      |              202 |                   5901 |             3.42 |
| OH      | Cutting the Electric Bill for Internet-Scale Systems                                            |               71 |                   2123 |             3.34 |
| MS      | Robust Regression and Outlier Detection                                                         |              180 |                   5543 |             3.25 |
| PF      | Optimal Parallel Scheduling under Concave Speedup Functions                                     |              122 |                   3758 |             3.25 |
| CE      | A continuum multi-species biofilm model with a novel interaction scheme                         |              103 |                   3266 |             3.15 |
| LO      | Language-Based Information-Flow Security                                                        |              145 |                   4785 |             3.03 |
| LG      | Causality: Models, Reasoning, and Inference                                                     |              140 |                   4802 |             2.92 |
| SY      | Three-Phase PLLs: A Review of Recent Advances                                                   |               81 |                   3040 |             2.66 |
| IR      | BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer |              110 |                   4146 |             2.65 |
| CR      | A Method for Obtaining Digital Signatures and Public-Key Cryptosystems                          |               91 |                   3482 |             2.61 |
| NA      | Numerical Linear Algebra                                                                        |              121 |                   4735 |             2.56 |
| DM      | Polyphase codes with good periodic correlation properties                                       |              107 |                   4282 |             2.5  |
| SC      | Planning Algorithms                                                                             |              110 |                   4482 |             2.45 |
| RO      | Human-Robot Interaction: A Survey                                                               |               96 |                   3931 |             2.44 |
| NE      | Handbook of Evolutionary Computation                                                            |              114 |                   4713 |             2.42 |
| DB      | MapReduce: Simplified Data Processing on Large Clusters                                         |               71 |                   3412 |             2.08 |

---

