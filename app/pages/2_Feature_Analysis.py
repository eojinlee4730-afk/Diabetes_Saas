import streamlit as st

from data_loader import load_data
from filters import render_sidebar_filters, apply_filters
from charts import create_correlation_heatmap

st.set_page_config(page_title="Feature Analysis", layout="wide")

st.title("Feature Analysis")

df = load_data()
filters = render_sidebar_filters(df)
filtered_df = apply_filters(df, filters)

st.subheader("Summary Statistics")
st.dataframe(filtered_df.describe(), use_container_width=True)

fig = create_correlation_heatmap(filtered_df)
st.plotly_chart(fig, use_container_width=True)
