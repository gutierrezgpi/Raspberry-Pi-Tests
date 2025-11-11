'''
Pinout

3.3V ---- [Button] ---- [GP15]
'''

import time
import board
import digitalio

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
    if button.value:
        print(f"[{time.monotonic()}] Botão pressionado!")
        time.sleep(0.2)
    else:
        print(f"[{time.monotonic()}] Botão não pressionado")
        time.sleep(0.2)