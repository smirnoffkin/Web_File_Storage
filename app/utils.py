from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
import models


# for imports

def is_item_exist_in_db(item: dict, db: Session = Depends(get_db)) -> bool:
    db_item = db.query(models.Item).filter(models.Item.id == item.get('id')).first()
    return False if db_item is None else True


def update_all_folders_date(item: models.Item, db: Session = Depends(get_db)) -> None:
    parent = db.query(models.Item).filter(models.Item.id == item.parentId).first()

    if parent:
        parent.date = item.date
        update_all_folders_date(parent, db)


# for nodes

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


def get_all_children_list(item_dict: dict, db: Session = Depends(get_db)) -> list:
    items = db.query(models.Item).filter(models.Item.parentId == item_dict.get('id')).all()

    for i in range(len(items)):
        items[i] = convert_models_class_to_dict(items[i])

    if items:
        for item in items:
            item['children'] = get_all_children_list(item, db)
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