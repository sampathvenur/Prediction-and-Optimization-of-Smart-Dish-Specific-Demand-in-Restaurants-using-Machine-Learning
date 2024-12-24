import React from 'react';

const ResultsVisualization = ({ prediction }) => {
  return (
    <div>
      <h2>Prediction Result</h2>
      <p>Estimated Votes: {prediction.toFixed(2)}</p>
      {/* Here you could add a chart or other visualization */}
    </div>
  );
};

export default ResultsVisualization;