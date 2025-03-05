from langchain_core.prompts import ChatPromptTemplate

PROMPT_CODE_GRAPH = ChatPromptTemplate.from_template(
        """You are a code analysis assistant. Given a piece of source code, create a graph representation where each node is a method or class, and the connecting nodes are the methods it calls. 
        Your response should be a list of dictionaries, where each dictionary uses the node name as the key and a list of connected methods as the value.
        Exclude any programming language related reserved methods or keywords.

        Here are two examples:

        Example 1:
        Input:

        python
        def main():
            data = fetch_data()
            processed = process_data(data)
            display_results(processed)

        def fetch_data():
            return [1, 2, 3, 4, 5]

        def process_data(data):
            return [x * 2 for x in data]

        def display_results(results):
            print(results)
        
        Output:

        [{{"main": ["fetch_data", "process_data", "display_results"]}},{{"fetch_data": []}},{{"process_data": []}},]

        Now, analyze the provided code and generate a comprehensive graph representation following this format. Focus on capturing the relationships between methods and classes, showing how they interact within the codebase. 
        Your final output should be a list of dictionaries, where each dictionary represents a node (method or class) as the key and its connections as a list value.
                "Code Content: {code_content}"
                "Response:"
    """)