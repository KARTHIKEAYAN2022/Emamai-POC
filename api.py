from fastapi import FastAPI, HTTPException, Response
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
    return {"@odata.context": "https://emamai-poc.onrender.com/$metadata#doubtful_debts",
        "value": data}

@app.get("/doubtful_debts/$metadata")
async def get_metadata():
    metadata = """
    <edmx:Edmx Version="4.0" xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx">
        <edmx:DataServices>
            <Schema Namespace="YourNamespace" xmlns="http://docs.oasis-open.org/odata/ns/edm">
            <EntityType Name="DoubtfulDebt">
                <Key>
                <PropertyRef Name="FiscalYear"/>
                <PropertyRef Name="Customer"/>
                </Key>
                <Property Name="FiscalYear" Type="Edm.String" Nullable="false"/>
                <Property Name="Customer" Type="Edm.String" Nullable="false"/>
                <Property Name="CompanyCode" Type="Edm.String" Nullable="false"/>
                <Property Name="DoubtfulDebts" Type="Edm.Decimal" Nullable="false"/>
                <Property Name="Unit" Type="Edm.String" Nullable="false"/>
            </EntityType>
            <EntityContainer Name="Container">
                <EntitySet Name="doubtful_debts" EntityType="YourNamespace.DoubtfulDebt"/>
            </EntityContainer>
            </Schema>
        </edmx:DataServices>
    </edmx:Edmx>
    """
    return Response(content=metadata, media_type="application/xml")

# Add additional routes and middleware as needed
