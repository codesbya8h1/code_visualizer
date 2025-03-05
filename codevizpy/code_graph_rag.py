from pathlib import Path
from pre_processing import load_code_files
from pre_processing import split_documents
from chains.rag_chains import create_structured_code_graph_chain
from logger import setup_logger


logger = setup_logger()

def process_code_graph(chain, code_content: str) -> str:
    response = chain.invoke(input={"code_content": code_content})
    return response

def create_code_graph(code_path):
    # Load code files/folder
    logger.info("loading source code...")
    documents = load_code_files(code_path)
    logger.info("source code loaded...")
    logger.info(f"number of documents: {len(documents)}")
    
    # Split documents if needed
    logger.info("splitting the source code if needed...")
    split_docs = split_documents(documents)
    logger.info("splitting completed...")
    logger.info(f"number of splitts: {len(split_docs)}")
    
    # Create RAG chain
    logger.info("creating rag chain...")
    rag_chain = create_structured_code_graph_chain()
    logger.info("rag chain creation complete...")

    
    code_graph = []
    logger.info("processing each document...")
    for doc in split_docs:
        response = process_code_graph(rag_chain, doc.page_content)
        print(type(response))
        print("response :", response)
        code_graph.append(response)
    logger.info("document processing completed...")

    # create overall graph

    return code_graph

