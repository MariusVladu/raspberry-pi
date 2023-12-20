import os
from bottle import route, run, template, request, TEMPLATE_PATH
import buzzer_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/buzzer", method="POST")
def buzzer():
    state = request.POST.get("state")
    if state == "on":
        buzzer_service.turn_on()
    else:
        buzzer_service.turn_off()


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    buzzer_service.dispose()
