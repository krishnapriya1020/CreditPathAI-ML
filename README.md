# CreditPathAI-ML

## 📌 Project Overview

CreditPathAI-ML is a Machine Learning-based Loan Default Prediction System that predicts the probability of loan default using borrower information. The project applies data preprocessing, exploratory data analysis (EDA), and multiple machine learning models to assess credit risk and support lending decisions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Logistic Regression, XGBoost, and LightGBM models
- ROC-AUC Evaluation
- Confusion Matrix
- Feature Importance Analysis
- Expected Loss Prediction
- Risk Level Classification
- FastAPI-based prediction API

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- XGBoost
- Matplotlib
- Seaborn
- FastAPI

---

## 🤖 Machine Learning Models

- Logistic Regression
- XGBoost
- LightGBM

LightGBM was selected as the final model based on its overall performance.

---

## 📂 Project Files

- `EDA.ipynb` – Data preprocessing, EDA, model training, and evaluation
- `app.py` – FastAPI application for loan default prediction
- `lightgbm_model.pkl` – Trained LightGBM model
- `requirements.txt` – Required Python libraries
- `Borrower.csv` – Sample dataset

---

## 📊 Results

- Built and compared multiple machine learning models.
- Evaluated models using Accuracy, ROC-AUC, Confusion Matrix, and Feature Importance.
- Developed an Expected Loss Engine to estimate financial risk and provide recommendations.

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```

3. Open the API documentation:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 👩‍💻 Author

**Krishna Priya Choda**

B.Tech – Computer Science and Engineering (Cyber Security)

Shri Vishnu Engineering College for Women
