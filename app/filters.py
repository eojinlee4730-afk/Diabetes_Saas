import pandas as pd
import streamlit as st


def render_sidebar_filters(df: pd.DataFrame) -> dict:
    """
    Render sidebar filters for the diabetes dataset.
    """

    st.sidebar.header("Filters")

    outcome_options = ["All", 0, 1]
    selected_outcome = st.sidebar.selectbox(
        "Outcome",
        options=outcome_options,
        index=0
    )

    age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
    selected_age_range = st.sidebar.slider(
        "Age Range",
        min_value=age_min,
        max_value=age_max,
        value=(age_min, age_max)
    )

    glucose_min, glucose_max = int(df["Glucose"].min()), int(df["Glucose"].max())
    selected_glucose_range = st.sidebar.slider(
        "Glucose Range",
        min_value=glucose_min,
        max_value=glucose_max,
        value=(glucose_min, glucose_max)
    )

    bmi_min, bmi_max = float(df["BMI"].min()), float(df["BMI"].max())
    selected_bmi_range = st.sidebar.slider(
        "BMI Range",
        min_value=float(bmi_min),
        max_value=float(bmi_max),
        value=(float(bmi_min), float(bmi_max))
    )

    pregnancies_min, pregnancies_max = int(df["Pregnancies"].min()), int(df["Pregnancies"].max())
    selected_pregnancies_range = st.sidebar.slider(
        "Pregnancies Range",
        min_value=pregnancies_min,
        max_value=pregnancies_max,
        value=(pregnancies_min, pregnancies_max)
    )

    return {
        "outcome": selected_outcome,
        "age_range": selected_age_range,
        "glucose_range": selected_glucose_range,
        "bmi_range": selected_bmi_range,
        "pregnancies_range": selected_pregnancies_range,
    }


def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Apply sidebar filters to the dataset.
    """

    filtered_df = df.copy()

    if filters["outcome"] != "All":
        filtered_df = filtered_df[filtered_df["Outcome"] == filters["outcome"]]

    filtered_df = filtered_df[
        (filtered_df["Age"] >= filters["age_range"][0]) &
        (filtered_df["Age"] <= filters["age_range"][1])
    ]

    filtered_df = filtered_df[
        (filtered_df["Glucose"] >= filters["glucose_range"][0]) &
        (filtered_df["Glucose"] <= filters["glucose_range"][1])
    ]

    filtered_df = filtered_df[
        (filtered_df["BMI"] >= filters["bmi_range"][0]) &
        (filtered_df["BMI"] <= filters["bmi_range"][1])
    ]

    filtered_df = filtered_df[
        (filtered_df["Pregnancies"] >= filters["pregnancies_range"][0]) &
        (filtered_df["Pregnancies"] <= filters["pregnancies_range"][1])
    ]

    return filtered_df
