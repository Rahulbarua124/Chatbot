
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState('');

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('image', image);
    const res = await axios.post('http://localhost:5000/predict', formData);
    setResult(res.data.prediction);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>🌱 FASAL: Crop Health Checker</h1>
      <input type="file" onChange={e => setImage(e.target.files[0])} />
      <br /><br />
      <button onClick={handleUpload}>Detect</button>
      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;
