@app.post("/predict")
def predict(data: BorrowerInput):
    try:
        input_df = pd.DataFrame([data.dict()])

        # match model features
        model_features = lgb.feature_name_

        for col in model_features:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[model_features]

        # prediction
        prob = lgb.predict_proba(input_df)[0][1]

        loan_amount = input_df["loanAmount"].values[0]
        expected_loss = prob * loan_amount

        # NEW LOGIC (based on probability)
        if prob < 0.3:
            risk = "Low"
            user_msg = "Your loan is safe. You can proceed."
            bank_msg = "Approve Loan"

        elif prob < 0.7:
            risk = "Medium"
            user_msg = "Try reducing loan amount or EMI."
            bank_msg = "Approve with conditions"

        else:
            risk = "High"
            user_msg = "Improve your credit profile before applying."
            bank_msg = "Reject or verify"

        return {
            "default_probability": float(prob),
            "expected_loss": float(expected_loss),
            "risk_level": risk,
            "user_recommendation": user_msg,
            "bank_recommendation": bank_msg
        }

    except Exception as e:
        return {"error": str(e)}