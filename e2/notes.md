# E2: Traffic Light
Victor Allen (vwallen@uw.edu)
## Description
This traffic ligjht simulation has 4 LEDs, the traditional red, yellow, green and a fourth blue LED to represent a "walk" sign. The switch determines the mode. In "test mode",  the A/B buttons cycle through lighting each of the signal lights, and the blue LEDs flashes when the green LED is lit. In "simulation mode" the main signal lights light in sequence on a timer. In this mode the blue LED lights when any button is pressed, and flashes when the light is green, turning off when it switches to yellow.

## Source

I used Circuit Python for this project. The source file can be found on GitHub:
https://github.com/vwallen/hcde539-a2020/tree/main/e2

## Demo

Gallery: https://photos.app.goo.gl/uxpEV2BqMcfpLSyw8

Video: https://photos.app.goo.gl/VRBsZovHHjXyXCG76

## Notes
* Continued to develop the event dispatcher for controls. The model is working well, so will continue with it. The light simulation definitely points to creating some basic state machine and sequencing code (either custom or 3rd party)
* Had some lexical scoping issues with Python variables in nested functions, but work it out eventually. I need to go back to my Python 2 docs and look for cleaner solutions, though.