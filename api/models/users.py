__all__ = [
    "BaseUser",
    "LoginUser",
    "PublicStoredUser",
    "PrivateStoredUser",
    "CreationUser",
    "UpdationUser",
]

from enum import Enum

from pydantic import BaseModel, Field, AliasChoices
from pydantic_mongo import PydanticObjectId


class CreationRole(str, Enum):
    customer = "customer"
    seller = "seller"


class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    seller = "seller"


class BaseUser(BaseModel):
    username: str
    role: Role = Role.customer
    name: str | None = Field(default=None)
    email: str = Field(default=None)
    image: str | None = Field(default=None)


class UpdationUser(BaseUser):
    username: str = Field(default=None)
    role: Role = Field(default=None)
    name: str | None = Field(default=None)
    email: str = Field(default=None)
    image: str | None = Field(default=None)


class CreationUser(BaseUser):
    role: CreationRole = CreationRole.customer
    password: str


class LoginUser(BaseModel):
    username: str
    password: str

#usuario que existe en base de datos y que tiene la data que yo le puedo devolver al cliente
class PublicStoredUser(BaseUser):
    id: PydanticObjectId = Field(validation_alias=AliasChoices("_id", "id"))

#usuario que existe en base de datos con el hash password, pero esta info se mantendra privada
class PrivateStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
