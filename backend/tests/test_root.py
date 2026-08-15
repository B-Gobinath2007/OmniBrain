from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root_endpoint():
    """Tests that the root GET / endpoint returns correct details and HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200
    
    json_data = response.json()
    assert "message" in json_data
    assert json_data["message"] == "OmniBrain API is running"
    assert "version" in json_data
    assert json_data["version"] == "1.0.0"
