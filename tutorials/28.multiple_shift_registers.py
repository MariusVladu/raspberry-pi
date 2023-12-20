import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

data_pin = 12
latch_pin = 10
clock_pin = 8

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)

GPIO.output(data_pin, GPIO.LOW)
GPIO.output(latch_pin, GPIO.LOW)
GPIO.output(clock_pin, GPIO.LOW)


def shift(buffer):
    for i in range(0, 16):
        GPIO.output(data_pin, 0b1000000000000000 & (buffer << i))
        GPIO.output(clock_pin, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(clock_pin, GPIO.LOW)

    GPIO.output(latch_pin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(latch_pin, GPIO.LOW)


def individual():
    led_value = 0b0000000000000001
    for i in range(0, 10):
        shift(led_value)
        led_value = led_value << 1
        time.sleep(1)
    shift(0)


def charging():
    for led_value in [
        0b0000000000000001,
        0b0000000000000011,
        0b0000000000000111,
        0b0000000000001111,
        0b0000000000011111,
        0b0000000000111111,
        0b0000000001111111,
        0b0000000011111111,
        0b0000000111111111,
        0b0000001111111111,
    ]:
        shift(led_value)
        time.sleep(0.5)
    shift(0)


def another_effect():
    for led_value in [
        0b0000001000000001,
        0b0000000100000010,
        0b0000000010000100,
        0b0000000001001000,
        0b0000000000110000,
        0b0000000001001000,
        0b0000000010000100,
        0b0000000100000010,
        0b0000001000000001,
    ]:
        shift(led_value)
        time.sleep(0.5)
    shift(0)


def barcode():
    barcode_array = [
        0b0000001001001001,
        0b0000000100100100,
        0b0000000010010010,
    ]
    for i in range(0, 10):
        shift(barcode_array[0])
        time.sleep(0.2)
        shift(barcode_array[1])
        time.sleep(0.2)
        shift(barcode_array[2])
        time.sleep(0.2)
    shift(0)


try:
    shift((1 << 16) - 1)
    while True:
        individual()
        time.sleep(0.5)

        charging()
        time.sleep(0.5)

        another_effect()
        time.sleep(0.5)

        barcode()
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    shift(0)
    GPIO.cleanup()
