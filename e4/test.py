import board
import time
import analogio
import digitalio
import pulseio
from adafruit_motor import servo


# Via https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo
pwm = pulseio.PWMOut(board.A1, duty_cycle=2**15, frequency=50)
motor = servo.Servo(pwm, min_pulse=700, max_pulse=2500)
knob = analogio.AnalogIn(board.A2)

power = digitalio.DigitalInOut(board.A0)
power.direction = digitalio.Direction.OUTPUT
power.value = True

angle = 0
while True:
    in_value = knob.value / 2.0**16
    out_value = int(in_value * 180)
    if abs(angle - out_value) > 3:
        angle = out_value
        motor.angle = angle
        print(angle)