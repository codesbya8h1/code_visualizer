from langchain.prompts import PromptTemplate

# Create a prompt template
CODE_GRAPH_PROMPT = PromptTemplate(input_variables=["code_contents"],
                                   template="""
                       Analyze the following Python code and generate a graph representation.
                       Include nodes for classes, functions, and important variables.
                       Include edges for function calls, class inheritance, and variable usage.
                       Return the result as a list of tuples: (node1, node2, relationship).

                       Code:
                       {code_contents}
                       """)
