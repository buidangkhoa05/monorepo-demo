from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class TextClassificationRequest(BaseModel):
    text: str
    model_type: Optional[str] = "bert-base-uncased"

class TrainingRequest(BaseModel):
    texts: List[str]
    labels: List[int]
    model_type: Optional[str] = "bert-base-uncased"

class PredictionResponse(BaseModel):
    predictions: List[float]
    model_type: str
    processing_time: float

class PredictionHistoryResponse(BaseModel):
    id: str
    text: str
    predictions: List[float]
    model_type: str
    timestamp: datetime
    type: str 