from time import sleep
import RPi.GPIO as GPIO

red_led_pin = 8
green_led_pin = 10
blue_led_pin = 12

GPIO.setmode(GPIO.BOARD)


def init_pwm(pin):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 1000)
    pwm.start(0)
    return pwm


def dim_cycle(pwms: list[any]):
    for i in range(100):
        for pwm in pwms:
            pwm.ChangeDutyCycle(i)
        sleep(0.01)

    for i in reversed(range(100)):
        for pwm in pwms:
            pwm.ChangeDutyCycle(i)
        sleep(0.01)


try:
    red_pwm = init_pwm(red_led_pin)
    green_pwm = init_pwm(green_led_pin)
    blue_pwm = init_pwm(blue_led_pin)

    while True:
        dim_cycle([red_pwm])
        dim_cycle([green_pwm])
        dim_cycle([blue_pwm])

        dim_cycle([red_pwm, blue_pwm])
        dim_cycle([red_pwm, green_pwm])
        dim_cycle([blue_pwm, green_pwm])

        dim_cycle([red_pwm, green_pwm, blue_pwm])
finally:
    GPIO.cleanup()
