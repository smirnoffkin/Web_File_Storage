from typing import Optional, List

from pydantic import BaseModel


class BaseItem(BaseModel):
    id: str
    type: str
    size: int = 0
    parentId: Optional[str] = None
    url: Optional[str] = None

    class Config:
        orm_mode = True


class Item(BaseItem):
    pass


class CreateItem(BaseModel):
    items: List[Item]
    updateDate: str

    class Config:
        orm_mode = True


class GetItem(BaseItem):
    date: str
    children: Optional[list] = None


class DeleteItem(BaseModel):
    id: str

    class Config:
        orm_mode = True
