import board
import time
from analogio import AnalogOut
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground import cp
from controls import Dispatcher

stop = DigitalInOut(board.A1)
stop.direction = Direction.OUTPUT

caution = DigitalInOut(board.A2)
caution.direction = Direction.OUTPUT

proceed = DigitalInOut(board.A3)
proceed.direction = Direction.OUTPUT

walk = DigitalInOut(board.A7)
walk.direction = Direction.OUTPUT

sign = [stop, caution, proceed]

def reset_sign():
    controls.unregisterAll(Dispatcher.CLICK_A, Dispatcher.CLICK_B, Dispatcher.UPDATE)
    sign = [stop, caution, proceed]
    for led in sign:
        led.value = False
    walk.value = False
    stop.value = True


def on_switch_off(cpx):

    print("Switching to manual mode")

    reset_sign()

    def on_click_a(cpx):
        for led in sign:
            led.value = False
        sign.append(sign.pop(0))
        sign[0].value = True

    def on_click_b(cpx):
        for led in sign:
            led.value = False
        sign.insert(0, sign.pop(-1))
        sign[0].value = True

    def on_update(cpx):
        if proceed.value:
            walk.value = not walk.value
        else:
            walk.value = False

    controls.register(Dispatcher.CLICK_A, on_click_a)
    controls.register(Dispatcher.CLICK_B, on_click_b)
    controls.register(Dispatcher.UPDATE, on_update, 250)


def on_switch_on(cpx):

    print("Switching to simulation mode")

    reset_sign()

    # wait 4 seconds
    # switch to green, wait 4 seconds
    # if walk sign is on, blink the sign
    # switch to yellow, turn off walk, wait 1.5 seconds
    # switch to red, GOTO 10
    walk_on = False
    base_time = time.monotonic()

    def on_update(cpx):
        walk_on
        dt = time.monotonic() - base_time
        if dt > 9.5:
            for led in sign:
                led.value = False
            stop.value = True
            base_time = time.monotonic() # reset base time to start again
        elif dt > 8:
            for led in sign:
                led.value = False
            caution.value = True
            walk.value = False
            walk_on = False
        elif dt > 4:
            for led in sign:
                led.value = False
            proceed.value = True
            if walk_on:
                walk.value = not walk.value
        else:
            walk.value = walk_on


    def on_click(cpx):
        walk_on
        walk_on = True

    # if button clicked, turn on walk
    controls.register(Dispatcher.CLICK_A, on_click)
    controls.register(Dispatcher.CLICK_B, on_click)
    controls.register(Dispatcher.UPDATE, on_update, 250)

controls = Dispatcher(cp)
controls.register(Dispatcher.SWITCH_ON, on_switch_on)
controls.register(Dispatcher.SWITCH_OFF, on_switch_off)
controls.start(10)