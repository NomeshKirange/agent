import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    try:
        # 1. Resolve Absolute Paths
        abs_working_directory = os.path.abspath(working_directory)
        target_path = os.path.join(abs_working_directory, file_path)
        abs_target_path = os.path.abspath(target_path)

        # 2. Security Check (Sandboxing)
        if not abs_target_path.startswith(abs_working_directory):
            return f'Error: Cannot run "{file_path}" as it is outside the permitted working directory'

        # 3. Check if file exists
        if not os.path.isfile(abs_target_path):
            return f'Error: File not found: "{file_path}"'

        # 4. Run the Python script
        result = subprocess.run(
            [sys.executable, abs_target_path],
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            check=False
        )

        # 5. Construct the Feedback String
        # This combines both outputs so the agent sees everything
        feedback = f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"

        # 6. Return the output
        if result.returncode != 0:
            # FIX: Use the 'feedback' variable here so we see what happened before the crash
            return f"Error: Exit code {result.returncode}.\n{feedback}"

        # FIX: Return the 'feedback' variable here too, not just stdout
        return feedback

    except Exception as e:
        return f"Error: {str(e)}"