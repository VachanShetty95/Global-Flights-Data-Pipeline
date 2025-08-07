import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load credentials
load_dotenv()

user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
db = os.getenv("PG_DB")

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

# Load CSV sample
df = pd.read_csv("datasets/flights_sample.csv")
df_airports = pd.read_csv("datasets/airports.csv")
df_airlines = pd.read_csv("datasets/airlines.csv")

# Optional: drop unnamed column if exists
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Write to PostgreSQL
try:
    df.to_sql("flights_raw", engine, if_exists="replace", index=False)
except:
    pass
df_airports.to_sql("airports", engine, if_exists="replace", index=False)
df_airlines.to_sql("airlines", engine, if_exists="replace", index=False)

print("Loaded flights_sample.csv into PostgreSQL table 'flights_raw'")
