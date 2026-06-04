import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv"
)

sector_weights = (
    df.groupby("sector")["weight_pct"]
      .sum()
      .sort_values(ascending=False)
)

top_sectors = sector_weights.head(10)

plt.figure(figsize=(10,10))

wedges, texts, autotexts = plt.pie(
    top_sectors,
    labels=top_sectors.index,
    autopct="%1.1f%%",
    startangle=90
)

centre_circle = plt.Circle(
    (0,0),
    0.70,
    fc="white"
)

fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sector Allocation Across Equity Funds")

plt.tight_layout()

plt.savefig(
    "sector_allocation_donut.png",
    dpi=300
)

plt.show()

print("Sector allocation donut chart saved successfully.")