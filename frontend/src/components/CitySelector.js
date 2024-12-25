import React, { useState } from 'react';
import { Checkbox, FormControlLabel, FormGroup } from '@material-ui/core';

const CitySelector = ({ onChange, cities }) => {
  const [selectedCities, setSelectedCities] = useState({});

  const handleCityChange = (event) => {
    const { name, checked } = event.target;
    setSelectedCities(prevState => ({
      ...prevState,
      [name]: checked
    }));
    onChange({ [name]: checked ? 1 : 0 }); // Convert to 1 or 0 for backend
  };

  return (
    <FormGroup>
      {cities.map(city => (
        <FormControlLabel
          key={city}
          control={
            <Checkbox
              checked={!!selectedCities[city]}
              onChange={handleCityChange}
              name={city}
              color="primary"
            />
          }
          label={city.replace('City_', '')} // Clean up display name if needed
        />
      ))}
    </FormGroup>
  );
};

// Example usage in PredictionForm.js
// const cities = ['City_New Delhi', 'City_Mumbai', 'City_Bangalore']; // Define your cities here

export default CitySelector;