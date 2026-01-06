"""01_read_and_peek.py
Run: python scripts/01_read_and_peek.py
"""
from pathlib import Path
from src.io_utils import load_healthcare_csv
from src.df_basics import basic_overview

DATA_PATH = Path("data") / "healthcare_data.csv"

df = load_healthcare_csv(DATA_PATH)
basic_overview(df)
