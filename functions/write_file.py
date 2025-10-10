import os

def write_file(working_directory, file_path, content):
    if file_path not in working_directory:
        f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    path = os.path.abspath(os.path.join(working_directory, file_path))

    print(f"Path: {path}")
    if not os.path.exists(path):
        os.makedirs(path)

    with open(file_path, "w")

    #f'Successfully wrote to "{file_path}" ({len(content)} characters written)'