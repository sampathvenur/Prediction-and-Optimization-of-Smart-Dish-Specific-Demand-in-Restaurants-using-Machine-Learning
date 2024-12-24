import React, { useState } from 'react';
import PredictionForm from './components/PredictionForm';
import ResultsVisualization from './components/ResultsVisualization';

function App() {
  const [prediction, setPrediction] = useState(null);

  const handlePrediction = (pred) => {
    setPrediction(pred);
  };

  return (
    <div className="App">
      <h1>Zomato Demand Predictor</h1>
      <PredictionForm onPrediction={handlePrediction} />
      {prediction && <ResultsVisualization prediction={prediction} />}
    </div>
  );
}

export default App;