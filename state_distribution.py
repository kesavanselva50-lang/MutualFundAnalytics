import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

state_amt = (
    df.groupby("state")["amount_inr"]
      .sum()
      .sort_values()
)

plt.figure(figsize=(10,8))

state_amt.plot(kind="barh")

plt.title("Investment Amount by State")

plt.xlabel("Amount (₹)")
plt.ylabel("State")

plt.savefig(
    "reports/state_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()