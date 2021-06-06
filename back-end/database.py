from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import Config

settings = Config()

engine = create_engine(settings.sqlalchemy_base_url)  # Just created engine
SessionLocal = sessionmaker(
    engine
)  # It's the way about request to database server from fastapi server
Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.colse()
