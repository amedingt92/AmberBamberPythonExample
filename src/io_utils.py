"""io_utils.py - simple IO helpers."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

def load_healthcare_csv(path: str | Path) -> pd.DataFrame:
    """Load the healthcare CSV into a DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path.resolve()}")
    return pd.read_csv(path)
