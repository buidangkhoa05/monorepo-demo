from datetime import datetime
from typing import List, Optional
from .base_repository import BaseRepository
from ..config.settings import get_settings

settings = get_settings()

class PredictionRepository(BaseRepository):
    def __init__(self):
        super().__init__(settings.PREDICTIONS_CONTAINER)
    
    async def create_prediction(self, text: str, predictions: List[float], model_type: str) -> dict:
        prediction_item = {
            "id": str(datetime.utcnow().timestamp()),
            "text": text,
            "predictions": predictions,
            "model_type": model_type,
            "timestamp": datetime.utcnow().isoformat(),
            "type": "prediction"  # partition key
        }
        return await self.create(prediction_item)
    
    async def get_predictions_by_model(self, model_type: str, limit: int = 100) -> List[dict]:
        query = """
        SELECT * FROM c 
        WHERE c.type = 'prediction' 
        AND c.model_type = @model_type 
        ORDER BY c.timestamp DESC 
        OFFSET 0 LIMIT @limit
        """
        parameters = {
            "@model_type": model_type,
            "@limit": limit
        }
        return await self.query(query, parameters)
    
    async def get_recent_predictions(self, limit: int = 100) -> List[dict]:
        query = """
        SELECT * FROM c 
        WHERE c.type = 'prediction' 
        ORDER BY c.timestamp DESC 
        OFFSET 0 LIMIT @limit
        """
        return await self.query(query, {"@limit": limit}) 