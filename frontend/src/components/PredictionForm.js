import React, { useState } from 'react';
import { TextField, Button } from '@material-ui/core';
import apiService from '../services/apiService';

const PredictionForm = ({ onPrediction }) => {
  const [formData, setFormData] = useState({
    'Average Cost for two': '',
    'Price range': '',
    'Aggregate rating': '',
    'Num_Cuisines': ''
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await apiService.predict(formData);
      onPrediction(response.predicted_votes);
    } catch (error) {
      console.error("Error making prediction:", error);
      alert('Failed to fetch prediction. Please try again.');
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(formData).map(key => (
        <TextField
          key={key}
          name={key}
          label={key}
          value={formData[key]}
          onChange={handleChange}
          type="number"
          margin="normal"
          fullWidth
        />
      ))}
      <Button type="submit" variant="contained" color="primary">Predict</Button>
    </form>
  );
};

export default PredictionForm;