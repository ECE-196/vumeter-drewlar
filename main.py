import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

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

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    leds[0].value = volume >= 23000 # Lowest level is independent
    for i in range(1,10):
        sleep(.005 * (9-i)) # The lower the volume the longer it takes to change
        leds[i].value = (volume >= 23000 + (500 * i)
                          or leds[i+1].value) # LED cannot turn off if the one above it is on
    leds[10].value = volume >= 27500 # Highest level is independent