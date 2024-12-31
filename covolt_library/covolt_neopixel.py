from microbit import *

MICROBIT_CAR_ADDR = 0x11
NEOPIXEL_ALL = 0x07
NEOPIXEL_ALONE = 0x08

class NeoPixel:
    NEOPIXEL_COLOR = {
        'RED': 0,
        'GREEN': 1,
        'BLUE': 2,
        'YELLOW': 3,
        'PURPLE': 4,
        'ORANGE': 5,
        'INDIGO': 6,
        'WHITE': 7,
        'OFF': 8,
    }

    NEOPIXEL_STATE = {
        'OFF': 0,
        'ON': 1,
    }

    def set_neo_all(self, value: str, color: str):
        buf = bytearray(3)
        buf[0] = NEOPIXEL_ALL
        buf[1] = self.NEOPIXEL_STATE[value]
        buf[2] = self.NEOPIXEL_COLOR[color]
        i2c.write(MICROBIT_CAR_ADDR, buf)

    def set_neo_index(self, index: int, value: str, color: str):
        if index > 3:
            index = 3
        elif index < 0 :
            index = 0
        buf = bytearray(4)
        buf[0] = NEOPIXEL_ALONE
        buf[1] = index
        buf[2] = self.NEOPIXEL_STATE[value]
        buf[3] = self.NEOPIXEL_COLOR[color]
        i2c.write(MICROBIT_CAR_ADDR, buf)
