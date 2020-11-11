import board
import time
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground import cp

# The trim pot provides is the input here
pot = AnalogIn(board.A1)
door = AnalogIn(board.A2)

#door = DigitalInOut(board.A3)
#door.direction = Direction.INPUT

# Color values for NeoPixels
BLACK = (0, 0, 0)
GREEN = (0, 32, 0)
BLUE = (0, 0, 64)

ARMED = (64, 0, 0)
FIRE_LO = (32, 8, 0)
FIRE_HI = (255, 0, 0)

armed = False
a_up = True

tone_a = 1174.66
tone_b = 493.88
fire_blink = False

door_was_closed = None

while True:

    pixels = [BLACK,] * 10

    if armed:
        # Check for high temperatures!
        # Pretend the trim pot is a reading between 0 - 100°F
        temp = int((100 * pot.value) / (2**16))
        if temp > 90:
            # It's getting hot in here!
            fire_blink = not fire_blink
            color = FIRE_HI if fire_blink else FIRE_LO
            if fire_blink:
                cp.play_tone(tone_a, 0.1)
            pixels[1] = color
            pixels[3] = color
            pixels[6] = color
            pixels[8] = color
            time.sleep(0.05)
        else:
            pixels[0] = ARMED if armed else BLACK

        # Check that the door is open
        # The magnetic switch is pretty noisy, so use
        # and analog input and check for a high  value
        door_open = door.value > 2**12
        if door_open:
            pixels[9] = BLUE
        if door_open and door_was_closed:
                cp.play_tone(tone_b, 2)
                door_was_closed = False
        elif not door_open:
            door_was_closed = True

    # Use a button to toggle whether the system is armed
    if cp.button_a:
        a_up = False
    else:
        if not a_up:
            a_up = True
            armed = not armed

    pixels[0] = ARMED if armed else BLACK

    for i, p in enumerate(pixels):
        cp.pixels[i] = p
