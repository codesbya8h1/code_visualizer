import os


def read_code_files(repo_path):
    code_contents = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(
                    '.py'):  # You can add more file extensions if needed
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    code_contents[file] = f.read()
    return code_contents
