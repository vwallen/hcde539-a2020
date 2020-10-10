from adafruit_circuitplayground import cp
from controls import Dispatcher
import os
import math
import time


sampled_temp = None
TEMP_DISPLAY_MIN = 10
TEMP_DISPLAY_MAX = 35
OFF = (0, 0, 0)

#-----------------------------------------------------
# Temperature Sampler
#
# A button starts sampling
# B button stops sampling
# Switch toggles display vs logging mode (if sampling)
#-----------------------------------------------------



def on_click_a(cpx):
    # start sampling temperature
    print("Start sampling")
    controls.register(Dispatcher.UPDATE, sample_temperature, 1000)


def on_click_b(cpx):
    # stop sampling temperature
    print("Stop sampling")
    controls.unregister(Dispatcher.UPDATE, sample_temperature)
    cpx.pixels.fill(OFF)


def on_switch_on(cpx):
    # start displaying the temp, stop logging it
    print("Enable display mode")
    controls.register(Dispatcher.UPDATE, display_temperature, 1000)
    controls.unregister(Dispatcher.UPDATE, log_temperature)
    cpx.pixels.fill(OFF)


def on_switch_off(cpx):
    # stop displaying the temp, start logging it
    print("Enable logging mode")
    controls.register(Dispatcher.UPDATE, log_temperature, 1000)
    controls.unregister(Dispatcher.UPDATE, display_temperature)


def sample_temperature(cpx):
    global sampled_temp
    sampled_temp = cpx.temperature


def display_temperature(cpx):
    global sampled_temp

    # Display the temp (from the min to max)
    # by lighting progressively "warmer" pixels
    # Don't update faster than the sampling rate
    # by resetting the sampled value after use
    cpx.pixels.fill(OFF)
    if sampled_temp is not None:
        # gate the temp between 10° - 30° C
        # and normalize to 0 - 10
        t = min(TEMP_DISPLAY_MAX, max(TEMP_DISPLAY_MIN, sampled_temp))
        t = int(10 * ((t - TEMP_DISPLAY_MIN)/(TEMP_DISPLAY_MAX - TEMP_DISPLAY_MIN)))

        cpx.pixels.fill(OFF)
        for n in range(t):
            r = n/t
            cpx.pixels[n] = (int(r * 128), int(255 - (r * 255)), 0)

        sampled_temp = None


def log_temperature(cpx):
    global sampled_temp

    # Save the current sampled temp to a file
    # along with a timestamp
    # Don't update faster than the sampling rate
    # by resetting the sampled value after use
    cpx.pixels.fill(OFF)

    if sampled_temp is not None:
        timestamp = "{0:>4}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}".format(*time.localtime())
        log = "{0}|{1:f}\n".format(timestamp, sampled_temp)
        try:
            with open("/logs/temperature_log.txt", "a") as log_file:
                log_file.write(log)
            cpx.pixels[0] = (0,128,0)
        except Exception as e:
            cpx.pixels[0] = (128,0,0)
            print(e)
        sampled_temp = None


# Initialize an event dispatcher and register the
# event handlers for buttons and the switch
controls = Dispatcher(cp)
controls.register(Dispatcher.CLICK_A, on_click_a)
controls.register(Dispatcher.CLICK_B, on_click_b)
controls.register(Dispatcher.SWITCH_ON, on_switch_on)
controls.register(Dispatcher.SWITCH_OFF, on_switch_off)

# Do this last, because it runs _forever_
controls.start()