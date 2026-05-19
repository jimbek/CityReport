# Defines the API endpoints and their corresponding controller functions.
# This file serves as the entry point for the Flask application and routes.
from flask import Flask

from routes.Categories import get_categories, get_category
from routes.Comments import create_comment, get_comments
from routes.Problems import create_problem, delete_problem, get_problem, get_problems, update_problem
from routes.States import get_state, get_states

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        You can find all available endpoints at collections.json file in the root directory of this project.
        For example, to get all categories, send a GET request to /categories endpoint.
    '''

app.add_url_rule('/states', methods = ['GET'], view_func = get_states)
app.add_url_rule('/states/<string:id>', methods = ['GET'], view_func = get_state)

app.add_url_rule('/categories', methods = ['GET'], view_func = get_categories)
app.add_url_rule('/categories/<string:id>', methods = ['GET'], view_func = get_category)

app.add_url_rule('/problems', methods = ['GET'], view_func = get_problems)
app.add_url_rule('/problems/<string:id>', methods = ['GET'], view_func = get_problem)
app.add_url_rule('/problems', methods = ['POST'], view_func = create_problem)
app.add_url_rule('/problems/<string:id>', methods = ['PUT'], view_func = update_problem)
app.add_url_rule('/problems/<string:id>', methods = ['DELETE'], view_func = delete_problem)
app.add_url_rule('/problems/<string:problemId>/comments', methods = ['GET'], view_func = get_comments)
app.add_url_rule('/problems/<string:problemId>/comments', methods = ['POST'], view_func = create_comment)

if __name__ == '__main__':
    app.run(debug = False)