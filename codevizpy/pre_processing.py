import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

def load_code_files(directory: str) -> List[Document]:
    documents = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.java', '.js', '.cpp')):  # Add more extensions as needed
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    documents.append(Document(page_content=content, metadata={"source": file_path}))
    return documents

def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)