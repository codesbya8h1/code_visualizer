import networkx as nx
from collections import namedtuple
import streamlit as st
from streamlit_react_flow import react_flow

# Define the CodeGraphResponse namedtuple
CodeGraphResponse = namedtuple('CodeGraphResponse', ['name', 'connections'])

# Sample data
code_graph_responses = [
    CodeGraphResponse(name='process_data', connections=['count_vowels']),
    CodeGraphResponse(name='display_result', connections=[]),
    CodeGraphResponse(name='main', connections=['greet_user', 'process_data', 'display_result']),
    CodeGraphResponse(name='greet_user', connections=['capitalize_words']),
    CodeGraphResponse(name='capitalize_words', connections=['str.split', 'str.join'])
]

def build_graph(responses):
    G = nx.DiGraph()
    
    # Add all nodes and direct edges
    for response in responses:
        G.add_node(response.name)
        for conn in response.connections:
            G.add_edge(response.name, conn)
    
    # Find indirect connections
    for response in responses:
        for conn in response.connections:
            if conn in G.nodes():
                descendants = nx.descendants(G, conn)
                for descendant in descendants:
                    G.add_edge(response.name, descendant)
    
    return G

def find_root_nodes(G):
    return [node for node in G.nodes() if G.in_degree(node) == 0]

def create_tree_layout(G):
    def dfs_layout(node, x, y, level_width, node_spacing):
        nonlocal current_x
        children = list(G.successors(node))
        if not children:
            node_positions[node] = {"x": current_x, "y": y}
            current_x += node_spacing
            return current_x - node_spacing

        start_x = current_x
        for child in children:
            end_x = dfs_layout(child, current_x, y + level_width, level_width, node_spacing)
            current_x = end_x + node_spacing

        node_positions[node] = {"x": (start_x + current_x - node_spacing) / 2, "y": y}
        return current_x - node_spacing

    node_positions = {}
    current_x = 0
    level_width = 150
    node_spacing = 200

    roots = find_root_nodes(G)
    for root in roots:
        dfs_layout(root, 0, 0, level_width, node_spacing)

    return node_positions

# Build the graph
G = build_graph(code_graph_responses)

# Create tree layout
node_positions = create_tree_layout(G)

# Create React Flow elements
elements = []

# Add nodes
for node, position in node_positions.items():
    node_type = "input" if G.in_degree(node) == 0 else "default"
    elements.append({
        "id": node,
        "data": {"label": node},
        "type": node_type,
        "position": position,
        "sourcePosition": "bottom",
        "targetPosition": "top"
    })

# Add edges
for edge in G.edges():
    elements.append({
        "id": f"e{edge[0]}-{edge[1]}",
        "source": edge[0],
        "target": edge[1],
        "animated": True,
        "type": "smoothstep"
    })

# Streamlit app
st.title("Code Graph Visualization")

# Calculate the required width and height based on node positions
flowStyles = { "height": 500,"width":1100 }

# Create an instance of the React Flow component
react_flow("code_graph", elements=elements, flow_styles=flowStyles)

# Optional: Print graph structure
if st.checkbox("Show Graph Structure"):
    st.subheader("Graph Structure")
    for root in find_root_nodes(G):
        st.text(root)
        for child in G.successors(root):
            st.text(f"  {child}")
            for grandchild in G.successors(child):
                st.text(f"    {grandchild}")