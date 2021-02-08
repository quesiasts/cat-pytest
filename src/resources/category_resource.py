from flask_restful import fields,marshal_with
from src.backend.dao.category_dao import CategoryDao
from src.backend.models.category import Category
from src.resources.base_resource import BaseResource

class CategoryResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "name": fields.String,
        "description": fields.String
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model_type = Category
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)