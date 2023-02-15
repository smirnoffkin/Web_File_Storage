import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app.main import app
from app.config import settings
from app.database import Base, get_db


DATABASE_URL = f"{settings.database_url}_test"

engine = create_engine(url=DATABASE_URL, echo=True)

TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def session():
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
