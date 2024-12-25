import React, { useState } from 'react';
import { TextField, Button, Select, MenuItem } from '@material-ui/core';
import CitySelector from './CitySelector';
import apiService from '../services/apiService';

const PredictionForm = ({ onPrediction }) => {
  const [formData, setFormData] = useState({
    'Average Cost for two': '',
    'Price range': '',
    'Aggregate rating': '',
    'Num_Cuisines': '',
    'Cuisine_Group': ''
  });

  // Define your cities here. Ensure they match the backend feature names
  const cities = ['City_New Delhi', 'City_Mumbai', 'City_Bangalore']; // Add more cities as needed

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Here you might want to spread formData and then add your city selections
      const dataToSend = { ...formData, ...cities.reduce((acc, city) => ({ ...acc, [city]: formData[city] || 0 }), {}) };
      const response = await apiService.predict(dataToSend);
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

  const handleCityChange = (cityData) => {
    setFormData(prevState => ({ 
      ...prevState, 
      ...cityData 
    }));
  };

  return (
    <form onSubmit={handleSubmit}>
      {['Average Cost for two', 'Price range', 'Aggregate rating', 'Num_Cuisines'].map(key => (
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
      <CitySelector onChange={handleCityChange} cities={cities} />
      <Select
        name="Cuisine_Group"
        value={formData['Cuisine_Group']}
        onChange={handleChange}
        fullWidth
        margin="normal"
      >
        <MenuItem value="">Select Cuisine</MenuItem>
        <MenuItem value="Indian">Indian</MenuItem>
        <MenuItem value="Italian">Italian</MenuItem>
        <MenuItem value="Asian">Asian</MenuItem>
        <MenuItem value="Mexican">Mexican</MenuItem>
        <MenuItem value="Others">Others</MenuItem>
      </Select>
      <Button type="submit" variant="contained" color="primary">Predict</Button>
    </form>
  );
};

export default PredictionForm;