from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

# Check filename from command-line argument
file_name = sys.argv[1] if len(sys.argv) > 1 else "request_1"

# Invoke the operator to download the audio
with open(f"src/prompts/{file_name}.txt", "r") as file:
    prompt = file.read()
    from importlib import import_module

    query_klass = {
        "request_1": "gemini_query.GeminiQuery",
        "request_2": "file_query.FileQuery",
    }.get(file_name)

    if query_klass:
        module_name, class_name = query_klass.rsplit(".", 1)
        query = getattr(import_module(module_name), class_name)()
        operator_list = query.generate_operator_list(prompt)
        for operator in operator_list:
            operator.get_audio()
