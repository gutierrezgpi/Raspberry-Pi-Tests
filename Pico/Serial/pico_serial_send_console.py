import usb_cdc
import time

# Obtém a interface de comunicação USB serial
serial = usb_cdc.console

while True:
    if serial:
        message = "Olá, Raspberry Pi!\n"
        serial.write(message.encode())  # Envia mensagem pela USB
        print("Enviado:", message.strip())  # Mostra no terminal do Pico
    time.sleep(1)
