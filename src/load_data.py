import pandas as pd
def load_gdp_data(filepath="data/gdp_raw.csv"):
    df = pd.read_csv(filepath, skiprows=4)
    return df
