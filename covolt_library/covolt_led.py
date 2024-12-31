from microbit import *

MICROBIT_CAR_ADDR = 0x11
RGB_LIGHT_ALL = 0x01
RGB_LIGHT_LEFT = 0x0B
RGB_LIGHT_RIGHT = 0x0C

class Led:
    COLOR_RGB = {
        'RED': 0,
        'GREEN': 1,
        'BLUE': 2,
        'YELLOW': 3,
        'ORANGE': 4,
        'PURPLE': 5,
        'LAKE': 6,
        'WHITE': 7,
        'OFF': 8
    }

    # 모든 LED 제어
    def rgb_led_all(self, color_name: str):
        buf = bytearray(2)
        buf[0] = RGB_LIGHT_ALL
        buf[1] = self.COLOR_RGB[color_name]  
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # 왼쪽 LED 제어
    def rgb_led_left(self, color_name: str):
        buf = bytearray(2)
        buf[0] = RGB_LIGHT_LEFT
        buf[1] = self.COLOR_RGB[color_name]
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # 오른쪽 LED 제어
    def rgb_led_right(self, color_name: str):
        buf = bytearray(2)
        buf[0] = RGB_LIGHT_RIGHT
        buf[1] = self.COLOR_RGB[color_name] 
        i2c.write(MICROBIT_CAR_ADDR, buf)