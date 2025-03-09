import time
import board
import analogio

# Configura o ADC no pino GP26 (A0)
ldr = analogio.AnalogIn(board.A0)

def ler_luminosidade():
    return ldr.value  # Retorna um valor entre 0 e 65535

while True:
    valor = ler_luminosidade()
    print(f"Luminosidade: {valor}")
    time.sleep(0.5)
