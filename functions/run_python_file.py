import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    combo_path = os.path.join(working_directory,file_path)
    full_path = os.path.abspath(combo_path)
    if os.path.abspath(combo_path).startswith(os.path.abspath(working_directory)) and os.path.isfile(full_path) and full_path.endswith('.py'):
        # subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)¶
        try:
            result = subprocess.run(['python', full_path] + args, capture_output=True, text=True, timeout = 30 )
            if not result.stdout:
                return "No output produced."
            if result.returncode == 0:
                return f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}" 
            else:
                return f"Process exited with code {result.returncode}\nSTDOUT:{result.stdout}\nSTDERR:{result.stderr}" 
        except Exception as e:
            return f'Error executing file: {str(e)}'

    elif not os.path.isfile(full_path):
        return(f'Error: File "{file_path}" not found.')
    elif not full_path.endswith('.py'):
        return(f'Error: "{file_path}" is not a Python file.')
    else:
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')


