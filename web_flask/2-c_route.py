#!/usr/bin/python3
""" C route module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """ Route that take variable """

    _text = text.replace('_', ' ')

    return "C {}".format(_text)


if __name__ == "__main__":
    # python3 -m web_flask.1-hbnb_route
    app.run(host='0.0.0.0', port=5000)
