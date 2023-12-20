import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trigger_pin = 16
echo_pin = 18

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

red_led_pin = 8
green_led_pin = 10
blue_led_pin = 12
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)


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


def detect_distance_cm():
    trigger()
    duration_seconds = get_echo_duration_seconds()
    return get_distance_cm(duration_seconds) / 2


def flash(pin, on_duration, off_duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(on_duration)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(off_duration)


try:
    while True:
        distance_cm = detect_distance_cm()
        print(f"Distance = {distance_cm} cm")

        if distance_cm < 25:
            flash(red_led_pin, on_duration=0.035, off_duration=0.025)
        else:
            flash(green_led_pin, on_duration=0.3, off_duration=0.2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
