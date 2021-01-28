from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

@validates('name')
def validate_name(self, key, name):
    if not name:
        raise ValueError("Name can't be empty")
    if not name:
        raise TypeError("Name can't be numbers")
    if not len(name) > 100:
        raise ValueError("Name can't be more than 100 characters")

category = Category('name', 'category description')