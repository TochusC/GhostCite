import pandas as pd
from pathlib import Path

INPUT_PATH = Path(r"d:\Project\GhostCite\Experiment\4_llm_generated_citations\llm_new_res_v3.csv")
OUTPUT_DIR = INPUT_PATH.parent
SAMPLE_SIZE = 400
RANDOM_SEED = 42


def main() -> None:
    if not INPUT_PATH.exists():
        raise SystemExit(f"Input file not found: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)

    required_cols = {"similarity_correct", "dblp_title_similarity"}
    missing = required_cols - set(df.columns)
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")

    sim_max = df[["similarity_correct", "dblp_title_similarity"]].max(axis=1)
    is_valid = sim_max >= 0.9

    valid_df = df[is_valid].copy()
    invalid_df = df[~is_valid].copy()

    if len(valid_df) < SAMPLE_SIZE or len(invalid_df) < SAMPLE_SIZE:
        raise SystemExit(
            f"Not enough samples. Valid={len(valid_df)}, Invalid={len(invalid_df)}"
        )

    valid_sample = valid_df.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED)
    invalid_sample = invalid_df.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED)

    valid_path = OUTPUT_DIR / "sample_valid_400.csv"
    invalid_path = OUTPUT_DIR / "sample_invalid_400.csv"
    combined_path = OUTPUT_DIR / "sample_validation_800.csv"

    valid_sample.to_csv(valid_path, index=False)
    invalid_sample.to_csv(invalid_path, index=False)

    combined = pd.concat(
        [
            valid_sample.assign(sample_label="valid"),
            invalid_sample.assign(sample_label="invalid"),
        ],
        ignore_index=True,
    )
    combined.to_csv(combined_path, index=False)

    print(f"Valid sample: {valid_path} ({len(valid_sample)})")
    print(f"Invalid sample: {invalid_path} ({len(invalid_sample)})")
    print(f"Combined sample: {combined_path} ({len(combined)})")


if __name__ == "__main__":
    main()
