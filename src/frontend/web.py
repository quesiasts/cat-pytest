import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect
from src.backend.controllers.category_controller import CategoryController
from src.backend.models.category import Category

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/create', methods=['GET'])
def add_category():
    return render_template('create_category.html')


@app.route('/category', methods=['GET'])
def list_category():
    categories = CategoryController().read_all()
    return render_template('list_category.html', categories=categories)


@app.route('/category', methods=['POST'])
def create_category():
    name = request.form.get('name')
    description = request.form.get('description')
    category = Category(name, description)
    CategoryController().create(category)
    return redirect('list_category')


@app.route('/category/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    category = CategoryController().read_by_id(id)
    if request.method == "POST":
        category.name = request.form.get('name')
        category.description = request.form.get('description')
        CategoryController().update(category)
        return redirect('list_category')
    return render_template('edit_category.html', category=category)


@app.route('/category/<int:id>/delete', methods=['GET'])
def delete_category(id: int):
    category = CategoryController().read_by_id(id)
    CategoryController().delete(category)
    return redirect('list_category')

                        
app.run(debug=True)
