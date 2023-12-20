import os
from bottle import route, run, template, TEMPLATE_PATH
import distance_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/refresh")
def refresh():
    distance = distance_service.detect_distance_cm()
    return "%d" % distance


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    distance_service.dispose()
