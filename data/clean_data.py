import pandas as pd
import os

# Define file paths
raw_data_path = "data/data.csv" # Make sure your downloaded Kaggle CSV is renamed to data.csv and placed in the data folder
cleaned_data_path = "data/cleaned_online_retail.csv"

if os.path.exists(raw_data_path):
    print("🔄 Loading raw dataset...")
    # Read dataset handling encoding variations
    df = pd.read_csv(raw_data_path, encoding="ISO-8859-1")
    
    print(f"📊 Initial Row Count: {len(df)}")
    
    # Rule 1: Remove rows where Quantity is less than 1 (Removes returns/cancellations)
    df = df[df['Quantity'] >= 1]
    
    # Rule 2: Remove rows where UnitPrice is less than 0
    df = df[df['UnitPrice'] >= 0]
    
    # Rule 3: Drop rows with missing CustomerID
    df = df.dropna(subset=['CustomerID'])
    
    # Convert CustomerID to integer strings so Tableau doesn't treat them as numeric measurements
    df['CustomerID'] = df['CustomerID'].astype(int).astype(str)
    
    # Create Calculated Field: Revenue
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    
    print(f"✅ Cleaned Row Count: {len(df)}")
    
    # Save the cleaned file
    df.to_csv(cleaned_data_path, index=False)
    print(f"💾 Cleaned data saved successfully to: {cleaned_data_path}")
else:
    print(f"❌ Error: Please place your downloaded Kaggle CSV file inside '{raw_data_path}' first!")
