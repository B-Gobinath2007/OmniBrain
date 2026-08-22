import os
import httpx
from typing import Dict, Any

# Get backend URL from environment variables, fallback to localhost
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def upload_file(file_name: str, file_bytes: bytes) -> Dict[str, Any]:
    """Sends a POST request to /upload with the file data."""
    url = f"{BACKEND_URL}/upload"
    files = {"file": (file_name, file_bytes)}
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(url, files=files)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return {
            "success": False,
            "filename": file_name,
            "document_id": "",
            "error": str(e)
        }

def query_backend(question: str) -> Dict[str, Any]:
    """Sends a POST request to /query with the user's question."""
    url = f"{BACKEND_URL}/query"
    payload = {"question": question}
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return {
            "answer": f"Error: Unable to connect to the backend server at {BACKEND_URL}.",
            "citations": []
        }
