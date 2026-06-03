-- 1. Top 5 funds by highest NAV
SELECT amfi_code, MAX(nav) AS max_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY max_nav DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- 3. Transaction count by type
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- 4. Transactions by state
SELECT state,
       COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio below 1%
SELECT scheme_name,
       expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 5 performing funds by 5-year return
SELECT scheme_name,
       return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Top fund houses by AUM
SELECT fund_house,
       MAX(aum_crore) AS max_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;

-- 8. Category with highest inflows
SELECT category,
       SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

-- 9. Top 10 portfolio holdings by weight
SELECT stock_name,
       weight_pct
FROM portfolio_holdings
ORDER BY weight_pct DESC
LIMIT 10;

-- 10. Highest benchmark index values
SELECT index_name,
       MAX(close_value) AS highest_close
FROM benchmark_indices
GROUP BY index_name
ORDER BY highest_close DESC;