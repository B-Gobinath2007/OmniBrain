from fastapi import APIRouter, UploadFile, File
from backend.schemas.models import UploadResponse
from backend.services.upload_service import UploadService
from backend.utils.logger import logger

router = APIRouter(tags=["Upload"])

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    logger.info(f"Received upload request for file: {file.filename}")
    result = UploadService.save_file(file)
    if result["success"]:
        logger.info(f"File {file.filename} saved successfully with ID: {result['document_id']}")
    else:
        logger.error(f"Failed to save file: {file.filename}")
    return result
