from time import sleep
import RPi.GPIO as GPIO

led_pin = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(1, 10):
    GPIO.output(led_pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(led_pin, GPIO.LOW)
    sleep(1)

GPIO.cleanup()
