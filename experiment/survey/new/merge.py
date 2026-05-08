import html
import json
import pandas as pd

# 根据你的实际路径修改
cn_path = "Chinese.csv"
en_path = "English.csv"
out_path = "Merged.csv"
mapping_path = "mapping.json"

# Comprehensive mapping from Chinese to English options
cn_to_en = {
    # Position (Q2)
    "本科生": "Undergraduate student",
    "硕士生": "Master's Student",
    "博士生": "PhD Student",
    "博士后": "Postdoc",
    "教职人员（教授/讲师）": "Faculty (Professor/Lecturer)",
    "研究员": "Researcher",
    "其他": "Other",

    # Research Area (Q3)
    "AI安全": "AI Security",
    "网络安全": "Network Security",
    "系统安全": "System Security",
    "密码学": "Cryptography",
    "软件工程": "Software Engineering",
    "人工智能与机器学习": "AI & Machine Learning",

    # Papers Published (Q4)
    "0": "0",
    "1-5": "1-5",
    "6-10": "6-10",
    "11-20": "11-20",
    "20+": "20+",

    # Yes/No
    "是": "Yes",
    "否": "No",
    "是，我同意参与调查": "Yes, I consent to participate.",
    "否，我不同意": "No",

    # AI Tool Types (Q10)
    "通用大语言模型（如 ChatGPT, Claude, Gemini）": "General-purpose LLMs (e.g., ChatGPT, Claude, Gemini)",
    "代码助手（如 GitHub Copilot, Cursor）": "Coding Assistants (e.g., GitHub Copilot, Cursor)",
    "学术专用搜索引擎（如 Elicit, Consensus, Scite, Semantic Scholar）": "Academic search engines (e.g., Elicit, Semantic Scholar)",
    "AI 驱动的阅读/笔记工具（如 ChatPDF, Humata）": "AI-powered reading tools (e.g., ChatPDF, Humata)",

    # Writing stage (Q7)
    "概念构思": "Conceptualization;",
    "概 念构思": "Conceptualization",
    "撰写引言": "Writing the Introduction",
    "文献搜索与综述": "Literature Search & Review",
    "技术细节描述": "Technical Description",
    "格式化参考文献": "Formatting References",

    # Related work search (Q8)
    "在谷歌学术/DBLP上进行关键词搜索": "Keyword search on Google Scholar/DBLP",
    "追踪其他论文的引用": "Following citations from other papers",
    "浏览会议论文集": "Browsing conference proceedings",
    "使用 AI 驱动的工具（如 ChatGPT, Connected Papers）": "Using AI-powered tools (e.g., ChatGPT, Connected Papers)",

    # Text polishing (Q11)
    "是，几乎每一句都用": "Yes, for almost every sentence",
    "是，仅针对特定的困难段落": "Yes, for specific difficult paragraphs",
    "是，但仅用于最后的校对": "Yes, but only for final proofreading",
    "否，我更相信自己的写作": "No, I trust my own writing more",

    # Citation AI usage (Q12)
    "格式转换:将参考文献转换为特定格式，比如 BibTeX": "Formatting: Converting references into specific formats (e.g., BibTeX)",
    "发现:要求 AI 推荐特定主题的论文": "Discovery: Asking AI to recommend papers on a specific topic",
    "填补空白:\"我需要为这句话找一个引用，请帮我找一个。\"": "Gap Filling: \"I need a citation for this statement, please find one.\"",
    "摘要:要求 AI 总结论文以决定是否引用": "Summarization: Asking AI to summarize a paper to decide whether to cite it",
    "验证:询问 AI 某篇论文是否存在": "Verification: Asking AI if a specific paper exists",
    "不使用:不在引用部分使用AI工具": "None: I do not use AI tools for citation-related tasks (Please do not select other options if this is checked)",

    # Hallucination frequency (Q13)
    "非常频繁（>50% 的时间）": "Very Often (>50%)",
    "经常（20-50%）": "Often (20-50%)",
    "偶尔（<20%）": "Occasionally (<20%)",
    "从未": "Never",
    "我不用通用 LLM 找参考文献": "I do not use General LLMs for finding references",

    # Verification (Q14)
    "是，我会通过谷歌学术/DBLP 100% 验证": "Always verify (100%)",
    "我只在需要阅读全文时才验证": "Only if reading full text",
    "我只在标题看起来可疑时验证": "Only if suspicious",
    "否，如果元数据连贯，我信任该工具": "Trust AI",

    # Cited without reading (Q15)
    "是，经常": "Yes, often",
    "是，一两次": "Yes, once or twice",
    "否，从不": "No, never",

    # Agreement scale
    "非常同意": "Strongly agree",
    "有点同意": "Somewhat agree",
    "中立": "Neutral",
    "有点不同意": "Somewhat disagree",
    "非常不同意": "Strongly disagree",

    # Broken DOI strategy (Q17)
    "我假设论文存在并尝试手动查找": "I assume the paper exists and try to find it manually",
    "我假设论文是幻觉并立即舍弃": "I assume the paper is a hallucination and discard it immediately",
    "我要求 AI 提供另一个链接": "I ask the AI to provide a different link",
    "我保留引用但删除 DOI": "I keep the citation but remove the DOI",

    # Metadata source (Q18)
    "直接从出版商导出": "Direct export from publisher",
    "谷歌学术的\"引用\"按钮": "Google Scholar \"Cite\" button",
    "复制粘贴自其他论文的参考文献列表": "Copy from other papers",
    "由 AI 工具生成": "AI-generated",

    # Verify claim frequency (Q19)
    "每次都会": "Every single time",
    "大部分时间": "Most of the time",
    "仅针对关键观点": "Only for critical claims",
    "很少": "Rarely",

    # Cite without full text (Q20)
    "是，如果有必要": "Yes, if necessary",

    # Reviewer check refs (Q22)
    "是，仔细检查": "Yes, carefully",
    "是，略读": "Yes, skimming",

    # What reviewers check (Q23)
    "自引滥用": "Self-citation abuse",
    "遗漏关键相关工作": "Missing key related work",
    "元数据的正确性（年份、会议）": "Correctness of metadata (Year, Venue)",
    "论文是否存在": "Existence of the papers",

    # Click DOI frequency (Q24)
    "经常": "Frequently",
    "偶尔": "Occasionally",
    "很少": "Rarely",
    "从未": "Never",

    # Verify preprint (Q26)
    "总是": "Always",
    "有时": "Sometimes",

    # Handle non-English (Q27)
    "我用翻译工具检查": "I check them using translation tools",
    "我忽略它们": "I ignore them",
    "我要求作者澄清": "I ask the authors to clarify",
    "我假设它们是有效的": "I assume they are valid",

    # Peer review effectiveness (Q29)
    "非常有效": "Very effective",
    "比较有效": "Somewhat effective",
    "不太有效": "Not very effective",
    "无效": "Ineffective",

    # Severity (Q30)
    "严重危机": "Critical crisis",
    "主要问题": "Major problem",
    "轻微干扰": "Minor nuisance",
    "不是问题": "Not a problem",

    # Responsibility (Q31)
    "作者": "Authors",
    "审稿人": "Reviewers",
    "出版商（编辑检查）": "Publishers",
    "AI 工具开发者": "AI tool developers",

    # Automated tools (Q32)
    "是，绝对应该": "Yes, absolutely",
    "也许": "Maybe",
    "否，负担太重": "No",

    # Reaction to one error (Q37)
    "拒稿": "Reject the paper",
    "要求大修": "Ask for major revision",
    "在次要意见中提及": "Mention in minor comments",
    "忽略": "Ignore",

    # Reaction to multiple errors (Q38)
    "立即拒稿（伦理问题）": "Reject immediately (Ethical concern)",
    "要求解释": "Ask for explanation",
    "认为是无心之失": "Consider innocent mistake",

    # Copy-paste BibTeX (Q40)
    "是，很少": "Yes, rarely",
    "否，从未": "No, never",

    # Report fake reference (Q39)
    "是，我会直接联系作者": "Yes, I would contact the authors directly",
    "是，我会联系程序委员会主席或期刊编辑": "Yes, I would contact the PC Chairs or Journal Editors",
    "否，我会私下验证但不采取行动": "No, I would verify it privately but take no action",
    "否，我会忽略它": "No, I would ignore it",

    # Skipped/empty
    "(跳过)": "",
    "(空)": "",

    # Metadata fields
    "微信": "WeChat",
    "企业微信": "WeCom",
    "手机提交": "Mobile",
    "链接": "Link",
    "直接访问": "Direct",
}


