from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load the CSV data
def load_data():
    df = pd.read_csv("Doubtful debts.csv")
    return df.to_dict(orient="records")

data = load_data()

@app.get("/doubtful_debts")
async def doubtful_debts():
    return {"@odata.context": "https://emamai-poc.onrender.com/%24metadata#doubtful_debts",
        "value":data}

