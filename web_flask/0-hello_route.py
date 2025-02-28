#!/usr/bin/python3
"""This module starts a Flask web application"""""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
