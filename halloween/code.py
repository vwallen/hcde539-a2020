import board
import time
import array
import math
from analogio import AnalogOut
import digitalio
from adafruit_circuitplayground import cp
from controls import Dispatcher

# Based on https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-tone

eye1 = digitalio.DigitalInOut(board.A1)
eye1.direction = digitalio.Direction.OUTPUT

eye2 = digitalio.DigitalInOut(board.A7)
eye2.direction = digitalio.Direction.OUTPUT

# Frequencies
Cs6 = 1108.73 # C# 6
D6  = 1174.66 # D  6
Fs5 = 739.99  # F# 6


beat = 8/136

ORANGE = (255, 64, 0)
OFF = (1,0,0)

while True:
    if cp.switch:

        cp.play_tone(Cs6, beat)
        cp.pixels.fill(ORANGE)
        eye1.value = False
        eye2.value = False

        cp.play_tone(Fs5, beat)
        cp.pixels.fill(OFF)
        eye1.value = True
        eye2.value = True

        cp.play_tone(Fs5, beat)

        cp.play_tone(Cs6, beat)
        cp.pixels.fill(ORANGE)
        eye1.value = False
        eye2.value = False

        cp.play_tone(Fs5, beat)
        cp.pixels.fill(OFF)
        eye1.value = True
        eye2.value = True

        cp.play_tone(Fs5, beat)

        cp.play_tone(Cs6, beat)
        cp.pixels.fill(ORANGE)
        eye1.value = False
        eye2.value = False

        cp.play_tone(Fs5, beat)
        cp.pixels.fill(OFF)
        eye1.value = True
        eye2.value = True

        cp.play_tone(D6, beat)
        cp.pixels.fill(ORANGE)
        eye1.value = False
        eye2.value = False

        cp.play_tone(Fs5, beat)
        cp.pixels.fill(OFF)
        eye1.value = True
        eye2.value = True

    else:
        cp.stop_tone()
        cp.pixels.fill(OFF)


#controls = Dispatcher(cp)
#controls.register(Dispatcher.SWITCH_ON, on_switch_on)
#controls.register(Dispatcher.SWITCH_OFF, on_switch_off)
#controls.start(10)