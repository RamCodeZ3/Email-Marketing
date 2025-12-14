from services.setting.supabase_client import supabase
from model.schemas import ProductModel
from typing import Literal


async def get_all_products():
    try:
        response = (
            supabase.table("products")
                .select("*")
                .execute()
        )
        print("✅ Se consiguieron los productos con éxito")
        return response.data or []
    
    except Exception as e:
        print("❌ Hubo un error consiguiendo los productos")
        return f"Hubo un error recibiendo los datos: {e}"


async def get_product_by_id(product_type: int):
    try:
        response = (
            supabase.table("products")
                .select("*")
                .eq('id', product_type)
                .execute()
        )

        print(f"✅ Se consiguió el producto con id {product_type} con éxito")
        return response.data
    
    except Exception as e:
        print(f"❌ Hubo un error consiguiendo el producto con id {product_type}")
        return f"Hubo un error recibiendo los datos: {e}"


async def get_product_by_type(product_type: Literal["product", "service"]):
    try:
        response = (
            supabase.table("products")
                .select("*")
                .eq('type', product_type)
                .execute()
        )

        print(f"✅ Se consiguió el producto de tipo {product_type} con éxito")
        return response.data
    
    except Exception as e:
        print(f"❌ Hubo un error consiguiendo el producto del tipo {product_type}")
        return f"Hubo un error recibiendo los datos: {e}"


async def create_product(data: ProductModel):
    try:
        response = (
            supabase.table("products")
                .insert(data.model_dump())
                .execute()
        )

        print("✅ Se añadió el nuevo producto con éxito a la base de datos")
        return "Se añadió el nuevo producto con éxito a la base de datos."
    
    except Exception as e:
        print("❌ Hubo un error añadiendo el nuevo producto")
        return f"Hubo un error añadiendo el nuevo producto: {e}"


async def update_product_by_id(product_type: int, data: ProductModel):
    try:
        response = (
            supabase.table("products")
                .update(data.model_dump())
                .eq('id', product_type)
                .execute()
        )

        print(f"✅ Se actualizó el producto con id {product_type} con éxito")
        return "Se actualizó el producto con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error actualizando el producto con id {product_type}")
        return f"Hubo un error actualizando el producto: {e}"


async def delete_product_by_id(product_type: int):
    try:
        response = (
            supabase.table("products")
                .delete()
                .eq('id', product_type)
                .execute()
        )

        print(f"✅ Se eliminó el producto con id {product_type} con éxito")
        return "Se eliminó el producto con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error eliminando el producto con id {product_type}")
        return f"Hubo un error eliminando el producto: {e}"
