from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import GetItem
import models
import utils


router = APIRouter(
    prefix="/nodes"
)


@router.get("/", response_model=List[GetItem], tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
async def get_all_items(db: AsyncSession = Depends(get_db)) -> list:
    items = await db.execute(select(models.Item))
    items = list(items.scalars().all())

    return items


@router.get("/{id}", response_model=GetItem, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
async def get_item(id: str, db: AsyncSession = Depends(get_db)) -> GetItem:
    item = await db.execute(select(models.Item).where(models.Item.id == id))
    item = item.scalar()

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    item_dict = utils.convert_models_class_to_dict(item)
    children_list = await utils.get_all_children_list(item_dict, db)

    if item_dict['type'] == 'FOLDER':
        item_dict['size'] = utils.get_full_size_root_folder(children_list)
    item_dict['children'] = children_list

    return item_dict