from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load the CSV data
def load_data():
    df = pd.read_csv("Doubtful debts.csv")
    return df

df = load_data()

@app.get("/doubtful_debts")
async def doubtful_debts():
    odata_json = {
        "d": {
            "results": []
        }
    }

    for _, row in df.iterrows():
        entry = {
            "__metadata": {
                "id": f"Customer({row['Customer']})",
                "uri": f"/odata/service/Customer({row['Customer']})",
                "type": "Namespace.Customer"
            },
            "FiscalYear": row["Fiscal Year"],
            "Customer": row["Customer"],
            "CompanyCode": row["Company code"],
            "DoubtfulDebts": row["Doubtful debts"],
            "Unit": row["Unit"]
        }
        odata_json["d"]["results"].append(entry)
    
    return odata_json