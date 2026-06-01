import serial
import time
from datetime import datetime

ser = serial.Serial("COM3", 115200)

while True:

    now = datetime.now()

    ser.write(f"T:{now.strftime('%H:%M:%S')}\n".encode())
    ser.write(f"D:{now.strftime('%d %b %Y')}\n".encode())

    time.sleep(1)