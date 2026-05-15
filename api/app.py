# Εκκινεί την εφαρμογή
from flask import Flask

from routes.Categories import create_category, delete_category, get_categories, get_category, update_category
from routes.problems import create_problem, delete_problem, get_problem, get_problems, update_problem

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

app.add_url_rule('/categories', methods = ['GET'], view_func = get_categories)
app.add_url_rule('/categories/<string:id>', methods = ['GET'], view_func = get_category)
app.add_url_rule('/categories', methods = ['POST'], view_func = create_category)
app.add_url_rule('/categories/<string:id>', methods = ['PUT'], view_func = update_category)
app.add_url_rule('/categories/<string:id>', methods = ['DELETE'], view_func = delete_category)

app.add_url_rule('/problems', methods = ['GET'], view_func = get_problems)
app.add_url_rule('/problems/<string:id>', methods = ['GET'], view_func = get_problem)
app.add_url_rule('/problems', methods = ['POST'], view_func = create_problem)
app.add_url_rule('/problems/<string:id>', methods = ['PUT'], view_func = update_problem)
app.add_url_rule('/problems/<string:id>', methods = ['DELETE'], view_func = delete_problem)

if __name__ == '__main__':
    app.run(debug=False)