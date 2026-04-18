import pandas as pd
import streamlit as st

from db import get_database_engine
from queries import SELECT_ALL_DIABETES_DATA


@st.cache_data
def load_data() -> pd.DataFrame:
    """
    Load diabetes data from the realtime_data table in Neon PostgreSQL.
    """

    engine = get_database_engine()
    df = pd.read_sql(SELECT_ALL_DIABETES_DATA, engine)

    numeric_columns = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
        "Outcome"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df
