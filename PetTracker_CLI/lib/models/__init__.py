from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This creates our SQLAlchemy engine, pointing to a local SQLite file.
engine = create_engine('sqlite:///pets.db')
Session = sessionmaker(bind=engine)
session = Session()

# This is the base class for our models.
Base = declarative_base()

# Import the models so SQLAlchemy knows about them
from .pet import Pet
from .task import Task