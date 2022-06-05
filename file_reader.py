import os

def read_files(directory):
    """
    Read Python code files from the specified directory.

    Args:
    - directory (str): The directory path from which files will be read.

    Returns:
    - code_files (dict): A dictionary containing file names as keys and code contents as values.
    """
    code_files = {}
    
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return code_files

    for file_name in os.listdir(directory):
        if file_name.endswith('.py'):
            file_path = os.path.join(directory, file_name)
