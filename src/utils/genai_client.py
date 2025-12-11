from google import genai
from google.genai import types
import os
from model.schema import EmailJSON


class GenaiClient:
    def __init__(self):
        self.API_KEY = os.getenv("GENAI_API_KEY")
        if not self.API_KEY: raise ValueError("No se encontro la api key")
        self.client = genai.Client(api_key=self.API_KEY)

    async def generate_body_email(self, data:EmailJSON):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=f'''
                    You are a creator of promotional email content for 
                    a product or service, 
                    using a maximum of 160 words in spanish no matter.'''
                ),
                
                contents=f"""
                Write a concise, persuasive promotional email body using this product info:
                Type: {data.product.type}, Name: {data.product.name_product}, 
                Description: {data.product.description}, Price: {data.product.price},
                Highlight benefits.""",
            )
            print("✅ La respuesta se genero exitosamente.")
            return response.text
        
        except:
            raise ValueError("❌ Hubo un error generado la respuesta.")
    
    async def generate_template_email(self, data:EmailJSON):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=f'''
                    You are a creator of eye-catching template HTML promotional email content for 
                    a product or service, 
                    using a maximum of 160 words in spanish no matter and only code HTML.'''
                ),
                
                contents=f"""
                Write a concise, persuasive promotional email body using this product info:
                Type: {data.product.type}, Name: {data.product.name_product}, 
                Description: {data.product.description}, Price: {data.product.price},
                Highlight benefits.""",
            )
            return response.text
        
        except:
            raise ValueError("❌ Hubo un error generado la respuesta.")
