from fastapi import FastAPI
from model.schema import EmailJSON


app = FastAPI()

@app.post('/create-email/{data}')
async def post_email(data:EmailJSON):
    return f'Se recibio una peticion {data.email_from.email}'
