# Raspberry Pi Tests

For the SD Card to work correctly it is necessary to create the sd folder on the CIRCUITPY drive

## Setup
- Raspberry Pi Pico with rp2040
- Adafruit CircuitPython 9.1.1
- BMP 280
![BMP 280](https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/BMP%20280.webp?raw=true)
- DHT 22
![DHT 22](https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/DHT%2022.webp?raw=true)
- Micro SD Card Module
![Micro SD Card Module](https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/Micro%20SD%20Card%20Module.webp?raw=true)


## Pinout

### BMP 280
|BMP280 | Pico   |
|-------|--------|
|VCC    |3V3(OUT)|
|GND    |GND     |
|SDA    |GP14    |
|SCL    |GP15    |

### DHT 22
|DHT22|Pico    |
|-----|--------|
|VCC  |3V3(OUT)|
|GND  |GND     |
|SDA  |GP13    |

### SD Card

|SD Card | Pico |
|--------|------|
|VCC     | VSYS |
|GND     | GND  |
|MISO    | GP12 |
|MOSI    | GP11 |
|SCK     | GP10 |
|CS      | GP13 |

### Media Control
|Comand              |Pico |
|--------------------|-----|
|PLAY_PAUSE          |GP14 |
|SCAN_PREVIOUS_TRACK |GP15 |
|SCAN_NEXT_TRACK     |GP13 |
|VOLUME_DECREMENT    |GP12 |
|VOLUME_INCREMENT    |GP11 |

## Modules
- [Adafruit_CircuitPython_BMP280](https://github.com/adafruit/Adafruit_CircuitPython_BMP280/releases/tag/3.3.2)
    - [Adafruit_CircuitPython_BusDevice](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases/tag/5.2.9)
- [Adafruit_CircuitPython_DHT](https://github.com/adafruit/Adafruit_CircuitPython_DHT/releases/tag/4.0.4)
- [Adafruit_CircuitPython_SD](https://github.com/adafruit/Adafruit_CircuitPython_SD/releases/tag/3.3.23)
    - [Adafruit_CircuitPython_BusDevice](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases/tag/5.2.9)
- [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/tag/6.1.1)
