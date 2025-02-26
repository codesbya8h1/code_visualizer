
import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (!files) return;

    setLoading(true);
    const formData = new FormData();
    
    for (let i = 0; i < files.length; i++) {
      formData.append('files', files[i]);
    }

    try {
      const response = await axios.post('http://0.0.0.0:8000/analyze/folder', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult(response.data.graph);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error analyzing files');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Code Visualizer</h1>
      <div className="upload-section">
        <input
          type="file"
          onChange={handleFileUpload}
          multiple
          accept=".py"
          id="file-upload"
        />
        <label htmlFor="file-upload" className="upload-button">
          Select Python Files
        </label>
      </div>
      
      {loading && <div className="loading">Analyzing files...</div>}
      
      {result && (
        <div className="result">
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
