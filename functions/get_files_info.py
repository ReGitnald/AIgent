import os


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


