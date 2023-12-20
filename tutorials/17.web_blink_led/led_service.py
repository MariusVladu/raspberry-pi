import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

led_pin = 8
GPIO.setup(led_pin, GPIO.OUT)


def turn_on():
    GPIO.output(led_pin, GPIO.HIGH)


def turn_off():
    GPIO.output(led_pin, GPIO.LOW)


def dispose():
    turn_off()
    GPIO.cleanup()
