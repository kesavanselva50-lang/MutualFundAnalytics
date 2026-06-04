import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv(
    "data/processed/05_category_inflows_cleaned.csv"
)

# Create pivot table
heatmap_data = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# Plot
plt.figure(figsize=(14,8))

sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    annot=True,
    fmt=".0f"
)

plt.title("Category-wise Net Inflows Heatmap")
plt.xlabel("Month")
plt.ylabel("Fund Category")

plt.tight_layout()

plt.savefig(
    "category_inflow_heatmap.png",
    dpi=300
)

plt.show()

print("Heatmap saved successfully.")