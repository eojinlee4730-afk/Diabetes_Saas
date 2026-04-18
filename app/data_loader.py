import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path: str = "data/diabetes.csv") -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Args:
        path (str): Path to CSV file

    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(path)

    # Convert date column if exists
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df
