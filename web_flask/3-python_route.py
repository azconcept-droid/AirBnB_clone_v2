#!/usr/bin/python3
""" Python route module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Say hello hbnb """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Say hbnb """

    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """ Say C <text> """

    _text = text.replace('_', ' ')

    return "C {}".format(_text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text):
    """ Return custom python message """

    _text = text.replace('_', ' ')

    return "Python {}".format(_text)


if __name__ == "__main__":
    # python3 -m web_flask.2-c_route
    app.run(host='0.0.0.0', port=5000)
