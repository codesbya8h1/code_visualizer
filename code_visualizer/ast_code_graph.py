import ast

def analyze_code(code):
    tree = ast.parse(code)
    method_calls = {}
    
    class MethodCallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.current_method = None
        
        def visit_FunctionDef(self, node):
            self.current_method = node.name
            method_calls[self.current_method] = []
            self.generic_visit(node)
            self.current_method = None
        
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and self.current_method:
                method_calls[self.current_method].append(node.func.id)
            self.generic_visit(node)
    
    MethodCallVisitor().visit(tree)
    return method_calls