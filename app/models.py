from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = 'items'

    id        =  Column(String(255), primary_key=True)
    type      =  Column(String(6),   nullable=False)
    size      =  Column(Integer,     nullable=False, default=0)
    date      =  Column(String(255), nullable=False)
    parentId  =  Column(String(255))
    url       =  Column(String(255))