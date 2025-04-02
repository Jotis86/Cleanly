import pytest
import pandas as pd
import numpy as np
from src.limpiar import clean_data, remove_outliers, remove_outliers_iqr

def test_clean_data():
    # Create a sample DataFrame with missing values and duplicates
    data = {
        "A": [1, 2, 2, np.nan],
        "B": [np.nan, 2, 2, 3],
        "C": ["a", "b", "b", None]
    }
    df = pd.DataFrame(data)
    
    # Apply clean_data
    cleaned_df = clean_data(df)
    
    # Check duplicates are removed
    assert cleaned_df.duplicated().sum() == 0
    
    # Check missing values are handled
    assert cleaned_df["A"].isnull().sum() == 0
    assert cleaned_df["B"].isnull().sum() == 0
    assert cleaned_df["C"].isnull().sum() == 0

def test_remove_outliers():
    # Create a sample DataFrame with outliers
    data = {"A": [1, 2, 3, 1000], "B": [10, 20, 30, 1000]}
    df = pd.DataFrame(data)
    
    # Apply remove_outliers
    df_no_outliers = remove_outliers(df)
    
    # Check that the outlier row is removed
    assert len(df_no_outliers) < len(df)

def test_remove_outliers_iqr():
    # Create a sample DataFrame with outliers
    data = {"A": [1, 2, 3, 1000], "B": [10, 20, 30, 1000]}
    df = pd.DataFrame(data)
    
    # Apply remove_outliers_iqr
    df_no_outliers = remove_outliers_iqr(df)
    
    # Check that the outlier row is removed
    assert len(df_no_outliers) < len(df)