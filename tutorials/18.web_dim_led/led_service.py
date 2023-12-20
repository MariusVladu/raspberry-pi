import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


def __init_pwm_led(pin):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 1000)
    pwm.start(0)
    return pwm


def set_led_brightness(brightness):
    brightness = min(max(0, brightness), 100)
    __led_pwm.ChangeDutyCycle(brightness)


def dispose():
    set_led_brightness(0)
    GPIO.cleanup()


__led_pwm = __init_pwm_led(8)
