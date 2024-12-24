import pandas as pd
import numpy as np

def preprocess_data(data):
    # Assuming 'data' has all expected features. Here we construct a DataFrame
    all_features = ['Average Cost for two', 'Price range', 'Aggregate rating', 'Num_Cuisines']
    # Add any one-hot encoded features your model expects here, e.g., 'City_New Delhi', 'Cuisine_Group_Indian'
    
    # Create a DataFrame with zeros for all features
    df = pd.DataFrame(np.zeros((1, len(all_features))), columns=all_features)

    # Fill in the data provided by the user
    for key, value in data.items():
        if key in df.columns:
            df[key] = value

    # This is where you'd add any additional preprocessing steps like scaling or one-hot encoding
    # For example:
    # df['Average Cost for two'] = (df['Average Cost for two'] - mean) / std  # If you scaled this feature during training
    
    # Ensure the DataFrame has the correct shape and features for your model
    return df.values  # Return as numpy array for prediction