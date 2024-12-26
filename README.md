# Prediction and Optimization of Smart Dish-Specific Demand in Restaurants

This project aims to address the challenges of predicting restaurant dish demand and optimizing inventory management. By leveraging machine learning models and a user-friendly web application, restaurant managers can minimize waste and improve operational efficiency.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Datasets](#datasets)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Contributing](#contributing)

---

## Introduction
The project focuses on predicting weekly demand for individual dishes in restaurants and calculating the corresponding raw material requirements. It includes:
1. Developing machine learning models for dish demand prediction.
2. Translating predictions into raw material requirements.
3. Creating a Flask-based web application for seamless interaction.

---

## Features
- Machine learning-based weekly dish demand forecasting.
- Inventory optimization by calculating precise ingredient requirements.
- Time-series analysis to identify trends and seasonality.
- Interactive web interface for restaurant managers.

---

## Installation
### Prerequisites
- Python 3.7 or higher
- Flask framework
- Required Python libraries (see `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   https://github.com/sampathvenur/Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning.git
   cd Prediction-and-Optimization-of-Smart-Dish-Specific-Demand-in-Restaurants-using-Machine-Learning
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the app at `http://127.0.0.1:5000/`.

---

## Usage
1. Input dish details such as week, center ID, and pricing into the web interface.
2. The application predicts:
   - Weekly dish demand.
   - Required ingredient quantities.
3. Visualize actual vs. predicted demand trends.
4. Optimize inventory based on the predictions.

---

## Datasets
- **Sales Report Database**: [Kaggle](https://www.kaggle.com/datasets/shivashi11/food-demand-prediction)
- **Dish Ingredient Database**: [RecipeDB](https://cosylab.iiitd.edu.in/recipedb/)
- **Cooking Measurement Conversion**:  
   - [Aqua-Calc](https://www.aqua-calc.com/calculate/food-volume-to-weight)
   - [The Calculator Site](https://www.thecalculatorsite.com/cooking/cooking-calculator.php)

---

## Technologies Used
- **Languages & Frameworks**: Python, Flask
- **Libraries**: 
  - Data processing: `pandas`, `numpy`
  - Machine learning: `scikit-learn`, `joblib`, `statsmodels`
  - Web scraping: `BeautifulSoup`, `requests`
  - Visualization: `matplotlib`
- **Models**:
  - Gradient Boosting Regressor
  - HistGradientBoosting Regressor
  - Random Forest Regressor

---

## Results
- **Gradient Boosting Regressor**:
  - R²: 99.86%
  - MAE: 8.58
  - MSE: 181.33
  - RMSE: 13.47
- **HistGradientBoosting Regressor**:
  - R²: 96.96%
  - MAE: 9.76
  - MSE: 4062.44
  - RMSE: 63.74
- **Random Forest Regressor**:
  - R²: 96.55%
  - MAE: 47.92
  - MSE: 4657.64
  - RMSE: 68.25

---

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

