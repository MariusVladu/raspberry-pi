import pigpio
import time

led = 14  # pin 8 in BOARD mode
button_up = 24  # pin 18 in BOARD mode
button_down = 8  # pin 24 in BOARD mode
brightness = 0

pi = pigpio.pi()

pi.set_mode(led, pigpio.OUTPUT)
pi.set_pull_up_down(button_up, pigpio.PUD_UP)
pi.set_pull_up_down(button_down, pigpio.PUD_UP)

try:
    while True:
        while pi.read(button_down) == 0:
            brightness = max(0, brightness - 1)
            pi.set_PWM_dutycycle(led, brightness)
            time.sleep(0.05)

        while pi.read(button_up) == 0:
            brightness = min(100, brightness + 1)
            pi.set_PWM_dutycycle(led, brightness)
            time.sleep(0.05)

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pi.stop()
