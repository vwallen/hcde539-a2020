import board
import time
import digitalio
from adafruit_circuitplayground import cp
from controls import Dispatcher

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    return newfunc

# Based on https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-tone

eye1 = digitalio.DigitalInOut(board.A1)
eye1.direction = digitalio.Direction.OUTPUT

eye2 = digitalio.DigitalInOut(board.A7)
eye2.direction = digitalio.Direction.OUTPUT

# Colors
ORANGE = (255, 64, 0)
OFF = (4,1,0)

# Frequencies
D6  = 1174.66 # D  6
Cs6 = 1108.73 # C# 6
C6  = 1046.50 # C 6
As5 = 932.33  # A3 5
B5  = 987.77  # B 5
G5  = 783.99  # G 5
Fs5 = 739.99  # F# 5
F5  = 698.46  # F# 5
E5  = 659.25  # E 5
Ds5 = 622.25  # D# 5
D5  = 587.33  # D 5
B4  = 493.88  # B 4

beat = 1/(8 * (136/60)) # 1/8th note at 136 BMP

def on_beat(tone, beats, ring):
    cp.play_tone(tone, beats)
    cp.pixels.fill(ring)
    eye1.value = not eye1.value
    eye2.value = not eye2.value

def play_sequence(seq):
    for s in seq:
        yield s

c1 = partial(on_beat, Cs6, beat, ORANGE)
f1 = partial(on_beat, Fs5, beat, OFF)
d1 = partial(on_beat, D6, beat, ORANGE)
c2 = partial(on_beat, C6, beat, ORANGE)
f2 = partial(on_beat, F5, beat, OFF)
b1 = partial(on_beat, B5, beat, ORANGE)
e1 = partial(on_beat, E5, beat, OFF)
a1 = partial(on_beat, B5, beat, ORANGE)
d2 = partial(on_beat, Ds5, beat, OFF)
b2 = partial(on_beat, B4, beat, OFF)
g1 = partial(on_beat, G5, beat, ORANGE)

seq1 = [c1, f1, f1, c1, f1, f1, c1, f1, d1, f1]
seq2 = [c2, f2, f2, c2, f2, f2, c2, f2, c1, f2]
seq3 = [b1, e1, e1, b1, e1, e1, b1, e1, c2, e1]
seq4 = [a1, d2, d2, a1, d2, d2, a1, d2, b1, d2]
seq5 = [f1, b2, b2, f1, b2, b2, f1, b2, g1, b2]
seq = (seq1 * 6) + (seq2 * 2) + seq1 + seq2 + (seq3 * 2) + (seq4 * 2) + (seq3 * 2) + seq4 + (seq5 * 6)

song = play_sequence(seq)
while True:
    if cp.switch:
        try:
            next(song)()
        except StopIteration as e:
            song = play_sequence(seq)
    else:
        if (int(time.monotonic()) % 2 == 0):
            cp.pixels.fill(OFF)
        else:
            cp.pixels.fill(ORANGE)
        eye1.value = not eye1.value
        eye2.value = not eye2.value
        time.sleep(0.17)


#controls = Dispatcher(cp)
#controls.register(Dispatcher.SWITCH_ON, on_switch_on)
#controls.register(Dispatcher.SWITCH_OFF, on_switch_off)
#controls.start(10)