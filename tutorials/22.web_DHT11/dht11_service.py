import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

__dht11_pin = 25  # pin 22 in BOARD mode
GPIO.setup(__dht11_pin, GPIO.IN)

__last_stable_humidity = 0
__last_stable_temperature = 0


def get_humidity_temperature():
    global __last_stable_humidity
    global __last_stable_temperature

    humidity, temperature = Adafruit_DHT.read_retry(
        Adafruit_DHT.DHT11,
        __dht11_pin,
    )
    if humidity is not None:
        __last_stable_humidity = humidity

    if temperature is not None:
        __last_stable_temperature = temperature

    return __last_stable_humidity, __last_stable_temperature


def dispose():
    GPIO.cleanup()
