from sqlalchemy import create_engine, engine, MetaData
import os

SERVER = os.environ["DB_HOST"]
DATABASE = os.environ["DB_NAME"]
DRIVER = "ODBC Driver 17 for SQL Server"
USERNAME = os.environ["DB_USER"]
PASSWORD = os.environ["DB_PASS"]
INSTANCE_NAME = os.environ["DB_INSTANCE"]
DATABASE_CONNECTION = f"mssql://{USERNAME}:{PASSWORD}@{SERVER}\{INSTANCE_NAME},1433/{DATABASE}?driver={DRIVER}"

engine = create_engine(DATABASE_CONNECTION)
meta = MetaData()
connection = engine.connect()
