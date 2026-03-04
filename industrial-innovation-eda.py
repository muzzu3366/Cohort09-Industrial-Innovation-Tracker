import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
def load_data(file_path="Industrial_Innovation_Tracker_Merged.csv"):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully\n")
    print(df.head())
    return df

#EDA + Correlation
def perform_eda(df):

    print("\nDataset Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    numeric_df = df.select_dtypes(include=['number'])

    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()