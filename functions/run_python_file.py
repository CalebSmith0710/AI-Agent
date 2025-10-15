import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_dir):
        return f'Error: File "{file_path}" not found.'
    if not target_dir.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = [sys.executable, target_dir] + args
        completed_process = subprocess.run(cmd, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
        return_code = completed_process.check_returncode()
        stdout = completed_process.stdout
        stderr = completed_process.stderr 
        string = f"STDOUT: {stdout} STDERR: {stderr}"
        if stdout == None and stderr == None:
            return f"{string}\nNo output produced"
        if return_code != 0:
            return f"{string}\nProcess exited with code {return_code}"
    except Exception as e:
        return f"Error: executing python file: {e}"