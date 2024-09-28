# Core Modules
from time import sleep
import board
import busio

# CircuitPython Libraries
import adafruit_bmp280

# Setup
i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
bmp280.sea_level_pressure = 1013.25
bmp280.mode = adafruit_bmp280.MODE_NORMAL
bmp280.standby_period = adafruit_bmp280.STANDBY_TC_500
bmp280.iir_filter = adafruit_bmp280.IIR_FILTER_X16
bmp280.overscan_pressure = adafruit_bmp280.OVERSCAN_X16
bmp280.overscan_temperature = adafruit_bmp280.OVERSCAN_X2

# Routine
sleep(1)

while True:

    try:
        bmp_temperature = str(bmp280.temperature)

        pressure = str(bmp280.pressure)

        altitude = str(bmp280.altitude)

        print(
            "BMP Temperature: "+bmp_temperature+" \'C, "+
            "Pressure: "+pressure+" Pa, "+
            "Altitude: "+altitude+" m"
        )

        sleep(1)
        
    except Exception as e:
        raise e
