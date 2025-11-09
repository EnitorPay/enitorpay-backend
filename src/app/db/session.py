from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.core.config import settings  # if your config file defines DATABASE_URL

# Create the database engine
engine = create_engine(settings.DATABASE_URL, echo=False, future=True)

# Create the session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Dependency for FastAPI routes
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
