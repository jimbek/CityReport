# Εκκινεί την εφαρμογή
from flask import Flask

from routes.problems import create_problem, get_problem, get_problems, update_problem

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

app.add_url_rule('/problems', methods = ['GET'], view_func = get_problems)
app.add_url_rule('/problems/<int:id>', methods = ['GET'], view_func = get_problem)
app.add_url_rule('/problems', methods = ['POST'], view_func = create_problem)
app.add_url_rule('/problems/<int:id>', methods = ['PUT'], view_func = update_problem)

if __name__ == '__main__':
    app.run(debug=False)