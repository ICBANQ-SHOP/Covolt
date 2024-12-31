from microbit import *
import utime
from machine import time_pulse_us

MICROBIT_CAR_ADDR = 0x11
BUZZER_STATE = 0x02
BUZZER_SOUND = 0x03
RGB_LIGHT_ALL = 0x01
RGB_LIGHT_LEFT = 0x0B
RGB_LIGHT_RIGHT = 0x0C
LINE_TRACKING = 0x0A
CAR_STATE = 0x04
MOTOR_SPEED = 0x05
NEOPIXEL_ALL = 0x07
NEOPIXEL_ALONE = 0x08
SERVO_STATE = 0x06

class Buzzer:
    SOUND_LEV = {
        'LEVEL_1': 0x02,
        'LEVEL_2': 0x04,
        'LEVEL_3': 0x06
    }

    # BEEP음 OFF
    def beep_off(self):
        buf = bytearray(2)
        buf[0] = BUZZER_STATE
        buf[1] = 0x00
        i2c.write(MICROBIT_CAR_ADDR, buf)

    # BEEP음 울림
    def beep_sound(self, timbre: int, duration: int, sound_level: str):
        # Timbre 범위 제한
        timbre = max(0, min(timbre, 1000))

        buf = bytearray(4)
        buf[0] = BUZZER_SOUND
        buf[1] = (timbre >> 8) & 0x0F
        buf[2] = timbre & 0xFF
        buf[3] = self.SOUND_LEV[sound_level]
        i2c.write(MICROBIT_CAR_ADDR, buf)

        # 지정된 시간 동안 대기 (밀리초)
        sleep(duration)

        # BEEP_OFF 함수 호출
        self.beep_off()

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

class LineTracing:
    LINE_POSITION = {
        'LEFT_MOST': 3,
        'LEFT': 2,
        'RIGHT': 1,
        'RIGHT_MOST': 0
    }
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    track_data = 0

    def get_linetracking(self):
        buf = bytearray([LINE_TRACKING])
        i2c.write(MICROBIT_CAR_ADDR, buf, True)
        data = i2c.read(MICROBIT_CAR_ADDR, 1)[0]
        black_line = []

        for _ in range(4):
            if (data >= 2 ** self.LINE_POSITION['LEFT_MOST']):
                data = data - 2 ** self.LINE_POSITION['LEFT_MOST']
                black_line.append('LEFT_MOST')

                if (data == 0):
                    return black_line
            elif (data >= 2 ** self.LINE_POSITION['LEFT']):
                data = data - 2 ** self.LINE_POSITION['LEFT']
                black_line.append('LEFT')

                if (data == 0):
                    return black_line
            elif (data >= 2 ** self.LINE_POSITION['RIGHT']):
                data = data - 2 ** self.LINE_POSITION['RIGHT']
                black_line.append('RIGHT')

                if (data == 0):
                    return black_line
            elif (data >= 2 ** self.LINE_POSITION['RIGHT_MOST']):
                data = data - 2 ** self.LINE_POSITION['RIGHT_MOST']
                black_line.append('RIGHT_MOST')

                if (data == 0):
                    return black_line
        return black_line
    # 들여쓰기 주의할 것

    def get_line_left_most(self):
        if 'LEFT_MOST' in self.get_linetracking():
            return 'WHITE'
        else:
            return 'BLACK'

    def get_line_left(self):
        if 'LEFT' in self.get_linetracking():
            return 'WHITE'
        else:
            return 'BLACK'

    def get_line_right_most(self):
        if 'RIGHT_MOST' in self.get_linetracking():
            return 'WHITE'
        else:
            return 'BLACK'

    def get_line_right(self):
        if 'RIGHT' in self.get_linetracking():
            return 'WHITE'
        else:
            return 'BLACK'

    def deal_tracing_value(self):
        track_data = self.get_linetracking()
        self.x1 = (track_data & 8) >> 3
        self.x2 = (track_data & 4) >> 2
        self.x3 = (track_data & 2) >> 1
        self.x4 = (track_data & 1) >> 0

    def save_tracking_value(self, position):
        if (position == self.LINE_POSITION['LEFT_MOST']):
            return self.x1
        elif (position == self.LINE_POSITION['LEFT']):
            return self.x2
        elif (position == self.LINE_POSITION['RIGHT']):
            return self.x3
        elif (position == self.LINE_POSITION['RIGHT_MOST']):
            return self.x4

    def track_line(self, position, value):
        if (position == self.LINE_POSITION['LEFT_MOST']):
            if (self.x1 == value):
                return True
            else:
                return False
        elif (position == self.LINE_POSITION['LEFT']):
            if (self.x2 == value):
                return True
            else:
                return False
        elif (position == self.LINE_POSITION['RIGHT']):
            if (self.x3 == value):
                return True
            else:
                return False
        elif (position == self.LINE_POSITION['RIGHT_MOST']):
            if (self.x4 == value):
                return True
            else:
                return False

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

