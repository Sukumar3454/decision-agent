from fastapi import FastAPI, HTTPException
from decision_engine import make_decision
from pydantic import BaseModel
from typing import List
import time
import json
import os
from datetime import datetime

app = FastAPI(title="Decision-Making AI Agent")


# ✅ Input schema
class Product(BaseModel):
    product: str
    revenue: float
    growth_rate: float
    cost: float
    customer_satisfaction: float


# ✅ Utility function to save results
def save_result(data):
    file_path = "data/results.json"

    # Load existing results
    try:
        with open(file_path, "r") as f:
            existing = json.load(f)
    except:
        existing = []

    # Append new result
    existing.append(data)

    # Save updated results
    with open(file_path, "w") as f:
        json.dump(existing, f, indent=4)


# ✅ Root endpoint
@app.get("/")
def root():
    return {"message": "Decision Agent is running 🚀"}


# ✅ Decision using API input
@app.post("/decision")
def decision_agent(data: List[Product]):
    if len(data) < 2:
        raise HTTPException(status_code=400, detail="At least 2 products required")

    start_time = time.time()

    # Convert Pydantic → dict
    products = [item.dict() for item in data]

    result = make_decision(products)

    latency = round(time.time() - start_time, 4)

    # Save result
    output = {
        "source": "api",
        "input": products,
        "result": result,
        "latency": latency,
        "timestamp": str(datetime.now())
    }
    save_result(output)

    return output


# ✅ Decision using JSON file
@app.get("/decision-from-file")
def decision_from_file():
    file_path = os.path.join("data", "products.json")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="products.json file not found")

    with open(file_path) as f:
        data = json.load(f)

    if not isinstance(data, list) or len(data) < 2:
        raise HTTPException(status_code=400, detail="Invalid or insufficient data in file")

    start_time = time.time()

    result = make_decision(data)

    latency = round(time.time() - start_time, 4)

    # Save result
    output = {
        "source": "file",
        "input": data,
        "result": result,
        "latency": latency,
        "timestamp": str(datetime.now())
    }
    save_result(output)

    return output


# ✅ View saved results (Bonus endpoint)
@app.get("/results")
def get_results():
    file_path = "data/results.json"

    if not os.path.exists(file_path):
        return {"message": "No results found"}

    with open(file_path) as f:
        data = json.load(f)

    return {
        "total_records": len(data),
        "results": data
    }