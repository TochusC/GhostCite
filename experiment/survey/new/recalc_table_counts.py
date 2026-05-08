import json
import html
from collections import Counter, defaultdict

import pandas as pd


def load_mapping(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_col(col):
    if isinstance(col, str) and col.endswith(".1"):
        return col[:-2]
    return col


def normalize_option(option):
    if not isinstance(option, str):
        return option
    option = html.unescape(option)
    option = option.replace("\u201c", '"').replace("\u201d", '"')
    option = option.replace("\u2018", "'").replace("\u2019", "'")
    return option.strip()


def load_cn_to_en():
    # Import from survey_data_parser.py to reuse CN_TO_EN
    import importlib.util
    import pathlib

    parser_path = pathlib.Path(__file__).resolve().parents[1] / "survey_data_parser.py"
    spec = importlib.util.spec_from_file_location("survey_data_parser", str(parser_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CN_TO_EN, module.translate_cn_to_en


def split_multi(value):
    if not isinstance(value, str):
        return []
    value = value.strip()
    if not value or value in {"(跳过)", "(空)", "(skip)", "(empty)"}:
        return []
    if "┋" in value:
        return [v.strip() for v in value.split("┋") if v.strip()]
    if ";" in value:
        return [v.strip() for v in value.split(";") if v.strip()]
    return [value]


def is_consented(val):
    if not isinstance(val, str):
        return False
    val = val.strip()
    return "同意" in val or "Yes, I consent" in val


def canonicalize_option(option, cn_to_en, translate_cn_to_en):
    if not isinstance(option, str):
        return option
    option = normalize_option(option)
    option = translate_cn_to_en(option)

    # Map English variants to canonical table labels
    synonyms = {
        "None: I do not use AI tools for citation-related tasks (Please do not select other options if this is checked)": "None (do not use AI for citations)",
        "None": "None (do not use AI for citations)",
        "Formatting": "Formatting (convert to BibTeX, etc.)",
        "Formatting: Converting references into specific formats (e.g., BibTeX)": "Formatting (convert to BibTeX, etc.)",
        "Discovery": "Discovery (recommend papers on topic)",
        "Discovery: Asking AI to recommend papers on a specific topic": "Discovery (recommend papers on topic)",
        "Summarization": "Summarization (decide whether to cite)",
        "Summarization: Asking AI to summarize a paper to decide whether to cite it": "Summarization (decide whether to cite)",
        "Gap-filling": "Gap-filling (citation for a sentence)",
        "Gap-filling: Find a citation for a sentence": "Gap-filling (citation for a sentence)",
        "Gap-filling: Asking AI to find a citation for a sentence": "Gap-filling (citation for a sentence)",
        "Gap-filling: Asking AI to find a citation for a sentence.": "Gap-filling (citation for a sentence)",
        "Verification": "Verification (ask if paper exists)",
        "Verification: Asking AI if a specific paper exists": "Verification (ask if paper exists)",
        "General-purpose LLMs (e.g., ChatGPT, Claude, Gemini)": "General-purpose LLMs (ChatGPT, Claude, Gemini)",
        "Coding Assistants (e.g., GitHub Copilot, Cursor)": "Coding Assistants (Copilot, Cursor)",
        "Academic search engines (e.g., Elicit, Semantic Scholar)": "Academic search (Elicit, Semantic Scholar)",
        "AI-powered reading tools (e.g., ChatPDF, Humata)": "AI reading tools (ChatPDF, Humata)",
        "Often (20-50%)": "Often (20--50%)",
        "Often (20-50%)": "Often (20--50%)",
        "Very Often (>50% of the time)": "Very Often (>50%)",
        "Very Often (>50%)": "Very Often (>50%)",
        "Don't use LLMs": "Don't use LLMs for finding refs",
        "I do not use General LLMs for finding references": "Don't use LLMs for finding refs",
        "Always verify (100%)": "Always (e.g., Scholar/DBLP)",
        "Yes, I verify 100% of them via Google Scholar/DBLP": "Always (e.g., Scholar/DBLP)",
        "Only if reading full text": "Only if reading full text",
        "I only verify if I need to read the full text": "Only if reading full text",
        "Only if suspicious": "Only if suspicious",
        "Trust AI": "Trust AI",
        "No, I trust my own writing more": "No, trust my own writing more",
        "Yes, but only for final proofreading": "Yes, only for final proofreading",
        "Yes, for almost every sentence": "Yes, for almost every sentence",
        "Yes, for specific difficult paragraphs": "Yes, for specific difficult paragraphs",
        "Google Scholar \"Cite\" button": "Google Scholar \"Cite\" button",
        "Direct export from publisher (IEEE/ACM)": "Direct export from publisher (IEEE/ACM)",
        "I assume the paper exists and try to find it manually": "Assume exists, find manually",
        "Copy from other papers": "Copy from other papers",
        "Other": "Other",
        "AI-generated": "AI-generated",
        "Every single time": "Every single time",
        "Most of the time": "Most of the time",
        "Only for critical claims": "Only for critical claims",
        "Rarely": "Rarely",
        "No, never": "No, never",
        "Yes, if necessary": "Yes, if necessary",
        "Yes, often": "Yes, often",
        "Somewhat agree": "Somewhat agree",
        "Neutral": "Neutral",
        "Somewhat disagree": "Somewhat disagree",
        "Strongly disagree": "Strongly disagree",
        "Strongly agree": "Strongly agree",
        "I ask the AI to provide a different link": "Ask AI for different link",
        "Ask AI for another link": "Ask AI for different link",
        "Try to find manually": "Assume exists, find manually",
        "Assume hallucination, discard": "Assume hallucination, discard",
        "Keep citation, remove DOI": "Keep citation but remove DOI",
        "Critical crisis": "Critical crisis",
        "Major problem": "Major problem",
        "Minor nuisance": "Minor nuisance",
        "Not a problem": "Not a problem",
        "Authors": "Authors",
        "Reviewers": "Reviewers",
        "Publishers (Editorial check)": "Publishers (Editorial)",
        "AI tool developers": "AI tool developers",
        "Yes, absolutely": "Yes, absolutely",
        "Maybe": "Maybe",
        "No": "No",
        "Yes, skimming": "Yes, skimming",
        "Yes, carefully": "Yes, carefully",
        "Missing key related work": "Missing key related work",
        "Correctness of metadata (Year, Venue)": "Correctness of metadata (Year, Venue)",
        "Existence of the papers": "Existence of the papers",
        "Self-citation abuse": "Self-citation abuse",
        "Occasionally": "Occasionally",
        "Frequently": "Frequently",
        "Yes": "Yes",
        "No": "No",
        "Mention it in minor comments": "Mention in minor comments",
        "Ask for major revision": "Ask for major revision",
        "Reject the paper": "Reject the paper",
        "Ignore": "Ignore",
        "Reject immediately (Ethical concern)": "Reject immediately (Ethical concern)",
        "Ask for explanation": "Ask for explanation",
        "Consider innocent mistake": "Consider innocent mistake",
        "Yes, I would verify it privately but take no action": "Verify privately, take no action",
        "Yes, I would contact the PC Chairs or Journal Editors": "Contact PC Chairs / Journal Editors",
        "Yes, I would contact the authors directly": "Contact authors directly",
        "No, I would ignore it": "Ignore",
    }

    if option in synonyms:
        return synonyms[option]
    return option


def count_question(df, col_base, options, base_n, cn_to_en, translate_cn_to_en, multi=False):
    # Find all columns that match this base after normalization
    matching_cols = [c for c in df.columns if normalize_col(c) == col_base]
    counts = Counter()

    for col in matching_cols:
        for val in df[col].dropna():
            items = split_multi(val) if multi else [val]
            for item in items:
                canon = canonicalize_option(item, cn_to_en, translate_cn_to_en)
                if canon in options:
                    counts[canon] += 1

    # Ensure all options exist
    for opt in options:
        counts.setdefault(opt, 0)

    # Percentages
    perc = {opt: (counts[opt] / base_n * 100.0) if base_n else 0.0 for opt in options}
    return counts, perc


def main():
    cn_path = "Chinese.csv"
    en_path = "English.csv"
    mapping_path = "mapping.json"

    cn_to_en, translate_cn_to_en = load_cn_to_en()

    df_cn = pd.read_csv(cn_path)
    df_en = pd.read_csv(en_path)

    mapping = load_mapping(mapping_path)
    df_cn = df_cn.rename(columns=mapping)

    # Filter invalid Chinese rows
    if "Index" in df_cn.columns:
        df_cn = df_cn[~df_cn["Index"].isin([28, 41, 78])]

    # Normalize columns
    df_cn.columns = [normalize_col(c) for c in df_cn.columns]
    df_en.columns = [normalize_col(c) for c in df_en.columns]

    consent_col = "By clicking \"Yes\" below, you confirm that:\n1.You understand that your participation is voluntary.\n2.You understand that you may stop the survey and quit at any time without giving a reason.\n3.You consent to the anonymous use of your responses for research purposes."

    df_cn = df_cn[df_cn[consent_col].apply(is_consented)]
    df_en = df_en[df_en[consent_col].apply(is_consented)]

    df_all = pd.concat([df_cn, df_en], ignore_index=True)

    total_n = len(df_all)
    chinese_n = len(df_cn)

    # AI users base
    ai_col = "Do you use AI-powered tools for research?"
    ai_yes = (df_all[ai_col] == "Yes") | (df_all[ai_col] == "是")
    ai_n = int(ai_yes.sum())

    print(f"Total N: {total_n}")
    print(f"Chinese N: {chinese_n}")
    print(f"AI users N: {ai_n}")

    # Table A config
    table_a = [
        ("Do you use AI-powered tools for research?", ["Yes", "No"], total_n, False),
        ("Specifically regarding CITATIONS, how do you use AI tools? (Select all that apply)",
         [
            "None (do not use AI for citations)",
            "Discovery (recommend papers on topic)",
            "Formatting (convert to BibTeX, etc.)",
            "Summarization (decide whether to cite)",
            "Gap-filling (citation for a sentence)",
            "Verification (ask if paper exists)",
         ], total_n, True),
        ("Which types of AI-powered tools do you use for research? (Select all that apply)",
         [
            "General-purpose LLMs (ChatGPT, Claude, Gemini)",
            "Coding Assistants (Copilot, Cursor)",
            "Academic search (Elicit, Semantic Scholar)",
            "AI reading tools (ChatPDF, Humata)",
         ], ai_n, True),
        ("Do you use AI tools specifically for text polishing, grammar checking, or rephrasing?",
         [
            "Yes, for specific difficult paragraphs",
            "Yes, for almost every sentence",
            "Yes, only for final proofreading",
            "No, trust my own writing more",
         ], ai_n, False),
        ("When asking a General LLM (e.g., ChatGPT) to find references, how often do you encounter \"hallucinations\" (non-existent papers)?",
         [
            "Often (20--50%)",
            "Don't use LLMs for finding refs",
            "Occasionally (<20%)",
            "Very Often (>50%)",
            "Never",
         ], total_n, False),
        ("If an AI tool provides a perfect-looking reference (Title, Author, Year, Venue all look correct), do you still verify it externally?",
         [
            "Always (e.g., Scholar/DBLP)",
            "Only if reading full text",
            "Don't use LLMs for finding refs",
            "Only if suspicious",
            "Trust AI",
         ], total_n, False),
        ("Have you ever cited a paper suggested by AI without reading the full text of that paper?",
         [
            "No, never",
            "Yes, once or twice",
            "Yes, often",
         ], total_n, False),
        ("When adding a citation to your paper, what is your primary source of metadata (title, year, venue)?",
         [
            "Google Scholar \"Cite\" button",
            "Direct export from publisher (IEEE/ACM)",
            "Assume exists, find manually",
            "Copy from other papers",
            "Other",
            "AI-generated",
         ], total_n, False),
        ("How often do you verify that a cited paper actually contains the claim you are attributing to it?",
         [
            "Every single time",
            "Most of the time",
            "Only for critical claims",
            "Rarely",
         ], total_n, False),
        ("If you cannot find the full text of a paper (e.g., paywalled or offline), do you still cite it based on its abstract or title?",
         [
            "No, never",
            "Yes, if necessary",
            "Yes, often",
         ], chinese_n, False),
        ("To what extent do you agree: \"There is pressure to include a high number of references to make the paper look more scholarly.\"",
         [
            "Somewhat agree",
            "Neutral",
            "Somewhat disagree",
            "Strongly disagree",
            "Strongly agree",
         ], total_n, False),
        ("To what extent do you agree: \"AI tools have made it easier to generate 'Related Work' sections, but harder to ensure citation accuracy.\"",
         [
            "Somewhat agree",
            "Strongly agree",
            "Neutral",
            "Somewhat disagree",
            "Strongly disagree",
         ], total_n, False),
        ("What is your strategy when an AI tool generates a citation with a broken link or DOI?",
         [
            "Assume exists, find manually",
            "Assume hallucination, discard",
            "Ask AI for different link",
            "Keep citation but remove DOI",
         ], total_n, False),
        ("How serious of an issue do you consider \"hallucinated citations\" (non-existent papers) in the era of AI?",
         [
            "Critical crisis",
            "Major problem",
            "Minor nuisance",
            "Not a problem",
         ], total_n, False),
        ("Who is primarily responsible for verifying the authenticity of cited references?",
         [
            "Authors",
            "Reviewers",
            "Publishers (Editorial)",
            "AI tool developers",
         ], total_n, False),
        ("Should conferences deploy automated tools to check for broken DOIs or fake references upon submission?",
         [
            "Yes, absolutely",
            "Maybe",
            "No",
         ], total_n, False),
    ]

    table_b = [
        ("To what extent do you agree: \"It is acceptable to cite a paper based on AI summarization without reading the original text.\"",
         [
            "Somewhat disagree",
            "Strongly disagree",
            "Neutral",
            "Somewhat agree",
            "Strongly agree",
         ], total_n, False),
        ("When reviewing a paper, do you explicitly check the Reference section?",
         [
            "Yes, skimming",
            "Yes, carefully",
            "No",
         ], total_n, False),
        ("What are you looking for when checking references? (Select all that apply)",
         [
            "Missing key related work",
            "Correctness of metadata (Year, Venue)",
            "Existence of the papers",
            "Self-citation abuse",
         ], total_n, True),
        ("Have you ever clicked on a DOI link in a submission's bibliography to verify the paper exists?",
         [
            "Occasionally",
            "Rarely",
            "Never",
            "Frequently",
         ], total_n, False),
        ("Have you ever suspected a submission contained fake or hallucinated references?",
         [
            "No",
            "Yes",
         ], total_n, False),
        ("What is your reaction if you find one incorrect citation (e.g., wrong year) in a paper you are reviewing?",
         [
            "Mention in minor comments",
            "Ask for major revision",
            "Reject the paper",
            "Ignore",
         ], total_n, False),
        ("What is your reaction if you find multiple (e.g., >5) incorrect or fake citations?",
         [
            "Reject immediately (Ethical concern)",
            "Ask for explanation",
            "Mention in minor comments",
            "Ask for major revision",
            "Reject the paper",
            "Consider innocent mistake",
         ], total_n, False),
        ("If you encounter a suspicious or clearly fake reference in a published paper, do you report it?",
         [
            "Verify privately, take no action",
            "Contact PC Chairs / Journal Editors",
            "Contact authors directly",
            "Ignore",
         ], total_n, True),
        ("Have you ever copy-pasted a BibTeX entry from the internet without checking its content?",
         [
            "No, never",
            "Yes, rarely",
            "Yes, often",
         ], total_n, False),
        ("Have you ever seen a reference list where the author names were clearly scrambled or incorrect (e.g., order reversed)?",
         [
            "No",
            "Yes",
         ], total_n, False),
        ("Have you ever seen a reference where the title existed but the venue/year was completely wrong?",
         [
            "No",
            "Yes",
         ], total_n, False),
        ("Do you think it is acceptable to cite a \"Technical Report\" if a peer-reviewed version exists?",
         [
            "Yes",
            "No",
         ], total_n, False),
        ("To what extent do you agree: \"I meticulously verify every single field (volume, issue, page numbers) of every BibTeX entry I import, ensuring 100% accuracy before submission.\"",
         [
            "Strongly agree",
            "Somewhat agree",
            "Neutral",
            "Somewhat disagree",
            "Strongly disagree",
         ], total_n, False),
        ("Do you use tools like \"Semantic Scholar\" or \"ResearchRabbit\" to build your bibliography?",
         [
            "No",
            "Yes",
         ], total_n, False),
        ("To what extent do you agree: \"The accuracy of the bibliography is as important as the accuracy of the experimental results.\"",
         [
            "Strongly agree",
            "Somewhat agree",
            "Neutral",
            "Somewhat disagree",
         ], chinese_n, False),
        ("Do you believe the current peer review process is effective at catching metadata errors in references?",
         [
            "Not very effective",
            "Somewhat effective",
            "Ineffective",
            "Very effective",
         ], chinese_n, False),
    ]

    def dump_table(table, name):
        print("\n" + name)
        for col_base, options, base_n, multi in table:
            counts, perc = count_question(
                df_all, col_base, options, base_n, cn_to_en, translate_cn_to_en, multi
            )
            print(f"\n[{col_base}] (base={base_n})")
            for opt in options:
                print(f"  {opt}: {counts[opt]} ({perc[opt]:.1f}%)")

    dump_table(table_a, "TABLE A")
    dump_table(table_b, "TABLE B")


if __name__ == "__main__":
    main()
