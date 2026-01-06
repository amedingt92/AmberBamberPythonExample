"""03_make_plots.py
Run: python scripts/03_make_plots.py

Creates plots in outputs/figures/
"""
from pathlib import Path
from src.io_utils import load_healthcare_csv
from src.plotting import plot_numeric_histogram, plot_category_bar

DATA_PATH = Path("data") / "healthcare_data.csv"
OUT_DIR = Path("outputs") / "figures"

df = load_healthcare_csv(DATA_PATH)

# Choose columns to plot (auto-detect common ones)
numeric_candidates = ["bill_amount", "charges", "cost", "amount", "age"]
cat_candidates = ["department", "diagnosis", "treatment", "gender", "status"]

num_col = next((c for c in numeric_candidates if c in df.columns), None)
cat_col = next((c for c in cat_candidates if c in df.columns), None)

if num_col is None and cat_col is None:
    print("Could not auto-detect columns to plot.")
    print("Available columns:", list(df.columns))
    print("Edit numeric_candidates and cat_candidates in this script.")
    raise SystemExit(1)

if num_col is not None:
    out1 = plot_numeric_histogram(df, num_col, OUT_DIR / f"hist_{num_col}.png")
    print("Saved:", out1)

if cat_col is not None:
    out2 = plot_category_bar(df, cat_col, OUT_DIR / f"bar_{cat_col}.png", top_n=15)
    print("Saved:", out2)
