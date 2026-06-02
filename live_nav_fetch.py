import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    print("\nScheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    print("\nFirst 5 Records:")
    print(nav_df.head())

    nav_df.to_csv(
        "data/raw/HDFC_Top100_NAV.csv",
        index=False
    )

    print("\nCSV Saved Successfully!")

else:
    print("API unavailable. Try again later.")