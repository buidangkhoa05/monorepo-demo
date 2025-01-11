from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "AI Data Processor"
    DEBUG_MODE: bool = False
    MODEL_PATH: str = "models/trained_model"
    API_V1_PREFIX: str = "/api/v1"
    # Cosmos DB Settings
    COSMOS_ENDPOINT: str
    COSMOS_KEY: str
    COSMOS_DATABASE: str = "ai_processor_db"
    PREDICTIONS_CONTAINER: str = "predictions"
    MODELS_CONTAINER: str = "models"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings() 