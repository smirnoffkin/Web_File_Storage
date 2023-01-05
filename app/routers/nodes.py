from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import Item
import oauth2
import models
import utils


router = APIRouter(
    prefix="/nodes"
)


@router.get("/", response_model=List[Item], tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
def get_all_items(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)) -> list:
    items = db.query(models.Item).all()
    return items


@router.get("/{id}", response_model=Item, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
def get_item(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)) -> Item:
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    item_dict = utils.convert_models_class_to_dict(item)
    children_list = utils.get_all_children_list(item_dict, db)

    if item_dict['type'] == 'FOLDER':
        item_dict['size'] = utils.get_full_size_root_folder(children_list)
    item_dict['children'] = children_list

    return item_dict