import argparse
from pathlib import Path
from typing import List, Optional

import pandas as pd


def _dedupe_columns(columns: List[str]) -> List[str]:
    seen = {}
    deduped = []
    for col in columns:
        if col in seen:
            seen[col] += 1
            deduped.append(f"{col}.{seen[col]}")
        else:
            seen[col] = 0
            deduped.append(col)
    return deduped


def _get_first_existing(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def _read_csv_with_fallback(path: Path) -> pd.DataFrame:
    for encoding in ("utf-8", "gbk", "gb18030"):
        try:
            return pd.read_csv(path, dtype=str, encoding=encoding)
        except UnicodeDecodeError:
            continue
    return pd.read_csv(path, dtype=str, encoding="utf-8", encoding_errors="replace")


def _read_invalid(path: Path) -> pd.DataFrame:
    df = _read_csv_with_fallback(path)
    df.columns = _dedupe_columns(list(df.columns))
    return df


def _read_valid(path: Path) -> pd.DataFrame:
    return _read_csv_with_fallback(path)


def _sample(df: pd.DataFrame, count: int, seed: int) -> pd.DataFrame:
    if count <= 0:
        return df.iloc[0:0].copy()
    if count > len(df):
        raise ValueError(f"Requested {count} rows but only {len(df)} available.")
    return df.sample(n=count, random_state=seed)


def _normalize_text(value: Optional[str]) -> str:
    if value is None:
        return ""
    value = str(value)
    return value.strip()


def build_benchmark(
    valid_path: Path,
    invalid_path: Path,
    valid_count: int,
    invalid_count: int,
    seed: int,
    corrected_only: bool,
    output_dir: Path,
) -> None:
    valid_df = _read_valid(valid_path)
    invalid_df = _read_invalid(invalid_path)

    # Identify invalid_summary columns (handles duplicate "Year")
    conf_year_col = _get_first_existing(invalid_df, ["Conference Year", "Year"])
    cite_year_col = _get_first_existing(invalid_df, ["Cite Year", "Year.1", "Year"])
    is_corrected_col = _get_first_existing(invalid_df, ["Is Corrected", "Is_Corrected", "IsCorrected"])

    if corrected_only and is_corrected_col:
        invalid_df = invalid_df[pd.to_numeric(invalid_df[is_corrected_col], errors="coerce") == 1]

    # Required columns
    for col in ["Cite Title", "Authors", "Venue"]:
        if col not in invalid_df.columns:
            raise ValueError(f"Missing column '{col}' in {invalid_path}.")

    if cite_year_col is None:
        raise ValueError(f"Missing citation year column in {invalid_path}.")

    # Sample
    valid_sample = _sample(valid_df, valid_count, seed)
    invalid_sample = _sample(invalid_df, invalid_count, seed)

    # Build ground truth rows
    gt_rows = []

    for _, row in valid_sample.iterrows():
        gt_rows.append(
            {
                "Cite Title": _normalize_text(row.get("original_title")) or _normalize_text(row.get("found_title")),
                "Authors": _normalize_text(row.get("original_authors")) or _normalize_text(row.get("found_authors")),
                "Year": _normalize_text(row.get("original_year")) or _normalize_text(row.get("found_year")),
                "Venue": _normalize_text(row.get("original_venue")) or _normalize_text(row.get("found_venue")),
                "Conference": _normalize_text(row.get("Conference")),
                "Conference Year": _normalize_text(row.get("Year")),
                "Filename": _normalize_text(row.get("File")),
                "Notes": "",
                "IsValid": 1,
            }
        )

    for _, row in invalid_sample.iterrows():
        gt_rows.append(
            {
                "Cite Title": _normalize_text(row.get("Cite Title")),
                "Authors": _normalize_text(row.get("Authors")),
                "Year": _normalize_text(row.get(cite_year_col)),
                "Venue": _normalize_text(row.get("Venue")),
                "Conference": _normalize_text(row.get("Conference")),
                "Conference Year": _normalize_text(row.get(conf_year_col)) if conf_year_col else "",
                "Filename": _normalize_text(row.get("Filename")),
                "Notes": _normalize_text(row.get("Notes")),
                "IsValid": 0,
            }
        )

    gt_df = pd.DataFrame(gt_rows)
    gt_df = gt_df.sample(frac=1, random_state=seed).reset_index(drop=True)

    # Build test set (IsValid blank)
    test_df = gt_df[["Cite Title", "Authors", "Year", "Venue"]].copy()
    test_df["IsValid"] = ""

    output_dir.mkdir(parents=True, exist_ok=True)
    gt_path = output_dir / "benchmark_ground_truth.csv"
    test_path = output_dir / "benchmark_test.csv"

    gt_df.to_csv(gt_path, index=False, encoding="utf-8")
    test_df.to_csv(test_path, index=False, encoding="utf-8")

    print(f"Ground truth saved to: {gt_path}")
    print(f"Test set saved to: {test_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build benchmark CSVs from valid/invalid citation sets.")
    parser.add_argument(
        "--valid-file",
        type=Path,
        default=Path(__file__).parent / "valid_sample_400.csv",
        help="Path to valid_sample_400.csv",
    )
    parser.add_argument(
        "--invalid-file",
        type=Path,
        default=Path(__file__).parent / "invalid_summary.csv",
        help="Path to invalid_summary.csv",
    )
    parser.add_argument("--valid-count", type=int, required=True, help="Number of valid samples to take")
    parser.add_argument("--invalid-count", type=int, required=True, help="Number of invalid samples to take")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument(
        "--include-uncorrected",
        action="store_true",
        help="Include invalid rows where Is Corrected != 1",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent / "benchmark",
        help="Output directory for benchmark CSVs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_benchmark(
        valid_path=args.valid_file,
        invalid_path=args.invalid_file,
        valid_count=args.valid_count,
        invalid_count=args.invalid_count,
        seed=args.seed,
        corrected_only=not args.include_uncorrected,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()
