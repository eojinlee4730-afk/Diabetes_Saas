import os
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = os.environ.get("DATABASE_URL", "")
# DATABASE_URL = DATABASE_URL.strip()

# print("DATABASE_URL exists:", bool(DATABASE_URL))
# print("DATABASE_URL prefix:", DATABASE_URL.split("://")[0] if DATABASE_URL else "EMPTY")
# print("contains @:", "@" in DATABASE_URL)
# print("contains /neondb:", "/neondb" in DATABASE_URL)
# print("contains sslmode=require:", "sslmode=require" in DATABASE_URL)
# print("length:", len(DATABASE_URL))

engine = create_engine(DATABASE_URL)

DATABASE_URL = os.environ["DATABASE_URL"]

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
