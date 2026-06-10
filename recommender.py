import pandas as pd

df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

result = (
    df[df['risk_grade'] == risk]
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print(
    result[
        [
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]
)