class RemoteController:
    # IR 신호 상태 상수
    IR_REPEAT = 256
    IR_INCOMPLETE = 257
    IR_DATAGRAM = 258

    # 버튼 타임아웃 시간
    REPEAT_TIMEOUT_MS = 120

    IR_BUTTONS = {
        0: "POWER",
        128: "UP",
        32: "LEFT",
        96: "RIGHT",
        144: "DOWN",
        64: "LIGHT",
        160: "BEEP",
        48: "PLUS",
        112: "MINUS",
        16: "TURN_LEFT",
        80: "TURN_RIGHT",
        176: "NUM0",
        8: "NUM1",
        136: "NUM2",
        72: "NUM3",
        40: "NUM4",
        168: "NUM5",
        104: "NUM6",
        24: "NUM7",
        152: "NUM8",
        88: "NUM9"
    }

    def __init__(self, pin):
        self.pin = pin
        self.ir_state = {
            "protocol": "NEC",
            "hasNewDatagram": False,
            "bitsReceived": 0,
            "addressSectionBits": 0,
            "commandSectionBits": 0,
            "hiword": 0,
            "loword": 0,
            "activeCommand": -1,
            "repeatTimeout": 0,
            "onIrButtonPressed": {},
            "onIrButtonReleased": {}
        }

    # state 상태가 지속되는 시간 측정
    def pulse_in(self, state):
        start_utime = utime.ticks_us()
        while self.pin.read_digital() == state:
            pass
        return utime.ticks_diff(utime.ticks_us(), start_utime)

    # 하나의 비트를 받아 32비트의 IR 데이터로 만드는 함수
    def append_bit_to_datagram(self, bit):
        self.ir_state["bitsReceived"] += 1

        if self.ir_state["bitsReceived"] <= 8:
            self.ir_state["hiword"] = (self.ir_state["hiword"] << 1) + bit
        elif self.ir_state["bitsReceived"] <= 16:
            self.ir_state["hiword"] = (self.ir_state["hiword"] << 1) + bit
        elif self.ir_state["bitsReceived"] <= 32:
            self.ir_state["loword"] = (self.ir_state["loword"] << 1) + bit

        if self.ir_state["bitsReceived"] == 32:
            self.ir_state["addressSectionBits"] = self.ir_state["hiword"] & 0xffff
            self.ir_state["commandSectionBits"] = self.ir_state["loword"] & 0xffff
            return self.IR_DATAGRAM
        else:
            return self.IR_INCOMPLETE

    # 마크와 스페이스 시간을 이용해 0과 1을 디코딩 & 비트 해석
    def decode(self, mark_and_space):
        if mark_and_space < 1600:
            return self.append_bit_to_datagram(0)
        elif mark_and_space < 2700:
            return self.append_bit_to_datagram(1)

        self.ir_state["bitsReceived"] = 0

        if mark_and_space < 12500:
            return self.IR_REPEAT
        elif mark_and_space < 14500:
            return self.IR_INCOMPLETE
        else:
            return self.IR_INCOMPLETE

    # IR 신호 수신을 감지하고 처리
    def enable_ir_detection(self):
        self.pin.set_pull(self.pin.PULL_UP)
        mark = 0
        space = 0

        while True:
            if self.pin.read_digital() == 0:  # LOW 신호 감지
                mark = self.pulse_in(0)
            elif self.pin.read_digital() == 1:  # HIGH 신호 감지
                space = self.pulse_in(1)
                status = self.decode(mark + space)

                if status == self.IR_DATAGRAM:
                    data = self.ir_state["commandSectionBits"] >> 8

                    return self.IR_BUTTONS[data]
                
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