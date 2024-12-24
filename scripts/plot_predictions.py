import pandas as pd
import matplotlib.pyplot as plt

# Path to predictions file
test_predictions_path = "D:/mini project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/results/test_predictions.csv"

# Load predictions
predictions_data = pd.read_csv(test_predictions_path)

# Sort data by date for sequential plotting
predictions_data["date"] = pd.to_datetime(predictions_data["date"])
predictions_data.sort_values(by="date", inplace=True)

# Create a proxy for actual orders (simulating actual orders by adding slight noise)
# Here, we're using predicted values as actual orders for demonstration
# You can replace this logic once you have the actual orders data
predictions_data["actual_num_orders"] = predictions_data["predicted_num_orders"] * 0.9 + 10  # Simulated actual orders

# Plot the actual vs predicted orders as line graph
plt.figure(figsize=(12, 6))
plt.plot(predictions_data["date"], predictions_data["actual_num_orders"], label="Actual Orders", color="blue", linewidth=2)
plt.plot(predictions_data["date"], predictions_data["predicted_num_orders"], label="Predicted Orders", color="orange", linewidth=2)

# Adding labels and title
plt.title("Actual vs Predicted Orders Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Orders", fontsize=12)
plt.legend(loc='upper left')
plt.grid(True)  # Optional: Adds grid lines for better readability
plt.tight_layout()

# Show the plot
plt.show()