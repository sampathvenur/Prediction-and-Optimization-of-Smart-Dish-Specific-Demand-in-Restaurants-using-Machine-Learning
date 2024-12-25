def preprocess_data(data):
    if all_features is None:
        raise ValueError("Feature list not loaded. Ensure setup() has run.")

    feature_dict = {feature: 0 for feature in all_features[:446]}
    
    for key, value in data.items():
        if key in feature_dict:
            try:
                feature_dict[key] = float(value)
            except ValueError:
                feature_dict[key] = 0  # Default to 0 if conversion fails
        else:
            print(f"Warning: Feature '{key}' not recognized, ignoring.")

    df = pd.DataFrame([feature_dict], columns=all_features[:446])
    
    df = df.astype('float32')
    
    return df.values  # Return as numpy array for prediction