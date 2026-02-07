from models.email_model import EmailModel
from services.email_service import (
    get_pending_emails_for_today,
    mark_email_as_sent
)
from utils.email_server import EmailServer

email_server = EmailServer()

async def process_scheduled_emails():
    emails = await get_pending_emails_for_today()

    if not emails:
        print("📭 No hay emails para enviar hoy")
        return

    for email_data in emails:
        try:
            await email_server.email_server(
                EmailModel(**email_data),
                True,
                False
            )
            await mark_email_as_sent(email_data["id"])
            print(f"✅ Email {email_data['id']} enviado")

        except Exception as e:
            print(f"❌ Error enviando email {email_data['id']}: {e}")
