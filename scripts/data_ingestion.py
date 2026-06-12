import pandas as pd

df = pd.read_csv("data/raw/HDFC_Top100_NAV.csv")

print(df["nav"].describe())