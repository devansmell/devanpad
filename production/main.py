import board
import busio
import usb_cdc
import time

import displayio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

keyboard.keymap = [
    [
        KC.MO(1),
        KC.VOLD,
        KC.V,
        KC.C
    ],
    [
        KC.NO,
        KC.VOLD,
        KC.F13,
        KC.RESET
    ]
]

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

mode = 0
time_text = ""
date_text = ""

def handle_serial():
    global time_text, date_text, mode

    if usb_cdc.data.in_waiting:
        line = usb_cdc.data.readline().decode().strip()

        if line.startswith("T:"):
            time_text = line[2:]

        if line.startswith("D:"):
            date_text = line[2:]

        if line == "NEXT":
            mode = (mode + 1) % 3

def render():
    oled.fill(0)

    if mode == 0:
        oled.text("TIME", 0, 0, 1)
        oled.text(time_text, 0, 12, 1)

    elif mode == 1:
        oled.text("DATE", 0, 0, 1)
        oled.text(date_text, 0, 12, 1)

    else:
        oled.text("Hello :)", 0, 10, 1)
        oled.text("Hack Club", 0, 22, 1)

    oled.show()

while True:
    keyboard.go()
    handle_serial()
    render()