import os
import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path, args=[]):
    combo_path = os.path.join(working_directory,file_path)
    full_path = os.path.abspath(combo_path)
    if os.path.abspath(combo_path).startswith(os.path.abspath(working_directory)) and os.path.isfile(full_path) and full_path.endswith('.py'):
        # subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)¶
        try:
            result = subprocess.run(['python', full_path] + args, capture_output=True, text=True, timeout = 30 )
            if not result.stdout and not result.stderr:
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

# def run_python_file(working_directory, file_path, args=None):
#     args = args or []
#     wd = Path(working_directory).resolve()
#     target = (wd / file_path).resolve()

#     if not target.is_file():
#         return f'Error: File "{file_path}" not found.'
#     if target.suffix != ".py":
#         return f'Error: "{file_path}" is not a Python file.'
#     if not str(target).startswith(str(wd) + os.sep):
#         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

#     try:
#         proc = subprocess.run(
#             ["uv", "run", file_path, *args],  # or ["python3", file_path, *args]
#             cwd=str(wd),
#             capture_output=True,
#             text=True,
#             timeout=30,
#             env={**os.environ, "PYTHONUNBUFFERED": "1"},
#         )
#         # out = (proc.stdout or "") + (proc.stderr or "")
#         # return out
#         if proc.returncode == 0:
#             return proc.stderr # return exactly what the script printed
#         # on failure, include stderr (and stdout if any)
#         return (proc.stdout + proc.stderr).strip() or f"Process exited with code {proc.returncode}"
#     except Exception as e:
#         return f"Error executing file: {e}"

