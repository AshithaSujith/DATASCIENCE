import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df=pd.read_csv("car.data", names=columns)
print(df.head())
print(df.isnull().sum())
le=LabelEncoder()
for col in df.columns:
    df[col]=le.fit_transform(df[col])
print(df.head())
X = df.drop("class", axis=1)
y = df["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))



