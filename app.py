from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import os
from typing import List

app = FastAPI(title="Health Risk Prediction API")

# Resolve model path correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "health_risk_model.pkl")

# Load model once at startup
model = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = [
    "age",
    "days_sick",
    "severity",
    "fever",
    "cough",
    "headache",
    "vomiting",
    "chest_pain",
    "breathlessness"
]

class PredictRequest(BaseModel):
    age: int = Field(..., example=25)
    days_sick: int = Field(..., example=3)
    severity: int = Field(..., example=2)
    fever: int = Field(..., example=1)
    cough: int = Field(..., example=0)
    headache: int = Field(..., example=1)
    vomiting: int = Field(..., example=0)
    chest_pain: int = Field(..., example=0)
    breathlessness: int = Field(..., example=1)

class PredictResponse(BaseModel):
    predicted_risk_level: int
    confidence: List[float]

@app.get("/")
def home():
    return {"message": "FastAPI ML API running on Hugging Face"}

@app.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    try:
        user_df = pd.DataFrame([data.dict()])
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid input data")

    prediction = int(model.predict(user_df)[0])
    probability = model.predict_proba(user_df)[0].tolist()

    return {
        "predicted_risk_level": prediction,
        "confidence": probability
    }

# Run locally:
# uvicorn app:app --reload
