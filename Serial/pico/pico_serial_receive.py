import usb_cdc
import time

usb = usb_cdc.data

if usb:
    while True:
        if usb.in_waiting > 0:
            data = usb.readline()
            if data:
                print(data.decode('utf-8').strip())
        time.sleep(0.1)
else:
    print("A interface usb_cdc.data não está disponível.")
