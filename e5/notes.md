# E5: Integrated Build
Victor Allen (vwallen@uw.edu)
## Description

Kept things simple this week:

- Button A toggles the system between armed and disarmed. An LED lights up red when armed.
- A trim pot substitutes for the thermometer. The value is translated to between 0 - 100. If the value is over 90, a fire alarm starts: for LEDs blink and an attention grabbing sound plays
- A magnetic contact switch is used to detect the opening and closing of a door (door not included). When the door opens, a tone plays and an LED turns blue.
- The LEDs are in different positions, so all indications can be shown simultaneously.

## Source

https://github.com/vwallen/hcde539-a2020/tree/main/e5

## Demo

Photos and video: https://photos.app.goo.gl/txC9SQr4SS5o33HXA

## Notes
* I originally wanted to use an external button, but I had a lot of difficulty getting one of the button from our kit to fit (and stay) in position on the breadboard. I will try again later when or solder the connections instead.
* I still need to get a handle on how tones work with the CPX. There are still some issues where LEDs turn off when a tone is playing, and/or all other execution stops while the sound plays. This will take a bit more experimentation on later builds.