import os
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)

CHUNK_SIZE = 10

with engine.begin() as conn:
    # Bring 10 rows from staging_realtime_data
    chunk = pd.read_sql(
        text(f"SELECT * FROM staging_realtime_data LIMIT {CHUNK_SIZE}"),
        conn
    )

    if chunk.empty:
        print("No rows left in staging_realtime_data.")
    else:
        # Add real time data at realtime_data
        chunk.to_sql(
            "realtime_data",
            con=conn,
            if_exists="append",
            index=False
        )

        # Remove row what you already used
        ids = chunk["patient_id"].tolist()

        conn.execute(
            text("DELETE FROM staging_realtime_data WHERE patient_id = ANY(:ids)"),
            {"ids": ids}
        )

        print(f"Inserted {len(chunk)} rows into realtime_data.")
