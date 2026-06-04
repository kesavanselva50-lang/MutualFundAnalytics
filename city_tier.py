import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

tier_counts = df["city_tier"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    tier_counts,
    labels=tier_counts.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 Investor Distribution")

plt.savefig(
    "reports/t30_b30_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()