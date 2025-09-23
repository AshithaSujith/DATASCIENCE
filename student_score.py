# Student Score Prediction using Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Step 1: Load dataset
df = pd.read_csv("student_scores.csv")   # make sure the CSV is in your folder
print("\n--- First 5 rows ---")
print(df.head())

# Step 2: Visualize raw data
plt.scatter(df["Hours"], df["Scores"], color="blue")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.title("Hours vs Scores")
plt.show()

# Step 3: Split data
X = df[["Hours"]]   # Features
y = df["Scores"]    # Target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate model
y_pred = model.predict(X_test)
print("\n--- Model Evaluation ---")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 6: Plot regression line
plt.scatter(X_train, y_train, color="blue", label="Training data")
plt.scatter(X_test, y_test, color="green", label="Test data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Best Fit Line")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.title("Regression Line - Student Score Prediction")
plt.legend()
plt.show()

# Step 7: Predict for a new student (corrected version using DataFrame)
hours = pd.DataFrame([[7]], columns=["Hours"])
predicted_score = model.predict(hours)
print(f"\nPredicted score for {hours['Hours'][0]} hours study = {predicted_score[0]:.2f}")

# Step 8: Save the trained model
joblib.dump(model, "student_score_model.pkl")
print("\n✅ Model saved as student_score_model.pkl")


