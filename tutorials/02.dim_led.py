from time import sleep
import RPi.GPIO as GPIO

led_pin = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

pwm_pin = GPIO.PWM(led_pin, 1000)
pwm_pin.start(0)

try:
    while True:
        for i in range(100):
            pwm_pin.ChangeDutyCycle(i)
            sleep(0.01)

        for i in reversed(range(100)):
            pwm_pin.ChangeDutyCycle(i)
            sleep(0.01)
finally:
    GPIO.cleanup()
