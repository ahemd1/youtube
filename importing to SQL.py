import pandas as pd
from sqlalchemy import create_engine
import urllib

# Step 1: Load the cleaned CSV
df = pd.read_csv("Trending_Cleaned.csv")

# Step 2: Define SQL Server connection string
print("Connecting to SQL Server")
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=youtube;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Step 3: Load data into SQL table
try:
    print("Loading data into 'youtubeTrending' table")
    df.to_sql("youtubeTrending", con=engine, if_exists="replace", index=False)
    print("Data loaded successfully!")
except Exception as e:
    print("Failed to load data:", e)
