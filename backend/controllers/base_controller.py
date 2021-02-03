from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel
from backend.models.category import Category


class BaseController():
    def __init__(self, dao: BaseDao) -> None:
        self.__dao = dao
    

    def create(self, model) -> BaseModel:
        if isinstance(model, BaseModel):
            result = self.__dao().save(model)
            return result
        else:
            raise TypeError("Model must be class BaseModel")
    

    def update(self, model: BaseModel) -> BaseModel:
        if isinstance(model, BaseModel):
            read = self.__dao().read_by_id(model.id)
            result = self.__dao().save(model)
            return result
        else:
            raise TypeError("Model must be class BaseModel")
    

    def read_all(self) -> list:
        result = self.__dao().read_all()
        return result
    

    def read_by_id(self, id: int) -> BaseModel:
        if isinstance(id, int):
            result = self.__dao().read_by_id(id)
            if result:
                return result
            raise Exception("Id not found")
        else:
            raise TypeError("Id must be Integer")
    
    
    def delete(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            result = self.__dao().read_by_id(model.id)
            self.__dao().delete(model)
        else:
            raise TypeError("Model must be class BaseModel")