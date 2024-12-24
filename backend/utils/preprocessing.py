all_features = ['Average Cost for two', 'Price range', 'Aggregate rating', 'Num_Cuisines', 
                'City_A', 'City_B', 'City_C', ...]  # Add all 150 features here

def preprocess_data(data):
    # ... (rest of the function remains the same)

import pandas as pd
import numpy as np

with open('models/features.txt', 'r') as f:
    all_features = [line.strip() for line in f]

def preprocess_data(data):
    feature_dict = {feature: 0 for feature in all_features}  # Default all to 0
    
    # Update with provided data
    for key, value in data.items():
        if key in feature_dict:
            feature_dict[key] = value

    # Create DataFrame with all features
    df = pd.DataFrame([feature_dict])
    
    # Ensure all data is numeric
    df = df.astype('float32')
    
    # If your model expects a specific shape, reshape here if necessary
    return df.values  # Return as numpy array for prediction