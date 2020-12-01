import board
import time
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction
from pulseio import PulseIn
from adafruit_circuitplayground import cp

# After this module:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

SAMPLE_SIZE = 100

trigger = DigitalInOut(board.A2)
trigger.direction = Direction.OUTPUT

echo = PulseIn(board.A1, maxlen=SAMPLE_SIZE)
echo.pause()
echo.clear()

while True:

    # clear input and send trigger pulse
    echo.clear()
    echo.resume()

    while len(echo) < SAMPLE_SIZE:
        trigger.value = True
        time.sleep(0.0001)
        trigger.value = False
        time.sleep(0.0001)

    echo.pause()
    pulses = [echo[i] for i in range(SAMPLE_SIZE)]
    duration = sum(pulses)//SAMPLE_SIZE

    # positive pulse time, in seconds, times 340 meters/sec, then
    # divided by 2 gives meters. Multiply by 100 for cm
    # 1/1000000 s/us * 340 m/s * 100 cm/m * 2 = 0.017
    distance_cm = duration * 0.017

    print(distance_cm)
