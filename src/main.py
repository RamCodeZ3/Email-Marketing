from fastapi import FastAPI
from dotenv import load_dotenv
from routes.email_routes import routes as routes_email
from routes.product_routes import routes as routes_product
from routes.user_routes import routes as routes_user


load_dotenv()
app = FastAPI()

# Endpoints emails
app.include_router(routes_email)

# Endpoints products
app.include_router(routes_product)

# Endpoints users
app.include_router(routes_user)
