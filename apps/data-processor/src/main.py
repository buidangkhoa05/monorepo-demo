from fastapi import FastAPI
from .api.v1.api import api_router
from .config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 