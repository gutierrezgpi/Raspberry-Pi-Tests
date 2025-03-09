import serial

porta_serial = None

try:
    
    porta_serial = serial.Serial('/dev/ttyACM1', 9600, timeout=1)

    while True:
        try:
            dados = porta_serial.readline().decode('utf-8').strip()
            if dados:
                print(dados)
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break
        except Exception as e:
            print(f"Erro: {e}")

finally:
    if porta_serial and porta_serial.is_open:
        porta_serial.close()
