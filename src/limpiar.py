import pandas as pd
import numpy as np


# Function to clean data
def clean_data(df):
    df = df.drop_duplicates()
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].mean())
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

# Function to remove outliers using Z-score
def remove_outliers(df, z_thresh=3):
    numeric_cols = df.select_dtypes(include=np.number).columns
    z_scores = np.abs((df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std())
    df = df[(z_scores < z_thresh).all(axis=1)]
    return df

# Function to remove outliers using IQR
def remove_outliers_iqr(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    Q1 = df[numeric_cols].quantile(0.25)
    Q3 = df[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) | (df[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df