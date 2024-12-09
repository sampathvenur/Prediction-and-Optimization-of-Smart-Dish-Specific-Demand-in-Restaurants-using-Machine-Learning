import pandas as pd
import numpy as np
import os
from datetime import timedelta

# Full paths to input and output datasets
input_file = "D:/sem 5/Mini Project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/data/test.csv"
output_file = "D:/sem 5/Mini Project/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning/data/test_replicated_with_dates.csv"

# Desired number of rows in the output dataset
desired_rows = 200000

def generate_dates(start_date, end_date, total_rows):
    """Generate continuous dates between start_date and end_date for the dataset."""
    date_range = pd.date_range(start=start_date, end=end_date)
    repeated_dates = np.tile(date_range, int(np.ceil(total_rows / len(date_range))))[:total_rows]
    return repeated_dates

def replicate_and_add_dates(input_path, output_path, target_rows):
    # Load the original dataset
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at {input_path}")
    
    original_data = pd.read_csv(input_path)
    print(f"Original dataset loaded with {len(original_data)} rows.")

    # Calculate replication factor
    replication_factor = -(-target_rows // len(original_data))  # Ceiling division
    print(f"Replication factor: {replication_factor}")

    # Replicate the data
    replicated_data = pd.concat([original_data] * replication_factor, ignore_index=True)
    replicated_data = replicated_data.iloc[:target_rows]  # Trim to the desired number of rows
    print(f"Replicated dataset now contains {len(replicated_data)} rows.")

    # Generate dates
    start_date = "2024-01-01"
    end_date = "2024-12-31"  # Full year of 2024
    dates = generate_dates(start_date, end_date, total_rows=target_rows)
    replicated_data["date"] = dates

    # Drop the week column and reorder columns
    if "week" in replicated_data.columns:
        replicated_data = replicated_data.drop(columns=["week"])
    columns = ["id", "date", "center_id", "meal_id", "checkout_price", "base_price",
               "emailer_for_promotion", "homepage_featured"]
    replicated_data = replicated_data[columns]

    # Save the replicated dataset
    replicated_data.to_csv(output_path, index=False)
    print(f"Replicated dataset with dates saved to {output_path}")

# Execute the replication
replicate_and_add_dates(input_file, output_file, desired_rows)