import pandas as pd
import numpy as np

#Data Loading step, checks statistics and structure of the data
df=pd.read_csv("Industrial_Innovation_Tracker_Merged.csv")
print(df.head())
print(df.info())
print(df.describe())

#Data Transformation step, log transformation of patent applications
df['Log_Patents']=np.log1p(df['Patent_Applications'])
print(df[['Patent_Applications','Log_Patents']].head())

