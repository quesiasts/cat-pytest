import sys
sys.path.append('.')

import pytest
from backend.models.category import Category


class TestCategory():
    name = 'automotivo'
    description = "melhores coisas de veículos para você"

    def test_blank_name(self):
        with pytest.raises(ValueError):
            category = Category('', self.description)

    def test_description_bigger(self):
        with pytest.raises(ValueError):
            category = Category(self.name, self.description * 200)
