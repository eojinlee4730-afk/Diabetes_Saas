import streamlit as st
import pandas as pd

def render_sidebar_filters(df: pd.DataFrame) -> dict:
    """
    Render sidebar filters and return selected values.
    """

    st.sidebar.header("Filters")

    region_options = ["All"]
    if "region" in df.columns:
        region_options += sorted(df["region"].dropna().unique().tolist())

    category_options = ["All"]
    if "category" in df.columns:
        category_options += sorted(df["category"].dropna().unique().tolist())

    selected_region = st.sidebar.selectbox(
        "Select Region",
        region_options,
        key="region_filter"
    )

    selected_category = st.sidebar.selectbox(
        "Select Category",
        category_options,
        key="category_filter"
    )

    return {
        "region": selected_region,
        "category": selected_category
    }


def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Apply selected filters to dataframe.
    """

    filtered_df = df.copy()

    if filters["region"] != "All" and "region" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["region"] == filters["region"]]

    if filters["category"] != "All" and "category" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["category"] == filters["category"]]

    return filtered_df
