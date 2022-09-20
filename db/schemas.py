

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