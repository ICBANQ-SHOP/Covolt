from microbit import *
from machine import time_pulse_us
import utime

MICROBIT_CAR_ADDR = 0x11

class UltraSonic:
    def sonic(self):
        distances = []

        for i in range(5):
            pin15.write_digital(0)
            utime.sleep_us(2)
            pin15.write_digital(1)
            utime.sleep_us(15)
            pin15.write_digital(0)

            d = time_pulse_us(pin16, 1, 43200)
            distances.append(d // 40)

        distances.sort()
        length = (distances[1] + distances[2] + distances[3]) // 3
        return length