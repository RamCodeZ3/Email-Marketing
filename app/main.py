from fastapi import FastAPI
from dotenv import load_dotenv
from routes.email_routes import routes as routes_email
from routes.product_routes import routes as routes_product
from routes.user_routes import routes as routes_user
from utils.scheduler import scheduler


load_dotenv()
app = FastAPI()
scheduler.start()

# Endpoints emails
app.include_router(routes_email)

# Endpoints products
app.include_router(routes_product)

# Endpoints users
app.include_router(routes_user)
