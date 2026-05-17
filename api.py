# Εκκινεί την εφαρμογή
from flask import Flask

from routes import define_routes

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

define_routes(app)

if __name__ == '__main__':
    app.run(debug=False)