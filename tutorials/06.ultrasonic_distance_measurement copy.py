# https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trigger_pin = 16
echo_pin = 18

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)


def trigger():
    required_duration = 0.00001
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(required_duration)
    GPIO.output(trigger_pin, GPIO.LOW)


def get_echo_duration_seconds():
    start_seconds = time.time()
    stop_seconds = time.time()

    while GPIO.input(echo_pin) == 0:
        start_seconds = time.time()

    while GPIO.input(echo_pin) == 1:
        stop_seconds = time.time()

    return stop_seconds - start_seconds


def get_distance_cm(duration_seconds):
    speed_of_sound_mps = 343
    speed_of_sound_centimeres_per_second = speed_of_sound_mps * 100
    return speed_of_sound_centimeres_per_second * duration_seconds


try:
    trigger()
    duration_seconds = get_echo_duration_seconds()
    distance_cm = get_distance_cm(duration_seconds) / 2

    if distance_cm < 400:
        print(f"Distance = {distance_cm}")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
