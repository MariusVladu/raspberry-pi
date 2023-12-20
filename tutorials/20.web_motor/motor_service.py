import RPi.GPIO as GPIO

__motor_speed_pin = 8
__direction_forward_pin = 10
__direction_backward_pin = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(__direction_forward_pin, GPIO.OUT)
GPIO.setup(__direction_backward_pin, GPIO.OUT)

GPIO.setup(__motor_speed_pin, GPIO.OUT)
__motor_speed_pwm = GPIO.PWM(__motor_speed_pin, 100)
__motor_speed_pwm.start(0)


def turn_off():
    __motor_speed_pwm.ChangeDutyCycle(0)
    GPIO.output(__direction_forward_pin, GPIO.LOW)
    GPIO.output(__direction_backward_pin, GPIO.LOW)


def turn_on_backward(speed: int):
    __motor_speed_pwm.ChangeDutyCycle(speed)
    GPIO.output(__direction_forward_pin, GPIO.HIGH)
    GPIO.output(__direction_backward_pin, GPIO.LOW)


def turn_on_forward(speed: int):
    __motor_speed_pwm.ChangeDutyCycle(speed)
    GPIO.output(__direction_forward_pin, GPIO.LOW)
    GPIO.output(__direction_backward_pin, GPIO.HIGH)


def dispose():
    GPIO.cleanup()
