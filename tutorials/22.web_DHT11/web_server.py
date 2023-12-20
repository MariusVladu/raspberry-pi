import os
from bottle import route, run, template, TEMPLATE_PATH
import dht11_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/refresh")
def refresh():
    humidity, temperature = dht11_service.get_humidity_temperature()
    return {
        "humidity": humidity,
        "temperature": temperature,
    }


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    dht11_service.dispose()
