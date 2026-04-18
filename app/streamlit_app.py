import streamlit as st

from db import run_query
from queries import REALTIME_DATA_QUERY
from filters import apply_filters
from charts import show_kpis, show_dashboard_charts


st.set_page_config(
    page_title="Diabetes Realtime Dashboard",
    layout="wide"
)

st.title("Diabetes Realtime Dashboard")

df = run_query(REALTIME_DATA_QUERY)

if df.empty:
    st.warning("No data found in realtime_data.")
    st.stop()

filtered_df = apply_filters(df)

show_kpis(filtered_df)
show_dashboard_charts(filtered_df)

with st.expander("Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
