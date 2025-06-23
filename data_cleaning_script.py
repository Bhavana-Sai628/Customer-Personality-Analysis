import pandas as pd
import os

# Load dataset 
df = pd.read_csv("marketing_campaign.csv")

# Print column names to confirm
print("Columns in CSV:", df.columns.tolist())

# Check if 'Dt_Customer' is in the dataset
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')
else:
    print(" 'Dt_Customer' column not found. Skipping date conversion.")

# Drop duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Rename columns to lowercase
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Save cleaned data
df.to_csv("cleaned_customer_personality.csv", index=False)

print(" Data cleaning complete.")
