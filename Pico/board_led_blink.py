# Core Modules
from time import sleep
import board
import digitalio

# Setup
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Routine
while True:
    led.value = not led.value
    sleep(1)
