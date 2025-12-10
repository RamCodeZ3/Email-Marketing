from fastapi import FastAPI
from model.schema import EmailJSON
from utils.email_server import EmailServer
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()
email = EmailServer()

@app.post('/create-email')
async def post_email(data:EmailJSON):
    print("✅ Se comenzo con la creacion y envio de emails.")
    await email.email_server(data)
    return f'Se envio el correo existosamente.'
