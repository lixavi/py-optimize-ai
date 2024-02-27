import os

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def get_python_files(directory="."):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
