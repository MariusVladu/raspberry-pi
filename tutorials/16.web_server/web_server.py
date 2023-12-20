import os
from bottle import route, run, template, TEMPLATE_PATH

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/hello-world")
def hello():
    return template("hello")


run(host="0.0.0.0", port=5000, debug=True)
