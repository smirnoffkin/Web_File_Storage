from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
import models


# for POST request

async def is_item_exist_in_db(item: dict, db: AsyncSession = Depends(get_db)) -> bool:
    db_item = await db.execute(select(models.Item).where(models.Item.id == item.get('id')))
    db_item = db_item.scalar()
    return False if db_item is None else True


async def update_all_folders_date(item: models.Item, db: AsyncSession = Depends(get_db)) -> None:
    parent = await db.execute(select(models.Item).where(models.Item.id == item.parentId))
    parent = parent.scalar()

    if parent:
        parent.date = item.date
        await update_all_folders_date(parent, db)


# for GET request

def convert_models_class_to_dict(item: models.Item) -> dict:
    item_dict = {
        'id': item.id,
        'type': item.type,
        'size': item.size,
        'parentId': item.parentId,
        'url': item.url,
        'date': item.date,
        'children': None
    }
    return item_dict


async def get_all_children_list(item_dict: dict, db: AsyncSession = Depends(get_db)) -> list:
    items = await db.execute(select(models.Item).where(models.Item.parentId == item_dict.get('id')))
    items = list(items.scalars())

    for i in range(len(items)):
        items[i] = convert_models_class_to_dict(items[i])

    if items:
        for item in items:
            item['children'] = await get_all_children_list(item, db)
            if item['type'] == 'FOLDER':
                item['size'] = sum_size(item['children'])
    else:
        return None

    return items


def get_full_size_root_folder(children: list) -> int:
    full_folder_size = 0
    for child in children:
        full_folder_size += child['size']
    return full_folder_size


def sum_size(children: list) -> int:
    result = 0
    for i in range(len(children)):
        result += children[i]['size']
    return result