import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add project root to Python path so imports work during testing
sys.path.append(str(Path(__file__).resolve().parents[1]))

from main import app
from src.utils.db import Base, get_db
from src.user.models import Usermodel
from src.utils.helpers import is_authenticated


# Separate SQLite database only for testing
TEST_DB_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Override the real DB dependency with the test DB
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create test tables before tests start, drop them after tests finish
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


# Client fixture for unauthenticated routes like register/login
@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# Client fixture for authenticated routes like /tasks
@pytest.fixture
def auth_client():
    db = TestingSessionLocal()

    # Create a fake authenticated user in test DB if not already present
    test_user = db.query(Usermodel).filter(Usermodel.username == "taskuser").first()
    if not test_user:
        test_user = Usermodel(
            name="Task User",
            username="taskuser",
            email="taskuser@gmail.com",
            hash_password="fakehashedpassword"
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)

    # Override authentication dependency
    def override_is_authenticated():
        return test_user

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[is_authenticated] = override_is_authenticated

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
    db.close()