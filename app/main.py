import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils import load_cleaned_data, get_summary_statistics

st.title(" Solar Potential Dashboard - West Africa")

country = st.selectbox("Select a country:", ["Benin", "Togo", "Sierra Leone"])
metric = st.radio("Select metric:", ["GHI", "DNI", "DHI"])

df = load_cleaned_data(country)

st.subheader(f"{country} - {metric} Distribution")

fig, ax = plt.subplots()
sns.boxplot(y=df[metric], ax=ax)
st.pyplot(fig)

st.subheader(f"Summary Statistics for {metric}")
stats = get_summary_statistics(df, metric)
st.json(stats)