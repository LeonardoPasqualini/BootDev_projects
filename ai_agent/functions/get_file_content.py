import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        content = ""
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # Check if the file was truncated
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            content += f"\n{file_content_string}"
        return content
    except Exception as e:
        return f'Error: {str(e)}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the file content of a file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to get the content from, relative to the working directory",
            ),
        },
    ),
)
    