import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('data/MachineLearningRating_v3.txt', sep='|', low_memory=False)
df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')

# Select and preprocess features
features = ['TotalPremium', 'Province', 'VehicleType', 'RegistrationYear']
target = 'TotalClaims'

# Handle categorical variables with one-hot encoding
df = df[features + [target]].dropna()
df = pd.get_dummies(df, columns=['Province', 'VehicleType'])

# Define features and target
X = df.drop(target, axis=1)
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split for modeling:", X_train.shape, X_test.shape)

# Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)
print(f"Linear Regression Mean Squared Error: {mse_lr}")

# Feature importance for Linear Regression
feature_importance_lr = pd.DataFrame({'Feature': X.columns, 'Coefficient': lr_model.coef_})
print("Linear Regression Feature Importance:\n", feature_importance_lr.sort_values(by='Coefficient', ascending=False))

# Random Forest Model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
print(f"Random Forest Mean Squared Error: {mse_rf}")

# Feature importance for Random Forest
feature_importance_rf = pd.DataFrame({'Feature': X.columns, 'Importance': rf_model.feature_importances_})
print("Random Forest Feature Importance:\n", feature_importance_rf.sort_values(by='Importance', ascending=False))