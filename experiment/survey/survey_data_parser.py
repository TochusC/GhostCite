"""
Survey Data Parser: Parse Chinese and English survey data and generate combined CSV

This script parses:
- Chinese Survey (chinese.md): 74 respondents (aggregated statistics)
- English Survey (CSV): 18 individual responses

Output: survey_combined_statistics.csv
"""

import pandas as pd
import re
import html
import os

# =============================================================================
# 1. Parse Chinese Survey Data (Aggregated Statistics)
# =============================================================================

def parse_chinese_survey(filepath='chinese.md'):
    """Parse Chinese survey from markdown format"""
    with open(filepath, 'r', encoding='utf-8') as f:
        cn_content = f.read()

    # Split by questions (第X题)
    question_pattern = r'第(\d+)题\s+(.+?)\s+\[([单多]选题|填空题)\]'
    questions = re.findall(question_pattern, cn_content)

    print(f"Found {len(questions)} questions in Chinese survey")
    for q_num, q_text, q_type in questions[:5]:
        print(f"  Q{q_num}: {q_text[:50]}... [{q_type}]")

    # Parse each question's options and counts
    cn_data = {}
    sections = re.split(r'第\d+题', cn_content)

    for i, (q_num, q_text, q_type) in enumerate(questions):
        section = sections[i+1] if i+1 < len(sections) else ""
        
        # Find table data: lines with "选项\t小计\t比例" pattern
        lines = section.strip().split('\n')
        options = {}
        
        in_table = False
        for line in lines:
            if '选项' in line and '小计' in line:
                in_table = True
                continue
            if '本题有效填写人次' in line:
                in_table = False
                continue
            if in_table and '\t' in line:
                parts = line.split('\t')
                if len(parts) >= 2:
                    option = parts[0].strip()
                    try:
                        count = int(parts[1].strip())
                        options[option] = count
                    except:
                        pass
        
        cn_data[int(q_num)] = {
            'text': q_text.strip(),
            'type': q_type,
            'options': options
        }

    print(f"\nParsed {len(cn_data)} questions with options")
    # Show sample
    for q_num in [2, 9, 13, 30]:
        if q_num in cn_data:
            print(f"\nQ{q_num}: {cn_data[q_num]['text'][:40]}...")
            for opt, cnt in list(cn_data[q_num]['options'].items())[:3]:
                print(f"  - {opt}: {cnt}")
    
    return cn_data


# =============================================================================
# 2. Parse English Survey Data (Individual Responses)
# =============================================================================

def count_english_responses(df, col_idx, col_idx2=None):
    """Count responses from one or two columns (for branching questions)"""
    counts = {}
    
    # Primary column
    if col_idx < len(df.columns):
        vals = df.iloc[:, col_idx].dropna()
        for val in vals:
            if str(val).strip():
                # Handle multi-select (semicolon separated)
                for v in str(val).split(';'):
                    v = v.strip()
                    if v:
                        counts[v] = counts.get(v, 0) + 1
    
    # Secondary column (for branching)
    if col_idx2 and col_idx2 < len(df.columns):
        vals = df.iloc[:, col_idx2].dropna()
        for val in vals:
            if str(val).strip():
                for v in str(val).split(';'):
                    v = v.strip()
                    if v:
                        counts[v] = counts.get(v, 0) + 1
    
    return counts


def parse_english_survey(filepath='Survey on Academic Writing Workflows, AI Tools, and Citation Integrity.csv'):
    """Load and parse English survey CSV"""
    df_en = pd.read_csv(filepath)
    n_en = len(df_en)
    print(f"\nEnglish survey: {n_en} responses")
    print(f"Columns: {len(df_en.columns)}")
    
    # Test position distribution
    position_counts_en = count_english_responses(df_en, 2)
    print("\nEnglish Position Distribution:")
    for k, v in position_counts_en.items():
        print(f"  {k}: {v}")
    
    return df_en


# =============================================================================
# 3. Chinese-English Option Mapping
# =============================================================================

