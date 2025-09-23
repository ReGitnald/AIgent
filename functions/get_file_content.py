import os

def get_file_content(working_directory, file_path):
    combo_path = os.path.join(working_directory,file_path)
    full_path = os.path.abspath(combo_path)
    if os.path.abspath(combo_path).startswith(os.path.abspath(working_directory)) and os.path.isfile(full_path):
        MAX_CHARS = 10000
        try:
            with open(full_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    file_content_string += f"[]...File \"{file_path}\" truncated at 10000 characters]" 
                return(file_content_string)
        except Exception as e:
            print(f"Error during text reading: {e}")

    elif not os.path.isfile(full_path):

        return(f'Error: File not found or is not a regular file: "{file_path}"')
    else:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')



def write_file(working_directory, file_path, content):
    combo_path = os.path.join(working_directory,file_path)
    full_path = os.path.abspath(combo_path)
    if os.path.abspath(combo_path).startswith(os.path.abspath(working_directory)):
        if not os.path.isfile(full_path):
            os.makedirs(full_path)
        try:
            with open(full_path, "w") as f:
                f.write(content) 
                return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
        except Exception as e:
            print(f"Error during writing: {e}")
    else:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

