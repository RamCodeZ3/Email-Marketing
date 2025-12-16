from fastapi import APIRouter
from model.schemas import ProductModel
from services import product_service as ps


routes = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@routes.get('/get-all')
async def get_all_products():
    try:
        return await ps.get_all_products()
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.get('/get/{product_id}')
async def get_product_by_id(product_id: int):
    try:
        return await ps.get_product_by_id(product_id)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.post('/create-product')
async def create_product(data: ProductModel):
    try:
        return await ps.create_product(data)
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.put('/update/{product_id}')
async def update_product(product_id: int):
    try:
        await ps.update_product_by_id(product_id)
        return "Se actualizo el producto con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')


@routes.delete('/delete/{product_id}')
async def delete_product(product_id: int):
    try:
        await ps.delete_product_by_id(product_id)
        return "Se Elimino el producto con éxito"
    
    except Exception as e:
        print(f'❌ Hubo un error realizando la peticion: {e}')
