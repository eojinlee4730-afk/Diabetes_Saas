import streamlit as st
import pandas as pd


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")

    filtered_df = df.copy()

    # Outcome filter
    if "Outcome" in filtered_df.columns:
        outcome_values = filtered_df["Outcome"].dropna().unique().tolist()
        outcome_options = sorted(outcome_values)

        selected_outcome = st.sidebar.selectbox(
            "Outcome",
            ["All"] + outcome_options
        )

        if selected_outcome != "All":
            filtered_df = filtered_df[filtered_df["Outcome"] == selected_outcome]

    # Age filter
    if "Age" in filtered_df.columns and not filtered_df["Age"].dropna().empty:
        age_min = int(filtered_df["Age"].min())
        age_max = int(filtered_df["Age"].max())

        selected_age = st.sidebar.slider(
            "Age Range",
            min_value=age_min,
            max_value=age_max,
            value=(age_min, age_max)
        )

        filtered_df = filtered_df[
            (filtered_df["Age"] >= selected_age[0]) &
            (filtered_df["Age"] <= selected_age[1])
        ]

    # Glucose filter
    if "Glucose" in filtered_df.columns and not filtered_df["Glucose"].dropna().empty:
        glucose_min = int(filtered_df["Glucose"].min())
        glucose_max = int(filtered_df["Glucose"].max())

        selected_glucose = st.sidebar.slider(
            "Glucose Range",
            min_value=glucose_min,
            max_value=glucose_max,
            value=(glucose_min, glucose_max)
        )

        filtered_df = filtered_df[
            (filtered_df["Glucose"] >= selected_glucose[0]) &
            (filtered_df["Glucose"] <= selected_glucose[1])
        ]

    # BMI filter
    if "BMI" in filtered_df.columns and not filtered_df["BMI"].dropna().empty:
        bmi_min = float(filtered_df["BMI"].min())
        bmi_max = float(filtered_df["BMI"].max())

        selected_bmi = st.sidebar.slider(
            "BMI Range",
            min_value=float(bmi_min),
            max_value=float(bmi_max),
            value=(float(bmi_min), float(bmi_max))
        )

        filtered_df = filtered_df[
            (filtered_df["BMI"] >= selected_bmi[0]) &
            (filtered_df["BMI"] <= selected_bmi[1])
        ]

    return filtered_df
