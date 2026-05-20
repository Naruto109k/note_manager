from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DB_URL = "sqlite:///notes.db"

engine = create_engine(DB_URL)

LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)



class Base(DeclarativeBase):
  pass