# Comprehensive mapping from Chinese to English options
CN_TO_EN = {
    # Position (Q2)
    '本科生': 'Undergraduate student',
    '硕士生': "Master's Student",
    '博士生': 'PhD Student',
    '博士后': 'Postdoc',
    '教职人员（教授/讲师）': 'Faculty (Professor/Lecturer)',
    '研究员': 'Researcher',
    '其他': 'Other',
    
    # Research Area (Q3)
    'AI安全': 'AI Security',
    '网络安全': 'Network Security',
    '系统安全': 'System Security',
    '密码学': 'Cryptography',
    '软件工程': 'Software Engineering',
    '人工智能与机器学习': 'AI & Machine Learning',
    
    # Papers Published (Q4)
    '0': '0',
    '1-5': '1-5',
    '6-10': '6-10',
    '11-20': '11-20',
    '20+': '20+',
    
    # Yes/No
    '是': 'Yes',
    '否': 'No',
    '是，我同意参与调查': 'Yes, I consent to participate.',
    '否，我不同意': 'No',
    
    # AI Tool Types (Q10)
    '通用大语言模型（如 ChatGPT, Claude, Gemini）': 'General-purpose LLMs (e.g., ChatGPT, Claude, Gemini)',
    '代码助手（如 GitHub Copilot, Cursor）': 'Coding Assistants (e.g., GitHub Copilot, Cursor)',
    '学术专用搜索引擎（如 Elicit, Consensus, Scite, Semantic Scholar）': 'Academic search engines (e.g., Elicit, Semantic Scholar)',
    'AI 驱动的阅读/笔记工具（如 ChatPDF, Humata）': 'AI-powered reading tools (e.g., ChatPDF, Humata)',
    
    # Text polishing (Q11)
    '是，几乎每一句都用': 'Yes, for almost every sentence',
    '是，仅针对特定的困难段落': 'Yes, for specific difficult paragraphs',
    '是，但仅用于最后的校对': 'Yes, but only for final proofreading',
    '否，我更相信自己的写作': 'No, I trust my own writing more',
    
    # Citation AI usage (Q12)
    '格式转换:将参考文献转换为特定格式，比如 BibTeX': 'Formatting',
    '发现:要求 AI 推荐特定主题的论文': 'Discovery',
    '填补空白:"我需要为这句话找一个引用，请帮我找一个。"': 'Gap-filling',
    '摘要:要求 AI 总结论文以决定是否引用': 'Summarization',
    '验证:询问 AI 某篇论文是否存在': 'Verification',
    '不使用:不在引用部分使用AI工具': 'None',
    
    # Hallucination frequency (Q13)
    '非常频繁（>50% 的时间）': 'Very Often (>50%)',
    '经常（20-50%）': 'Often (20-50%)',
    '偶尔（<20%）': 'Occasionally (<20%)',
    '从未': 'Never',
    '我不用通用 LLM 找参考文献': "Don't use LLMs",
    
    # Verification (Q14)
    '是，我会通过谷歌学术/DBLP 100% 验证': 'Always verify (100%)',
    '我只在需要阅读全文时才验证': 'Only if reading full text',
    '我只在标题看起来可疑时验证': 'Only if suspicious',
    '否，如果元数据连贯，我信任该工具': 'Trust AI',
    
    # Cited without reading (Q15)
    '是，经常': 'Yes, often',
    '是，一两次': 'Yes, once or twice',
    '否，从不': 'No, never',
    
    # Agreement scale
    '非常同意': 'Strongly agree',
    '有点同意': 'Somewhat agree',
    '中立': 'Neutral',
    '有点不同意': 'Somewhat disagree',
    '非常不同意': 'Strongly disagree',
    
    # Broken DOI strategy (Q17)
    '我假设论文存在并尝试手动查找': 'Try to find manually',
    '我假设论文是幻觉并立即舍弃': 'Assume hallucination, discard',
    '我要求 AI 提供另一个链接': 'Ask AI for another link',
    '我保留引用但删除 DOI': 'Keep citation, remove DOI',
    
    # Metadata source (Q18)
    '直接从出版商导出': 'Direct export from publisher',
    '谷歌学术的"引用"按钮': 'Google Scholar "Cite" button',
    '复制粘贴自其他论文的参考文献列表': 'Copy from other papers',
    '由 AI 工具生成': 'AI-generated',
    
    # Verify claim frequency (Q19)
    '每次都会': 'Every single time',
    '大部分时间': 'Most of the time',
    '仅针对关键观点': 'Only for critical claims',
    '很少': 'Rarely',
    
    # Cite without full text (Q20)
    '是，如果有必要': 'Yes, if necessary',
    
    # Reviewer check refs (Q22)
    '是，仔细检查': 'Yes, carefully',
    '是，略读': 'Yes, skimming',
    
    # What reviewers check (Q23)
    '自引滥用': 'Self-citation abuse',
    '遗漏关键相关工作': 'Missing key related work',
    '元数据的正确性（年份、会议）': 'Correctness of metadata',
    '论文是否存在': 'Existence of papers',
    
    # Click DOI frequency (Q24)
    '经常': 'Frequently',
    '偶尔': 'Occasionally',
    '很少': 'Rarely',
    '从未': 'Never',
    
    # Verify preprint (Q26)
    '总是': 'Always',
    '有时': 'Sometimes',
    
    # Handle non-English (Q27)
    '我用翻译工具检查': 'Check with translation tools',
    '我忽略它们': 'Ignore them',
    '我要求作者澄清': 'Ask authors to clarify',
    '我假设它们是有效的': 'Assume they are valid',
    
    # Peer review effectiveness (Q29)
    '非常有效': 'Very effective',
    '比较有效': 'Somewhat effective',
    '不太有效': 'Not very effective',
    '无效': 'Ineffective',
    
    # Severity (Q30)
    '严重危机': 'Critical crisis',
    '主要问题': 'Major problem',
    '轻微干扰': 'Minor nuisance',
    '不是问题': 'Not a problem',
    
    # Responsibility (Q31)
    '作者': 'Authors',
    '审稿人': 'Reviewers',
    '出版商（编辑检查）': 'Publishers',
    'AI 工具开发者': 'AI tool developers',
    
    # Automated tools (Q32)
    '是，绝对应该': 'Yes, absolutely',
    '也许': 'Maybe',
    '否，负担太重': 'No',
    
    # Reaction to one error (Q37)
    '拒稿': 'Reject the paper',
    '要求大修': 'Ask for major revision',
    '在次要意见中提及': 'Mention in minor comments',
    '忽略': 'Ignore',
    
    # Reaction to multiple errors (Q38)
    '立即拒稿（伦理问题）': 'Reject immediately (Ethical concern)',
    '要求解释': 'Ask for explanation',
    '认为是无心之失': 'Consider innocent mistake',
    
    # Copy-paste BibTeX (Q40)
    '是，很少': 'Yes, rarely',
    '否，从未': 'No, never',
    
    # Report fake reference (Q39)
    '是，我会直接联系作者': 'Yes, I would contact the authors directly',
    '是，我会联系程序委员会主席或期刊编辑': 'Yes, I would contact the PC Chairs or Journal Editors',
    '否，我会私下验证但不采取行动': 'No, I would verify it privately but take no action',
    '否，我会忽略它': 'No, I would ignore it',
}


