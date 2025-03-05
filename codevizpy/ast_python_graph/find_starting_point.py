def find_starting_point(execution_flow):
    """
    Find the starting point of the execution flow graph.

    Args:
        execution_flow (dict): A dictionary representing the execution flow graph.
                               Keys are functions, and values are lists of functions they call.

    Returns:
        str: The starting point of the graph.
    """
    # Step 1: Collect all nodes (functions)
    all_nodes = set(execution_flow.keys())  # Functions defined in the graph
    called_nodes = set()  # Functions that are called by other functions

    for calls in execution_flow.values():
        called_nodes.update(calls)

    # Step 2: Find nodes that are in `all_nodes` but not in `called_nodes`
    starting_points = all_nodes - called_nodes

    # Step 3: Return the starting point (there should be only one in a valid execution flow)
    if len(starting_points):
        return list(starting_points)
    else:
        raise ValueError("No starting point found in the execution flow.")
