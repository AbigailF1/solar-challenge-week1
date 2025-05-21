import pandas as pd
import pytest
from src.data_utils import load_data, clean_column_names


def test_load_data():
    # Create a sample CSV file
    sample_data = """Name,Age\nAlice,30\nBob,25"""
    with open("tests/sample.csv", "w") as f:
        f.write(sample_data)

    df = load_data("tests/sample.csv")
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Name", "Age"]


def test_clean_column_names():
    df = pd.DataFrame({"  Name ": ["Alice"], "A!ge": [30], "Country/Region": ["Benin"]})
    cleaned_df = clean_column_names(df)
    expected_cols = ["name", "age", "country_region"]
    assert list(cleaned_df.columns) == expected_cols
