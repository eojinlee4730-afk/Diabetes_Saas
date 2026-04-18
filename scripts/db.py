import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

@st.cache_resource
def get_engine():
    return create_engine(st.secrets["DATABASE_URL"])

def load_realtime_data():
    query = """
    SELECT *
    FROM realtime_data
    """
    return pd.read_sql(query, get_engine())
