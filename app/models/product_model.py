from pydantic import BaseModel
from typing import Literal


class ProductModel(BaseModel):
    name: str
    type: Literal['product', 'service']
    description: str
    link_product: str
    price: int
    url_img_product: str
