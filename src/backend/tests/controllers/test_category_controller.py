import sys
sys.path.append('.')

import pytest
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.backend.models.category import Category
from src.backend.controllers.category_controller import CategoryController


class TestCategoryController:
    @pytest.fixture
    def category_instance(self) -> Category:
        return Category('Nome', 'Descrição')
    

    def test_create_instance(self, category_instance) -> None:
        assert isinstance(CategoryController(), CategoryController)
    
    
    def test_create(self, category_instance) -> None:
        c = category_instance
        result = CategoryController().create(c)
        assert isinstance(result, Category)
        CategoryController().delete(result)


    def test_not_create(self) -> None:
        with pytest.raises(TypeError):
            result = CategoryController().create('error')


    def test_update(self, category_instance) -> None:
        result = CategoryController().create(category_instance)
        result.name = 'update'
        result.description = 'update'
        result = CategoryController().update(result)
        assert isinstance(result, Category)
        assert result.name == 'update'
        assert result.description == 'update'
        CategoryController().delete(result)
    

    def test_not_update(self) -> None:
        with pytest.raises(TypeError):
            result = CategoryController().update('error')


    def test_read_all(self) -> None:
        result = CategoryController().read_all()
        assert isinstance(result, list)
        assert all(isinstance(item, Category) for item in result)
    

    def test_read_by_id(self, category_instance) -> None:
        create = CategoryController().create(category_instance)
        result = CategoryController().read_by_id(create.id)
        assert isinstance(result, Category)
        CategoryController().delete(result)
    

    def test_not_read_by_id(self) -> None:
        with pytest.raises(Exception) as exc:
            result = CategoryController().read_by_id(999999999999999)
            assert isinstance(exc.value, 'Id not found')
    

    @pytest.mark.parametrize('errors', ['error', [], ()])
    def test_read_by_id_TypeError(self, errors) -> None:
        with pytest.raises(TypeError):
            result = CategoryController().read_by_id(errors)
    
    
    def test_delete(self, category_instance) -> None:
        create = CategoryController().create(category_instance)
        CategoryController().delete(create)
        with pytest.raises(Exception) as exc:
            result = CategoryController().read_by_id(created.id)
            assert isinstance(exc.value, 'Id not found')
    
    
    @pytest.mark.parametrize('errors', ['error', 9.0, [], ()])
    def test_not_delete(self, errors) -> None:
        with pytest.raises(TypeError):
            CategoryController().delete(errors)