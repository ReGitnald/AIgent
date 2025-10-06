import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import *

system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
available_functions = types.Tool(
function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]
)

MAX_CHARS = 10000
WORKING_DIR = "./calculator"
MAX_ITERS = 20
config=types.GenerateContentConfig(
tools=[available_functions], system_instruction=system_prompt
)



# print("Before load_dotenv():", "GEMINI_API_KEY" in os.environ)
# result = load_dotenv()
# print("load_dotenv() returned:", result)  # Should return True if it found and loaded a .env file
# print("After load_dotenv():", "GEMINI_API_KEY" in os.environ)
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    result = load_dotenv('.env')
    print("Hello from aigent!")
    api_key = os.environ.get("GEMINI_API_KEY")
    print("The api key is ", api_key)
    client = genai.Client(api_key=api_key)
    verbose = '--verbose' in sys.argv
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    # else:
    #     print(resp.text)
    # if '--verbose' in sys.argv:
    #     print(f"User prompt: {sys.argv[0]}")
    #     print("Prompt tokens:",resp.usage_metadata.prompt_token_count)
    #     print("Response tokens:",resp.usage_metadata.candidates_token_count)




def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="user", parts=function_responses))






if __name__ == "__main__":
    main()
