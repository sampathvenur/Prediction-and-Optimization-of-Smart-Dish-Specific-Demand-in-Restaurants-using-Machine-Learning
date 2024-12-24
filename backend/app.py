from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from utils.preprocessing import preprocess_data

app = Flask(__name__)

CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        # Load the model inside the function for each request
        model = load_model('zomato_demand_model.keras')
        
        # Preprocess the data
        processed_data = preprocess_data(data)

        # Make prediction
        prediction = model.predict(processed_data)
        predicted_votes = prediction[0][0]  # Assuming single prediction

        return jsonify({"predicted_votes": predicted_votes}), 200

    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request. Please try again."}), 500

@app.route('/')
def home():
    return "Welcome to the Zomato Demand Predictor API"

if __name__ == '__main__':
    app.run(debug=True)