def normalize_option(option):
    """Normalize Chinese option text by decoding HTML entities and normalizing quotes"""
    if not isinstance(option, str):
        return option
    # Decode HTML entities like &gt; -> > and &lt; -> <
    option = html.unescape(option)
    # Normalize Chinese quotes to ASCII quotes
    option = option.replace('\u201c', '"').replace('\u201d', '"')
    option = option.replace('\u2018', "'").replace('\u2019', "'")
    return option


def translate_cn_to_en(option):
    """Translate Chinese option to English"""
    normalized = normalize_option(option)
    return CN_TO_EN.get(normalized, CN_TO_EN.get(option, option))


# =============================================================================
# 4. Question Mapping and Merge Statistics
# =============================================================================

# Define question mapping between Chinese (by number) and English (by column index)
QUESTION_MAPPING = {
    # Demographics
    2: {'en_col': 2, 'name': 'position'},
    3: {'en_col': 3, 'name': 'research_area'},
    4: {'en_col': 4, 'name': 'papers_published'},
    5: {'en_col': 5, 'name': 'native_english'},
    6: {'en_col': 6, 'name': 'is_reviewer'},
    
    # AI Usage
    9: {'en_col': [9, 23], 'name': 'use_ai_tools'},
    10: {'en_col': [10, 24], 'name': 'ai_tool_types'},
    11: {'en_col': [11, 25], 'name': 'ai_text_polish'},
    12: {'en_col': [12, 26], 'name': 'ai_citation_usage'},
    13: {'en_col': [13, 27], 'name': 'hallucination_freq'},
    14: {'en_col': [14, 28], 'name': 'verify_ai_ref'},
    15: {'en_col': [15, 29], 'name': 'cite_without_reading'},
    16: {'en_col': [16, 30], 'name': 'agree_ai_easier_harder'},
    17: {'en_col': [17, 31], 'name': 'broken_doi_strategy'},
    
    # Citation practices (all respondents)
    18: {'en_col': [18, 32], 'name': 'metadata_source'},
    19: {'en_col': [19, 33], 'name': 'verify_claim_freq'},
    20: {'en_col': [20, 34], 'name': 'cite_without_fulltext'},
    21: {'en_col': [21, 35], 'name': 'pressure_many_refs'},
    
    # Reviewer perspective (only reviewers)
    22: {'en_col': 36, 'name': 'reviewer_check_refs'},
    23: {'en_col': 37, 'name': 'what_reviewers_check'},
    24: {'en_col': 38, 'name': 'click_doi_verify'},
    25: {'en_col': 39, 'name': 'suspected_fake'},
    26: {'en_col': 40, 'name': 'verify_preprint'},
    27: {'en_col': 41, 'name': 'handle_non_english'},
    
    # Integrity perception (all)
    28: {'en_col': 42, 'name': 'agree_bib_accuracy'},
    29: {'en_col': 43, 'name': 'peer_review_effective'},
    30: {'en_col': 44, 'name': 'severity'},
    31: {'en_col': 45, 'name': 'responsibility'},
    32: {'en_col': 46, 'name': 'automated_tools'},
    33: {'en_col': 47, 'name': 'agree_cite_ai_summary'},
    
    # Edge cases
    34: {'en_col': 49, 'name': 'seen_scrambled_authors'},
    35: {'en_col': 50, 'name': 'seen_wrong_venue_year'},
    36: {'en_col': 51, 'name': 'accept_tech_report'},
    37: {'en_col': 52, 'name': 'reaction_one_error'},
    38: {'en_col': 53, 'name': 'reaction_multiple_errors'},
    39: {'en_col': 54, 'name': 'report_fake_ref'},
    40: {'en_col': 48, 'name': 'copypaste_bibtex'},
    41: {'en_col': 55, 'name': 'verify_all_bibtex_fields'},
    42: {'en_col': 56, 'name': 'use_semantic_scholar'},
}


