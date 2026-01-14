import os
from functions.get_files_content import get_file_content


def main():
    # Setup dummy files first so tests don't fail on missing files
    

    print("--- Test 1: Truncation Check (lorem.txt) ---")
    content = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(content)}")
    print(f"Ends with: {content[-60:]}") # Show the truncation message
    
    print("\n--- Test 2: Standard File (main.py) ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- Test 3: Nested File (pkg/calculator.py) ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n--- Test 4: Security Violation (/bin/cat) ---")
    # Note: On Windows this tests C:/bin/cat, which is definitely outside 'calculator'
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Test 5: Missing File ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()