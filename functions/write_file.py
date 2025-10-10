import os

def write_file(working_directory, file_path, content):
    if file_path not in working_directory:
        f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        with open(path, "w") as a_file:
            a_file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
