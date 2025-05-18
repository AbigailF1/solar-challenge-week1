import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)

def clean_data(df):
    """
    Clean the data by dropping rows with missing values.
    You can modify this to do more sophisticated cleaning later.
    """
    return df.dropna()

def plot_time_series(df, date_column, value_column, title):
    """
    Plot a time series line chart.
    
    Parameters:
    - df: DataFrame containing the data
    - date_column: name of the column with dates
    - value_column: name of the column with values to plot
    - title: title for the chart
    """
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x=date_column, y=value_column)
    plt.title(title)
    plt.xlabel(date_column)
    plt.ylabel(value_column)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
