# import os 

# def get_files_info(working_directory, directory="."): 
#     abs_working_directory = os.path.abspath(working_directory)
    
#     if directory is None:
#         directory = "."

#     target_path = os.path.join(abs_working_directory, directory)
#     abs_directory = os.path.abspath(target_path)

#     if not abs_directory.startswith(abs_working_directory):
#         return f'Error: "{directory}" is not inside the working directory'
    
#     final_response = ""
    
#     if not os.path.exists(abs_directory):
#         return f"Error: Directory '{abs_directory}' does not exist"

#     contents = os.listdir(abs_directory)
    
#     for content in contents:
#         content_path = os.path.join(abs_directory, content)
        
#         is_dir = os.path.isdir(content_path)
#         size = os.path.getsize(content_path)
        
#         final_response += f" - {content}: file_size = {size} bytes, is_dir = {is_dir}\n"
        
#     return final_response

import os

# --- PASTE THE FUNCTION DIRECTLY HERE ---
def get_files_info(working_directory, directory="."): 
    abs_working_directory = os.path.abspath(working_directory)
    if directory is None:
        directory = "."
    target_path = os.path.join(abs_working_directory, directory)
    abs_directory = os.path.abspath(target_path)
    
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: "{directory}" is not inside the working directory'
    if not os.path.exists(abs_directory):
        return f"Error: Directory '{abs_directory}' does not exist"

    final_response = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f" - {content}: file_size = {size} bytes, is_dir = {is_dir}\n"
    return final_response
# ----------------------------------------