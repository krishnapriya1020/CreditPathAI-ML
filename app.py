from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import joblib

# ==============================
# Create FastAPI App
# ==============================
app = FastAPI(
    title="CreditPath AI",
    description="Loan Default Prediction System",
    version="1.0"
)

# ==============================
# Templates & Static Files
# ==============================
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# ==============================
# Load Model
# ==============================
lgb = joblib.load("lightgbm_model.pkl")

# ==============================
# Input Schema
# ==============================
class BorrowerInput(BaseModel):
    loanAmount: float
    interestRate: float
    monthlyPayment: float
    purpose: str
    term: str
    grade: str
    isJointApplication: int


# ==============================
# Home Page
# ==============================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ==============================
# Prediction API
# ==============================
@app.post("/predict")
def predict(data: BorrowerInput):

    try:

        input_df = pd.DataFrame([{

            "loanAmount": data.loanAmount,
            "interestRate": data.interestRate,
            "monthlyPayment": data.monthlyPayment,
            "isJointApplication": data.isJointApplication

        }])

        # -------------------------
        # Purpose Encoding
        # -------------------------
        purposes = [

            "auto",
            "business",
            "debtconsolidation",
            "education",
            "healthcare",
            "homeimprovement",
            "other"

        ]

        for p in purposes:

            input_df[f"purpose_{p}"] = 1 if data.purpose.lower() == p else 0

        # -------------------------
        # Term Encoding
        # -------------------------
        terms = [

            "36 months",
            "48 months",
            "60 months"

        ]

        for t in terms:

            col = t.replace(" ", "_")

            input_df[f"term_{col}"] = 1 if data.term == t else 0

        # -------------------------
        # Grade Encoding
        # -------------------------
        grades = [

            "A1","A2","A3",
            "B1","B2","B3",
            "C1","C2","C3",
            "D1","D2","D3",
            "E1","E2","E3"

        ]

        for g in grades:

            input_df[f"grade_{g}"] = 1 if data.grade.upper() == g else 0

        # -------------------------
        # Match Model Features
        # -------------------------
        model_features = lgb.feature_name_

        for col in model_features:

            if col not in input_df.columns:

                input_df[col] = 0

        input_df = input_df[model_features]

        # -------------------------
        # Prediction
        # -------------------------
        probability = float(lgb.predict_proba(input_df)[0][1])

        expected_loss = probability * data.loanAmount

        # -------------------------
        # Risk Logic
        # -------------------------
        if probability < 0.30:

            risk = "🟢 LOW"

            user_msg = "Your loan is safe. You can proceed."

            bank_msg = "Approve Loan"

        elif probability < 0.70:

            risk = "🟡 MEDIUM"

            user_msg = "Try reducing loan amount or EMI."

            bank_msg = "Approve with Conditions"

        else:

            risk = "🔴 HIGH"

            user_msg = "Improve your credit profile before applying."

            bank_msg = "Reject or Verify"

        return {

            "default_probability": round(probability,4),

            "expected_loss": round(expected_loss,2),

            "risk_level": risk,

            "user_recommendation": user_msg,

            "bank_recommendation": bank_msg

        }

    except Exception as e:

        return {

            "error": str(e)

        }