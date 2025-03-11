import pandas as pd
from datetime import datetime

df = pd.read_csv("raw_cafe_sales.csv")

# trim spaces
df.columns = df.columns.str.strip()

# convert to numeric type
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")

# fix 'Total Spent' where the value is 'ERROR'
df.loc[df["Total Spent"].str.upper() == "ERROR", "Total Spent"] = df["Quantity"] * df["Price Per Unit"]

df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Replace 'UNKNOWN' values
df["Payment Method"] = df["Payment Method"].replace("UnKNOWN", "Not Specified")
df["Location"] = df["Location"].replace("UNKNOWN", "Not Specified")

# standardize date format
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce").dt.strftime("%Y-%m-%d")

df.to_csv("cleaned_cafe_sales.csv", index=False)
print("Data transformtion complete! Saved as 'cleaned_cafe_sales.csv'.")