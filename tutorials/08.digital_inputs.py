import pigpio
import time

led_pin = 14  # pin 8 in BOARD mode
button_on_pin = 24  # pin 18 in BOARD mode
button_off_pin = 8  # pin 24 in BOARD mode

pi = pigpio.pi()

pi.set_mode(led_pin, pigpio.OUTPUT)
pi.set_pull_up_down(button_on_pin, pigpio.PUD_UP)
pi.set_pull_up_down(button_off_pin, pigpio.PUD_UP)

try:
    while True:
        if pi.read(button_on_pin) == 0:
            pi.write(led_pin, 1)
        if pi.read(button_off_pin) == 0:
            pi.write(led_pin, 0)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pi.stop()
