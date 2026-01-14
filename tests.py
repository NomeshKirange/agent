from functions.get_files_info import get_files_info
# def main():
#     working_dir = "calculator"
#     root_content = get_files_info(working_dir,".")
#     pkg_content = get_files_info("pkg",".")
#     bit_content = get_files_info("/bin")
#     check_content = get_files_info("../")

#     print(root_content)
#     print(pkg_content)
#     print(bit_content)
#     print(check_content)

# main()
# coding is wrong cause its escaping to its ouwn main directory 
# def main():
#     # Test 1: Check the CURRENT folder (guaranteed to work)
#     print("--- Test 1: Current Directory ---")
#     print(get_files_info(".", "."))

#     # Test 2: Check Parent Directory
#     print("\n--- Test 2: Parent Directory ---")
#     print(get_files_info("../", "."))

# if __name__ == "__main__":
#     main()

import os
from functions.get_files_info import get_files_info

def main():
    # 1. Setup: Create a dummy safe folder so the test works
    if not os.path.exists("calculator"):
        os.makedirs("calculator")

    print("--- Security Test: Sandboxing ---")
    
    # SCENARIO: The AI is locked inside the "calculator" folder.
    # We tell the function: "Your universe is ONLY the 'calculator' folder."
    jail_cell = "calculator"

    # ATTEMPT 1: AI behaves nicely and asks for files inside the jail.
    print("\n1. AI checks inside the jail:")
    print(get_files_info(jail_cell, ".")) 
    # RESULT: Success (prints contents of calculator)

    # ATTEMPT 2: AI tries to hack out to read your main.py
    # It asks for "../" which means "go up one level"
    print("\n2. AI tries to escape to parent folder:")
    print(get_files_info(jail_cell, "../"))
    # RESULT: Should print "Error: ... not inside working directory"
    print(get_files_info(jail_cell, "/bin"))


if __name__ == "__main__":
    main()