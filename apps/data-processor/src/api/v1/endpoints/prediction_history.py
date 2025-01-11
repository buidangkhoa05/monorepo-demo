from fastapi import APIRouter, Query
from typing import List
from ...repositories.prediction_repository import PredictionRepository
from ...schemas.request_models import PredictionHistoryResponse

router = APIRouter()
prediction_repo = PredictionRepository()

@router.get("/history", response_model=List[PredictionHistoryResponse])
async def get_prediction_history(
    model_type: str = None,
    limit: int = Query(default=100, le=1000)
):
    if model_type:
        predictions = await prediction_repo.get_predictions_by_model(model_type, limit)
    else:
        predictions = await prediction_repo.get_recent_predictions(limit)
    return predictions 