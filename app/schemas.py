from pydantic import BaseModel
from typing import Optional, List


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