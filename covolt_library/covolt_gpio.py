from microbit import *

MICROBIT_CAR_ADDR = 0x11

class Gpio:
    PIN_GPIO = {
        'P0': 0,
        'P1': 1,
        'P2': 2,
        'P12': 12,
    }

    PIN_READ_MODE = {
        'Digital': 0,
        'Analog': 1,
    }

    # GPIO핀 디지털 출력 제어
    def gpio_output(self, GpioPin: str, value: int):
        if (self.PIN_GPIO[GpioPin] == 0):
            return pin0.write_digital(value)
        if (self.PIN_GPIO[GpioPin] == 1):
            return pin1.write_digital(value)
        if (self.PIN_GPIO[GpioPin] == 2):
            return pin2.write_digital(value)
        if (self.PIN_GPIO[GpioPin] == 12):
            return pin12.write_digital(value)

    # GPIO핀 아날로그 출력 제어
    def gpio_output_analog(self, GpioPin: str, value: int):
        if (self.PIN_GPIO[GpioPin] == 0):
            return pin0.write_analog(value)
        if (self.PIN_GPIO[GpioPin] == 1):
            return pin1.write_analog(value)
        if (self.PIN_GPIO[GpioPin] == 2):
            return pin2.write_analog(value)
        if (self.PIN_GPIO[GpioPin] == 12):
            return pin12.write_analog(value)
        
    # GPIO핀 입력 제어
    def gpio_input(self, GpioPin: str, mode: int):
        if (mode == 'Digital'):
            if (self.PIN_GPIO[GpioPin] == 0):
                return pin0.read_digital()
            if (self.PIN_GPIO[GpioPin] == 1):
                return pin1.read_digital()
            if (self.PIN_GPIO[GpioPin] == 2):
                return pin2.read_digital()
            if (self.PIN_GPIO[GpioPin] == 12):
                return pin12.read_digital()
        elif (mode == 'Analog'):
            if (self.PIN_GPIO[GpioPin] == 0):
                return pin0.read_analog()
            if (self.PIN_GPIO[GpioPin] == 1):
                return pin1.read_analog()
            if (self.PIN_GPIO[GpioPin] == 2):
                return pin2.read_analog()
            if (self.PIN_GPIO[GpioPin] == 12):
                return pin12.read_analog()

        return 0