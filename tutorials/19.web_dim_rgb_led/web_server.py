import os
from bottle import route, run, template, request, TEMPLATE_PATH
import led_service

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))


@route("/")
def index():
    return template("index.html")


@route("/rgb-led", method="POST")
def led():
    color_component = request.POST.get("color_component")
    brightness = int(request.POST.get("brightness"))
    led_service.set_rgb_component_brightness(color_component, brightness)


try:
    run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    pass
finally:
    led_service.dispose()
