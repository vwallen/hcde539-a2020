import board
import time
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground import cp

# The motion sensor is connected pin A0
input = DigitalInOut(board.A0)
input.direction = Direction.INPUT

# Pin A1 is connected to an LED
output = DigitalInOut(board.A1)
output.direction = Direction.OUTPUT

# Color values for NeoPixels
BLACK = (0, 0, 0)
GREEN = (0, 32, 0)

while True:
    # the sensor itself is not that responsive
    # so sampling more than a handful of times
    # per second is a waste
    output.value = input.value
    print(output.value)
    time.sleep(0.25)