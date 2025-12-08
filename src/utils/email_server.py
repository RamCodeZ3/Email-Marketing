import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from model.schema import EmailJSON
from utils.genai_client import GenaiClient


class EmailServer:
    def __init__(self):
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587
        self.EMAIL_FROM = os.getenv("SMTP_EMAIL_FROM")
        self.EMAIL_PASSWORD = os.getenv("SMTP_EMAIL_PASSWORD")
        self.genai = GenaiClient()

    async def email_server(self, data: EmailJSON):
        
        emails = data.receiver_list

        try:
            # Content email
            for email in emails:
                msg = MIMEMultipart()
                msg['From'] = self.EMAIL_FROM
                msg['To'] = emails
                msg["Subject"] = data.product.title

                body = self.genai.generate_email(data)
                msg.attach(MIMEText(body, "Plain"))

                # send email
                server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
                server.starttls()
                server.login(self.EMAIL_FROM, self.EMAIL_PASSWORD)
                server.sendmail(self.EMAIL_FROM, email, msg.as_string())
                server.quit()
            
            print("Correo enviado correctamente.")
        
        except Exception as e:
            print("Error enviando el correo:", e)
