#!/usr/bin/python3

""" a script that starts a flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states_list')
def route_state():
    """ a route to the state """
    from models.state import State
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """ closes the database again at the end of the request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
