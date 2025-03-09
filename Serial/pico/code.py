import usb_cdc
import time

usb = usb_cdc.data

if usb:
    while True:
        message = "Pi Pico respondendo por usb_cdc data!\n"
        usb.write(message.encode("utf-8"))
        time.sleep(2)
else:
    print("A interface usb_cdc.data não está disponível.")
