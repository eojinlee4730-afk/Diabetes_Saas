import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine using Streamlit secrets.
    """

    database_url = st.secrets["DATABASE_URL"]
    engine = create_engine(database_url)

    return engine
