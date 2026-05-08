#!/usr/bin/env python3
"""从各会议 recheck CSV 中提取 problem_valid_invalid 为 True 的行，合并到一个新 CSV。"""

import csv
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
OUTPUT_PATH = Path(__file__).resolve().parent / "problem_valid_invalid_true.csv"
FILES = [
    "aaai_recheck_valid_sort_token_cache.csv",
    "ccs_recheck_valid_sort_token_cache.csv",
    "ndss_recheck_valid_sort_token_cache.csv",
    "sp_recheck_valid_sort_token_cache.csv",
    "usenix_recheck_valid_sort_token_cache.csv",
]


def extract_problem_true():
    fieldnames = None
    rows = []

    for name in FILES:
        path = RESULTS_DIR / name
        if not path.exists():
            print(f"跳过（不存在）: {name}")
            continue
        with open(path, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if fieldnames is None:
                fieldnames = list(reader.fieldnames) + ["source_file"]
            for row in reader:
                val = (row.get("problem_valid_invalid") or "").strip().lower()
                if val not in ("true", "1", "yes"):
                    continue
                row["source_file"] = name
                rows.append(row)

    if not rows:
        print("没有找到 problem_valid_invalid=True 的行。")
        return

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"已提取 {len(rows)} 条 problem_valid_invalid=True 记录 -> {OUTPUT_PATH}")


if __name__ == "__main__":
    extract_problem_true()
