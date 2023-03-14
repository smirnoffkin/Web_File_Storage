from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas


router = APIRouter(
    prefix="/delete",
)


@router.delete("/{id}", response_model=schemas.DeleteItem, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
def delete_item(id: str, db: Session = Depends(get_db)) -> schemas.DeleteItem:
    item_to_delete = db.query(models.Item).filter(models.Item.id == id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete