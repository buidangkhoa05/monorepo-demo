from typing import Dict
import time
from ..models.text_classifier import TextClassifier
from ..config.settings import get_settings
from ..repositories.prediction_repository import PredictionRepository

class ModelService:
    def __init__(self):
        self.models: Dict[str, TextClassifier] = {}
        self.settings = get_settings()
        self.prediction_repo = PredictionRepository()
    
    def get_or_create_model(self, model_type: str) -> TextClassifier:
        if model_type not in self.models:
            self.models[model_type] = TextClassifier(model_name=model_type)
        return self.models[model_type]
    
    async def predict(self, text: str, model_type: str):
        start_time = time.time()
        model = self.get_or_create_model(model_type)
        predictions = model.predict(text)
        processing_time = time.time() - start_time
        
        # Store prediction in Cosmos DB
        await self.prediction_repo.create_prediction(
            text=text,
            predictions=predictions,
            model_type=model_type
        )
        
        return {
            "predictions": predictions,
            "model_type": model_type,
            "processing_time": processing_time
        } 