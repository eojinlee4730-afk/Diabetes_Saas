import streamlit as st
from data_loader import load_data
from filters import render_sidebar_filters, apply_filters
from charts import (
    create_sales_by_region_chart,
    create_category_distribution_chart,
    create_trend_chart
)

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard")

# Load data
df = load_data()

# Render filters
filters = render_sidebar_filters(df)

# Apply filters
filtered_df = apply_filters(df, filters)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(filtered_df))

if "sales" in filtered_df.columns:
    col2.metric("Total Sales", f"{filtered_df['sales'].sum():,.0f}")
else:
    col2.metric("Total Sales", "N/A")

if "region" in filtered_df.columns:
    col3.metric("Regions", filtered_df["region"].nunique())
else:
    col3.metric("Regions", "N/A")

# Charts
fig1 = create_sales_by_region_chart(filtered_df)
fig2 = create_category_distribution_chart(filtered_df)
fig3 = create_trend_chart(filtered_df)

if fig1:
    st.plotly_chart(fig1, use_container_width=True)

col4, col5 = st.columns(2)

if fig2:
    col4.plotly_chart(fig2, use_container_width=True)

if fig3:
    col5.plotly_chart(fig3, use_container_width=True)
