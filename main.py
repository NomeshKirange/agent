# def main():
#     print("Hello from agent!")


# if __name__ == "__main__":
#     main()

# import os
# import sys
# from dotenv import load_dotenv
# from google import genai

# def main():
#     load_dotenv()
#     api_key = os.environ.get("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)
#     if len(sys.argv) < 2 :
#         print("I need Prompt")
#         sys.exit[1]
#     prompt = sys.argv[1]
#     response = client.models.generate_content(model='gemini-2.5-flash', contents= prompt)
#     if  response is None or response.usage_metadata is None :
#         print("Response is malformed !!")
#         return 
    
#     print(response.text)

#     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#     print(f"Prompt tokens: {response.usage_metadata.prompt_tokens_details}")

#     print(f"Response tokens: {response.usage_metadata.prompt_token_count}")
#     print(f"Prompt tokens: {response.usage_metadata.prompt_tokens_details}")
# main()
import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types 
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Argument parsing
    parser = argparse.ArgumentParser(description="Chatbot")
    
    # --- FIX START: You were missing this line ---
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI")
    # ---------------------------------------------
    
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()

    # Create the message payload
    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=args.user_prompt)
            ]
        )
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash', 
        contents=messages
    )

    if response is None or response.usage_metadata is None:
        print("Response is malformed !!")
        return 
    
    print(response.text)

    # Only show stats if --verbose flag is used (Optional improvement based on your flag)
    if args.verbose:
        print("\n--- Usage Stats ---")
        print(f"Prompt tokens:   {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}") 
        print(f"Total tokens:    {response.usage_metadata.total_token_count}")

#if __name__ == "__main__":
#    main()
print(get_files_info("calculator","pkg"))