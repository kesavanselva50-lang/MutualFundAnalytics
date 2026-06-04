import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

sip_df = df[
    df["transaction_type"] == "Sip"
]

plt.figure(figsize=(10,6))

sns.boxplot(
    data=sip_df,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount Distribution by Age Group")

plt.xlabel("Age Group")
plt.ylabel("SIP Amount (₹)")

plt.savefig(
    "reports/sip_boxplot_agegroup.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()