from google import genai
from google.genai import types
import os
from model.schema import EmailJSON


class GenaiClient:
    def __init__(self):
        self.API_KEY = os.getenv("GENAI_KEY_API")

    def generate_email(self, data:EmailJSON):
        client = genai.Client(api_key=self.API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=f'''
                You are a creator of promotional email content for 
                a product or service, 
                using a maximum of 120 words in spanish.'''
            ),
            contents="",
        )
        print(response.text)

if __name__ == '__main__':
    g = GenaiClient()
    g.generate_email()