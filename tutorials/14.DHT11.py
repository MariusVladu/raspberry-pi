import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

dht11 = 25  # pin 22 in BOARD mode
GPIO.setup(dht11, GPIO.IN)


def get_humidity_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, dht11)
    return humidity, temperature


try:
    while True:
        humidity, temperature = get_humidity_temperature()
        if humidity is not None and temperature is not None:
            print(f"{temperature = } {humidity = }")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
