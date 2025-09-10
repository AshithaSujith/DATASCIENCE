import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

data=load_breast_cancer()
df=pd.DataFrame (data.data, columns=data.feature_names)
df["target"]=data.target
df_small=df[["mean radius","mean texture","mean perimeter","mean area","mean smoothness","target"]]