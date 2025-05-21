import pandas as pd

def load_cleaned_data(country):
    file_path = f"data/{country.lower().replace(' ', '')}_clean.csv"
    df = pd.read_csv(file_path)
    return df

def get_summary_statistics(df, column):
    return {
    "mean": round(df[column].mean(), 2),
    "median": round(df[column].median(), 2),
    "std": round(df[column].std(), 2)
    }