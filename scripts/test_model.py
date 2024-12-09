import pandas as pd
import joblib

# Paths to files
model_path = "D:/mini project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/models/random_forest_model.pkl"
test_data_path = "D:/mini project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/data/test_replicated_with_dates.csv"
output_predictions_path = "D:/mini project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/results/test_predictions.csv"

# Load the trained model
loaded_model = joblib.load(model_path)
print("Model loaded successfully.")

# Load the test data
test_data = pd.read_csv(test_data_path)
print(f"Test data loaded with {len(test_data)} rows.")

# Prepare test features
X_test = test_data.drop(columns=["id", "date"])  # Exclude ID and date

# Make predictions
test_data["predicted_num_orders"] = loaded_model.predict(X_test)
print("Predictions completed.")

# Save the predictions
test_data[["id", "date", "predicted_num_orders"]].to_csv(output_predictions_path, index=False)
print(f"Predictions saved to {output_predictions_path}")