import usb_cdc
import time
import board
import analogio

usb = usb_cdc.data
ldr = analogio.AnalogIn(board.A0)

def ler_luminosidade():
    return ldr.value

if usb:
    message = "Pi Pico respondendo por usb_cdc data!\n"
    usb.write(message.encode("utf-8"))
    while True:
        valor = ler_luminosidade()
        message = f"Luminosidade: {valor}"
        usb.write(message.encode("utf-8"))
        time.sleep(2)
else:
    print("A interface usb_cdc.data não está disponível.")
