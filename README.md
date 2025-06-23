# Customer-Personality-Analysis
1. Import Required Libraries
import pandas as pd
import os
pandas is used for data manipulation and analysis.
os can be used for file handling (though not used in this snippet, it's often included for flexibility).

2. Load Dataset
df = pd.read_csv("marketing_campaign.csv")
Loads the raw dataset (marketing_campaign.csv) into a Pandas DataFrame called df.

3. Display Column Names
print("Columns in CSV:", df.columns.tolist())
Prints the list of column names in the dataset to confirm the structure and check for expected fields.

4. Convert Date Column
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')
else:
    print(" 'Dt_Customer' column not found. Skipping date conversion.")
Checks for the presence of the Dt_Customer column, which represents the date when a customer joined.

If it exists, the script converts it to datetime format using pd.to_datetime().

The errors='coerce' parameter replaces any invalid or improperly formatted dates with NaT (Not a Time).

5. Remove Duplicates and Missing Values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
drop_duplicates(): Removes duplicate rows in the dataset.

dropna(): Removes any rows with missing (NaN) values to ensure data quality.

6. Standardize Column Names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
Converts all column names to lowercase.

Strips leading/trailing whitespace.

Replaces spaces with underscores (_) for consistency and easier access in code (e.g., Year_Birth → year_birth).

7. Save Cleaned Dataset
df.to_csv("cleaned_customer_personality.csv", index=False)
Saves the cleaned dataset as cleaned_customer_personality.csv in the same directory.

index=False prevents writing the DataFrame index as a separate column.

 8. Completion Message
print(" Data cleaning complete.")
Prints a message confirming successful execution and data cleaning.
