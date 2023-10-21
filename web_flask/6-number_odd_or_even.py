#!/usr/bin/python3

"""
a script that starts a flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ this is the homepage """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ this is the hbnb page """
    return "HBNB"


@app.route("/c/<text>")
def C(text):
    """ this is using the passed in var """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def Python(text="is_cool"):
    """ this is the python default route page """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>')
def number(n):
    """ shows the number passed """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ gives a html template page """
    myNumber = f"Number: {n}"
    return render_template('5-number.html', my_object=myNumber)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """ gives a html template page """
    ans = ""
    if n % 2 == 0:
        ans += 'even'
    else:
        ans += 'odd'

    myNumber = f"Number: {n} is {ans}"
    return render_template('5-number.html', my_object=myNumber)


if __name__ == "__main__":
    """ this is the unimportable script """
    app.run(host="0.0.0.0", port="5000")
