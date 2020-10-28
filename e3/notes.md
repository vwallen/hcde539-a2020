# E3: Individual Builds
Victor Allen (vwallen@uw.edu)
## Description
Three builds demonstrating the use of breadboards with the CPX.

- **Build 1**: _Trim Pot Indicator_. This build the trim value to the console and translates it into a value from 0 to 9, to light up the NeoPixels to indicate the trim position.
- **Build 2**: _LED Control_. This build implements the challenge from class. As the trim value changes the freqeuncy of the flashing LED changes, from ~2ms to ~250ms each cycle. Logging to the console, and the quality of the LED, means the flashes do not correspond exactly to the delay values.
- **Build 3**: _Motion Sensor_. This build uses the NeoPixels to indicate values from a PIR Motion Sensor (purchased separately, not part of our kits)

## Source

I used Circuit Python for this project. The source file can be found on GitHub:
https://github.com/vwallen/hcde539-a2020/tree/main/e3

## Demo

Videos: https://photos.app.goo.gl/fmXeDoqEJYo4Kw5x7

## Notes
* The first two builds were pretty straightforward. Not much to say there, but the breadboard feels pretty comfortable now
* The motion sensor is trickier, the module itself has a number of onboard options (breakers, and a couple of potentiometers) in addition to the connections. It uses 5V, so the Vout pin is the only connection that will work from the  CPX. This means it will also only work with the USB power that I have currently.
* I had intended to plug the sensor directly into the breadboard in the same way as the potentiometer, but unfortunately there are a couple of capacitors (I think) that get in the way. I didn't have an appropriate connector so I sacrificed some patch cables and soldered them directly to the pins so I could plug those in to the breadboard. I ended up connecting those to the CPS with alligator clips instead, but it all worked out in the end.
* I will need to adjust the various onboard settings to see if I can get any improvement, but at the moment it seems not particularly accurate... but I can't tell yet.