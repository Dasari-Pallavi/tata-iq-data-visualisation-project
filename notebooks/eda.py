"""EDA for the Superstore dataset.
Run: python notebooks/eda.py (needs pandas; put the CSV at data/superstore.csv)
"""
import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding="latin-1")

print("Shape:", df.shape)
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSummary:\n", df.describe())

# Dates and basic cleaning
df["Order Date"] = pd.to_datetime(df["Order Date"])
df = df.drop_duplicates()

# Quick answers to the CEO / CMO questions
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print(f"\nTotal sales: {total_sales:,.0f}")
print(f"Total profit: {total_profit:,.0f}")
print(f"Profit margin: {total_profit / total_sales:.1%}")

print("\nProfit by region:\n", df.groupby("Region")["Profit"].sum().sort_values())
print("\nProfit by sub-category:\n", df.groupby("Sub-Category")["Profit"].sum().sort_values())

df["Discount Band"] = pd.cut(
    df["Discount"], [-0.01, 0, 0.2, 0.4, 1], labels=["0%", "1-20%", "21-40%", "40%+"]
)
print("\nProfit by discount band:\n", df.groupby("Discount Band", observed=True)["Profit"].sum())

monthly = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
print("\nSales by month:\n", monthly)

orders = df.groupby("Customer ID")["Order ID"].nunique()
print(f"\nRepeat customers: {(orders > 1).mean():.1%}")

df.to_csv("data/cleaned_superstore.csv", index=False)
print("\nSaved data/cleaned_superstore.csv")
