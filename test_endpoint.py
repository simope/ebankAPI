from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mypassword@localhost/ebank"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "id": 1000,
            "full_name": "John Testing",
            "email": "test@testing.com",
            "password": "toppassword"
            },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "test@testing.com"
    assert "id" in data

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200, response.text

def test_get_user():
    response = client.get("/users/1000")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "test@testing.com"
    assert "id" in data

def test_update_user():
    response = client.put(
        "/users/1000",
        json={
            "id": 1000,
            "full_name": "John Testing 2.0",
            "email": "test@testing.com",
            "password": "toppasswordnuova"
            })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["full_name"] == "John Testing 2.0"
    assert "id" in data

def test_delete_user():
    response = client.delete(
        "/users/1000",
    )
    assert response.status_code == 204, response.text