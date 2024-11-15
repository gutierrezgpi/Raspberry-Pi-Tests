"""
Pinout

|DHT22|Pico    |
|-----|--------|
|VCC  |3V3(OUT)|
|GND  |GND     |
|SDA  |GP13    |

GitHub Modules
https://github.com/adafruit/Adafruit_CircuitPython_DHT/releases/tag/4.0.4
"""
# Core Modules
from time import sleep
import board

# CircuitPython Libraries
import adafruit_dht

# Setup
dht22 = adafruit_dht.DHT22(board.GP9)

# Routine
sleep(2)

while True:
    
    try:
        dht_temperature = str(dht22.temperature)

        humidity = str(dht22.humidity)

        print(
            "DHT Temperature: "+dht_temperature+" \'C, "+
            "Humidity: "+humidity+" %, "
        )

        sleep(2)

    except Exception as e:
        raise e