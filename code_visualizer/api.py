
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import tempfile
from pathlib import Path
from typing import List
import os
from ast_code_graph import get_file_execution_flow, get_project_execution_flow
from find_starting_point import find_starting_point
from ascii_visualization import build_ascii_graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/file")
async def analyze_file(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    
    try:
        execution_graph = get_file_execution_flow(tmp_path)
        entry_point = find_starting_point(execution_graph)
        graph_output = build_ascii_graph(execution_graph, entry_point)
        os.unlink(tmp_path)
        return {"graph": graph_output}
    except Exception as e:
        os.unlink(tmp_path)
        return {"error": str(e)}

@app.post("/analyze/folder")
async def analyze_folder(files: List[UploadFile] = File(...)):
    temp_dir = tempfile.mkdtemp()
    try:
        for file in files:
            if file.filename.endswith('.py'):
                file_path = Path(temp_dir) / file.filename
                with open(file_path, 'wb') as f:
                    shutil.copyfileobj(file.file, f)
        
        execution_graph = get_project_execution_flow(temp_dir)
        entry_point = find_starting_point(execution_graph)
        graph_output = build_ascii_graph(execution_graph, entry_point)
        shutil.rmtree(temp_dir)
        return {"graph": graph_output}
    except Exception as e:
        shutil.rmtree(temp_dir)
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
