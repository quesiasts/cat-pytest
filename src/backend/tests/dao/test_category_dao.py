import sys
sys.path.append('.')

import pytest
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.backend.models.category import Category
from src.backend.dao.category_dao import CategoryDao


class TestCategoryDao:
    @pytest.fixture
    def category_instance(self) -> Category:
        return Category('Nome', 'Descrição')
    
    
    def test_create_instance(self, category_instance) -> None:
        assert isinstance(CategoryDao(), CategoryDao)
    
    
    def test_save(self, category_instance) -> None:
        result = CategoryDao().save(category_instance)
        assert isinstance(result, Category)
        CategoryDao().delete(result)
    

    def test_not_save(self) -> None:
        with pytest.raises(UnmappedInstanceError):
            result = CategoryDao().save('error')
    

    def test_read_all(self) -> None:
        result = CategoryDao().read_all()
        assert isinstance(result, list)
        assert all(isinstance(item, Category) for item in result)
    

    def test_read_by_id(self, category_instance) -> None:
        create = CategoryDao().save(category_instance)
        result = CategoryDao().read_by_id(create.id)
        assert isinstance(result, Category)
        CategoryDao().delete(result)
    

    def test_not_read_by_id(self) -> None:
        result = CategoryDao().read_by_id(999999999999999)
        assert result is None
    

    @pytest.mark.parametrize('errors', ['error', [], ()])
    def test_read_by_id_TypeError(self, errors) -> None:
        with pytest.raises(TypeError):
            result = CategoryDao().read_by_id(errors)
    
    
    def test_delete(self, category_instance) -> None:
        create = CategoryDao().save(category_instance)
        CategoryDao().delete(create)
        result = CategoryDao().read_by_id(create.id)
        assert result is None
    
    @pytest.mark.parametrize('errors', ['error', 9.0, [], (), True, 1])
    def test_not_delete(self, errors) -> None:
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().delete(errors)