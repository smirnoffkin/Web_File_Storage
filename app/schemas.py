from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class BaseItemClass(BaseModel):
    id: str
    type: str
    size: int = 0
    parentId: Optional[str] = None
    url: Optional[str] = None

    class Config:
        orm_mode=True


class Item(BaseItemClass):
    date: str
    children: Optional[list] = None


class ItemImport(BaseItemClass):
    pass


class ItemImportRequest(BaseModel):
    items: List[ItemImport]
    updateDate: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None