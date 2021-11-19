from sqlalchemy import create_engine, engine, MetaData
import os

SERVER = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
DRIVER = "ODBC Driver 17 for SQL Server"
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")
DATABASE_CONNECTION = f"mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"

engine = create_engine(DATABASE_CONNECTION)
meta = MetaData()
connection = engine.connect()
