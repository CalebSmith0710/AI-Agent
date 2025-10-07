import os

def get_files_info(working_directory, directory="."):
	full_path = os.path.join(working_directory, directory)
	if working_directory not in full_path:
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	if not os.path.isdir(directory):
		return f'Error: "{directory}" is not a directory'
	return ' '.join(map(lambda x: f"- {x}: file_size={os.path.getsize(x)} bytes, is_dir={os.path.isdir(x)}\n", os.listdir()))