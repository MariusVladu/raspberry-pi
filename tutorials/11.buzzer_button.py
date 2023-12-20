import pigpio
import time

pi = pigpio.pi()

buzzer = 18  # pin 12 in BOARD mode
button = 8  # pin 24 in BOARD mode

pi.set_pull_up_down(button, pigpio.PUD_UP)

try:
    while True:
        while pi.read(button) == 0:
            pi.hardware_PWM(buzzer, 200, 500000)

        if pi.read(button) == 1:
            pi.hardware_PWM(buzzer, 0, 0)

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pi.write(buzzer, 0)
    pi.stop()
