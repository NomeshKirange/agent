import os

def write_file(working_directory, file_path, content):
    try:
        # 1. Resolve Absolute Paths
        abs_working_directory = os.path.abspath(working_directory)
        target_path = os.path.join(abs_working_directory, file_path)
        abs_target_path = os.path.abspath(target_path)

        # 2. Security Check (Sandboxing)
        if not abs_target_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # 3. Check if path is a directory (we can't write content to a folder)
        if os.path.isdir(abs_target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # 4. Create parent directories if they don't exist
        # We use os.path.dirname() to get the folder part (stripping the filename)
        parent_dir = os.path.dirname(abs_target_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # 5. Write the content
        with open(abs_target_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"