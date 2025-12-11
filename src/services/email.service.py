from setting.supabase_client import supabase
import asyncio


async def get_all_emails():
    data = (
        supabase
            .table("emails")
            .select("*")
            .execute()
        )
    print(data.data)

asyncio.run(get_all_emails())