#!/usr/bin/python3

""" a script that starts a flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'state_id': '0'})
@app.route('/states/<state_id>')
def cities_in_state(state_id):
    """ cities in a state given the id """
    if state_id == '0':
        states = list(storage.all(State).values())
        states.sort(key=lambda x: x.name)
        return render_template("9-states.html", myObject=states)
    else:
        states = storage.all(State)
        key = "State."
        key += state_id
        state = states[key]
        return render_template("9-states.html", myObject=state)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the database again at the end of the request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
