from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load saved files
model = joblib.load("loan_default_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")


class LoanData(BaseModel):
    age: int
    annual_income: float
    monthly_income: float
    debt_to_income_ratio: float
    credit_score: int
    loan_amount: float
    interest_rate: float
    loan_term: int
    installment: float
    num_of_open_accounts: int
    total_credit_limit: float
    current_balance: float
    delinquency_history: int
    public_records: int
    num_of_delinquencies: int


@app.get("/")
def home():
    return {
        "message": "Loan Default Risk Prediction API is running",
        "features": len(columns)
    }


@app.post("/predict")
def predict(data: LoanData):

    # Convert input to DataFrame
    df = pd.DataFrame([data.dict()])

    # Create missing encoded columns
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Maintain same feature order as training
    df = df[columns]

    # Scale input
    scaled_data = scaler.transform(df)

    # Make prediction
    prediction = model.predict(scaled_data)[0]

    # Get probability
    probability = model.predict_proba(scaled_data)[0][1]

    # Friendly result
    risk_level = "Likely To Repay"

    if prediction == 0:
        risk_level = "High Risk Customer"

    return {
        "risk_level": risk_level,
        "prediction": int(prediction),
        "repayment_probability": round(float(probability), 2)
    }