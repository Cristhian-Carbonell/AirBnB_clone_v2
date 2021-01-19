#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    replace = "C {}".format(escape(text))
    replace1 = replace.replace("_", " ")
    return replace1


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    replace = "Python {}".format(escape(text))
    replace1 = replace.replace("_", " ")
    return replace1


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(escape(n))

if __name__ == "__main__":
    app.run(debug=True)
