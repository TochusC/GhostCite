#!/usr/bin/env python3
"""从各会议 recheck CSV 中提取 new_status 为 invalid 的行，合并到一个新 CSV。"""

import csv
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
OUTPUT_PATH = Path(__file__).resolve().parent / "all_invalid.csv"
FILES = [
    "aaai_recheck_valid_sort_token_cache.csv",
    "ccs_recheck_valid_sort_token_cache.csv",
    "ndss_recheck_valid_sort_token_cache.csv",
    "sp_recheck_valid_sort_token_cache.csv",
    "usenix_recheck_valid_sort_token_cache.csv",
]


def extract_invalid():
    fieldnames = None
    invalid_rows = []

    for name in FILES:
        path = RESULTS_DIR / name
        if not path.exists():
            print(f"跳过（不存在）: {name}")
            continue
        with open(path, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if fieldnames is None:
                # 使用第一个文件的表头，并加上 source_file
                fieldnames = list(reader.fieldnames) + ["source_file"]
            for row in reader:
                if (row.get("new_status") or "").strip().lower() != "invalid":
                    continue
                row["source_file"] = name
                invalid_rows.append(row)

    if not invalid_rows:
        print("没有找到 new_status=invalid 的行。")
        return

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(invalid_rows)

    print(f"已提取 {len(invalid_rows)} 条 invalid 记录 -> {OUTPUT_PATH}")


if __name__ == "__main__":
    extract_invalid()
