import sys
import argparse
from pathlib import Path
from code_graph_rag import create_code_graph
from logger import setup_logger

logger = setup_logger()

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description=
        "Code Visualizer: Generate execution graphs from source code.")
    parser.add_argument("--file",
                        type=str,
                        help="Path to a code file to analyze.")
    parser.add_argument(
        "--folder",
        type=str,
        help="Path to a folder containing code files to analyze.")

    args = parser.parse_args()

    # Validate input arguments
    if not (args.file or args.folder):  # or args.code we can add this later
        print("Error: You must provide one of --file, --folder")
        sys.exit(1)

    input_path = None
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

    response = create_code_graph(input_path)
    print("response :", response)


if __name__ == "__main__":
    main()