def normalize_option(option):
    if not isinstance(option, str):
        return option
    option = html.unescape(option)
    option = option.replace("\u201c", '"').replace("\u201d", '"')
    option = option.replace("\u2018", "'").replace("\u2019", "'")
    return option


def translate_cn_to_en(option):
    normalized = normalize_option(option)
    return cn_to_en.get(normalized, cn_to_en.get(option, option))


def translate_cell(value):
    if not isinstance(value, str):
        return value
    value = value.strip()
    if not value:
        return value
    value = normalize_option(value)
    if value.endswith("秒"):
        digits = value[:-1].strip()
        if digits.isdigit():
            return f"{digits}s"
    if "┋" in value:
        parts = [p.strip() for p in value.split("┋")]
        return " & ".join(translate_cn_to_en(p) for p in parts)
    if ";" in value:
        parts = [p.strip() for p in value.split(";")]
        return " & ".join(translate_cn_to_en(p) for p in parts)
    return translate_cn_to_en(value)

# 读取中文问卷
df_cn = pd.read_csv(cn_path)

# 读取英文问卷
df_en = pd.read_csv(en_path)

# 读取中英列名映射：{ "中文列名": "English header" }
with open(mapping_path, "r", encoding="utf-8") as mapping_file:
    col_mapping = json.load(mapping_file)

