from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root_endpoint():
    """Tests that the root GET / endpoint returns correct details and HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200
    
    json_data = response.json()
    assert json_data == {"message": "OmniBrain API is running"}

def test_upload_endpoint():
    """Tests that the POST /upload endpoint accepts a file and returns success with a doc ID."""
    files = {"file": ("sample.pdf", b"PDF file dummy data", "application/pdf")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    json_data = response.json()
    assert json_data["success"] is True
    assert json_data["filename"] == "sample.pdf"
    assert "document_id" in json_data
    assert json_data["document_id"].startswith("doc_")

def test_query_endpoint():
    """Tests that the POST /query endpoint accepts a question and returns default skeleton payload."""
    payload = {"question": "What is the document about?"}
    response = client.post("/query", json=payload)
    assert response.status_code == 200
    
    json_data = response.json()
    assert json_data["answer"] == "Query received successfully."
    assert json_data["citations"] == []
