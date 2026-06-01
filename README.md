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
This hackpad uses [QMK](https://qmk.fm/) firmware for everything. 

- The 4 keys currently act as macros.
- The OLED will be used to show date and time alongside customisable text :)

#### To get the python script running for d&t:
```
pip install -r host/requirements.txt
python host/main.py
```

I might add more in the future! That's it for now

## BOM:
Here should be everything you need to make this hackpad

- 4x Cherry MX Switches
- 4x DSA Keycaps
- 5x M3x5x4 Heatset inserts
- 2X M2x12mm SHCS Bolts
- 1x 0.91" 128x32 OLED Display
- 1x XIAO RP2040
- 1x Base (3D Printed or lasercut! !!)


## Extra stuff
Built mine over 6 hours without realising it didn't count toward my Stardance hours LOL!!
