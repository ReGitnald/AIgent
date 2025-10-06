import os
from google.genai import types
from functions.get_file_content import write_file
from functions.run_python_file import run_python_file

def get_files_info(working_directory, directory="."):
    combo_path = os.path.join(working_directory,directory)
    full_path = os.path.abspath(combo_path)
    if os.path.abspath(combo_path).startswith(os.path.abspath(working_directory)) and os.path.isdir(full_path):
        pathlist = os.listdir(full_path)
        string_out = ""
        for path in pathlist:
            full_item_path = os.path.join(full_path, path)
            item = path
            try:
                string_out += f"- {item}: file_size={os.path.getsize(full_item_path)} bytes, is_dir={os.path.isdir(full_item_path)}\n"
            except:
                return(f'Error: Problem with "{full_item_path}"')
    elif not os.path.isdir(full_path):

        return(f'Error: "{directory}" is not a directory')
    else:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    return string_out

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file in the given directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in the directory where the file is listed.",
            ),
        },
    ),
)



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python file in the current working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in the directory where the file is listed.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes given content to a file in the given directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory where the file should be written to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

def call_function(function_call_part, verbose=False):
    if function_call_part.name == "get_files_info":
        directory = function_call_part.args.get("directory", ".")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        if verbose:
            print(f"Calling get_files_info with directory: {directory}")
        function_result = function_result =get_files_info("calculator", directory)
    elif function_call_part.name == "get_file_content":
        file_path = function_call_part.args.get("file_path")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        if verbose:
            print(f"Calling get_file_content with file_path: {file_path}")
        from functions.get_file_content import get_file_content
        function_result = get_file_content("calculator", file_path)
    elif function_call_part.name == "run_python_file":
        file_path = function_call_part.args.get("file_path")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        if verbose:
            print(f"Calling run_python_file with file_path: {file_path}")
        from functions.run_python_file import run_python_file
        function_result = run_python_file("calculator", file_path)
    elif function_call_part.name == "write_file":
        file_path = function_call_part.args.get("file_path")
        content = function_call_part.args.get("content")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        if verbose:
            print(f"Calling write_file with file_path: {file_path} and content length: {len(content) if content else 0}")
        
        function_result = write_file("calculator", file_path, content)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
            )
        ],
    )
        

