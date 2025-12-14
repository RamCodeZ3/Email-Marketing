from fastapi import FastAPI
from model.schemas import EmailMode
from utils.email_server import EmailServer
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()
email = EmailServer()

@app.post('/email/create-body-auto')
async def create_email_auto(data:EmailMode):
    try:
        print("✅ Se comenzo con la creacion y envio de emails con IA.")
        await email.email_server(data, True)
        return f'Se envio el correo existosamente.'
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')

@app.post('/email/send-emails')
async def create_email(data:EmailMode):
    try:
        print("✅ Se comenzo con el envio de emails.")
        await email.email_server(data, False)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


