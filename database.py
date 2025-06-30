from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta

DATABASE_URI = "postgresql+psycopg2://postgres:147896325@localhost:5432/test-db" 
engine = create_engine(DATABASE_URI, echo=True)
Sessionlocal = sessionmaker(bind=engine)

Base: DeclarativeMeta = declarative_base()