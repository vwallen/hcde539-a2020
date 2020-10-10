import board
import digitalio
import storage
import os

# Make the file system writable
# Via: https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
# If the switch pin is connected to ground CircuitPython can write to the drive
# Also used this to re-enable writing after a bad boot.py edit:
# https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem

switch = digitalio.DigitalInOut(board.D7)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# This allows both the host system and python to write to the file system
# This is "dangerous" for unspecified reasons, so let's jump the canyon
storage.remount("/", readonly=False, disable_concurrent_write_protection=True)