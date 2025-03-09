import usb_cdc
import time

usb = usb_cdc.console

if usb:
    while True:
        message = "Pi Pico respondendo por usb_cdc console!\n"
        usb.write(message.encode("utf-8"))
        print("Enviado:", message.strip())
        time.sleep(2)
else:
    print("A interface usb_cdc.data não está disponível.")