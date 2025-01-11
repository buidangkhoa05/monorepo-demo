from fastapi import APIRouter
from .endpoints import prediction, prediction_history

api_router = APIRouter()
api_router.include_router(prediction.router, prefix="/prediction", tags=["prediction"])
api_router.include_router(prediction_history.router, prefix="/predictions", tags=["predictions"]) 