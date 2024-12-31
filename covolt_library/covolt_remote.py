from microbit import *
import utime

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
                