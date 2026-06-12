import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

datasets = {
    "fund_master": "01_fund_master_cleaned.csv",
    "nav_history": "02_nav_history_cleaned.csv",
    "aum_by_fund_house": "03_aum_by_fund_house_cleaned.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows_cleaned.csv",
    "category_inflows": "05_category_inflows_cleaned.csv",
    "industry_folio_count": "06_industry_folio_count_cleaned.csv",
    "scheme_performance": "07_scheme_performance_cleaned.csv",
    "investor_transactions": "08_investor_transactions_cleaned.csv",
    "portfolio_holdings": "09_portfolio_holdings_cleaned.csv",
    "benchmark_indices": "10_benchmark_indices_cleaned.csv"
}

for table_name, file_name in datasets.items():
    df = pd.read_csv(f"data/processed/{file_name}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded")

print("\nAll 10 datasets loaded successfully!")