import ast
from pathlib import Path
import builtins

class ExecutionOrderVisitor(ast.NodeVisitor):
    def __init__(self):
        self.execution_order = {}
        self.current_function = None
        self.builtins = dir(builtins)  # List of all Python built-in functions and methods

    def visit_FunctionDef(self, node):
        # Track the current function being visited
        self.current_function = node.name
        self.execution_order[self.current_function] = []
        
        # Visit each statement in the function body
        self.generic_visit(node)
        
        # Reset current function after visiting
        self.current_function = None

    def visit_Call(self, node):
        # If inside a function, record the called function
        if self.current_function:
            if isinstance(node.func, ast.Name):  # Direct function call
                # Exclude built-in functions
                if node.func.id not in self.builtins:
                    self.execution_order[self.current_function].append(node.func.id)
            elif isinstance(node.func, ast.Attribute):  
                if isinstance(node.func.value, ast.Name):  # Ensure it's a valid variable
                    qualified_name = f"{node.func.value.id}.{node.func.attr}"
                    if node.func.attr not in self.builtins:  # Exclude built-in methods
                        self.execution_order[self.current_function].append(qualified_name)
        
        # Continue visiting nested calls or arguments
        self.generic_visit(node)

def get_file_execution_flow(file):
    with open(file, "r") as f:
        source_code = f.read()
        
    tree = ast.parse(source_code)  # Parse the code into an AST
    visitor = ExecutionOrderVisitor()
    visitor.visit(tree)  # Visit all nodes in the AST
    return visitor.execution_order

def get_project_execution_flow(folder):
    """
    Traverse through a project folder and return an overall execution flow graph.
    
    Args:
        folder (str): Path to the project folder.

    Returns:
        dict: A combined execution flow graph for all Python files in the project.
    """
    folder_path = Path(folder)
    
    if not folder_path.is_dir():
        raise ValueError(f"The path '{folder}' is not a valid directory.")
    
    overall_execution_flow = {}
    
    # Recursively find all Python files in the folder
    python_files = list(folder_path.rglob("*.py"))
    
    for file_path in python_files:
        file_execution_flow = get_file_execution_flow(file_path)
        
        # Merge the file's execution flow into the overall execution flow
        for func, calls in file_execution_flow.items():
            # Use "file_name.function_name" as keys to differentiate between files
            qualified_func_name = func #f"{file_path.stem}.{func}"
            overall_execution_flow[qualified_func_name] = []

            for call in calls:
                if "." not in call:  # Local function call (within the same file)
                    overall_execution_flow[qualified_func_name].append(call)
                else:  # External method or attribute access (e.g., imported functions)
                    overall_execution_flow[qualified_func_name].append(call)

    return overall_execution_flow