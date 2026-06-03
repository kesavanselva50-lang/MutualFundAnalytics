import pandas as pd
import os

folder = "data/raw"

for file in sorted(os.listdir(folder)):
    if file.endswith(".csv"):
        try:
            df = pd.read_csv(os.path.join(folder, file))
            print("\n" + "=" * 60)
            print("FILE:", file)
            print("COLUMNS:")
            print(df.columns.tolist())
        except Exception as e:
            print(f"Error reading {file}: {e}")