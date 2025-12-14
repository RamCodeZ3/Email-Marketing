from setting.supabase_client import supabase
from model.schemas import EmailMode


async def get_all_emails():
    try:
        response = (
            supabase.table("emails")
                .select("*")
                .execute()
        )
        print("✅ Se consiguieron los emails con éxito")
        return response.data or []
    
    except Exception as e:
        print("❌ Hubo un error consiguiendo los emails")
        return f"Hubo un error recibiendo los datos: {e}"
    

async def get_email_by_id(email_id: int):
    try:
        response = (
            supabase.table("emails")
                .select("*")
                .eq('id', email_id)
                .execute()
        )

        print(f"✅ Se consiguió el email con id {email_id} con éxito")
        return response.data
    
    except Exception as e:
        print(f"❌ Hubo un error consiguiendo el email con id {email_id}")
        return f"Hubo un error recibiendo los datos: {e}"


async def create_email(data: EmailMode):
    try:
        response = (
            supabase.table("emails")
                .insert(data.model_dump())
                .execute()
        )

        print("✅ Se añadió el nuevo email con éxito a la base de datos")
        return "Se añadió el nuevo email con éxito a la base de datos."
    
    except Exception as e:
        print("❌ Hubo un error añadiendo el nuevo email")
        return f"Hubo un error añadiendo el nuevo email: {e}"


async def update_email_by_id(email_id: int, data: EmailMode):
    try:
        response = (
            supabase.table("emails")
                .update(data)
                .eq('id', email_id)
                .execute()
        )

        print(f"✅ Se actualizó el email con id {email_id} con éxito")
        return "Se actualizó el email con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error actualizando el email con id {email_id}")
        return f"Hubo un error actualizando el email: {e}"


async def delete_email_by_id(email_id: int):
    try:
        response = (
            supabase.table("emails")
                .delete()
                .eq('id', email_id)
                .execute()
        )

        print(f"✅ Se eliminó el email con id {email_id} con éxito")
        return "Se eliminó el email con éxito."
    
    except Exception as e:
        print(f"❌ Hubo un error eliminando el email con id {email_id}")
        return f"Hubo un error eliminando el email: {e}"
