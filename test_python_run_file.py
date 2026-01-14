import os
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def main():
    # Setup: Ensure folder exists
    if not os.path.exists("calculator"):
        os.makedirs("calculator")

    print("--- Test 1: Run a simple Hello World ---")
    # 1. Create the file first
    write_file("calculator", "hello.py", "print('Hello from the sandbox!')")
    # 2. Run it
    output = run_python_file("calculator", "hello.py")
    print(f"Output: {output.strip()}")

    print("\n--- Test 2: Run a script that calculates something ---")
    code = """
x = 10
y = 20
print(f'The sum is {x + y}')
"""
    write_file("calculator", "calc_test.py", code)
    print(f"Output: {run_python_file('calculator', 'calc_test.py').strip()}")

    print("\n--- Test 3: Run a script that crashes (Error Handling) ---")
    write_file("calculator", "crash.py", "print('Start'); raise ValueError('Oops!')")
    print(run_python_file("calculator", "crash.py"))

    print("\n--- Test 4: Security Check ---")
    print(run_python_file("calculator", "../main.py"))

if __name__ == "__main__":
    main()