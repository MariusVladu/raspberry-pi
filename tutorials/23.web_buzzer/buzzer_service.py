import pigpio

__pi = pigpio.pi()

__buzzer = 18  # pin 12 in BOARD mode


def turn_on():
    __pi.hardware_PWM(__buzzer, 1000, 500000)


def turn_off():
    __pi.hardware_PWM(__buzzer, 0, 0)


def dispose():
    __pi.hardware_PWM(__buzzer, 0, 0)
    __pi.stop()
