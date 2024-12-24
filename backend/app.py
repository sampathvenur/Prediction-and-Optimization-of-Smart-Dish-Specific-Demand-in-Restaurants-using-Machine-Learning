from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from utils.preprocessing import preprocess_data

app = Flask(__name__)

# Load the model once at startup
model = load_model('models/zomato_demand_model.keras')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        # Preprocess the data
        processed_data = preprocess_data(data)

        # Make prediction
        prediction = model.predict(processed_data)
        predicted_votes = prediction[0][0]  # Assuming single prediction

        return jsonify({"predicted_votes": predicted_votes}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)