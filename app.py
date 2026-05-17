# Εκκινεί την εφαρμογή
from flask import Flask

from api.routes.all import define_routes

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

define_routes(app)

if __name__ == '__main__':
    app.run(debug=False)