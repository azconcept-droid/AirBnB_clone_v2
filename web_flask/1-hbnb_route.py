#!/usr/bin/python3
""" HBNB route module """

from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Say hbnb"""

    return "HBNB"


if __name__ == "__main__":
    # python3 -m web_flask.1-hbnb_route
    app.run(host='0.0.0.0', port=5000)
