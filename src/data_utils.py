# src/data_utils.py

import pandas as pd
import os
import re

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data from a given file path.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)





import re

def clean_column_names(df):
    df.columns = [
        re.sub(r'[ /]', '_', re.sub(r'[^\w\s/]', '', col.strip().lower()))
        for col in df.columns
    ]
    return df
