from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import date


class EmailFrom(BaseModel):
    email: str
    name_company: Optional[str] = None


class Product(BaseModel):
    name_product: str
    type: Literal['product', 'service']
    title: str
    description: str
    link_product: str
    price: int
    url_img_product: str


class EmailJSON(BaseModel):
    email_from: EmailFrom
    receiver_list: List[str]
    product: Product
    date_send: date
