from dotenv import load_dotenv
import os
import sys
import json
import google.generativeai as genai

# Set up the Google Generative AI API
load_dotenv()
api_key = os.environ.get("GG_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# Check filename from command-line argument
file_name = sys.argv[1] if len(sys.argv) > 1 else "request_1"

# Define response model
class ResponseModel:
    def __init__(self, title: str, youtube_url: str):
        self.title = title
        self.youtube_url = youtube_url

# submit prompt and get response
with open(f"src/prompts/{file_name}.txt", "r") as file:
    prompt = file.read()
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    response_arr = json.loads(response.text)
    response_models = [
        ResponseModel(
            title=response_data.get("title", ""),
            youtube_url=response_data.get("youtube_url", "")
        )
        for response_data in response_arr
    ]
    print(response.text)
