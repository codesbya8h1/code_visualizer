import sys
# import argparse
from pathlib import Path
from code_graph_rag import create_code_graph
from logger import setup_logger
import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from streamlit_flow.state import StreamlitFlowState
from streamlit_file_browser import st_file_browser
import networkx as nx
import wx
# import time
import os
from pathlib import Path
from tkinter import Tk, filedialog
logger = setup_logger()

# Function to select a folder using tkinter
def select_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.wm_attributes('-topmost', 1)  # Bring the dialog to the front
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path

# Function to process files in a folder
def process_folder(folder_path):
    # Example: List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files


def build_graph(responses):
    G = nx.DiGraph()
    for response in responses:
        G.add_node(response.name)
        for conn in response.connections:
            G.add_edge(response.name, conn)
    return G

def top_down_layout(G):
    def dfs_layout(node, x, y, level_width, node_spacing):
        nonlocal current_x
        children = list(G.successors(node))
        if not children:
            node_positions[node] = (current_x, y)
            current_x += node_spacing
            return current_x - node_spacing

        start_x = current_x
        for child in children:
            end_x = dfs_layout(child, current_x, y + level_width, level_width, node_spacing)
            current_x = end_x + node_spacing

        node_positions[node] = ((start_x + current_x - node_spacing) / 2, y)
        return current_x - node_spacing

    node_positions = {}
    current_x = 0
    level_width = 150
    node_spacing = 200

    roots = [node for node in G.nodes() if G.in_degree(node) == 0]
    for root in roots:
        dfs_layout(root, 0, 0, level_width, node_spacing)

    return node_positions
def run_streamlit_app(input_path):
    
    st.set_page_config("Code Graph Visualization", layout="wide")
    st.title("Code Graph Visualization")
    
    # Generate code flow graph
    code_flow_graph = create_code_graph(input_path)
    G = build_graph(code_flow_graph)
    node_positions = top_down_layout(G)

    if 'curr_state' not in st.session_state:
        nodes = [
            StreamlitFlowNode(
                node,
                (pos[0], pos[1]),
                {'content': node},
                'default',
                'bottom',
                'top'
            ) for node, pos in node_positions.items()
        ]

        edges = [
            StreamlitFlowEdge(
                f"{edge[0]}-{edge[1]}",
                edge[0],
                edge[1],
                animated=True,
                type='smoothstep',
                marker_end={'type': 'arrow'}
            ) for edge in G.edges()
        ]
        st.session_state.curr_state = StreamlitFlowState(nodes, edges)

    streamlit_flow(
        'code_graph_flow', 
        st.session_state.curr_state, 
        fit_view=True, 
        height=800, 
        show_minimap=True, 
        hide_watermark=True,
    )

def browse_file_or_folder(select_files=True):
    """Opens a file/folder browser dialog using wxPython."""
    app = wx.App(False)  # Create a wx App instance
    if select_files:
        # File selection dialog
        dialog = wx.FileDialog(
            None,
            "Select a file:",
            wildcard="*.*",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        )
    else:
        # Folder selection dialog
        dialog = wx.DirDialog(None, "Select a folder:", style=wx.DD_DEFAULT_STYLE)

    if dialog.ShowModal() == wx.ID_OK:
        selected_path = dialog.GetPath()
    else:
        selected_path = None
    dialog.Destroy()
    return selected_path

def main():
    # Debug print to see what arguments are being received
    # Debug print to see what arguments are being received
    # print("Received arguments:", sys.argv)

    # Set up argument parsing
    # parser = argparse.ArgumentParser(
    #     description="Code Visualizer: Generate execution graphs from source code.")
    # parser.add_argument("--file", type=str, help="Path to a code file to analyze.")
    # parser.add_argument("--folder", type=str, help="Path to a folder containing code files to analyze.")

    # # Parse known arguments
    # args, unknown = parser.parse_known_args()

    # # Debug print to see parsed arguments
    # print("Parsed arguments:", args)
    # print("Unknown arguments:", unknown)

    # # Handle unknown arguments
    # if unknown:
    #     if args.folder is None and args.file is None:
    #         # Assume the first unknown argument is the folder path
    #         args.folder = unknown[0]
    #     else:
    #         print(f"Warning: Unrecognized arguments: {' '.join(unknown)}")

    # # Validate input arguments
    # if not (args.file or args.folder):
    #     print("Error: You must provide one of --file or --folder")
    #     sys.exit(1)

    # input_path = Path(args.file or args.folder)

    # if args.file and not input_path.is_file():
    #     print(f"Error: File '{input_path}' does not exist.")
    #     sys.exit(1)
    # elif args.folder and not input_path.is_dir():
    #     print(f"Error: Folder '{input_path}' does not exist.")
    #     sys.exit(1)

    # print("Input path:", input_path)

    # time.sleep(10)
    # from streamlit.web import cli as stcli
    # sys.argv = ["streamlit", "run", __file__, "--", str(input_path)]
    # sys.exit(stcli.main())

    # Streamlit UI
    st.title("File/Folder Processor")

    # Input box and browse button
    col1, col2 = st.columns([4, 1])
    with col1:
        path_input = st.text_input("Selected path:", value="", key="path_input")
    with col2:
        browse_mode = st.radio("Browse Mode:", ["File", "Folder"], horizontal=True)
        if st.button("Browse"):
            select_files = browse_mode == "File"
            selected_path = browse_file_or_folder(select_files)
            if selected_path:
                st.session_state.path_input = selected_path  # Update session state
                st.experimental_rerun()

    # Display the selected path in the input box
    if "path_input" in st.session_state and st.session_state.path_input:
        st.success(f"Selected Path: {st.session_state.path_input}")

    # Process button
    if st.button("Process"):
        if "path_input" in st.session_state and Path(st.session_state.path_input).exists():
            selected_path = Path(st.session_state.path_input)
            if selected_path.is_file():
                st.success(f"Processing file: {selected_path}")
                with open(selected_path, "r") as f:
                    content = f.read()
                    st.text_area("File Content:", content, height=200)
            elif selected_path.is_dir():
                st.success(f"Processing folder: {selected_path}")
                files = list(selected_path.glob("*"))
                st.write(f"Found {len(files)} items:")
                st.json([str(f) for f in files])
        else:
            st.error("Invalid path selected!")
    # input_path = selected_folder if selected_folder else selected_file
    # run_streamlit_app(input_path)

if __name__ == "__main__":
    main()
        
