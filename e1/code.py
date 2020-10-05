import math
import time
from adafruit_circuitplayground import cp
from collections import namedtuple

# Create a collection of color themes
ColorTheme = namedtuple('Theme', ['base', 'primary', 'secondary'])
themes = [
    ColorTheme((0, 0, 0), (0, 255, 0), (8, 8, 0)),
    ColorTheme((0, 0, 0), (0, 0, 255), (4, 0, 4)),
    ColorTheme((0, 0, 0), (255, 0, 0), (64, 32, 0)),
    ColorTheme((1, 2, 1), (0, 255, 0), (8, 12, 0)),
    ColorTheme((1, 1, 1), (0, 0, 255), (16, 4, 16)),
    ColorTheme((2, 1, 0), (255, 0, 0), (64, 32, 0)),
]
theme = themes[0]

# Map positions of the compass to indexes of
# cp.pixels, including positions with no
# LED present (90° and 120°)
positions = [7, 8, 9, None, 0, 1, 2, 3, 4, None, 5, 6]
num_positions = len(positions)

FULL_CIRCLE = math.pi * 2

button_a_up = True
button_b_up = True

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

    # Use buttones to cycle through color themes
    # Trigger action on release, to represent "clicks"
    if cp.button_a:
        button_a_up = False
    else:
        if not button_a_up:
            theme = themes[(themes.index(theme) + 1) % len(themes)]
        button_a_up = True

    if cp.button_b:
        button_b_up = False
    else:
        if not button_b_up:
            theme = themes[(themes.index(theme) - 1)]
        button_b_up = True

    cp.pixels.fill(theme.base)

    # Don't change the color of non-existent LEDs
    if index is not None:
        cp.pixels[index] = theme.primary

    if index_a is not None:
        cp.pixels[index_a] = theme.secondary

    if index_b is not None:
        cp.pixels[index_b] = theme.secondary

    time.sleep(0.066) # 66ms = ~15fps