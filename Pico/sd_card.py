"""
Pinout

|SD Card | Pico |
|--------|------|
|VCC     | VSYS |
|GND     | GND  |
|MISO    | GP12 |
|MOSI    | GP11 |
|SCK     | GP10 |
|CS      | GP13 |

GitHub Modules
https://github.com/adafruit/Adafruit_CircuitPython_SD/releases/tag/3.3.23
https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases/tag/5.2.9
"""

# Core Modules
from time import sleep
import board
import busio
import digitalio
import storage
import microcontroller

# CircuitPython Libraries
import adafruit_sdcard

# Setup
SCK = board.GP10
MOSI = board.GP11
MISO = board.GP12
CS = board.GP13

spi = busio.SPI(SCK, MOSI, MISO)
cs = digitalio.DigitalInOut(CS)

try:
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
except Exception as e:
    print(f"Error mounting SD card: {e}")
    while True:
        pass
    
# Routine
with open("/sd/testfile.txt", "w") as writefile:
    print("First Line", file=writefile)

with open("/sd/testfile.txt", "a") as appendfile:
    print("Second Line", file=appendfile)

with open("/sd/testfile.txt", "r") as inputfile:
    for line in inputfile:
        print(line)

print("Saving microcontroller temperature to SD card...")
while True:
    try:
        with open("/sd/temphistory.txt", "a") as appendfile:
            print(microcontroller.cpu.temperature, file=appendfile)
    except Exception as e:
        print(f"Error writing to file: {e}")
    sleep(5)
