import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_br import KeyboardLayoutBR

# Inicializa teclado e layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutBR(keyboard)

# Abre o menu
keyboard.send(Keycode.WINDOWS)
time.sleep(0.5)

# Digita "notepad.exe" e pressiona Enter
layout.write("notepad.exe")
time.sleep(0.3)
keyboard.send(Keycode.ENTER)
time.sleep(1)

# Teste de escrita em português
layout.write("ação\n")
layout.write("Coração\n")
layout.write("ãéíõú\n")
