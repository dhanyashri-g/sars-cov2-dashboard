import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="SARS-CoV-2 Genomic Surveillance Dashboard")

st.title("SARS-CoV-2 Genomic Surveillance Dashboard")
st.markdown("Explore SARS-CoV-2 variant distributions, mutation loads, and trends over time.")

# Load data
data = pd.read_csv("data/sars_cov2_mock_data.csv")

# Variant distribution by lineage
st.subheader("Variant Distribution by Lineage")
fig1, ax1 = plt.subplots()
sns.countplot(data=data, x="lineage", hue="variant", ax=ax1)
st.pyplot(fig1)

# Mutation load by region
st.subheader("Mutation Load by Region")
fig2, ax2 = plt.subplots()
sns.barplot(data=data, x="region", y="mutation_count", ci=None, ax=ax2)
st.pyplot(fig2)

# Temporal trend of variants
st.subheader("Temporal Trends by Lineage")
fig3, ax3 = plt.subplots()
data['date'] = pd.to_datetime(data['date'])
sns.lineplot(data=data, x="date", y="mutation_count", hue="lineage", marker="o", ax=ax3)
st.pyplot(fig3)
