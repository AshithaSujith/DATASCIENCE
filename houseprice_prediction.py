import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load dataset
data = pd.read_csv(r'C:\Users\pc44\Desktop\DATASCIENCE\House Price Prediction Dataset.csv')
print(data.head())
print(data.isnull().sum())

# 1. Drop ID (not useful)
data = data.drop(columns=['Id'])

# 2. Features and target
X = data.drop(columns=['Price'])   # all columns except Price
y = data['Price']                  # target column

# 3. Encode categorical columns (Location, Condition, Garage)
X = pd.get_dummies(X, drop_first=True)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)
