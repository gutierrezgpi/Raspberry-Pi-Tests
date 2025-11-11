import time
from adafruit_datetime import datetime

while True:
    print("Date and Time: "+str(datetime.now()))
    time.sleep(2)
