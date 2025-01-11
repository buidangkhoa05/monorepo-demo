# AI Data Processor Service

A FastAPI-based service for AI model inference and data processing, integrated with Azure Cosmos DB for data persistence.

## Project Structure

``` cmd
data-processor/
├── src/
│ ├── api/ # API Layer
│ │ └── v1/
│ │ ├── api.py # API router configuration
│ │ └── endpoints/
│ │ ├── prediction.py # Prediction endpoints
│ │ └── prediction_history.py # History endpoints
│ │
│ ├── models/ # Models Layer
│ │ ├── base_model.py # Abstract base model class
│ │ └── text_classifier.py # BERT text classifier implementation
│ │
│ ├── services/ # Services Layer
│ │ └── model_service.py # Model management & business logic
│ │
│ ├── repositories/ # Data Access Layer
│ │ ├── base_repository.py # Generic repository pattern
│ │ └── prediction_repository.py # Prediction data access
│ │
│ ├── config/ # Configuration Layer
│ │ ├── settings.py # App settings & environment vars
│ │ └── database.py # Database configuration
│ │
│ ├── schemas/ # Schema Layer
│ │ └── request_models.py # Data validation schemas
│ │
│ └── scripts/ # Utility Scripts
│ └── init_db.py # Database initialization
│
├── tests/ # Test Suite
│ ├── conftest.py # Test configuration
│ ├── test_api/ # API tests
│ └── test_models/ # Model tests
│
├── requirements.txt # Python dependencies
├── project.json # Nx project configuration
└── README.md # Project documentation
```