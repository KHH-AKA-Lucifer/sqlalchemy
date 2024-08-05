# import datatype and column to create tables
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
# import relationship to create relationship between tables
from sqlalchemy.orm import relationship
# import base from database.py
# inherit from it
from .database import Base 

class User(Base):

    # table name
    __tablename__ = "users"
    # columns 
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # relationship to items table
    items = relationship("Item", back_popualtes="owner")

class Item(Base):

    # table name 
    __tablename__ = "items"
    # columns 
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # relationship to users table
    owner = relationship("User", back_populates="items")