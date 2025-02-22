from IPython.display import Image
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    pass

class MyNode:
    def __call__(self, state: State) -> State:
        return state

def build_ascii_graph(execution_flow, entry_points):
        
    for entry_point in entry_points:
        # Initialize the graph builder with a state
        builder = StateGraph(State)

        added_nodes = set()  # Keep track of added nodes to avoid duplicates

        for func, calls in execution_flow.items():
            # Add the current function node if not already added
            if func not in added_nodes:
                builder.add_node(func, MyNode)
                added_nodes.add(func)
            
            # Add edges for each function call
            for call in calls:
                if call not in added_nodes:  # Ensure the called function is also added as a node
                    builder.add_node(call, MyNode)
                    added_nodes.add(call)
                builder.add_edge(func, call)

        # Add START point of the graph
        builder.add_edge(START, entry_point)  # Entry point is "main"

        # Compile the graph
        execution_graph = builder.compile()
        print("Execution Graph for : ", entry_point)
        print(execution_graph.get_graph().draw_ascii())
        print()
