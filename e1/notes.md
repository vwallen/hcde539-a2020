# E1: Interactive Gauge
Victor Allen (vwallen@uw.edu)
## Description
I chose to use the accelerometer sensors to produce a gauge indicating the tilt of the board. The LED closest to the direction of the tilt (downward direction) lights with a "primary" color, while the LEDs on either side light with a "secondary" color. The other LEDs in the ring light with the "base" color (which can be "off"). Two of the twelve clock positions have no LED, so those positions are ignored, and the secondary LEDs provide context for the direction
.
To gain experience responding to button clicks, I added the option for multiple color palettes, which can be cycled through using the A and B buttons.
## Source
I used Circuit Python for this project. The source file can be found on GitHub:
https://github.com/vwallen/hcde539-a2020/blob/main/e1/code.py
## Demonstration
Image gallery: https://photos.app.goo.gl/Cnaa4jikWn78HU8H8 
Video: https://photos.app.goo.gl/2fCeitPBTF82qxJ97 
## Notes
* It was very easy to update the boot loader and switch to Circuit Python.
* The Mu editor made it easy to work with Python directly on the device, and the serial connection plus REPL was indispensable if getting things right.
* Combining the Mu workflow with version control is going to take some thought. As it is, I edit on the device and then copy the resulting file to my repository, which is not ideal.
* Documentation is a mixed bag. Circuit Python is well documented, but the CPX specific APi is mostly present via examples or tutorials on Adafruit.
* The dynamic range on the LEDs is not what I was expecting. The perceptual difference between values in the 1-8 range is much higher than the perceptual difference between 128-255. It is going to take some work to create subtle effects with these.
* Using MakeCode, the sleep times seemed to be limited to 100ms minimum, I was able to use much shorter sleep times with Python
* Certain behavior patterns (like "click") will need to be coded manually in Python
* Now that the logic is sound for this application (which took longer to get right that I was hoping TBH), I'd like to try to port this to other languages (Arduino, Rust)