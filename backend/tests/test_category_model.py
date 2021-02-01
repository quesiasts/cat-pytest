import sys
sys.path.append('.')

import pytest
from backend.models.category import Category


class TestCategory():
    name = "automotivo"
    description = "melhores coisas de veículos para você"

    @pytest.mark.parametrize("name, description", [
        ("categoria boa", "bem boa"),
        ("categoria massa", "muito massa"),
        ("categoria", "bem descrita")
    ])
    def test_create_instance(self, name, description):
        category = Category(name, description)
        assert isinstance(category, Category)

    @pytest.mark.parametrize("name", ["", " ", " " * 50])
    def test_name_empty(self, name):
        with pytest.raises(ValueError):
            category = Category(name, self.description)

    @pytest.mark.parametrize("name", [1, 3.14, ("tu", "pla"), ["lista"]])
    def test_name_not_string(self, name):
        with pytest.raises(TypeError):
            category = Category(name, self.description)

    @pytest.mark.parametrize("name", ["a" * 500, "b" * 250])
    def test_name_length(self, name):
        with pytest.raises(ValueError):
            category = Category(name, self.description)

    @pytest.mark.parametrize("description", [
        1, 3.14, ("tu", "pla"), ["lista"]
    ])
    def test_description_not_string(self, description):
        with pytest.raises(TypeError):
            category = Category(self.name, description)

    @pytest.mark.parametrize("description", ["a" * 500, "b" * 258])
    def test_description_length(self, description):
        with pytest.raises(ValueError):
            category = Category(self.name, description)