def merge_counts(cn_opts, en_counts):
    """Merge Chinese (translated) and English counts"""
    merged = {}
    
    # Add Chinese counts (translated)
    for cn_opt, count in cn_opts.items():
        en_opt = translate_cn_to_en(cn_opt)
        merged[en_opt] = merged.get(en_opt, 0) + count
    
    # Add English counts
    for en_opt, count in en_counts.items():
        # Try to match with existing keys (handle slight variations)
        matched = False
        for key in merged:
            if key.lower() in en_opt.lower() or en_opt.lower() in key.lower():
                merged[key] += count
                matched = True
                break
        if not matched:
            merged[en_opt] = merged.get(en_opt, 0) + count
    
    return merged


def build_combined_statistics(cn_data, df_en):
    """Build combined statistics from Chinese and English data"""
    combined_stats = {}

    for cn_q, mapping in QUESTION_MAPPING.items():
        if cn_q not in cn_data:
            continue
            
        cn_opts = cn_data[cn_q]['options']
        
        # Get English counts
        en_cols = mapping['en_col']
        if isinstance(en_cols, list):
            en_counts = count_english_responses(df_en, en_cols[0], en_cols[1] if len(en_cols) > 1 else None)
        else:
            en_counts = count_english_responses(df_en, en_cols)
        
        # Merge
        merged = merge_counts(cn_opts, en_counts)
        
        combined_stats[mapping['name']] = {
            'cn_text': cn_data[cn_q]['text'],
            'counts': merged,
            'cn_n': sum(cn_opts.values()),
            'en_n': sum(en_counts.values()),
        }

    print(f"\nBuilt combined statistics for {len(combined_stats)} questions")
    return combined_stats


def export_to_csv(combined_stats, output_path='survey_combined_statistics.csv'):
    """Export summary statistics to CSV"""
    summary_rows = []

    for name, data in combined_stats.items():
        for option, count in data['counts'].items():
            summary_rows.append({
                'question': name,
                'option': option,
                'count': count,
                'cn_total': data['cn_n'],
                'en_total': data['en_n']
            })

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(output_path, index=False)
    print(f"\nSaved combined statistics to: {output_path}")
    print(f"Total rows: {len(summary_df)}")
    return summary_df


def display_sample_stats(combined_stats):
    """Display sample combined statistics"""
    print("\n" + "="*60)
    print("Sample Combined Statistics")
    print("="*60)
    
    for name in ['position', 'use_ai_tools', 'hallucination_freq', 'severity']:
        if name in combined_stats:
            print(f"\n=== {name} ===")
            print(f"CN: {combined_stats[name]['cn_n']}, EN: {combined_stats[name]['en_n']}")
            for opt, cnt in sorted(combined_stats[name]['counts'].items(), key=lambda x: -x[1]):
                print(f"  {opt}: {cnt}")


# =============================================================================
# Main
# =============================================================================

def main():
    """Main function to parse surveys and generate combined CSV"""
    print("="*60)
    print("Survey Data Parser")
    print("="*60)
    
    # Parse Chinese survey
    print("\n[1] Parsing Chinese Survey...")
    cn_data = parse_chinese_survey('chinese.md')
    
    # Parse English survey
    print("\n[2] Parsing English Survey...")
    df_en = parse_english_survey('Survey on Academic Writing Workflows, AI Tools, and Citation Integrity.csv')
    
    # Build combined statistics
    print("\n[3] Building Combined Statistics...")
    combined_stats = build_combined_statistics(cn_data, df_en)
    
    # Display sample
    display_sample_stats(combined_stats)
    
    # Export to CSV
    print("\n[4] Exporting to CSV...")
    export_to_csv(combined_stats)
    
    print("\n" + "="*60)
    print("Done!")
    print("="*60)
    
    return combined_stats


if __name__ == '__main__':
    combined_stats = main()
