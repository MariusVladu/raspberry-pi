import os
from bottle import route, run, template, request, TEMPLATE_PATH
import led_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/led", method="POST")
def led():
    state = request.POST.get("state")
    if state == "on":
        led_service.turn_on()
    else:
        led_service.turn_off()
    return "ok"


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    led_service.dispose()
