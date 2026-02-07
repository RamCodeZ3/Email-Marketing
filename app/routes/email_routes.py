from fastapi import APIRouter
from models.email_model import EmailModel
from utils.email_server import EmailServer
from services import email_service as es


routes = APIRouter(
    prefix="/email",
    tags=["Email"]
)

email_server = EmailServer()

@routes.get('/get-all')
async def get_all_emails():
    try:
        return await es.get_all_emails()
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.get('/get/{email_id}')
async def get_email_by_id(email_id: int):
    try:
        return await es.get_email_by_id(email_id)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


# Send Email
@routes.post('/create-body-auto')
async def create_email_auto(data:EmailModel):
    try:
        print("✅ Se comenzo con la creacion y envio de emails con IA.")
        await email_server.email_server(data, True, True)
        return f'Se envio el correo existosamente.'
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.post('/send-emails')
async def create_email(data:EmailModel):
    try:
        created = await es.create_email(data)
        # send email to users
        await email_server.email_server(data, False, True)

        # if we have the inserted id, mark it as sent
        try:
            if created and isinstance(created, dict) and created.get('id'):
                await es.mark_email_as_sent(created['id'])
                return "Correo enviado y estado actualizado a 'sent'."
        except Exception:
            pass

        return 'Se intento enviar el correo.'
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.put('/update/{email_id}')
async def update_email(email_id: int, data:EmailModel):
    try:
        await es.update_email_by_id(email_id, data)
        return "Se actualizo el email con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.delete('/delete/{email_id}')
async def delete_email(email_id: int):
    try:
        await es.delete_email_by_id(email_id)
        return "Se Elimino el email con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')
