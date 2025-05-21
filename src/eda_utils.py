import pandas as pd

def count_missing_values(df):
    """Return total number of missing values in a DataFrame."""
    return df.isnull().sum().sum()
