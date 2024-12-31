from microbit import *

MICROBIT_CAR_ADDR = 0x11
CAR_STATE = 0x04
MOTOR_SPEED = 0x05

class Motor:
    MOTOR_STATE = {
        'STOP' : 0,
        'RUN' : 1,
        'BACK' : 2,
        'LEFT' : 3,
        'RIGHT' : 4,
        'LEFT_TURN' : 5,
        'RIGHT_TURN' : 6
    }

    # 자동차 이동
    def move(self, state: str, speed: int):
        if speed < 0:
            speed = 0
        elif speed > 1000:
            speed = 1000

        buf = bytearray(4)
        buf[0] = CAR_STATE
        buf[1] = self.MOTOR_STATE[state]
        buf[2] = (speed >> 8) & 0x0F
        buf[3] = speed & 0xFF
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # 자동차 멈추기
    def stop(self):
        buf = bytearray(2)
        buf[0] = CAR_STATE
        buf[1] = self.MOTOR_STATE['STOP']
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # 절댓값 함수
    def abs(self, number: int):
        if (number < 0):
            return -number
        return number

    # 양쪽 모터 값 다르게 제어
    def move_motor(self, speed_L: int, speed_R: int):
        if speed_L > 1000:
            speed_L = 1000
        elif speed_L < -1000:
            speed_L = -1000

        if speed_R > 1000:
            speed_R = 1000
        elif speed_R < -1000:
            speed_R = -1000

        speed_L_send = self.abs(speed_L)
        speed_R_send = self.abs(speed_R)
        buf = bytearray(7)
        buf[0] = MOTOR_SPEED

        if (speed_L < 0):
            buf[3] = 1
        else:
            buf[3] = 0

        if (speed_L < 0):
            buf[6] = 1
        else:
            buf[6] = 0

        buf[1] = (speed_L_send >> 8) & 0x00FF
        buf[2] = speed_L_send & 0x00FF
        buf[4] = (speed_R_send >> 8) & 0x00FF
        buf[5] = speed_R_send & 0x00FF

        i2c.write(MICROBIT_CAR_ADDR, buf)