# devanpad
devanpad is a 4 key macropad with an OLED Display, and QMK firmware.

It serves as an example piece/reference for the hackpad YSWS, since it contains an implementation of every common part.

## Features:
- Open faced ~~sandwich~~ PCB board design.
- OLED Date and Time / Customisable text through python!
- 4 Keys for whatever you want!

## CAD Model:
I quite like the aesthetics of an open PCB, makes me feel like a bond villian; so I am only making a base for the circuit board to sit into. Everything is held together by 4 screws going into the base through the PCB.

<img width="300" alt="Base" src="https://github.com/user-attachments/assets/e7bff4f8-eab2-40aa-9a26-943bc6ffcf5c" />


Modeled in OnShape.


## PCB
Here's my PCB! It was made in KiCad. The silkscreen is a collection of inside jokes and random images from my computer.

Schematic

<img width="300" alt="image" src="https://github.com/user-attachments/assets/5d65a47d-ebc9-4d46-8bcc-16d649e5767b" />


PCB

<img width="300" alt="PCB RENDER" src="https://github.com/user-attachments/assets/92ec38dd-0426-4c15-a85f-c71d2cbcacd0" />


I used Cherry MX1's for the keyswitch footprints. My routing is god awful but if it aint broke dont fix it !!!!

## Firmware Overview

Originally I planned to use QMK firmware, but I switched to CircuitPython + KMK because it made OLED control and development significantly easier.

The firmware:
- Reads key inputs via KMK
- Drives OLED display in real time
- Receives time/date from a Python script over USB serial
- Cycles display modes using a keypress

---

## Host Software (PC Time Sync)

The keyboard receives live system time and date from a Python script running on the computer.

### Setup

```bash
pip install -r host/requirements.txt
python host/main.py
```

This sends:
- Current time every second
- Current date updates
- Optional mode switching commands

## OLED Modes
### Mode 0 — Time
Displays current time from the PC.

### Mode 1 — Date
Displays current date from the PC.

### Mode 2 — Hello Screen
A simple greeting screen.

## BOM:
Here should be everything you need to make this hackpad

- 4x Cherry MX Switches
- 4x DSA Keycaps
- 5x M3x5x4 Heatset inserts
- 2X M2x12mm SHCS Bolts
- 1x 0.91" 128x32 OLED Display
- 1x XIAO RP2040
- 1x Base (3D Printed)

### Build Notes
Designed as a simple open PCB macropad
Firmware is fully CircuitPython-based (no compilation required)
OLED is driven over I2C
PC <----> device communication uses USB serial

## Extra Stuff
Built this over a whole day and somehow didn’t realize it didn’t count toward my hackatime hours #killme 

_Theoretically_ this will work
