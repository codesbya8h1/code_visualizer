from openai import OpenAI


def generate_graph_from_code(code_contents):
    prompt = f"""
  Analyze the following Python code and generate a graph representation.
  Include nodes for classes, functions, and important variables.
  Include edges for function calls, class inheritance, and variable usage.
  Return the result as a list of tuples: (node1, node2, relationship).

  Code:
  {code_contents}
  """

    response = OpenAI.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            "system",
            "content":
            "You are a code analysis assistant that generates graph representations of code."
        }, {
            "role": "user",
            "content": prompt
        }])

    # Parse the response to extract the graph edges
    graph_edges = eval(response.choices[0].message['content'])
    return graph_edges
