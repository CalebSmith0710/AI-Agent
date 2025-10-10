from config import MAX_CHARS
import os

def get_file_content(working_directory, file_path):
    if file_path not in working_directory:
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.isfile(path):
        f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open (path, 'r', encoding="utf-8") as a_file:
            file_content_string = a_file.read(MAX_CHARS)
            return file_content_string
    except Exception as e:
        return f"Error getting file content: {e}"