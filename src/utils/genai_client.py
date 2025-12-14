from google import genai
from google.genai import types
import os
from model.schemas import EmailModel
from services import email_service as es


class GenaiClient:
    def __init__(self):
        self.API_KEY = os.getenv("GENAI_API_KEY")
        if not self.API_KEY: raise ValueError("No se encontro la api key")
        self.client = genai.Client(api_key=self.API_KEY)

    async def generate_body_email(self, data:EmailModel):
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
            
            email_to_save = data.model_copy(update={
                "body": response.text
            })

            print("✅ La respuesta se genero exitosamente.")
            await es.create_email(email_to_save)
            return response.text

        except:
            raise ValueError("❌ Hubo un error generado la respuesta.")
