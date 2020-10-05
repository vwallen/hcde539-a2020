import math
import time
from adafruit_circuitplayground import cp

# Color presets
OFF = (0, 0, 0)
COLOR_A = (0, 0, 128) # main pointer color
COLOR_B = (1, 0, 1) # peripheral pointer color

# Map positions of the compass to indexes of
# cp.pixels, including positions with no
# LED present (90° abd 120°)
positions = [7, 8, 9, None, 0, 1, 2, 3, 4, None, 5, 6]
num_positions = len(positions)

FULL_CIRCLE = math.pi * 2


n = 0
while True:
    x, y, z = cp.acceleration

    # Calculate angle of rotation from x and y
    # Flip x and y to product the "down" direction
    # Normalize and convert to LED indexes
    theta = (math.atan2(-y, -x) + FULL_CIRCLE) % FULL_CIRCLE # 0 - 2pi
    position = math.floor(num_positions * theta/FULL_CIRCLE) # 0 - 11
    index = positions[position]
    index_a = positions[(position + 1) % num_positions] # use modulo to wrap
    index_b = positions[position - 1]

    cp.pixels.fill(OFF)

    # Don't change the color of non-existent LEDs
    if index is not None:
        cp.pixels[index] = COLOR_A

    if index_a is not None:
        cp.pixels[index_a] = COLOR_B

    if index_b is not None:
        cp.pixels[index_b] = COLOR_B

    time.sleep(0.066) # 66ms = ~15fps