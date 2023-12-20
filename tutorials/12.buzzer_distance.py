import pigpio
import time
import RPi.GPIO as GPIO

pi = pigpio.pi()
buzzer = 18  # pin 12 in BOARD mode
pi.set_mode(buzzer, pigpio.OUTPUT)

GPIO.setmode(GPIO.BOARD)
trigger_pin = 11
echo_pin = 13
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


def detect_distance_cm():
    trigger()
    duration_seconds = get_echo_duration_seconds()
    distance_cm = get_distance_cm(duration_seconds) / 2
    if distance_cm < 2 or distance_cm > 400:
        return 0
    else:
        return distance_cm


try:
    while True:
        distance = detect_distance_cm()
        print(f"{distance = }")
        if distance < 25:
            pi.hardware_PWM(buzzer, 200, 500000)
            time.sleep(0.05)
            pi.hardware_PWM(buzzer, 0, 0)
            time.sleep(0.05)
        else:
            pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pi.write(buzzer, 0)
    pi.stop()
    GPIO.cleanup()
