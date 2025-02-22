import sys
import argparse
from pathlib import Path
from ascii_visualization import build_ascii_graph
from ast_code_graph import get_file_execution_flow, get_project_execution_flow
from find_starting_point import find_starting_point


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Code Visualizer: Generate execution graphs from Python source code."
    )
    parser.add_argument(
        "--file", type=str, help="Path to a Python file to analyze."
    )
    parser.add_argument(
        "--folder", type=str, help="Path to a folder containing Python files to analyze."
    )

    args = parser.parse_args()

    # Validate input arguments
    if not (args.file or args.folder): # or args.code we can add this later
        print("Error: You must provide one of --file, --folder, or --code.")
        sys.exit(1)

    # Read input based on the provided argument
    if args.file:
        input_path = Path(args.file)
        if not input_path.is_file():
            print(f"Error: File '{args.file}' does not exist.")
            sys.exit(1)
        
    elif args.folder:
        input_path = Path(args.folder)
        if not input_path.is_dir():
            print(f"Error: Folder '{args.folder}' does not exist.")
            sys.exit(1)
    
    if args.file:
        execution_graph = get_file_execution_flow(args.file)

        
    elif args.folder:
        folder = Path(args.folder)
        # entry_point = detect_project_entry_point(folder)
        execution_graph = get_project_execution_flow(folder)
    
    entry_point = find_starting_point(execution_graph)
    print(entry_point)
    print(execution_graph)
    build_ascii_graph(execution_graph, entry_point)

if __name__ == "__main__":
    main()