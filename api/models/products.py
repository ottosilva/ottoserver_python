__all__ = ["Product", "StoredProduct", "UpdationProduct"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Product(BaseModel):
    seller_id: str
    name: str
    price: float
    quantity: int
    description: str = Field(default=None)
    image: str = Field(default=None)


class UpdationProduct(BaseModel):
    seller_id: PydanticObjectId = Field(default=None)
    name: str = Field(default=None)
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    description: str = Field(default=None)
    image: str = Field(default=None)


class StoredProduct(Product):
    # Otros nombres que podria recibir esta clase son:
    # DatabaseProduct: Indica que el producto proviene de una base de datos.
    # PersistedProduct: Representa un producto que ha sido persistido o almacenado en algún tipo de almacenamiento
    # SavedProduct: Hace referencia a un producto que ha sido guardado en un almacenamiento permanente.
    id: PydanticObjectId = Field(alias="_id")
