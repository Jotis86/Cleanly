import pandas as pd
import numpy as np


# Function to clean data
def clean_data(df):
    df = df.copy()  # Crear una copia explícita para evitar warnings
    df = df.drop_duplicates()
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].mean())
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

# Function to remove outliers using Z-score
def remove_outliers(df, z_thresh=3):
    df = df.copy()
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    # Usar mediana y MAD (Median Absolute Deviation) en lugar de media y std
    # MAD es más robusto a outliers extremos
    median = df[numeric_cols].median()
    mad = np.median(np.abs(df[numeric_cols] - median), axis=0)
    
    # Evitar división por cero
    mad = np.where(mad == 0, 1e-8, mad)
    
    # Calcular z-scores modificados (basados en MAD)
    z_scores = 0.6745 * np.abs(df[numeric_cols] - median) / mad
    
    # Filtrar filas
    df = df[~(z_scores > z_thresh).any(axis=1)]
    return df

# Function to remove outliers using IQR
def remove_outliers_iqr(df):
    df = df.copy()  # Crear una copia explícita para evitar warnings
    numeric_cols = df.select_dtypes(include=np.number).columns
    Q1 = df[numeric_cols].quantile(0.25)
    Q3 = df[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) | (df[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df