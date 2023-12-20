import pigpio
import time

pi = pigpio.pi()
servo_motor = 18  # pin 12 in BOARD mode
pi.set_mode(servo_motor, pigpio.OUTPUT)

try:
    while True:
        pi.set_servo_pulsewidth(servo_motor, 500)  # 90 degrees
        time.sleep(1)

        pi.set_servo_pulsewidth(servo_motor, 1500)  # 0 degrees
        time.sleep(1)

        pi.set_servo_pulsewidth(servo_motor, 2500)  # -90 degrees
        time.sleep(1)

        pi.set_servo_pulsewidth(servo_motor, 1500)  # 0 degrees
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    pi.set_servo_pulsewidth(servo_motor, 0)
    pi.stop()
