from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


DATABASE_URL = "mssql+pyodbc://sa:SQL@.\\SQLExpress2/MovieApp?driver=ODBC+Driver+17+for+SQL+Server"

def test_connection(database_url):
    try:
        engine = create_engine(database_url)
        with engine.connect():
            print("Connection successful!")
    except OperationalError as e:
        print(f"Connection error: {e}")

test_connection(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()