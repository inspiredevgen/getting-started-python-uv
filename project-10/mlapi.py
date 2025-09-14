#Importing necessary libraries

from fastapi import FastAPI
from pydantic import BaseModel

politicians = []

app = FastAPI()

class ScoringPolitician(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    party: str
    province: str


@app.get("/")
async def scoring_endpoint():
    return {"message": "Welcome to the ML API!"}

@app.post("/politician")
async def predict_politician(politician: ScoringPolitician):
    # Here you would typically call your ML model to make a prediction
    # For demonstration, we will return the politician's data
    return {
        "first_name": politician.first_name,
        "last_name": politician.last_name,
        "date_of_birth": politician.date_of_birth,
        "party": politician.party,
        "province": politician.province,
        "prediction": "This is a placeholder for the model's prediction."
    }

@app.post("/politicians")
async def add_politician(politician: ScoringPolitician):
    politicians.append(politician)
    return {"message": "Politician added successfully", "politician": politician}

@app.get("/politicians")
async def get_politicians():
    return {"politicians": politicians}

@app.delete("/politicians/{index}")
async def delete_politician(index: int):
    if 0 <= index < len(politicians):
        removed_politician = politicians.pop(index)
        return {"message": "Politician deleted successfully", "politician": removed_politician}
    else:
        return {"error": "Index out of range"}