import board
import time
import analogio
import digitalio
import pulseio
from adafruit_motor import servo
from adafruit_circuitplayground import cp


# Via https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo
pwm = pulseio.PWMOut(board.A1, duty_cycle=2**15, frequency=50)
motor = servo.Servo(pwm, min_pulse=700, max_pulse=2400)
knob = analogio.AnalogIn(board.A2)

power = digitalio.DigitalInOut(board.A0)
power.direction = digitalio.Direction.OUTPUT
power.value = True

CLOSED_ANGLE = 110
OPEN_ANGLE = 15

angle = OPEN_ANGLE
direction = 3
while True:
    if cp.switch:
        angle = angle + direction
        time.sleep(0.05)
    elif cp.button_a:
        angle = angle + abs(direction)
    elif cp.button_b:
        angle = angle - abs(direction)

    if angle > CLOSED_ANGLE or angle < OPEN_ANGLE:
        direction = -direction
        angle = max(OPEN_ANGLE, min(CLOSED_ANGLE, angle))
    else:
        if angle != motor.angle:
            motor.angle = angle

    time.sleep(0.01)
    print(angle)