
import pandas as pd


def clean_gdp_data(df):
    df = df[["Country Name", "Country Code", "Year", "Value"]].copy()

    df = df.rename(columns={
        "Country Name": "Country",
        "Country Code": "Code",
        "Value": "GDP"
    })

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["GDP"] = pd.to_numeric(df["GDP"], errors="coerce")

    df = df.dropna(subset=["Country", "Year", "GDP"])

    df = df[df["Year"].between(2000, 2022)]

    df["Year"] = df["Year"].astype(int)

    df = df.sort_values(["Country", "Year"]).reset_index(drop=True)

    return df
