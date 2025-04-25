import os
import google.generativeai as genai
import json
from response_operator import ResponseOperator


class GeminiQuery:
    def __init__(self):
        api_key = os.environ.get("GG_API_KEY")
        genai.configure(api_key=api_key)
        self.gemini_model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_operator_list(self, prompt):
        response = self.gemini_model.generate_content(
            prompt, generation_config={"response_mime_type": "application/json"}
        )
        print(response.text)
        response_arr = json.loads(response.text)
        return [
            ResponseOperator(
                title=response_data.get("title", ""),
                url=response_data.get("url", ""),
            )
            for response_data in response_arr
        ]
