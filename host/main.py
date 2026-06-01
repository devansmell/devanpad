import hid
import time
from datetime import datetime

VID = 0xFEED
PID = 0x0001

device = hid.device()
device.open(VID, PID)

print("Hackpad connected")

while True:

    now = datetime.now()

    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d %b %Y")

    time_packet = bytearray(32)
    time_packet[0] = ord('T')
    time_packet[1:1+len(time_str)] = time_str.encode()

    date_packet = bytearray(32)
    date_packet[0] = ord('D')
    date_packet[1:1+len(date_str)] = date_str.encode()

    device.write(time_packet)
    device.write(date_packet)

    time.sleep(1)