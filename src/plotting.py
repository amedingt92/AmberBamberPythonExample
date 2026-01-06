"""plotting.py - beginner-friendly plotting helpers."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def plot_numeric_histogram(df: pd.DataFrame, col: str, out_file: str | Path) -> Path:
    """Save a histogram of a numeric column."""
    out_file = Path(out_file)
    ensure_dir(out_file.parent)

    series = pd.to_numeric(df[col], errors='coerce').dropna()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(series.values, bins=30)
    ax.set_title(f"Histogram: {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")

    fig.savefig(out_file, bbox_inches="tight", dpi=150)
    plt.close(fig)
    return out_file

def plot_category_bar(df: pd.DataFrame, col: str, out_file: str | Path, top_n: int = 15) -> Path:
    """Save a bar chart of the top N value counts of a categorical column."""
    out_file = Path(out_file)
    ensure_dir(out_file.parent)

    counts = df[col].astype(str).value_counts(dropna=False).head(top_n)

    fig = plt.figure(figsize=(9, 5))
    ax = fig.add_subplot(111)
    ax.barh(counts.index[::-1], counts.values[::-1])
    ax.set_title(f"Top {top_n} categories: {col}")
    ax.set_xlabel("Count")
    ax.set_ylabel(col)

    fig.savefig(out_file, bbox_inches="tight", dpi=150)
    plt.close(fig)
    return out_file
