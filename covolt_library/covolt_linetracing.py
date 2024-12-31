from microbit import *

MICROBIT_CAR_ADDR = 0x11
LINE_TRACKING = 0x0A

class LineTracing:
    LINE_POSITION = {
        'LEFT_MOST': 3,
        'LEFT': 2,
        'RIGHT': 1,
        'RIGHT_MOST': 0
    }
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