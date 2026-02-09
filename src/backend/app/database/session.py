from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from ..core.config import settings

# Create the database engine
engine = create_engine(settings.database_url)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator:
    """
    Dependency to get a database session
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()