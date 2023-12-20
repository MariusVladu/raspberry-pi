import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
_trigger_pin = 16
_echo_pin = 18
GPIO.setup(_trigger_pin, GPIO.OUT)
GPIO.setup(_echo_pin, GPIO.IN)


def detect_distance_cm():
    _trigger()
    duration_seconds = _get_echo_duration_seconds()
    distance_cm = _get_distance_cm(duration_seconds) / 2
    if distance_cm < 2 or distance_cm > 400:
        return 0
    else:
        return distance_cm


def _trigger():
    required_duration = 0.00001
    GPIO.output(_trigger_pin, GPIO.HIGH)
    time.sleep(required_duration)
    GPIO.output(_trigger_pin, GPIO.LOW)


def _get_echo_duration_seconds():
    start_seconds = time.time()
    stop_seconds = time.time()

    while GPIO.input(_echo_pin) == 0:
        start_seconds = time.time()

    while GPIO.input(_echo_pin) == 1:
        stop_seconds = time.time()

    return stop_seconds - start_seconds


def _get_distance_cm(duration_seconds):
    speed_of_sound_mps = 343
    speed_of_sound_centimeres_per_second = speed_of_sound_mps * 100
    return speed_of_sound_centimeres_per_second * duration_seconds


def dispose():
    GPIO.cleanup()
