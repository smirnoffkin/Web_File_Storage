from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import ItemImportRequest
import oauth2
import models
import utils


router = APIRouter()


@router.post("/imports", response_model=Dict, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
def create_item(data: ItemImportRequest, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)) -> ItemImportRequest:
    data_dict = data.dict()

    items = data_dict.get('items')
    update_date = data_dict.get('updateDate')

    for item in items:
        if utils.is_item_exist_in_db(item, db):
            item_to_update = db.query(models.Item).filter(models.Item.id == item.get('id')).first()
            item_to_update.type = item.get('type')
            item_to_update.size = item.get('size')
            item_to_update.date = update_date
            item_to_update.parentId = item.get('parentId')
            item_to_update.url = item.get('url')

            utils.update_all_folders_date(item_to_update, db)

            db.commit()
        else:
            new_item = models.Item(
                id = item.get('id'),
                type = item.get('type'),
                size = item.get('size'),
                date = update_date,
                parentId = item.get('parentId'),
                url = item.get('url')
            )

            utils.update_all_folders_date(new_item, db)

            db.add(new_item)
            db.commit()

    return data


@router.put("/imports", response_model=Dict, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
def update_item(data: ItemImportRequest, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)) -> ItemImportRequest:
    data_dict = data.dict()

    items = data_dict.get('items')
    update_date = data_dict.get('updateDate')

    for item in items:
        item_to_update = db.query(models.Item).filter(models.Item.id == item.get('id')).first()

        if item_to_update is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        else:
            item_to_update.type = item.get('type')
            item_to_update.size = item.get('size')
            item_to_update.date = update_date
            item_to_update.parentId = item.get('parentId')
            item_to_update.url = item.get('url')

            utils.update_all_folders_date(item_to_update, db)
            db.commit()

    return data