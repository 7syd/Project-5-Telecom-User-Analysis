import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Telecom Customer Satisfaction API")

model = joblib.load("models/satisfaction_regression_model.pkl")


class CustomerFeatures(BaseModel):
    Sessions_Score: float
    Duration_Score: float
    Traffic_Score: float
    TCP_DL_Score: float
    TCP_UL_Score: float
    RTT_DL_Score: float
    RTT_UL_Score: float
    Throughput_DL_Score: float
    Throughput_UL_Score: float


@app.get("/")
def home():
    return {"message": "Telecom Customer Satisfaction API is running"}


@app.post("/predict")
def predict(features: CustomerFeatures):

    data = pd.DataFrame([{
        "Sessions_Score": features.Sessions_Score,
        "Duration_Score": features.Duration_Score,
        "Traffic_Score": features.Traffic_Score,
        "TCP_DL_Score": features.TCP_DL_Score,
        "TCP_UL_Score": features.TCP_UL_Score,
        "RTT_DL_Score": features.RTT_DL_Score,
        "RTT_UL_Score": features.RTT_UL_Score,
        "Throughput_DL_Score": features.Throughput_DL_Score,
        "Throughput_UL_Score": features.Throughput_UL_Score
    }])

    prediction = model.predict(data)[0]

    return {
        "predicted_satisfaction_score": float(prediction)
    }