import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load NAV data
df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Select first 10 funds
top_funds = df["amfi_code"].unique()[:10]

df = df[df["amfi_code"].isin(top_funds)]

# Pivot data
pivot_df = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot_df.pct_change().dropna()

# Correlation matrix
corr_matrix = returns.corr()

# Plot
plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("NAV Return Correlation Matrix (10 Funds)")

plt.tight_layout()

plt.savefig(
    "nav_correlation_matrix.png",
    dpi=300
)

plt.show()

print("Correlation matrix saved successfully.")