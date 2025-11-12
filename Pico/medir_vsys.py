import analogio
import board
import time

# Config
vbat = analogio.AnalogIn(board.VOLTAGE_MONITOR)
CALIBRACAO_VSYS = 4.721 / 4.677
SMA_TAMANHO = 100
alpha = 0.1

# SMA: janela + soma acumulada
sma_val = []
sma_sum = 0.0

# EMA
ema = None

print("VSYS Monitor com SMA(100) + EMA iniciado!")

while True:
    raw = vbat.value
    voltage_divided = raw * 3.3 / 65536
    vsys = round(voltage_divided * 3, 4)

    # --- SMA (Média Móvel Simples) ---
    sma_val.append(vsys)
    sma_sum += vsys

    if len(sma_val) > SMA_TAMANHO:
        removido = sma_val.pop(0)
        sma_sum -= removido

    sma = sma_sum / len(sma_val)

    # --- EMA (Média Móvel Exponencial) ---
    if ema is None:
        ema = vsys
    else:
        ema = round(alpha * vsys + (1 - alpha) * ema, 4)

    # --- Calibração ---
    vsys_cal = round(voltage_divided * 3 * CALIBRACAO_VSYS, 4)

    # --- PRINT ---
    print(f"VSYS: {vsys:.3f} SMA: {sma:.3f} EMA: {ema:.3f} CAL: {vsys_cal:.3f}")

    time.sleep(1)