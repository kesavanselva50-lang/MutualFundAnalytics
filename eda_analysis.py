import pandas as pd
import plotly.express as px


nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

fund_df = pd.read_csv(
    "data/processed/01_fund_master_cleaned.csv"
)

nav_df["date"] = pd.to_datetime(nav_df["date"])

df = nav_df.merge(
    fund_df[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

print(df.head())
fig = px.line(
    df,
    x="date",
    y="nav",
    color="scheme_name",
    title="NAV Trend Analysis (2022–2026)"
)
fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    fillcolor="green",
    opacity=0.12,
    line_width=0,
    annotation_text="2023 Bull Run"
)
fig.add_vrect(
    x0="2024-01-01",
    x1="2024-12-31",
    fillcolor="red",
    opacity=0.12,
    line_width=0,
    annotation_text="2024 Correction"
)

fig.show()
fig.write_html("nav_trend_analysis.html")

print("NAV chart saved successfully.")