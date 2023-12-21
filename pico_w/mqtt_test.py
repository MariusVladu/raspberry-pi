# https://core-electronics.com.au/guides/getting-started-with-mqtt-on-raspberry-pi-pico-w-connect-to-the-internet-of-things/

import machine
import ubinascii
import network
import secrets
import time
import json
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.wifi_ssid, secrets.wifi_password)
while wlan.isconnected() is False:
    print("Waiting for connection...")
    time.sleep(1)
print("Connected to WiFi")

client_id = ubinascii.hexlify(machine.unique_id())

mqtt_client = MQTTClient(
    client_id=client_id,
    server="raspberrypi.local",
    user="",
    password="",
)
mqtt_client.connect()
print("Connected to MQTT")

try:
    counter = 0

    while True:
        mqtt_client.publish(
            "client_test",
            json.dumps(
                {
                    "client_id": client_id,
                    "counter": counter,
                }
            ),
        )
        counter += 1
        time.sleep(3)
except Exception as e:
    print(f"Failed to publish message: {e}")
finally:
    mqtt_client.disconnect()
