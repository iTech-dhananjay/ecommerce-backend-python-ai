import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def new_user():
    return {
        "email": "test@example.com",
        "password": "securepass123",
        "full_name": "Test User"
    }

def test_register_user(new_user):
    response = client.post("/users/register", json=new_user)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == new_user["email"]

def test_login_user(new_user):
    client.post("/users/register", json=new_user)
    response = client.post("/users/login", json={
        "email": new_user["email"],
        "password": new_user["password"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json()