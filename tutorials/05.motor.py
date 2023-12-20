from time import sleep
import RPi.GPIO as GPIO

motor_speed_pin = 8
direction_left_pin = 10
direction_right_pin = 22

delay_on = 3
delay_off = 1.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(direction_left_pin, GPIO.OUT)
GPIO.setup(direction_right_pin, GPIO.OUT)

GPIO.setup(motor_speed_pin, GPIO.OUT)
motor_speed_pwm = GPIO.PWM(motor_speed_pin, 100)
motor_speed_pwm.start(0)


def turn_off():
    motor_speed_pwm.ChangeDutyCycle(0)
    GPIO.output(direction_left_pin, GPIO.LOW)
    GPIO.output(direction_right_pin, GPIO.LOW)
    sleep(delay_off)


def turn_on_left(speed: int):
    motor_speed_pwm.ChangeDutyCycle(speed)
    GPIO.output(direction_left_pin, GPIO.HIGH)
    GPIO.output(direction_right_pin, GPIO.LOW)
    sleep(delay_on)


def turn_on_right(speed: int):
    motor_speed_pwm.ChangeDutyCycle(speed)
    GPIO.output(direction_left_pin, GPIO.LOW)
    GPIO.output(direction_right_pin, GPIO.HIGH)
    sleep(delay_on)


try:
    turn_on_left(100)
    turn_off()

    turn_on_right(100)
    turn_off()

    turn_on_left(50)
    turn_off()

    turn_on_right(50)
    turn_off()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
