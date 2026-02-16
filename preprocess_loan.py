import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("Loading datasets...")

# ----------------------------
# 1. Load Data
# ----------------------------
loan = pd.read_csv("Loan.csv")
borrower = pd.read_csv("Borrower.csv")

print("Loan shape:", loan.shape)
print("Borrower shape:", borrower.shape)

# ----------------------------
# 2. Merge Datasets
# ----------------------------
data = pd.merge(loan, borrower, on="memberId", how="inner")

print("Merged shape:", data.shape)

# ----------------------------
# 3. Handle Missing Values
# ----------------------------
data = data.fillna(data.median(numeric_only=True))

# ----------------------------
# 4. Encode Target Variable
# ----------------------------
data['loanStatus'] = data['loanStatus'].map({
    'Current': 0,
    'Default': 1
})

# ----------------------------
# 5. Convert Categorical Variables
# ----------------------------
data = pd.get_dummies(data, drop_first=True)

# ----------------------------
# 6. Feature Scaling
# ----------------------------
scaler = StandardScaler()

numeric_cols = data.select_dtypes(include=np.number).columns
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

# ----------------------------
# 7. Drop Unnecessary Columns
# ----------------------------
data = data.drop(columns=['loanId', 'memberId'], errors='ignore')

# ----------------------------
# 8. Save Processed Dataset
# ----------------------------
data.to_csv("Merged_Preprocessed_Data.csv", index=False)

print("✅ Merging and Preprocessing Completed Successfully!")
