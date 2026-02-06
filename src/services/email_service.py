from services.setting.supabase_client import supabase
from model.schemas import EmailModel
from datetime import date


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


async def create_email(data: EmailModel):
    try:
        email_dict = data.model_dump(mode="json")
        # remove keys with None so DB defaults are preserved
        filtered = {k: v for k, v in email_dict.items() if v is not None}

        # If no status provided, default to 'pendient' so scheduler can pick it up
        if 'status' not in filtered:
            filtered['status'] = 'pendient'

        response = (
            supabase.table("emails")
                .insert(filtered)
                .execute()
        )

        print("✅ Se añadió el nuevo email con éxito a la base de datos")
        # return the inserted record (supabase returns it in response.data)
        return response.data[0] if response.data else response.data
    
    except Exception as e:
        print(f"❌ Hubo un error añadiendo el nuevo email: {e}")
        return f"Hubo un error añadiendo el nuevo email: {e}"


async def update_email_by_id(email_id: int, data: EmailModel):
    try:
        update_dict = data.model_dump(mode="json")
        # avoid overwriting fields with None
        filtered = {k: v for k, v in update_dict.items() if v is not None}

        response = (
            supabase.table("emails")
                .update(filtered)
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


async def get_pending_emails_for_today():
    try:
        today = date.today().isoformat()

        response = (
            supabase
            .table("emails")
            .select("*")
            .eq("status", "pendient")
            .eq("date_send", today)
            .execute()
        )
        return response.data or []
    
    except Exception as e:
        print(f"❌ Hubo un error obteniendo los emails:{e}")

async def mark_email_as_sent(email_id: int):
    try:
        response = (
            supabase
            .table("emails")
            .update({"status": "sent"})
            .eq("id", email_id)
            .execute()
        )

        return response.data

    except Exception as e:
        print(f"❌ Hubo un error actualizado los emails: {e}")    
