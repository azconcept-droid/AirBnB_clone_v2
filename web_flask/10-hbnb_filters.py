#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ filter states and amenities """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5007)
