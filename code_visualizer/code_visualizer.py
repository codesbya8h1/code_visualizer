import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain.prompts import ChatPromptTemplate
from response_model import json_schema
from visualizer import visualize_code_flow

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"

# Load the Python code file
loader = TextLoader("/Users/a8h1/coding/code_visualizer/code_visualizer/test_src_code.py")
documents = loader.load()

# Initialize the chat model
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Define the prompt template
prompt = ChatPromptTemplate.from_template("""
Analyze the following Python code:

{code}

Create a dictionary called 'code_graph' where:
- Each key is a method name, if it's a class method, use the format 'ClassName.method_name'
- Each value is a list of methods directly called by that method

Also identify the entry point of the code.

Format your response as a Python dictionary with two keys:
1. 'code_entry': The entry point method or class name
2. 'code_graph': The dictionary of method calls

Include all methods in 'code_graph', even if they don't call any other methods (use an empty list in such cases).
""")

code = documents[0].page_content

# Create the chain
chain = prompt | model.with_structured_output(json_schema)

# Invoke the chain
result = chain.invoke({"code": code})

print(result)
visualize_code_flow(result)

