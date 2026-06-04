import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv"
)


df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
plt.figure(figsize=(15,7))

sns.barplot(
    data=df,
    x="fund_house",
    y="aum_crore",
    hue="year"
)

plt.title("AUM Growth by Fund House (2022–2025)")
plt.xlabel("Fund House")
plt.ylabel("AUM (₹ Crore)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("aum_growth.png", dpi=300)
plt.annotate(
    "SBI Dominates\n₹12.5 Lakh Cr",
    xy=(0.3, 1250000),
    xytext=(1.5, 1100000),
    arrowprops=dict(arrowstyle="->")
)
plt.show()

print("Chart saved as aum_growth.png")