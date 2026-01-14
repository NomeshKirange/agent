import os
from functions.write_file import write_file

def main():
    # Setup: Ensure the base sandbox directory exists
    if not os.path.exists("calculator"):
        os.makedirs("calculator")

    print("--- Test 1: Write simple file ---")
    # Should print: Successfully wrote to "lorem.txt" (28 characters written)
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("\n--- Test 2: Write file in nested folder (Auto-creation) ---")
    # Should print: Successfully wrote to "pkg/morelorem.txt" (26 characters written)
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("\n--- Test 3: Security Violation ---")
    # Should print: Error: Cannot write to ... outside permitted working directory
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print("\n--- Test 4: Create new folder 'pkg2' and file inside ---")
    # This should automatically create the "pkg2" folder inside "calculator"
    # and then write "Hello World" into "hello.txt"
    print(write_file("calculator", "pkg2/hello.txt", "Hello World"))

if __name__ == "__main__":
    main()