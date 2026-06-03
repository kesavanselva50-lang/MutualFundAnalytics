import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("Starting data cleaning...")


fund = pd.read_csv("data/raw/01_fund_master.csv")

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund = fund.drop_duplicates()

fund.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("01_fund_master cleaned")


nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("02_nav_history cleaned")


aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(aum["date"])

aum = aum.drop_duplicates()

aum = aum[aum["aum_crore"] > 0]

aum.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("03_aum_by_fund_house cleaned")


sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

sip = sip.drop_duplicates()

sip.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("04_monthly_sip_inflows cleaned")


cat = pd.read_csv("data/raw/05_category_inflows.csv")

cat = cat.drop_duplicates()

cat.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)

print("05_category_inflows cleaned")


folio = pd.read_csv("data/raw/06_industry_folio_count.csv")

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)

print("06_industry_folio_count cleaned")


perf = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.drop_duplicates()

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    & (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("07_scheme_performance cleaned")


txn = pd.read_csv("data/raw/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]
txn = txn[txn["transaction_type"].isin(valid_types)]

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]
txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("08_investor_transactions cleaned")


hold = pd.read_csv("data/raw/09_portfolio_holdings.csv")

hold["portfolio_date"] = pd.to_datetime(
    hold["portfolio_date"]
)

hold = hold[hold["weight_pct"] >= 0]

hold = hold.drop_duplicates()

hold.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("09_portfolio_holdings cleaned")


bench = pd.read_csv("data/raw/10_benchmark_indices.csv")

bench["date"] = pd.to_datetime(
    bench["date"]
)

bench = bench.drop_duplicates()

bench.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)

print("10_benchmark_indices cleaned")

print("\nAll 10 datasets cleaned successfully!")