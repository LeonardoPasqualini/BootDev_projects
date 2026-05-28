import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("No api key found")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

client = genai.Client(api_key=api_key)

messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

finished = False

for _ in range(20):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        )
    )
        
    if not response.usage_metadata:
        raise RuntimeError("Fail to request API")
    
    # Build a history to the agent remember
    for candidate in response.candidates:
        messages.append(candidate.content)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.function_calls:
        function_parts_list = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call)
            if not function_call_result.parts:
                raise Exception("Parts is empty")
            
            function_response = function_call_result.parts[0].function_response
            if not function_response:
                raise Exception("Function response is None")
            
            result = function_response.response
            if not result:
                raise Exception("Function response result is None")
            
            function_parts_list.append(function_call_result.parts[0])
            
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
            # collect the function rensponse for history purpose
            messages.append(types.Content(role="user", parts=function_parts_list))
            
    else:
        print(response.text)
        finished = True
        break

if not finished:
    print("The model couldn't reach a conclusion")
    exit(1)