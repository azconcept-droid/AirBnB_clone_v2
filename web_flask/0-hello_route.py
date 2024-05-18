#!/usr/bin/python3
""" Hello HBNB module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Say hello hbnb"""

    return "Hello HBNB!"


if __name__ == "__main__":
    # python3 -m web_flask.0-hello_route
    app.run(host='0.0.0.0', port=5000)
