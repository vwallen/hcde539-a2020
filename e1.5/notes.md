# E1.5: Interactive Gauge with Logging
Victor Allen (vwallen@uw.edu)
## Description
This project displays or logs the current temperature (within a certain min/max because the temperature doesn't change that much around here). 

- When the switch is in the "off" position, the device is in *log mode* and saves temperature samples to a log file. When in the "on" position, it switches to *display mode* lights LEDs to display the temperature. 
- The device does not start sampling until the A button is clicked. It samples roughly once per second. Clicking the B button stops sampling. The logging / display is only active while sampling.

## Source
I used Circuit Python for this project. The source file can be found on GitHub:
https://github.com/vwallen/hcde539-a2020/tree/main/e1.5

## Notes
* Circuit Python discourages mounting the filesystem as writeable by both the USB connected system and the running code. The [examples](https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage) use the switch to toggle between which system can write to it (on boot). There's an additional argument that can be passed to `storage.remount` which disables the safety measure, we'll see if that turns out to be a bad idea or not (probably). I would prefer initializing a separate mount point with different permissions. This may not be possible without using an SD card.
* MakeCode/JavaScript uses an event-based programming model, which is rather nice. Circuit Python requires some state management to handle clicks. etc. I wrote a `Dispatcher` class that handles the state and allows event handlers to be registered/unregistered in Python. This makes the button and switch handling much cleaner. The current version handles things in an infinite loop, so every other ongoing code needs to use the dispatcher's `update` event. 
* Sampling rate was a little trickier (buttons should respond ASAP, but temp reading shouldn't). I wrote a `Handler` class that is used when registering functions with the dispatcher to allow different functions to receive `update` events at different rates. 
* The log is written as a text file, but I would have preferred to use SQLite. Unfortunately there doesn't appear to be a SQLite library for Circuit Python (though there is for Arduino).