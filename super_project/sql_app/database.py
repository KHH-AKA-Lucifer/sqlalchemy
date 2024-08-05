# create engine
from sqlalchemy import create_engine
# create a base
from sqlalchemy.ext.declarative import declarative_base
# for database session
from sqlalchemy.orm import sessionmaker

# create a database link
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# create an engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
)

# create a session
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

# create a base class
# we will use this class later to construct tables
Base = declarative_base()