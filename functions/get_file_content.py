import os
from config import MAX_CHARS
from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a file at the specified file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file for which we want to retrieve the content.",
            ),
        },
    ),
)

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