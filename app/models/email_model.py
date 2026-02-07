from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date


class EmailModel(BaseModel):
    name_company: Optional[str] = None
    title: str
    body: Optional[str] = None
    product_id: int
    status: Optional[Literal['sent', 'pendient']] = None
    date_send: Optional[date] = None