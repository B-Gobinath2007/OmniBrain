import os
import uuid
import shutil
from fastapi import UploadFile
from pathlib import Path

# Temporary upload folder inside backend
TEMP_DIR = Path(__file__).resolve().parent.parent / "temp_uploads"

class UploadService:
    @staticmethod
    def save_file(file: UploadFile) -> dict:
        """Saves an uploaded file to the temporary uploads directory.
        
        Generates a unique document ID and returns the status, filename, and document ID.
        """
        # Ensure temp directory exists
        os.makedirs(TEMP_DIR, exist_ok=True)
        
        # Generate a unique document ID (e.g. doc_a3f12b)
        doc_id = f"doc_{uuid.uuid4().hex[:6]}"
        
        # Target path for saving the file
        file_path = TEMP_DIR / file.filename
        
        try:
            # Save file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            return {
                "success": True,
                "filename": file.filename,
                "document_id": doc_id
            }
        except Exception as e:
            return {
                "success": False,
                "filename": file.filename,
                "document_id": ""
            }
