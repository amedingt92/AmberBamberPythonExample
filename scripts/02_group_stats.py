"""02_group_stats.py
Run: python scripts/02_group_stats.py
"""
from pathlib import Path
from src.io_utils import load_healthcare_csv
from src.df_basics import simple_group_stats

DATA_PATH = Path("data") / "healthcare_data.csv"

# Change these to whatever columns exist in your dataset:
GROUP_COL_CANDIDATES = ["department", "diagnosis", "treatment", "gender"]
VALUE_COL_CANDIDATES = ["bill_amount", "charges", "cost", "amount"]

df = load_healthcare_csv(DATA_PATH)

# Pick the first candidate columns that exist
group_col = next((c for c in GROUP_COL_CANDIDATES if c in df.columns), None)
value_col = next((c for c in VALUE_COL_CANDIDATES if c in df.columns), None)

if group_col is None or value_col is None:
    print("Could not auto-detect group/value columns.")
    print("Available columns:", list(df.columns))
    print("Edit GROUP_COL_CANDIDATES and VALUE_COL_CANDIDATES in this script.")
    raise SystemExit(1)

out = simple_group_stats(df, group_col=group_col, value_col=value_col)
print(f"\nGrouped stats for {value_col} by {group_col} (top 15):\n")
print(out.head(15))
