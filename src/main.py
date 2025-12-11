from fastapi import FastAPI
from model.schema import EmailJSON
from utils.email_server import EmailServer
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()
email = EmailServer()

@app.post('/email/create-body-auto')
async def create_email_auto(data:EmailJSON):
    try:
        print("✅ Se comenzo con la creacion y envio de emails con IA.")
        await email.email_server(data, True)
        return f'Se envio el correo existosamente.'
    
    except:
        raise ValueError('❌ Hubo un error realizando la peticion')

@app.post('/email/create-body')
async def create_email(data:EmailJSON):
    try:
        print("✅ Se comenzo con el envio de emails.")
        await email.email_server(data, False)
    
    except:
        raise ValueError('❌ Hubo un error realizando la peticion')

@app.post('/email/create-template')
async def create_email_and_template(data:EmailJSON):
    try:
        print("✅ Se comenzo con la creacion y envio de emails con IA.")
        await email.email_server(data, False, True)
        return f'Se envio el correo existosamente.'
    
    except:
        raise ValueError('❌ Hubo un error realizando la peticion')
