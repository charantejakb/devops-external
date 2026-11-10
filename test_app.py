
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_students(client):
    response = client.get("/Students")
    assert response.status_code == 200

def test_invalid_student(client):
    response = client.get("/Students/999")
    assert response.status_code == 405
