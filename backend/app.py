from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)
CORS(app)

# Global variables for model and features
model = None
all_features = None

def load_model_and_features():
    global model, all_features
    try:
        # Load the model
        model_path = os.path.join('models', 'zomato_demand_model.keras')
        model = load_model(model_path)
        print("Model loaded successfully.")

        # Load feature names
        features_path = os.path.join('models', 'features.txt')
        if os.path.exists(features_path):
            with open(features_path, 'r') as f:
                all_features = [line.strip() for line in f]
        else:
            raise FileNotFoundError("Features file not found. Make sure 'features.txt' exists in the 'models' directory.")
        
        print(f"Loaded {len(all_features)} features.")
    except Exception as e:
        print(f"Error loading model or features: {e}")
        # In a production environment, you might want to exit or serve an error page here
        raise

# Load model and features when the app starts
try:
    load_model_and_features()
except Exception as e:
    print(f"Failed to start application: {e}")
    import sys
    sys.exit(1)

def preprocess_data(data):
    if all_features is None:
        raise ValueError("Feature list not loaded. Ensure setup() has run.")

    # Create a dictionary with all features set to 0
    feature_dict = {feature: 0 for feature in all_features}
    
    # Update with provided data
    for key, value in data.items():
        if key in feature_dict:
            # Convert to float or int based on what's expected by the model
            try:
                feature_dict[key] = float(value)
            except ValueError:
                feature_dict[key] = 0  # Default to 0 if conversion fails
        else:
            print(f"Warning: Feature '{key}' not recognized, ignoring.")

    # Create DataFrame with all features
    df = pd.DataFrame([feature_dict], columns=all_features)
    
    # Ensure all data is of the correct type (float32 is common for TensorFlow models)
    df = df.astype('float32')
    
    return df.values  # Return as numpy array for prediction

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        processed_data = preprocess_data(data)
        prediction = model.predict(processed_data)
        predicted_votes = prediction[0][0]

        return jsonify({"predicted_votes": predicted_votes}), 200

    except Exception as e:
        app.logger.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request. Please try again."}), 500

@app.route('/')
def home():
    return "Welcome to the Zomato Demand Predictor API"

if __name__ == '__main__':
    app.run(debug=True)