from category import Category

class TestCategory():
    name = 'automotivo'
    description = "melhores coisas de veículos para você"

def test_blank_name(self, name):
    if Category.name == int:
        try:
            print('Please, put a valid name')
        except Exception as error:
            assert isinstance(ValueError)

def test_description_bigger(self, description):
    if Category.description > len(255):
        try:
            print('Please, descriptions only 255 characters')
        except Exception as error:
            assert isinstance(error, ValueError)