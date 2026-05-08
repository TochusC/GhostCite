# GhostCite — Cloud Sync Package

> 精简版实验数据包，用于云端同步与多设备协作。

---

## 说明

本目录从 `reference/Usenix26-Early_Reject/Experiment/` 和 `OpenScience/` 中提取了**核心数据、绘图脚本与关键图表**，移除了体积庞大且可重新生成/下载的文件，方便上传云端。

---

## 目录结构

```
cloud_sync/
├── core_metrics.csv              # 核心指标汇总表（论文关键数字）
├── llm_benchmark/
│   ├── scripts/                  # Python 脚本与 Jupyter Notebook
│   ├── data/                     # 汇总 CSV（幻觉率、相似度、样本等）
│   └── figures/                  # 论文图表（PDF/PNG）
├── paper_audit/
│   ├── scripts/                  # 分析 notebook + 脚本
│   ├── data/                     # 统计汇总 CSV
│   └── figures/                  # 时序与分布图
├── survey/
│   ├── scripts/                  # 问卷分析 notebook
│   ├── data/                     # 原始问卷数据与统计 CSV
│   └── figures/                  # 关键汇总图
├── llm_judger/                   # LLM Judger 基准测试
├── citeverifier/                 # CiteVerifier 开源框架代码
├── archival_analysis/            # 存档分析
└── user_study/                   # 用户研究
```

---

## 核心指标表（core_metrics.csv）

`core_metrics.csv` 汇总了论文三大研究的所有关键数字，共 181 行，按 `Module → Category → Metric` 组织：

| 模块 | 内容 |
|------|------|
| **LLM Benchmark** | 13 模型幻觉率、40 领域敏感度、在线搜索影响、稳定性、时间分布 |
| **Paper Audit** | 8 会议分布、2020–2025 趋势、无效引用分布 |
| **Survey** | 人口学、AI 采用、验证行为、审稿人行为、感知与责任 |
| **LLM Judger** | 13 模型判断准确率 |

可直接用 Excel / Google Sheets / Python pandas 打开筛选。

---

## 已排除的大文件

以下文件**未包含**在本包中（体积过大或可从其他渠道获取）：

- DBLP 数据库文件（`.db` / `.xml` / `.sqlite`，~23 GB）
- 原始 LLM 生成引用（`llm_reference/`，194 MB）
- 逐条验证结果 JSON（`validation_results/`，122 MB）
- 大型中间 CSV（`llm_new_res_v*.csv`，~1.2 GB）
- 论文审计中间结果（`results/`，~260 MB）
- Python 虚拟环境（`.venv/`，~15 MB）
- 编译产物（`.exe` / `.zip` / `.pyc`）

如需以上文件，请在原始工作区 `reference/Usenix26-Early_Reject/` 中查找。

---

## LLM Benchmark 聚合数据（替代 166 MB 原始文件）

原始 `llm_new_res_v3.csv`（166 MB，33 万行）**未包含在本包中**。作为替代，本地预处理生成了以下 5 个轻量级聚合文件，**总计 < 2 MB**，可远程直接复现全部 LLM Benchmark 图表：

| 文件 | 大小 | 可复现图表 |
|------|------|-----------|
| `llm_benchmark/data/results_by_config.csv` | ~1.9 MB | **核心聚合表**：模型幻觉率、在线搜索影响、引用数量影响 |
| `llm_benchmark/data/model_topic_heatmap.csv` | ~15 KB | **模型×领域热力图** |
| `llm_benchmark/data/temporal_distribution.csv` | ~5 KB | **时间分布图**（2000–2025） |
| `llm_benchmark/data/stability_data.csv` | ~1.4 KB | **幻觉稳定性 & 有效引用稳定性** |
| `llm_benchmark/data/top_cited_by_topic.csv` | ~4 KB | **各领域最常引用论文** |

### 快速使用示例

```python
import pandas as pd

# 1) 模型幻觉率 + 在线搜索 + 引用数量
results = pd.read_csv('llm_benchmark/data/results_by_config.csv')
model_rate = results.groupby('model')['hallucination_rate'].mean()
online = results.groupby(['model', 'thinking', 'online'])['hallucination_rate'].mean()
scaling = results.groupby(['model', 'num_refs'])['hallucination_rate'].mean()

# 2) 模型×领域热力图
heatmap = pd.read_csv('llm_benchmark/data/model_topic_heatmap.csv')
pivot = heatmap.pivot(index='model', columns='topic', values='hallucination_rate')

# 3) 时间分布
temporal = pd.read_csv('llm_benchmark/data/temporal_distribution.csv')

# 4) 稳定性
stability = pd.read_csv('llm_benchmark/data/stability_data.csv')
```

---

## 使用方式

1. **写论文时引用数据**：直接打开 `core_metrics.csv` 查找所需数字。
2. **复现 LLM Benchmark 图表**：使用上述聚合 CSV，无需原始大文件。
3. **复现其他模块图表**：进入对应模块的 `scripts/`，用 Jupyter Notebook 或 Python 重新运行。
4. **补充分析**：在 `data/` 下的 CSV 基础上继续处理。

---

## 体积对比

| 项目 | 大小 |
|------|------|
| 原始实验数据 | ~24.7 GB |
| 本精简包 | ~43 MB |
| 压缩比 | **> 99.8%** |

---

*Generated: 2026-05-06*
