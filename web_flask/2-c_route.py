#!/usr/bin/python3
"""This module starts a Flask web application"""""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"

#!/usr/bin/python3
"""start a flack server listening on port 5000 handling '/'"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """handling / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """handling hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """handling varible routes"""
    return f"C {escape(text.replace('_', ' '))}"

if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
