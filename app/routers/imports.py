from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import CreateItem
import models
import utils


router = APIRouter()


@router.post("/imports", response_model=Dict, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
async def create_item(data: CreateItem, db: AsyncSession = Depends(get_db)) -> CreateItem:
    data_dict = data.dict()

    items = data_dict.get('items')
    update_date = data_dict.get('updateDate')

    for item in items:
        if await utils.is_item_exist_in_db(item, db):
            item_to_update = await db.execute(select(models.Item).where(models.Item.id == item.get('id')))
            item_to_update = item_to_update.scalar()

            item_to_update.type = item.get('type')
            item_to_update.size = item.get('size')
            item_to_update.date = update_date
            item_to_update.parentId = item.get('parentId')
            item_to_update.url = item.get('url')

            await utils.update_all_folders_date(item_to_update, db)

            await db.commit()
        else:
            new_item = models.Item(
                id=item.get('id'),
                type=item.get('type'),
                size=item.get('size'),
                date=update_date,
                parentId=item.get('parentId'),
                url=item.get('url')
            )

            await utils.update_all_folders_date(new_item, db)

            db.add(new_item)
            await db.commit()

    return data


@router.put("/imports", response_model=Dict, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
async def update_item(data: CreateItem, db: AsyncSession = Depends(get_db)) -> CreateItem:
    data_dict = data.dict()

    items = data_dict.get('items')
    update_date = data_dict.get('updateDate')

    for item in items:
        item_to_update = await db.execute(select(models.Item).where(models.Item.id == item.get('id')))
        item_to_update = item_to_update.scalar()

        if item_to_update is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        else:
            item_to_update.type = item.get('type')
            item_to_update.size = item.get('size')
            item_to_update.date = update_date
            item_to_update.parentId = item.get('parentId')
            item_to_update.url = item.get('url')
            
            await utils.update_all_folders_date(item_to_update, db)
            await db.commit()

    return data