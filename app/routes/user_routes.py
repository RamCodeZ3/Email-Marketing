from fastapi import APIRouter
from models.user_model import UserModel
from services import user_service as us


routes = APIRouter(
    prefix="/user",
    tags=["User"]
)


@routes.get('/get-all')
async def get_all_users():
    try:
        return await us.get_all_users()
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la petición: {e}')


@routes.get('/get/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        return await us.get_user_by_id(user_id)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la petición: {e}')


@routes.post('/create-user')
async def create_user(data: UserModel):
    try:
        return await us.create_user(data)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la petición: {e}')


@routes.put('/update/{user_id}')
async def update_user(user_id: int, data: UserModel):
    try:
        await us.update_user_by_id(user_id, data)
        return "✅ El usuario se actualizó con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la petición: {e}')


@routes.delete('/delete/{user_id}')
async def delete_user(user_id: int):
    try:
        await us.delete_user_by_id(user_id)
        return "✅ El usuario se eliminó con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la petición: {e}')
