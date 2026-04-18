import streamlit as st

from data_loader import load_data
from filters import render_sidebar_filters, apply_filters

st.set_page_config(page_title="Raw Data", layout="wide")

st.title("Raw Data")

df = load_data()
filters = render_sidebar_filters(df)
filtered_df = apply_filters(df, filters)

st.dataframe(filtered_df, use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_diabetes_data.csv",
    mime="text/csv"
)
