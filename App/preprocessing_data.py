import numpy as np
import pandas as pd
from sklearn.utils import resample
import matplotlib.pyplot as plt
import seaborn as sns
def check_null(df):
    is_null= df.isnull().sum()
    return pd.DataFrame([is_null.index, is_null.values])
def check_num_unique(df):
    return pd.DataFrame([df.nunique().index,df.nunique().values])
def handle_null(df,option,default_value):
    if option=="MODE (thay null bằng giá trị xuất hiện nhiều nhất trong cột đó)":
        for c in df.columns:
            df[c]= df[c].fillna(df[c].mode()[0]) 
        return df
    elif option=="DROP (loại bỏ null)":
        return df.dropna()
    else:
        return df.fillna(default_value)