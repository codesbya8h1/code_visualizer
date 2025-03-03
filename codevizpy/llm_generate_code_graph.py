from llm.llm_preset import openai_llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

CODE_GRAPH_PROMPT = """
   Analyze the following Python code and generate a graph representation.
   Include nodes for classes, functions, and important variables.
   Include edges for function calls, class inheritance, and variable usage.
   Return the result as a list of tuples: (node1, node2, relationship).

   Code:
   {code_contents}
   """


def generate_graph_from_code(code_contents):
    # Create a prompt template from the CODE_GRAPH_PROMPT string
    prompt_template = PromptTemplate(input_variables=["code_contents"],
                                     template=CODE_GRAPH_PROMPT)
    # Create an LLM chain
    chain = LLMChain(llm=openai_llm, prompt=prompt_template)

    # Run the chain
    result = chain.run(code_contents)
    print(result)
    return result

    # response = OpenAI.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{
    #         "role":
    #         "system",
    #         "content":
    #         "You are a code analysis assistant that generates graph representations of code."
    #     }, {
    #         "role": "user",
    #         "content": CODE_GRAPH_PROMPT
    #     }])

    # # Parse the response to extract the graph edges
    # graph_edges = eval(response.choices[0].message['content'])
    # return graph_edges
