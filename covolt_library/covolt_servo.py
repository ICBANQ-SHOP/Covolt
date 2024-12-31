from microbit import *

MICROBIT_CAR_ADDR = 0x11
SERVO_STATE = 0x06

class Servo:
    SERVO_ID_PWM = {
        'SERVO_S1' : 0,
        'SERVO_S2' : 1,
        'SERVO_S3' : 2,
        'SERVO_S4' : 3,
    }

    # SERVO 모터 180도 제어
    def set_pwm_servo_180(self, servoID: str, angle: int):
        if (angle > 180):
            angle = 180
        elif (angle < 0):
            angle = 0

        buf = bytearray(3)
        buf[0] = SERVO_STATE
        buf[1] = self.SERVO_ID_PWM[servoID]
        buf[2] = angle

        i2c.write(MICROBIT_CAR_ADDR, buf)

    # SERVO 모터 270도 제어
    def set_pwm_servo_270(self, servoID: str, angle: int):
        if (angle > 270):
            angle = 270
        elif (angle < 0):
            angle = 0

        angle = angle / 270 * 180
        angle = round(angle)

        buf = bytearray(3)
        buf[0] = SERVO_STATE
        buf[1] = self.SERVO_ID_PWM[servoID]
        buf[2] = angle
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # SERVO 모터 360도 제어
    def set_pwm_servo_360(self, servoID: str, angle: int):
        if (angle > 360):
            angle = 360
        elif (angle < 0):
            angle = 0

        angle = angle / 360 * 180
        angle = round(angle)

        buf = bytearray(3)
        buf[0] = SERVO_STATE
        buf[1] = self.SERVO_ID_PWM[servoID]
        buf[2] = angle
        i2c.write(MICROBIT_CAR_ADDR, buf)