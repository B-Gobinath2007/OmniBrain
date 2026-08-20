from pydantic import BaseModel
from typing import List, Any

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    citations: List[Any] = []

class UploadResponse(BaseModel):
    success: bool
    filename: str
    document_id: str
