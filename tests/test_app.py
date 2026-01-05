from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_success():
    # Assuming we can signup
    response = client.post("/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"})
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

def test_signup_activity_not_found():
    response = client.post("/activities/NonExistent/signup", params={"email": "test@example.com"})
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]