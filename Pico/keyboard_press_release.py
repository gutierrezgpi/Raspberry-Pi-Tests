import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Initialize Keyboard
keyboard = Keyboard(usb_hid.devices)

while True:
    
    # Press and release CapsLock.
    keyboard.press(Keycode.CAPS_LOCK)
    keyboard.release(Keycode.CAPS_LOCK)
    
    time.sleep(1)
    
    # Check status of the LED_CAPS_LOCK
    print(keyboard.led_on(Keyboard.LED_CAPS_LOCK))