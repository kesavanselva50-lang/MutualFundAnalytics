import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(
    "data/processed/06_industry_folio_count_cleaned.csv"
)

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o",
    linewidth=2
)

plt.title("Mutual Fund Folio Growth (2022–2025)")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")

# First point annotation
plt.annotate(
    f"{df.iloc[0]['total_folios_crore']} Cr",
    xy=(df.iloc[0]["month"], df.iloc[0]["total_folios_crore"]),
    xytext=(20, 10),
    textcoords="offset points"
)

# Last point annotation
plt.annotate(
    f"{df.iloc[-1]['total_folios_crore']} Cr",
    xy=(df.iloc[-1]["month"], df.iloc[-1]["total_folios_crore"]),
    xytext=(-60, 10),
    textcoords="offset points"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "folio_growth.png",
    dpi=300
)

plt.show()

print("Folio growth chart saved successfully.")