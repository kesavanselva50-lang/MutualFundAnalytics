Mutual Fund Analytics - Data Dictionary

01_fund_master

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique mutual fund code |
| fund_house | TEXT | Asset management company |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Regular or Direct plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio percentage |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP amount |
| min_lumpsum_amount | REAL | Minimum lump sum amount |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk classification |
| sebi_category_code | TEXT | SEBI category code |

---

02_nav_history

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

03_aum_by_fund_house

| Column | Type | Description |
|----------|----------|----------|
| date | DATE | Reporting date |
| fund_house | TEXT | Asset management company |
| aum_lakh_crore | REAL | AUM in lakh crore |
| aum_crore | REAL | AUM in crore |
| num_schemes | INTEGER | Number of schemes |

---

 04_monthly_sip_inflows

| Column | Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| sip_inflow_crore | REAL | SIP inflow amount |
| active_sip_accounts_crore | REAL | Active SIP accounts |
| new_sip_accounts_lakh | REAL | New SIP accounts |
| sip_aum_lakh_crore | REAL | SIP AUM |
| yoy_growth_pct | REAL | Year-over-year growth percentage |

---

05_category_inflows

| Column | Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| category | TEXT | Fund category |
| net_inflow_crore | REAL | Net inflow amount |

---

06_industry_folio_count

| Column | Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| total_folios_crore | REAL | Total folios |
| equity_folios_crore | REAL | Equity folios |
| debt_folios_crore | REAL | Debt folios |
| hybrid_folios_crore | REAL | Hybrid folios |
| others_folios_crore | REAL | Other folios |

---

07_scheme_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| return_1yr_pct | REAL | One-year return |
| return_3yr_pct | REAL | Three-year return |
| return_5yr_pct | REAL | Five-year return |
| expense_ratio_pct | REAL | Expense ratio |
| aum_crore | REAL | Assets under management |

---

08_investor_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | INTEGER | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Mutual fund code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |

---

09_portfolio_holdings

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund code |
| stock_symbol | TEXT | Stock symbol |
| stock_name | TEXT | Company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight percentage |
| market_value_cr | REAL | Market value in crore |
| current_price_inr | REAL | Current stock price |
| portfolio_date | DATE | Portfolio reporting date |

---

10_benchmark_indices

| Column | Type | Description |
|----------|----------|----------|
| date | DATE | Index date |
| index_name | TEXT | Benchmark index name |
| close_value | REAL | Closing index value |