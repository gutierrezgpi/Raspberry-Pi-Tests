# Raspberry Pi Tests

For the SD Card to work correctly it is necessary to create the sd folder on the CIRCUITPY drive

## Setup
- Adafruit CircuitPython 9.1.1

<div style="display: flex; flex-direction: row; justify-content: center; gap: 20px;">
    <figure style="text-align: center; margin: 0;">
        <img src="https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/Raspberry_Pi_Pico.webp?raw=true" alt="Raspberry Pi Pico" width="200">
        <figcaption style="text-align: center;">Raspberry Pi Pico</figcaption>
    </figure>
    <figure style="text-align: center; margin: 0;">
        <img src="https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/BMP_280.webp?raw=true" alt="BMP 280 Sensor" width="200">
        <figcaption style="text-align: center;">BMP 280 Sensor</figcaption>
    </figure>
    <figure style="text-align: center; margin: 0;">
        <img src="https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/DHT_22.webp?raw=true" alt="DHT 22 Sensor" width="200">
        <figcaption style="text-align: center;">DHT 22 Sensor</figcaption>
    </figure>
    <figure style="text-align: center; margin: 0;">
        <img src="https://github.com/gutierrezgpi/Raspberry-Pi-Tests/blob/main/Pico/Img/Micro_SD_Card_Module.webp?raw=true" alt="Micro SD Card Module" width="200">
        <figcaption style="text-align: center;">Micro SD Card Module</figcaption>
    </figure>
</div>

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
