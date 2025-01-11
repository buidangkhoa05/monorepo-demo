from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DataItem(BaseModel):
    id: int
    value: str

@app.get("/")
async def root():
    return {"message": "Data Processor Service"}

@app.post("/process")
async def process_data(item: DataItem):
    return {"processed": True, "item": item} 