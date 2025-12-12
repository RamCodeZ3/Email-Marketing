from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import date


class EmailJSON(BaseModel):
    name_company: Optional[str] = None
    title: str
    receiver_list: List[str]
    product_id: int
    status: Literal['sent', 'pendient']
    date_send: date


class Product(BaseModel):
    name_product: str
    type: Literal['product', 'service']
    description: str
    link_product: str
    price: int
    url_img_product: str
