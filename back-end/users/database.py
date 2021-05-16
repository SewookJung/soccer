from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_BASE_URL = "postgresql://admin:lyjsw132!#@@localhost/soccer"

engine = create_engine(SQLALCHEMY_BASE_URL)
SessionLocal = sessionmaker(engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