# 基础校验
# 允许多个中文列名映射到同一个英文列名（比如不同引号/转义版本）

missing_cn = [col for col in df_cn.columns if col not in col_mapping]
if missing_cn:
    raise ValueError(f"列名映射不完整：Chinese 未映射列={missing_cn}")

# 用映射将中文列名统一为英文列名
df_cn = df_cn.rename(columns=col_mapping)

# Drop sensitive metadata columns
sensitive_columns = {
    "Timestamp",
    "Duration",
    "Source",
    "Source Detail",
    "IP Address",
}
df_cn = df_cn.drop(columns=[c for c in df_cn.columns if c in sensitive_columns])
df_en = df_en.drop(columns=[c for c in df_en.columns if c in sensitive_columns])

# Translate Chinese responses to English
no_translate_columns = {
    "Any additional comments on the state of academic integrity and writing tools?",
}
df_cn = df_cn.apply(
    lambda col: col.map(translate_cell) if col.name not in no_translate_columns else col
)

# Replace skip markers in free-text comments with empty string
comments_col = "Any additional comments on the state of academic integrity and writing tools?"
if comments_col in df_cn.columns:
    df_cn[comments_col] = df_cn[comments_col].replace({"(跳过)": "", "(skip)": ""})
if comments_col in df_en.columns:
    df_en[comments_col] = df_en[comments_col].replace({"(跳过)": "", "(skip)": ""})

# 按中文问卷顺序对齐为统一的英文表头
target_columns = list(df_cn.columns)

# English 中缺失的列补空值，多余列直接丢弃
for col in target_columns:
    if col not in df_en.columns:
        df_en[col] = pd.NA

df_en = df_en[target_columns]

# 按行合并
df_merged = pd.concat([df_cn, df_en], ignore_index=True)

# 去掉最后一列
df_merged = df_merged.iloc[:, :-1]


# 导出合并后的文件
df_merged.to_csv(out_path, index=False, encoding="utf-8-sig")



print(f"合并完成，已保存到：{out_path}")