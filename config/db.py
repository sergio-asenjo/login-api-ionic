from sqlalchemy import create_engine, engine
import os
import pandas as pd

SERVER = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
DRIVER = "SQL Server Native Client 11.0"
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")
DATABASE_CONNECTION = f"mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"

engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

df = pd.read_sql_query("SELECT * FROM [dbo].[Usuario]", connection)