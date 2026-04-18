import streamlit as st
from modules.data_loader import load_data
from modules.filters import render_sidebar_filters, apply_filters
from modules.charts import sales_by_region_chart, sales_by_category_chart, trend_chart

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard")

df = load_data()
filters = render_sidebar_filters(df)
filtered_df = apply_filters(df, filters)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(filtered_df))

with col2:
    if "sales" in filtered_df.columns:
        st.metric("Total Sales", f"{filtered_df['sales'].sum():,.0f}")
    else:
        st.metric("Total Sales", "N/A")

with col3:
    if "region" in filtered_df.columns:
        st.metric("Regions", filtered_df["region"].nunique())
    else:
        st.metric("Regions", "N/A")

fig1 = sales_by_region_chart(filtered_df)
fig2 = sales_by_category_chart(filtered_df)
fig3 = trend_chart(filtered_df)

if fig1:
    st.plotly_chart(fig1, use_container_width=True)

col4, col5 = st.columns(2)

with col4:
    if fig2:
        st.plotly_chart(fig2, use_container_width=True)

with col5:
    if fig3:
        st.plotly_chart(fig3, use_container_width=True)
