import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file_path="C:\Users\pc44\Desktop\DATASCIENCE\50_startups_sample (6).csv"
data=pd.read_csv(file_path)
print("\n--- First 5 Rows ---")
print(data.head())
# Features and Target
X=data[['R&D Spend', 'Administration', 'Marketing Spend', 'State']]
y=data['Profit']
# One-hot encode State (drop='first' to avoid dummy trap)
ct=ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['State'])],
                     remainder='passthrough')
