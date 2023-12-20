import os
from bottle import route, run, template, request, TEMPLATE_PATH
import led_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/led", method="POST")
def led():
    state = int(request.POST.get("state"))
    led_service.set_led_brightness(state)
    return "ok"


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    led_service.dispose()
