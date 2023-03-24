from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession 

from database import get_db
from schemas import DeleteItem
import models


router = APIRouter(
    prefix="/delete",
)


@router.delete("/{id}", response_model=DeleteItem, tags=['Базовые задачи'], status_code=status.HTTP_200_OK)
async def delete_item(id: str, db: AsyncSession = Depends(get_db)) -> DeleteItem:
    async with db.begin():
        item_to_delete = await db.execute(select(models.Item).where(models.Item.id == id))
        item_to_delete = item_to_delete.scalar()

        if item_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")
        
        await db.delete(item_to_delete)

    return item_to_delete