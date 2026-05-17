# Δηλώνουμε τα routes που θα χρησιμοποιήσουμε στο API μας
from flask import Flask

from api.resources.Categories import create_category, delete_category, get_categories, get_category, update_category
from api.resources.Comments import create_comment, get_comments
from api.resources.Problems import create_problem, delete_problem, get_problem, get_problems, update_problem
from api.resources.States import create_state, delete_state, get_state, get_states, update_state

def define_routes(app : Flask):
    app.add_url_rule('/states', methods = ['GET'], view_func = get_states)
    app.add_url_rule('/states/<string:id>', methods = ['GET'], view_func = get_state)
    app.add_url_rule('/states', methods = ['POST'], view_func = create_state)
    app.add_url_rule('/states/<string:id>', methods = ['PUT'], view_func = update_state)
    app.add_url_rule('/states/<string:id>', methods = ['DELETE'], view_func = delete_state)

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
    app.add_url_rule('/problems/<string:problemId>/comments', methods = ['GET'], view_func = get_comments)
    app.add_url_rule('/problems/<string:problemId>/comments', methods = ['POST'], view_func = create_comment)