# Core Modules
from time import sleep
from microcontroller import cpu

# Routine
while True :
    print("Temp: " + str(cpu.temperature))
    sleep(1)
