from fastapi import FastAPI
from dotenv import load_dotenv
from routes.email_routes import routes as routes_email


load_dotenv()
app = FastAPI()

# Endpoints emails
app.include_router(routes_email)

# Endpoints products


# Endpoints users
