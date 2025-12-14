from setting.supabase_client import supabase
from model.schemas import UserModel


async def get_all_users():
    try:
        response = (
            supabase.table("users")
                .select("*")
                .execute()
        )
        print("✅ Se consiguieron los usuarios con éxito")
        return response.data or []
    
    except Exception as e:
        print("❌ Hubo un error consiguiendo los usuarios")
        return f"Hubo un error recibiendo los datos: {e}"
    

async def get_user_by_id(user_id: int):
    try:
        response = (
            supabase.table("users")
                .select("*")
                .eq('id', user_id)
                .execute()
        )

        print(f"✅ Se consiguió el usuario con id {user_id} con éxito")
        return response.data
    
    except Exception as e:
        print(f"❌ Hubo un error consiguiendo el usuario con id {user_id}")
        return f"Hubo un error recibiendo los datos: {e}"


async def create_user(data: UserModel):
    try:
        response = (
            supabase.table("users")
                .insert(data.model_dump())
                .execute()
        )

        print("✅ Se añadió el nuevo usuario con éxito a la base de datos")
        return "Se añadió el nuevo usuario con éxito a la base de datos."
    
    except Exception as e:
        print("❌ Hubo un error añadiendo el nuevo usuario")
        return f"Hubo un error añadiendo el nuevo usuario: {e}"


async def update_user_by_id(user_id: int, data: UserModel):
    try:
        response = (
            supabase.table("users")
                .update(data.model_dump())
                .eq('id', user_id)
                .execute()
        )

        print(f"✅ Se actualizó el usuario con id {user_id} con éxito")
        return "Se actualizó el usuario con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error actualizando el usuario con id {user_id}")
        return f"Hubo un error actualizando el usuario: {e}"


async def delete_user_by_id(user_id: int):
    try:
        response = (
            supabase.table("users")
                .delete()
                .eq('id', user_id)
                .execute()
        )

        print(f"✅ Se eliminó el usuario con id {user_id} con éxito")
        return "Se eliminó el usuario con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error eliminando el usuario con id {user_id}")
        return f"Hubo un error eliminando el usuario: {e}"
