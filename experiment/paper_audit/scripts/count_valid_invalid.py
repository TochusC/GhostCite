#!/usr/bin/env python3
"""统计各会议 recheck CSV 中 valid 和 invalid 的数量。"""

import csv
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
FILES = [
    "aaai_recheck_valid_sort_token_cache.csv",
    "ccs_recheck_valid_sort_token_cache.csv",
    "ndss_recheck_valid_sort_token_cache.csv",
    "sp_recheck_valid_sort_token_cache.csv",
    "usenix_recheck_valid_sort_token_cache.csv",
]


def count_status(csv_path: Path) -> tuple[int, int]:
    """统计 CSV 中 new_status 列为 valid 和 invalid 的数量。"""
    valid_count = 0
    invalid_count = 0
    with open(csv_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if "new_status" not in reader.fieldnames:
            # 若无 new_status，则用 final_status
            status_col = "final_status"
        else:
            status_col = "new_status"
        for row in reader:
            s = (row.get(status_col) or "").strip().lower()
            if s == "valid":
                valid_count += 1
            elif s == "invalid":
                invalid_count += 1
    return valid_count, invalid_count


def main():
    print("File\tValid\tInvalid\tTotal")
    print("-" * 60)
    total_valid = 0
    total_invalid = 0
    for name in FILES:
        path = RESULTS_DIR / name
        if not path.exists():
            print(f"{name}\t(文件不存在)")
            continue
        v, i = count_status(path)
        total_valid += v
        total_invalid += i
        print(f"{name}\t{v}\t{i}\t{v + i}")
    print("-" * 60)
    print(f"Total\t{total_valid}\t{total_invalid}\t{total_valid + total_invalid}")


if __name__ == "__main__":
    main()
