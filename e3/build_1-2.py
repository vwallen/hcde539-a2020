import board
import time
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground import cp

# The trim pot provides is the input here
input = AnalogIn(board.A1)

# Pin A2 is connected to an LED
output = DigitalInOut(board.A2)
output.direction = Direction.OUTPUT

# Color values for NeoPixels
BLACK = (0, 0, 0)
GREEN = (0, 32, 0)

while True:
    value = input.value

    if cp.switch:
        # Build 1:
        # if switch is on, use neopixels to show potentiometer level
        # and log the value to the console
        output.value = False
        step = int((11 * value) / (2**16))
        if step == 0:
            cp.pixels.fill(BLACK)
        else:
            for n in range(1, 11):
                cp.pixels[n - 1] = BLACK if n > step else GREEN
        print("Trim value %d, step value: %d" % (value, step))
    else:
        # Build 2:
        # if switch is off, vary the blink rate between 0 - 250ms
        delay = 0.25 * value / (2**16)
        output.value = not output.value
        if delay > 0:
            time.sleep(delay)
        print("Trim value %d, delay value: %sms" % (value, 1000*delay))