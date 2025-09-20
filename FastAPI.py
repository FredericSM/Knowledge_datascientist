# app.py
from __future__ import annotations
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import math
import io
import csv

# --------- Minimal "ML model" you can replace later ----------
class ToyModel:
    """
    A tiny deterministic model: y = a*x1 + b*x2 + bias, with a,b,bias fixed.
    Replace with your own sklearn/torch model (load from disk) later.
    """
    def __init__(self, a: float = 0.7, b: float = 0.3, bias: float = 0.5):
        self.a = a
        self.b = b
        self.bias = bias

    def predict_one(self, x1: float, x2: float) -> float:
        y = self.a * x1 + self.b * x2 + self.bias
        # add a simple nonlinearity to make it less trivial
        return float(round(y + 0.05 * math.tanh(x1 - x2), 6))

    def predict_many(self, X: List[List[float]]) -> List[float]:
        out = []
        for row in X:
            if len(row) < 2:
                raise ValueError("Each row must have at least two features: x1, x2")
            out.append(self.predict_one(row[0], row[1]))
        return out

model = ToyModel()

# --------- FastAPI app ----------
app = FastAPI(title="FastAPI DS Playground", version="0.1.0")

# CORS (optional, useful if you’ll call it from a web app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------- Schemas ----------
class PredictIn(BaseModel):
    x1: float = Field(..., description="Feature 1")
    x2: float = Field(..., description="Feature 2")

class PredictOut(BaseModel):
    prediction: float

class BatchPredictIn(BaseModel):
    rows: List[List[float]] = Field(..., description="Rows of features [[x1, x2], ...]")

class BatchPredictOut(BaseModel):
    predictions: List[float]

# --------- Routes ----------
@app.get("/", tags=["meta"])
def home():
    return {"message": "Salut, monde! 👋 Welcome to your FastAPI DS playground."}

@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}

@app.get("/metrics", tags=["meta"])
def metrics():
    # toy metrics you can expand (e.g., counters, latencies)
    return {"model": "ToyModel", "version": "0.1.0", "features_required": 2}

@app.post("/predict", response_model=PredictOut, tags=["inference"])
def predict(payload: PredictIn):
    y = model.predict_one(payload.x1, payload.x2)
    return {"prediction": y}

@app.post("/predict-batch", response_model=BatchPredictOut, tags=["inference"])
def predict_batch(payload: BatchPredictIn):
    try:
        ys = model.predict_many(payload.rows)
        return {"predictions": ys}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def _train_job(log_id: str):
    # Simulate training: here you’d load data, fit sklearn model, save artifact, etc.
    # For demo, we just "update" parameters.
    model.a *= 1.01
    model.b *= 0.99
    # You could write logs to a file named by log_id.

@app.post("/train", tags=["ops"])
def kick_off_training(background_tasks: BackgroundTasks, log_id: Optional[str] = None):
    background_tasks.add_task(_train_job, log_id or "train-log")
    return {"status": "training-started", "log_id": log_id or "train-log"}

# --------- Simple error example (for testing) ----------
@app.get("/boom", tags=["debug"])
def boom():
    raise HTTPException(status_code=418, detail="I'm a teapot ☕ (demo error)")
