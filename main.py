import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import monotonic_ns

# setup pins
microphone = AnalogIn(board.IO1) # Microphone is set up on SIG / IO1

status = DigitalInOut(board.IO17) # ??
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
   
]


lookup = [(DigitalInOut(pin),23000 + 1000 * i) for i,pin in enumerate(led_pins)]
rlookup = lookup[::-1]

for led in lookup:
    led[0].direction = Direction.OUTPUT

last_change = monotonic_ns()
# main loop
while True:
    volume = microphone.value
    for l,t in lookup:
        if l.value:
            continue
        if volume < t:
            break
        l.value = True

    if monotonic_ns() - last_change >= 100000000:
        for l,t in rlookup:
            if not l.value:
                continue
            if microphone.value >= t:
                break
            l.value = False
            last_change = monotonic_ns()
            break