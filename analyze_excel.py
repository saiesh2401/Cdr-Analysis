import pandas as pd
import os

files = ['JIO IP.xlsx', 'Airtel Format.xlsx', 'JIO IP.xlsx']
files = [f for f in files if os.path.exists(f)]

for file in files:
    print(f"--- ANALYZING {file} ---")
    try:
        df = pd.read_excel(file)
        print("COLUMNS:", df.columns.tolist())
        print("FIRST ROW:", df.iloc[0].tolist() if not df.empty else "Empty")
    except Exception as e:
        print(f"Error reading {file}: {e}")
    print("\n")
