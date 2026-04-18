import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Realtime Diabetes Dashboard")

# Connecting DB
DATABASE_URL = st.secrets["DATABASE_URL"]
engine = create_engine(DATABASE_URL)

# Bring Data
query = """
SELECT *
FROM realtime_data
LIMIT 100
"""

df = pd.read_sql(query, engine)

st.write(f"Rows: {len(df)}")
st.dataframe(df)
