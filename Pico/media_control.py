# Core Modules
import board
import digitalio
from time import sleep
import usb_hid

# CircuitPython Libraries
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Setup
button_play_pause = digitalio.DigitalInOut(board.GP14)
button_previous = digitalio.DigitalInOut(board.GP15)
button_next = digitalio.DigitalInOut(board.GP13)
button_volume_decrement = digitalio.DigitalInOut(board.GP12)
button_volume_increment = digitalio.DigitalInOut(board.GP11)

button_play_pause.switch_to_input(pull=digitalio.Pull.DOWN)
button_previous.switch_to_input(pull=digitalio.Pull.DOWN)
button_next.switch_to_input(pull=digitalio.Pull.DOWN)
button_volume_decrement.switch_to_input(pull=digitalio.Pull.DOWN)
button_volume_increment.switch_to_input(pull=digitalio.Pull.DOWN)

media_control = ConsumerControl(usb_hid.devices)

# Routine
while True:
    if button_play_pause.value:
        print("Play/Pause")
        media_control.send(ConsumerControlCode.PLAY_PAUSE)
        sleep(0.1)

    if button_previous.value:
        print("Previous")
        media_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        sleep(0.1)

    if button_next.value:
        print("Next")
        media_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        sleep(0.1)

    if button_volume_decrement.value:
        print("Volume Decrement")
        media_control.send(ConsumerControlCode.VOLUME_DECREMENT)
        sleep(0.1)
        
    if button_volume_increment.value:
        print("Volume Increment")
        media_control.send(ConsumerControlCode.VOLUME_INCREMENT)
        sleep(0.1)
    
    # Small delay to reduce CPU usage
    sleep(0.1)
    