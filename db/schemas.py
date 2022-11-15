

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    name: str
    email: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Client(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    user_id: int
    payment_method: bool = False
    phone_number: str
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ClientResponse(BaseModel):
    user: User
    client: Client

class Employee(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    user_id: int
    salon_id: int
    is_manager: bool
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Salon(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    employee_id: int
    name: str
    phone_number: str
    description: str
    address_id: str
    opening_hours: str
    type_id: str
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

