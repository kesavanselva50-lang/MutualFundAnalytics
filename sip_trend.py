import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv"
)

df["month"] = pd.to_datetime(df["month"])

fig = px.line(
    df,
    x="month",
    y="sip_inflow_crore",
    markers=True,
    title="Monthly SIP Inflows (2022–2025)"
)

max_row = df.loc[df["sip_inflow_crore"].idxmax()]

fig.add_annotation(
    x=max_row["month"],
    y=max_row["sip_inflow_crore"],
    text=f"Peak ₹{max_row['sip_inflow_crore']:,} Cr",
    showarrow=True,
    arrowhead=2
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="SIP Inflow (₹ Crore)"
)

fig.write_html("sip_inflow_trend.html")

fig.show()

print("SIP trend chart saved successfully.")