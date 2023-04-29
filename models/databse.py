from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from dotenv import load_dotenv
import os 
load_dotenv()

DB_URL = os.environ.get("DB_URL")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False , autocommit = False , bind=engine)
Base = declarative_base()
db = SessionLocal()

def connect_db():
    try:
        yield db
        print('Connected to database')
    except Exception as error:
        return error
    finally:db.close()