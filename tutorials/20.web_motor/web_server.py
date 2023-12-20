import os
from bottle import route, run, template, request, TEMPLATE_PATH
import motor_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/forward", method="POST")
def forward():
    speed = int(request.POST.get("speed"))
    motor_service.turn_on_forward(speed)


@route("/backward", method="POST")
def backward():
    speed = int(request.POST.get("speed"))
    motor_service.turn_on_backward(speed)


@route("/stop")
def stop():
    motor_service.turn_off()


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    motor_service.dispose()
