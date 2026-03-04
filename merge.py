import pandas as pd

#to load a World Bank CSV and reshape it into a clean long format
def load_and_convert(file_path, value_name):
    # World Bank files include metadata at the top, so we skip those rows
    df = pd.read_csv(file_path, skiprows=4)

    # Keeping the country info plus columns that are actual years
    year_columns = [col for col in df.columns if col.isdigit()]
    df = df[['Country Name', 'Country Code'] + year_columns]

    # Convert from wide (one column per year) to long (one row per country-year)
    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name=value_name
    )

    # Store years as integers for easier filtering and merging
    df_long['Year'] = df_long['Year'].astype(int)

    return df_long

# Load each indicator file
rd_df = load_and_convert(
    'API_GB.XPD.RSDV.GD.ZS_DS2_en_csv_v2_38.csv',
    'R&D_Expenditure_%GDP'
)

researchers_df = load_and_convert(
    'API_SP.POP.SCIE.RD.P6_DS2_en_csv_v2_5802.csv',
    'Researchers_per_Million'
)

patents_df = load_and_convert(
    'API_IP.PAT.RESD_DS2_en_csv_v2_72.csv',
    'Patent_Applications'
)


# Merge all three datasets using country and year as keys
merged_df = rd_df.merge(
    researchers_df,
    on=['Country Name', 'Country Code', 'Year'],
    how='inner'
)

merged_df = merged_df.merge(
    patents_df,
    on=['Country Name', 'Country Code', 'Year'],
    how='inner'
)


# Drop incomplete rows and export the final combined dataset
merged_df = merged_df.dropna()

merged_df.to_csv('Industrial_Innovation_Tracker.csv', index=False)

print("Industrial_Innovation_Tracker.csv created successfully")

