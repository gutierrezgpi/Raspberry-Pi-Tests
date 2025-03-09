import usb_cdc
import time

# Verifica se a interface usb_cdc.data está disponível
usb = usb_cdc.data

if usb:
    while True:
        message = "Olá do Raspberry Pi Pico via USB CDC!\n"
        usb.write(message.encode("utf-8"))  # Envia a mensagem pela USB
        time.sleep(1)  # Aguarda 1 segundo antes de enviar novamente
else:
    print("A interface usb_cdc.data não está disponível.")
