from microbit import *

BUZZER_STATE = 0x02
BUZZER_SOUND = 0x03

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