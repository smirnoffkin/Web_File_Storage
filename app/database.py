from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from config import settings

engine = create_engine(url=settings.database_url, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()