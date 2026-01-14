import os

# Assignment requirement: Limit reading to avoid token burn
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        # 1. Resolve Absolute Paths
        abs_working_directory = os.path.abspath(working_directory)
        target_path = os.path.join(abs_working_directory, file_path)
        abs_target_path = os.path.abspath(target_path)

        # 2. Security Check (Sandboxing)
        if not abs_target_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # 3. Check if file exists and is a regular file
        if not os.path.isfile(abs_target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # 4. Read the file with limits
        # We use 'errors="replace"' to avoid crashing on weird binary characters
        with open(abs_target_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read(MAX_CHARS)
            
            # Check if there is more data left (Truncation check)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return content

    except Exception as e:
        # Catch any other OS errors (permissions, etc.)
        return f"Error: {str(e)}"