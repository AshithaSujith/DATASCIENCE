import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\pc44\Desktop\DATASCIENCE\student_scores.csv')
print(data.head())
print(data.isnull().sum())

X=data[['Hours']]
y=data['Scores']

X=pd.get_dummies(X,drop_first=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("\n--- Model Evaluation ---")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))  
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))    

plt.figure(figsize=(10,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Actual vs Predicted Scores")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
plt.show()