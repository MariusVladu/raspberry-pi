from time import sleep
import RPi.GPIO as GPIO

red_led_pin = 8
green_led_pin = 10
blue_led_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(red_led_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(red_led_pin, GPIO.LOW)

        GPIO.output(green_led_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(green_led_pin, GPIO.LOW)

        GPIO.output(blue_led_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(blue_led_pin, GPIO.LOW)
finally:
    GPIO.cleanup()
