from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import date


class EmailModel(BaseModel):
    name_company: Optional[str] = None
    title: str
    body: Optional[str] = None
    product_id: int
    status: Literal['sent', 'pendient']
    date_send: date


class ProductModel(BaseModel):
    name: str
    type: Literal['product', 'service']
    description: str
    link_product: str
    price: int
    url_img_product: str


class UserModel(BaseModel):
    name: str
    email: str
