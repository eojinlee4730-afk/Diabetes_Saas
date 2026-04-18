import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

@st.cache_resource
def get_engine():
    return create_engine(st.secrets["DATABASE_URL"])

@st.cache_data(ttl=10)
def run_query(query: str) -> pd.DataFrame:
    return pd.read_sql(query, get_engine())
