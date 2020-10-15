import board
import time
from analogio import AnalogOut
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground import cp
from controls import Dispatcher

red = DigitalInOut(board.A1)
red.direction = Direction.OUTPUT

yellow = DigitalInOut(board.A2)
yellow.direction = Direction.OUTPUT

green = DigitalInOut(board.A3)
green.direction = Direction.OUTPUT

blue = DigitalInOut(board.A4)
blue.direction = Direction.OUTPUT

leds = [red, yellow, green]

def on_click_a(cpx):
    for led in leds:
        led.value = False
    leds.append(leds.pop(0))
    leds[0].value = True

def on_click_b(cpx):
    for led in leds:
        led.value = False
    leds.insert(0, leds.pop(-1))
    leds[0].value = True

def on_update(cpx):
    if green.value:
        blue.value = not blue.value
    else:
        blue.value = False

controls = Dispatcher(cp)
controls.register(Dispatcher.CLICK_A, on_click_a)
controls.register(Dispatcher.CLICK_B, on_click_b)
controls.register(Dispatcher.UPDATE, on_update, 250)
controls.start(10)