import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL is not set.")

    engine = create_engine(database_url)
    return engine
