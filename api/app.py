from fastapi import FastAPI, HTTPException
import joblib
import json
import os
from utils import send_alert_email

app = FastAPI()

# TODO: Load model.pkl (students must train & save it)
MODEL_PATH = "model.pkl"

@app.get("/")
def root():
    return {"message": "KT Practical Exam - FastAPI Server Running"}

@app.post("/predict")
def predict(payload: dict):
    """
    TODO:
    1. Validate payload schema.
    2. Load model.
    3. Run prediction.
    4. On any exception → call send_alert_email() with error details.
    """
    try:
        # TODO: validate keys: sqft, bedrooms, bathrooms
        # TODO: convert to list and run model.predict
        return {"prediction": "TODO"}
    except Exception as e:
        # Trigger email alert
        send_alert_email(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")
