import pigpio
import time

pi = pigpio.pi()

buzzer = 18  # pin 12 in BOARD mode

try:
    while True:
        pi.hardware_PWM(buzzer, 500, 500000)
        time.sleep(2)
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)

        pi.hardware_PWM(buzzer, 1000, 500000)
        time.sleep(2)
        pi.hardware_PWM(buzzer, 0, 0)
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    pi.hardware_PWM(buzzer, 0, 0)
    pi.stop()
