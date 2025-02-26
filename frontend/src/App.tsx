
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [files, setFiles] = useState<FileList | null>(null);
  const [graphs, setGraphs] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!files) return;

    setLoading(true);
    setError(null);
    
    const formData = new FormData();
    
    if (files.length === 1) {
      formData.append('file', files[0]);
      try {
        const response = await axios.post('http://localhost:8000/analyze/file', formData);
        setGraphs([response.data.graph]);
      } catch (err) {
        setError('Failed to analyze file');
      }
    } else {
      Array.from(files).forEach(file => {
        formData.append('files', file);
      });
      try {
        const response = await axios.post('http://localhost:8000/analyze/folder', formData);
        setGraphs([response.data.graph]);
      } catch (err) {
        setError('Failed to analyze folder');
      }
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Code Visualizer</h1>
      <form onSubmit={handleSubmit}>
        <div className="upload-box">
          <input
            type="file"
            multiple
            onChange={(e) => setFiles(e.target.files)}
            accept=".py"
          />
          <p>Drop Python files or folder here</p>
        </div>
        <button type="submit" disabled={!files || loading}>
          {loading ? 'Analyzing...' : 'Analyze Code'}
        </button>
      </form>
      
      {error && <div className="error">{error}</div>}
      
      {graphs.map((graph, index) => (
        <pre key={index} className="graph">
          {graph}
        </pre>
      ))}
    </div>
  );
}

export default App;
