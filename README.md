# 📧 Email Marketing API

**Email Marketing API** es una API desarrollada con **FastAPI** que permite gestionar y enviar **emails promocionales de productos o servicios** de forma automatizada.  
El sistema es capaz de **programar envíos**, **generar automáticamente el cuerpo del email usando GenAI (genai_2.5_flash)** y **almacenar registros en Supabase**.

---

## 🚀 Características principales

- ✅ Gestión completa de **emails promocionales**
- ✅ Gestión de **productos / servicios**
- ✅ Gestión de **usuarios destinatarios**
- ✅ Generación automática del cuerpo del email con **GenAI**
- ✅ Programación de envíos con **APScheduler**
- ✅ Envío de correos mediante **SMTP**
- ✅ Persistencia de datos usando **Supabase**
- ✅ API REST clara y modular

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python**
- ⚡ **FastAPI**
- ⏰ **APScheduler**
- 🤖 **GenAI (genai_2.5_flash)** — generación automática del cuerpo del email
- 🗄️ **Supabase** — almacenamiento y registro de emails
- ✉️ **smtplib** — envío de correos electrónicos

---

## 📂 Estructura del proyecto

```
📦 email-marketing-api
┃
┣ 📂 app
┃ ┣ 📂 models       # Modelos de datos
┃ ┣ 📂 routes       # Endpoints de la API
┃ ┣ 📂 services     # Lógica de negocio
┃ ┣ 📂 utils        # Utilidades (scheduler, helpers, etc.)
┃ ┣ 📂 config       # configuracion y conexion al supabase
┃ ┣ 📜 main.py      # Archivo principal
┃
┣ 📜 .env           # Variables de entorno
┣ 📜 .env.example   # Ejemplo de variables de entorno
┣ 📜 requirements.txt
┣ 📜 README.md
┣ 📜 LICENSE
┗ 📜 .gitignore
```

---

## 🌐 Endpoints disponibles

### 📧 Emails
```
GET     /email/get-all
GET     /email/get/{email_id}
POST    /email/create-body-auto
POST    /email/send-emails
PUT     /email/update/{email_id}
DELETE  /email/delete/{email_id}
```

### 📦 Productos / Servicios
```
GET     /product/get-all
GET     /product/get/{product_id}
POST    /product/create-product
PUT     /product/update/{product_id}
DELETE  /product/delete/{product_id}
```

### 👤 Usuarios
```
GET     /user/get-all
GET     /user/get/{user_id}
POST    /user/create-user
PUT     /user/update/{user_id}
DELETE  /user/delete/{user_id}
```

---

## 🤖 Generación automática de emails

El endpoint `/email/create-body-auto` utiliza **GenAI (genai_2.5_flash)** para generar automáticamente el cuerpo del email promocional a partir de la información del producto o servicio, creando mensajes profesionales y persuasivos.

---

## ⏰ Programación de envíos

Gracias a **APScheduler**, la API permite **programar cuándo se enviarán los correos**, ideal para campañas de marketing automatizadas.

---

## ⚙️ Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SUPABASE_URL=
SUPABASE_KEY=
GENAI_API_KEY=
SMTP_EMAIL_FROM=
SMTP_EMAIL_PASSWORD=
```

---

## ▶️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/email-marketing-api.git
cd email-marketing-api
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la API
```bash
uvicorn src.main:app --reload
```

---

## 📚 Documentación automática

FastAPI genera documentación interactiva automáticamente:

- 📘 **Swagger UI:**  
  `http://127.0.0.1:8000/docs`

- 📕 **ReDoc:**  
  `http://127.0.0.1:8000/redoc`

---

## 📌 Notas importantes

- Configura correctamente el **SMTP** para el envío de correos.
- GenAI requiere una **API Key válida**.
- Supabase se utiliza como backend de almacenamiento y registro.
- Ideal para **campañas de marketing**, **promociones** y **notificaciones automáticas**.

---

## 📝 Licencia

Este proyecto está bajo la licencia **MIT**.
