import argparse
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path
from typing import Dict, Optional, Tuple

import pandas as pd
from rapidfuzz import fuzz, process


def normalize_title(text: str) -> str:
    text = str(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_all_entries(conn: sqlite3.Connection) -> Tuple[list[str], list[Tuple[str, str, str, str, str, str]]]:
    cur = conn.cursor()
    cur.execute("SELECT title_norm, dblp_key, type, title, year, venue, authors FROM entries")
    rows = cur.fetchall()
    norms = [r[0] for r in rows]
    entries = [(r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]
    return norms, entries


def find_best_match(
    title_norm: str,
    all_norms: list[str],
    all_entries: list[Tuple[str, str, str, str, str, str]],
    candidate_limit: int,
) -> Optional[Tuple[str, str, str, str, str, str, float]]:
    # First pass: quick candidate selection
    candidates = process.extract(
        title_norm,
        all_norms,
        scorer=fuzz.partial_ratio,
        limit=candidate_limit,
    )
    if not candidates:
        return None

    best_score = -1.0
    best_idx = -1
    for _, _, idx in candidates:
        score = fuzz.ratio(title_norm, all_norms[idx])
        if score > best_score:
            best_score = score
            best_idx = idx

    if best_idx < 0:
        return None
    entry = all_entries[best_idx]
    return (*entry, best_score / 100.0)


def _read_csv_with_fallback(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="utf-8", encoding_errors="ignore")


def run_search(
    input_csv: Path,
    output_csv: Path,
    db_path: Path,
    sim_threshold: float = 0.9,
    sim_column: str = "similarity_correct",
    title_column: str = "original_title",
    checkpoint_interval: int = 0,
    resume: bool = False,
    candidate_limit: int = 10,
) -> None:
    if not input_csv.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_csv}")
    if not db_path.exists():
        raise FileNotFoundError(f"DB not found: {db_path}")

    checkpoint_path = output_csv.parent / (output_csv.stem + "_checkpoint.csv")

    if resume and checkpoint_path.exists():
        print(f"[db_searcher] resume from: {checkpoint_path}")
        df = _read_csv_with_fallback(checkpoint_path)
    else:
        df = _read_csv_with_fallback(input_csv)
    if sim_column not in df.columns:
        raise ValueError(f"Missing column: {sim_column}")
    if title_column not in df.columns:
        raise ValueError(f"Missing column: {title_column}")

    for col in (
        "dblp_key",
        "dblp_type",
        "dblp_title",
        "dblp_year",
        "dblp_venue",
        "dblp_authors",
        "dblp_title_similarity",
    ):
        if col not in df.columns:
            df[col] = None

    mask = pd.to_numeric(df[sim_column], errors="coerce") < sim_threshold
    target_indices = df.index[mask].tolist()
    print(f"[db_searcher] total rows: {len(df)}")
    print(f"[db_searcher] to verify ({sim_column} < {sim_threshold}): {len(target_indices)}")

    conn = sqlite3.connect(str(db_path))
    print("[db_searcher] loading DB entries for fuzzy matching...")
    all_norms, all_entries = load_all_entries(conn)
    conn.close()
    print(f"[db_searcher] loaded {len(all_norms):,} titles")
    cache: Dict[str, Optional[Tuple[str, str, str, str, str, str, float]]] = {}

    total_targets = len(target_indices)
    processed = 0
    last_checkpoint = 0

    for idx in target_indices:
        title = df.loc[idx, title_column]
        title_norm = normalize_title(title)
        if not title_norm:
            continue

        if title_norm not in cache:
            cache[title_norm] = find_best_match(
                title_norm,
                all_norms,
                all_entries,
                candidate_limit,
            )

        row = cache[title_norm]
        if row:
            dblp_key, dblp_type, dblp_title, year, venue, authors, score = row
            df.loc[idx, "dblp_key"] = dblp_key
            df.loc[idx, "dblp_type"] = dblp_type
            df.loc[idx, "dblp_title"] = dblp_title
            df.loc[idx, "dblp_year"] = year
            df.loc[idx, "dblp_venue"] = venue
            df.loc[idx, "dblp_authors"] = authors
            df.loc[idx, "dblp_title_similarity"] = score
        else:
            df.loc[idx, "dblp_title_similarity"] = 0.0

        processed += 1
        if checkpoint_interval > 0 and processed - last_checkpoint >= checkpoint_interval:
            output_csv.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(checkpoint_path, index=False)
            last_checkpoint = processed
            print(f"[db_searcher] progress {processed}/{total_targets} (checkpoint saved)")
        elif processed % 1000 == 0:
            print(f"[db_searcher] progress {processed}/{total_targets}")

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    if checkpoint_path.exists():
        checkpoint_path.unlink()
    print(f"[db_searcher] saved: {output_csv}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Re-validate low-similarity rows with DBLP DB.")
    parser.add_argument(
        "--input-csv",
        type=Path,
        default=Path("Experiment/4_llm_generated_citations/dblp/llm_new_res_v2.csv"),
        help="Input CSV (default: llm_new_res_v2.csv)",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=Path("Experiment/4_llm_generated_citations/dblp/llm_new_res_v3.csv"),
        help="Output CSV (default: llm_new_res_v3.csv)",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=Path("Experiment/4_llm_generated_citations/dblp/dblp_titles.sqlite"),
        help="SQLite DB created by db_builder.py",
    )
    parser.add_argument(
        "--sim-threshold",
        type=float,
        default=0.9,
        help="Only re-validate rows with similarity_correct below this threshold",
    )
    parser.add_argument(
        "--checkpoint-interval",
        type=int,
        default=5000,
        help="Save checkpoint every N verified rows (0 = disabled)",
    )
    parser.add_argument(
        "--candidate-limit",
        type=int,
        default=10,
        help="Number of candidates to score with ratio (default: 10)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last checkpoint if it exists",
    )
    parser.add_argument(
        "--sim-column",
        type=str,
        default="similarity_correct",
        help="Similarity column name (default: similarity_correct)",
    )
    parser.add_argument(
        "--title-column",
        type=str,
        default="original_title",
        help="Title column name (default: original_title)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        run_search(
            input_csv=args.input_csv,
            output_csv=args.output_csv,
            db_path=args.db,
            sim_threshold=args.sim_threshold,
            sim_column=args.sim_column,
            title_column=args.title_column,
            checkpoint_interval=args.checkpoint_interval,
            resume=args.resume,
            candidate_limit=args.candidate_limit,
        )
    except Exception as exc:
        print(f"[db_searcher] error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
