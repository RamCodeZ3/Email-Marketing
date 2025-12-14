import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from model.schemas import EmailMode
from utils.genai_client import GenaiClient


class EmailServer:
    def __init__(self):
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587
        self.EMAIL_FROM = os.getenv("SMTP_EMAIL_FROM")
        self.EMAIL_PASSWORD = os.getenv("SMTP_EMAIL_PASSWORD")
        self.genai = GenaiClient()

    async def email_server(
            self, 
            data: EmailMode, 
            auto: bool, 
    ):
        emails = data.receiver_list
        body_email = data.product.description

        if auto: 
            body_email = self.genai.generate_body_email(data)
        
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
                {data.product.title}
            </h1>
            <img 
                src="{data.product.url_img_product}" 
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
                href="{data.product.link_product}"
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
                © {data.email_from.name_company if data.email_from.name_company else "Nuestra Empresa"}
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
                msg['To'] = email
                msg["Subject"] = data.product.title
                
                msg.attach(MIMEText(body, "html"))

                # send email
                with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                    server.starttls()
                    server.login(self.EMAIL_FROM, self.EMAIL_PASSWORD)
                    server.sendmail(self.EMAIL_FROM, email, msg.as_string())
            
            print("✅ Correos enviado exitosamente a los siguientes emails:")
            for email in data.receiver_list:
                print("-- {}".format(email))
        
        except Exception as e:
            print("❌ Error enviando el correo:", e)
