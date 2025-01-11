from fastapi import APIRouter, Depends
from ...schemas.request_models import TextClassificationRequest, PredictionResponse
from ...services.model_service import ModelService

router = APIRouter()
model_service = ModelService()

@router.post("/predict", response_model=PredictionResponse)
async def predict_text(request: TextClassificationRequest):
    result = await model_service.predict(
        text=request.text,
        model_type=request.model_type
    )
    return result 