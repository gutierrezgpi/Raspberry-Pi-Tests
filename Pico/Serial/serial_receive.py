import serial

try:
    # Porta Windows
    #porta_serial = serial.Serial('COM4', 9600)
    # Porta Linux
    porta_serial = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

    while True:
        try:
            dados = porta_serial.readline().decode('utf-8', errors='ignore').strip()
            if dados:
                print(dados)
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break
        except Exception as e:
            print(f"Erro: {e}")

finally:
    porta_serial.close()
