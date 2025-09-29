from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
