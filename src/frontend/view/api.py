import sys
sys.path.append('.')
from flask import Flask
from flask_restful import Api
from src.resources.category_resource import CategoryResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, 'api/category/<int:id>', endpoint='categories')
api.add_resource(CategoryResource, 'api/category', endpoint='category')

@app.route('/api/category')
def home():
    return 'Bem vindo!'

app.run(debug=True)
