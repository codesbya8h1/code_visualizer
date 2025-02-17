import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from graphviz import Digraph

def visualize_code_graph(data):
    G = nx.DiGraph()
    for method, calls in data['code_graph'].items():
        G.add_node(method)
        for call in calls:
            G.add_edge(method, call)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, arrows=True)
    nx.draw_networkx_nodes(G, pos, nodelist=[data['code_entry']], node_color='lightgreen', node_size=3000)
    plt.title("Code Structure Visualization")
    plt.axis('off')
    plt.show()



def visualize_code_graph_plotly(data):
    G = nx.DiGraph()
    for method, calls in data['code_graph'].items():
        G.add_node(method)
        for call in calls:
            G.add_edge(method, call)
    
    pos = nx.spring_layout(G)
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x, node_y = [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    fig = go.Figure(data=[
        go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines'),
        go.Scatter(x=node_x, y=node_y, mode='markers+text', hoverinfo='text', marker=dict(size=30, color='lightblue'), text=list(G.nodes()), textposition='middle center')
    ])
    fig.update_layout(showlegend=False, hovermode='closest', margin=dict(b=0,l=0,r=0,t=0))
    fig.show()


def visualize_code_graph_graphviz(data):
    from graphviz import Digraph

def visualize_code_flow(data):
    dot = Digraph(comment='Code Execution Flow')
    dot.attr(rankdir='TB', size='8,8')  # Top to Bottom layout
    
    # Add nodes
    for method in data['code_graph']:
        if method == data['code_entry']:
            dot.node(method, method, style='filled', fillcolor='lightgreen')
        else:
            dot.node(method, method)
    
    # Add edges
    for method, calls in data['code_graph'].items():
        for call in calls:
            dot.edge(method, call)
    
    dot.render('code_execution_flow', view=True, format='png')

