import streamlit as st
import plotly.express as px
from data_loader import load_data
from filters import render_sidebar_filters, apply_filters

st.set_page_config(page_title="Region Analysis", layout="wide")

st.title("Region Analysis")

df = load_data()
filters = render_sidebar_filters(df)
filtered_df = apply_filters(df, filters)

if "region" in filtered_df.columns and "sales" in filtered_df.columns:

    region_df = (
        filtered_df
        .groupby("region", as_index=False)["sales"]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )

    region_df.columns = ["region", "total_sales", "avg_sales", "count"]

    st.dataframe(region_df, use_container_width=True)

    fig = px.bar(
        region_df,
        x="region",
        y="total_sales",
        title="Total Sales by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Required columns are missing: region, sales")
