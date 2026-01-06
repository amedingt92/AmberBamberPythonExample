"""df_basics.py - beginner-friendly dataframe operations."""
from __future__ import annotations
import pandas as pd

def basic_overview(
    df: pd.DataFrame,
    show_duplicate_rows: int = 5,
    show_missing_rows: int = 5,
) -> None:
    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== COLUMNS ===")
    print(list(df.columns))

    print("\n=== DTYPES ===")
    print(df.dtypes)

    print("\n=== HEAD (first 5 rows) ===")
    print(df.head())

    print("\n=== MISSING VALUES (per column) ===")
    missing_by_col = df.isna().sum().sort_values(ascending=False)
    print(missing_by_col)

    # ---- Missing row inspection ----
    print("\n=== ROWS WITH MISSING VALUES ===")
    missing_mask = df.isna().any(axis=1)
    missing_row_count = int(missing_mask.sum())
    print(f"Total rows with at least one missing value: {missing_row_count}")

    if missing_row_count > 0:
        print("\nShowing rows with missing values (NaNs highlighted):")
        missing_rows = df.loc[missing_mask].copy()

        # Show which columns are missing for each row
        missing_cols = missing_rows.isna().apply(
            lambda r: [col for col, is_na in r.items() if is_na], axis=1
        )
        missing_rows["_missing_columns"] = missing_cols

        print(missing_rows.head(show_missing_rows))
        if missing_row_count > show_missing_rows:
            print(f"... ({missing_row_count - show_missing_rows} more rows with missing values)")
    else:
        print("No missing values found.")

    # ---- Duplicate inspection ----
    print("\n=== DUPLICATE ROWS ===")
    dup_mask = df.duplicated(keep=False)
    dup_count = int(dup_mask.sum())
    print(f"Total duplicate rows: {dup_count}")

    if dup_count > 0:
        dup_rows = df.loc[dup_mask].copy()

        # Convert pandas index to CSV line numbers (header is line 1)
        dup_rows["_pandas_index"] = dup_rows.index
        dup_rows["_csv_line_number_guess"] = dup_rows.index + 2

        # Group identical rows together visually
        dup_rows = dup_rows.sort_values(by=list(df.columns))

        print("\nShowing duplicate rows (with pandas index + CSV line number):")
        print(dup_rows.head(show_duplicate_rows))
    else:
        print("No duplicate rows found.")





def simple_group_stats(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Return count + mean + median of value_col grouped by group_col."""
    if group_col not in df.columns:
        raise KeyError(f"Missing column: {group_col}")
    if value_col not in df.columns:
        raise KeyError(f"Missing column: {value_col}")

    # Try to coerce value_col to numeric (common beginner issue)
    values = pd.to_numeric(df[value_col], errors="coerce")
    out = (
        df.assign(_value=values)
        .groupby(group_col, dropna=False)['_value']
        .agg(['count', 'mean', 'median'])
        .sort_values('mean', ascending=False)
    )
    return out
