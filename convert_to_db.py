import pandas as pd
import sqlite3

# connect to database
conn = sqlite3.connect("loan_database.db")

# RAW CSV FILE → raw_loans table
raw_df = pd.read_csv("Borrower.csv")
raw_df.to_sql("raw_loans", conn, if_exists="replace", index=False)

# PREPROCESSED CSV FILE → processed_loans table
processed_df = pd.read_csv("Loan_cleaned.csv")
processed_df.to_sql("processed_loans", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("raw_loans and processed_loans tables created successfully!")