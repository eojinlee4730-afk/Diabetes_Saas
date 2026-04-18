import streamlit as st
from db import load_realtime_data
from charts import (
    show_outcome_distribution,
    show_glucose_trend,
    show_bmi_trend,
    show_age_distribution,
    show_blood_pressure_trend,
)

st.set_page_config(page_title="Diabetes Dashboard", layout="wide")
st.title("Diabetes Realtime Dashboard")

df = load_realtime_data()

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rows", len(df))
if "Glucose" in df.columns:
    col2.metric("Avg Glucose", round(df["Glucose"].mean(), 1))
if "BMI" in df.columns:
    col3.metric("Avg BMI", round(df["BMI"].mean(), 1))
if "Age" in df.columns:
    col4.metric("Avg Age", round(df["Age"].mean(), 1))

# Charts
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    show_outcome_distribution(df)
with row1_col2:
    show_glucose_trend(df)

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    show_bmi_trend(df)
with row2_col2:
    show_age_distribution(df)

show_blood_pressure_trend(df)

with st.expander("Raw Data"):
    st.dataframe(df)
