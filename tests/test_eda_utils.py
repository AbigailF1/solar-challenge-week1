import pandas as pd
from src.eda_utils import count_missing_values

def test_count_missing_values():
    # Create a small test DataFrame
    df = pd.DataFrame({
        'a': [1, None, 3],
        'b': [4, 5, None]
    })
    assert count_missing_values(df) == 2
