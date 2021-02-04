from src.backend.dao.base_dao import BaseDao
from src.backend.models.category import Category


class CategoryDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Category)