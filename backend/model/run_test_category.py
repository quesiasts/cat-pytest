from category import Category

class TestCategory(Category):
    name = 1
    description = "melhores coisas de veículos para você jdfklfjlsflsfs"

def test_blank_name(self, name):
    if Category.name == int:
        try:
            print('Please, put a valid name')
        except Exception as error:
            assert isinstance(ValueError)

def test_description_bigger_100(self, description):
    if Category.description > len(100):
        try:
            print('Please, descriptions only 100 characters')
        except Exception as error:
            assert isinstance(error, ValueError)