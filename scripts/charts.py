import streamlit as st
import pandas as pd


def show_kpis(df: pd.DataFrame) -> None:
    st.subheader("Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", len(df))

    if "Glucose" in df.columns and not df["Glucose"].dropna().empty:
        col2.metric("Avg Glucose", round(df["Glucose"].mean(), 1))
    else:
        col2.metric("Avg Glucose", "-")

    if "BMI" in df.columns and not df["BMI"].dropna().empty:
        col3.metric("Avg BMI", round(df["BMI"].mean(), 1))
    else:
        col3.metric("Avg BMI", "-")

    if "Age" in df.columns and not df["Age"].dropna().empty:
        col4.metric("Avg Age", round(df["Age"].mean(), 1))
    else:
        col4.metric("Avg Age", "-")


def show_outcome_distribution(df: pd.DataFrame) -> None:
    if "Outcome" in df.columns and not df["Outcome"].dropna().empty:
        st.subheader("Outcome Distribution")
        outcome_counts = df["Outcome"].value_counts().sort_index()
        st.bar_chart(outcome_counts)


def show_glucose_trend(df: pd.DataFrame) -> None:
    if "Glucose" in df.columns and not df["Glucose"].dropna().empty:
        st.subheader("Glucose Trend")
        st.line_chart(df["Glucose"].reset_index(drop=True))


def show_age_distribution(df: pd.DataFrame) -> None:
    if "Age" in df.columns and not df["Age"].dropna().empty:
        st.subheader("Age Distribution")
        age_counts = df["Age"].value_counts().sort_index()
        st.bar_chart(age_counts)


def show_bmi_trend(df: pd.DataFrame) -> None:
    if "BMI" in df.columns and not df["BMI"].dropna().empty:
        st.subheader("BMI Trend")
        st.line_chart(df["BMI"].reset_index(drop=True))


def show_blood_pressure_trend(df: pd.DataFrame) -> None:
    if "BloodPressure" in df.columns and not df["BloodPressure"].dropna().empty:
        st.subheader("Blood Pressure Trend")
        st.line_chart(df["BloodPressure"].reset_index(drop=True))


def show_insulin_trend(df: pd.DataFrame) -> None:
    if "Insulin" in df.columns and not df["Insulin"].dropna().empty:
        st.subheader("Insulin Trend")
        st.line_chart(df["Insulin"].reset_index(drop=True))


def show_dashboard_charts(df: pd.DataFrame) -> None:
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        show_outcome_distribution(df)

    with row1_col2:
        show_glucose_trend(df)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        show_age_distribution(df)

    with row2_col2:
        show_bmi_trend(df)

    show_blood_pressure_trend(df)
    show_insulin_trend(df)
