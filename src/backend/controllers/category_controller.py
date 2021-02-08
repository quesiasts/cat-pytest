import sys
sys.path.append('.')
from src.backend.dao.category_dao import CategoryDao
from src.backend.controllers.base_controller import BaseController

class CategoryController(BaseController):
    def __init__(self) -> None:
        super().__init__(CategoryDao)
