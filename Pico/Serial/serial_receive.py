import serial

porta_serial = serial.Serial('COM4', 9600)

while True:
    try:
        dados = porta_serial.readline()
        print(dados.decode('utf-8').strip())
    except KeyboardInterrupt:
        porta_serial.close()
        break
