from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base


class Item(Base):
    __tablename__ = 'items'

    id        =  Column(String(255), primary_key=True)
    type      =  Column(String(6),   nullable=False)
    size      =  Column(Integer,     nullable=False, default=0)
    date      =  Column(String(255), nullable=False)
    parentId  =  Column(String(255))
    url       =  Column(String(255))


class User(Base):
    __tablename__ = 'users'

    id          =  Column(Integer, primary_key=True)
    email       =  Column(String(255), nullable=False, unique=True)
    password    =  Column(String(255), nullable=False)
    created_at  =  Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))