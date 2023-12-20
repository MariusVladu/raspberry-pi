import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


def __init_pwm_led(pin):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 1000)
    pwm.start(0)
    return pwm


def set_rgb_component_brightness(component, brightness):
    if component == "r":
        __set_led_brightness(__red_led_pwm, brightness)
    if component == "g":
        __set_led_brightness(__green_led_pwm, brightness)
    if component == "b":
        __set_led_brightness(__blue_led_pwm, brightness)


def __set_led_brightness(led_pwm, brightness):
    brightness = min(max(0, brightness), 100)
    led_pwm.ChangeDutyCycle(brightness)


def dispose():
    GPIO.cleanup()


__red_led_pwm = __init_pwm_led(8)
__green_led_pwm = __init_pwm_led(10)
__blue_led_pwm = __init_pwm_led(12)
