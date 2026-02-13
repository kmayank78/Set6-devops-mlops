import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("data/data.csv")

X = df[["sqft", "bedrooms", "bathrooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
predictions = model.predict(X)
mae = mean_absolute_error(y, predictions)

# MLflow tracking
mlflow.start_run()
mlflow.log_metric("MAE", mae)
mlflow.log_metric("rows", len(df))
mlflow.sklearn.log_model(model, "model")
mlflow.end_run()

print("MLflow logging done")

