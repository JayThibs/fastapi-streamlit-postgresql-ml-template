from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

# Defining connection URL to the database
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+pygresql://postgres:{DB_PASSWORD}@localhost/banknote"
)

# Set up connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for our database models
Base = declarative_base()

# We will import this in other files later to get the session to use.
def get_db():
    """This function retrieves a database session."""
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
