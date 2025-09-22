import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


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
    resp = client.models.generate_content(model = 'gemini-2.0-flash-001', 
                                          contents = messages)
    print(resp.text)
    if '--verbose' in sys.argv:
        print(f"User prompt: {sys.argv[0]}")
        print("Prompt tokens:",resp.usage_metadata.prompt_token_count)
        print("Response tokens:",resp.usage_metadata.candidates_token_count)
if __name__ == "__main__":
    main()
