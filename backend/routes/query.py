from fastapi import APIRouter
from backend.schemas.models import QueryRequest, QueryResponse
from backend.services.query_service import QueryService
from backend.utils.logger import logger

router = APIRouter(tags=["Query"])

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    logger.info(f"Received query request with question: '{request.question}'")
    result = QueryService.process_query(request)
    logger.info("Query processed successfully.")
    return result
