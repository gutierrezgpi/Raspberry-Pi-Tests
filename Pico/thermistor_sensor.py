'''
Pinout

3.3V ---- [Resistor 10kΩ] ----+---- [Termistor NTC] ---- GND
                              |
                          (ADC1 GP27)

'''

import time
import board
import analogio
import math

# Configura o ADC no pino GP27 (A1)
termistor = analogio.AnalogIn(board.A1)

# Constantes para cálculo da temperatura (valores para um termistor NTC 10kΩ)
BETA = 3950  # Coeficiente beta do termistor
R0 = 10000   # Resistor de referência (10kΩ)
T0 = 298.15  # Temperatura ambiente em Kelvin (25°C)

def ler_temperatura():
    # Lê a tensão do ADC (0 a 65535 mapeado para 0V a 3.3V)
    tensao = (termistor.value * 3.3) / 65535
    resistencia = (R0 * tensao) / (3.3 - tensao)  # Fórmula do divisor de tensão

    # Fórmula de Steinhart-Hart para converter resistência em temperatura
    temperatura_kelvin = 1 / ((1 / T0) + (1 / BETA) * math.log(resistencia / R0))
    temperatura_celsius = temperatura_kelvin - 273.15  # Converte para Celsius

    return temperatura_celsius

while True:
    temp = ler_temperatura()
    print(f"Temperatura: {temp:.2f} °C")
    time.sleep(2)
