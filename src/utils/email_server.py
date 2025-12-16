import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from model.schemas import EmailModel
from utils.genai_client import GenaiClient
from services.user_service import get_all_users
from services.product_service import get_product_by_id


class EmailServer:
    def __init__(self):
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587
        self.EMAIL_FROM = os.getenv("SMTP_EMAIL_FROM")
        self.EMAIL_PASSWORD = os.getenv("SMTP_EMAIL_PASSWORD")
        self.genai = GenaiClient()

    async def email_server(
            self, 
            data: EmailModel, 
            auto: bool, 
    ):
        emails = await get_all_users()
        product = (await get_product_by_id(data.product_id))[0]

        body_email = data.body

        if auto: 
            body_email = await self.genai.generate_body_email(data, product)
        
        # HTML of email
        body = f"""
        <html>
        <body style="margin:0; padding:0; font-family: Arial, sans-serif; background-color:#f4f4f4; height:100%;min-height:100vh;">
            <div style="
                max-width: 600px;
                margin: 30px auto;
                background: #ffffff;
                padding: 25px;
                text-align: center;
                border: 1px solid #e5e5e5;
            ">
            <h1 style="font-size: 24px; color: #333333; margin-bottom: 20px; text-aling: left;">
                {data.title}
            </h1>
            <img 
                src="{product["url_img_product"]}" 
                alt="Imagen del producto" 
                width="95%" 
                style="border-radius: 8px; margin-bottom: 20px;"
            >

            <div style="text-aling: left;">
                <span style="font-size: 16px; color: #555555; line-height: 1.5; margin-bottom: 25px;">
                    {body_email}
                </span>
            </div>
            <a 
                href="{product["link_product"]}"
                style="
                display: inline-block;
                background-color: #007bff;
                color: #ffffff;
                text-decoration: none;
                padding: 12px 20px;
                border-radius: 6px;
                font-size: 16px;
                "
            >
                Visita nuestra web
            </a>

            <p style="margin-top: 30px; font-size: 12px; color:#999999;">
                © {data.name_company if data.name_company else "Nuestra Empresa"}
            </p>
            </div>
        </body>
        </html>
         """

        try:
            # estructure of email
            for email in emails:
                
                msg = MIMEMultipart()
                msg['From'] = self.EMAIL_FROM
                msg['To'] = email["email"]
                msg["Subject"] = data.title
                
                msg.attach(MIMEText(body, "html"))

                # send email
                with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                    server.starttls()
                    server.login(self.EMAIL_FROM, self.EMAIL_PASSWORD)
                    server.sendmail(self.EMAIL_FROM, email["email"], msg.as_string())
            
            print("✅ Correos enviado exitosamente a todos los usuarios")
        
        except Exception as e:
            print("❌ Error enviando el correo:", e)
