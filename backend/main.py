from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.config import settings
from backend.utils.logger import logger
from backend.routes import upload, query

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("OmniBrain API is starting up...")
    logger.info(f"Settings loaded: APP_NAME='{settings.APP_NAME}', APP_VERSION='{settings.APP_VERSION}', DEBUG={settings.DEBUG}, MOCK_MODE={settings.MOCK_MODE}")
    yield

app = FastAPI(
    title="OmniBrain API",
    version="1.0.0",
    description="Backend API for the OmniBrain platform.",
    lifespan=lifespan
)

# Include routers
app.include_router(upload.router)
app.include_router(query.router)

@app.get("/", status_code=200)
async def root_endpoint():
    logger.debug("Root endpoint GET / called")
    return {
        "message": "OmniBrain API is running"
    }
