import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

data_pin = 12
latch_pin = 10
clock_pin = 8

led_9_pin = 18
led_10_pin = 16

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(led_9_pin, GPIO.OUT)
GPIO.setup(led_10_pin, GPIO.OUT)

GPIO.output(data_pin, GPIO.LOW)
GPIO.output(latch_pin, GPIO.LOW)
GPIO.output(clock_pin, GPIO.LOW)
GPIO.output(led_9_pin, GPIO.LOW)
GPIO.output(led_10_pin, GPIO.LOW)


def shift(buffer):
    for i in range(0, 8):
        GPIO.output(data_pin, 128 & (buffer << i))
        GPIO.output(clock_pin, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(clock_pin, GPIO.LOW)

    GPIO.output(latch_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(latch_pin, GPIO.LOW)


def individual():
    for led_value in [
        0b00000001,
        0b00000010,
        0b00000100,
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000000,
        0b10000000,
    ]:
        shift(led_value)
        time.sleep(1)

    shift(0)

    GPIO.output(led_9_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_9_pin, GPIO.LOW)

    GPIO.output(led_10_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_10_pin, GPIO.LOW)


def charging():
    for led_value in [
        0b00000001,
        0b00000011,
        0b00000111,
        0b00001111,
        0b00011111,
        0b00111111,
        0b01111111,
        0b11111111,
    ]:
        shift(led_value)
        time.sleep(0.5)

    GPIO.output(led_9_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_10_pin, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(led_9_pin, GPIO.LOW)
    GPIO.output(led_10_pin, GPIO.LOW)
    shift(0)


try:
    while True:
        individual()
        time.sleep(0.5)

        charging()
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    shift(0)
    GPIO.cleanup()
