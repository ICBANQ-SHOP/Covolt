from microbit import *

Camera_Add = 0x14
Card = 2
Face = 6
Ball = 7
Tracking = 8
Color = 9
Learn = 10
numberCards = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letterCards = ["A", "B", "C", "D", "E"]
otherCards = ["Mouse", "micro:bit", "Ruler", "Cat", "Peer", "Ship", "Apple", "Car", "Pan", "Dog", "Umbrella",
              "Airplane", "Clock", "Grape", "Cup", "Turn left", "Turn right", "Forward", "Stop", "Back"]
colorList = ["Green", "Blue", "Yellow", "Black", "Red", "White"]


class AILENS(object):

    def __init__(self):
        self.__Data_buff = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i2c.init()
        sleep(5000)
        try:
            i2c.read(Camera_Add, 1)
        except:
            display.scroll("Init AILens Error!")

    def switch_function(self, func):
        i2c.write(Camera_Add, bytearray([0x20, func]))

    def get_image(self):
        self.__Data_buff = i2c.read(Camera_Add, 9)
        sleep(100)

    def get_ball_color(self):
        if self.__Data_buff[0] == 7:
            if self.__Data_buff[1] == 1:
                return "Blue"
            elif self.__Data_buff[1] == 2:
                return "Red"
        else:
            return "No Ball"

    def get_ball_data(self):
        """
        :return: BallData [x,y,w,h,confidence,total,order]
        """
        BallData = []
        for i in range(7):
            BallData.append(self.__Data_buff[i + 2])
        return BallData

    def get_face(self):
        return self.__Data_buff[0] == 6

    def get_face_data(self):
        """
        :return: FaceData [x,y,w,h,confidence,total,order]
        """
        FaceData = []
        for i in range(7):
            FaceData.append(self.__Data_buff[i + 2])
        return FaceData

    def get_card_content(self):
        if self.__Data_buff[0] == 2:
            return numberCards[self.__Data_buff[1] - 1]
        elif self.__Data_buff[0] == 4:
            return letterCards[self.__Data_buff[1] - 1]
        elif self.__Data_buff[0] == 3 and self.__Data_buff[1] < 21:
            return otherCards[self.__Data_buff[1] - 1]
        else:
            return "No Card"

    def get_card_data(self):
        """
        :return: CardData [x,y,w,h,confidence,total,order]
        """
        CardData = []
        for i in range(7):
            CardData.append(self.__Data_buff[i + 2])
        return CardData

    def get_color_type(self):
        if self.__Data_buff[0] == 9:
            return colorList[self.__Data_buff[1] - 1]
        else:
            return "No Color"

    def get_color_data(self):
        """
        :return: ColorData [x,y,w,h,confidence,total,order]
        """
        ColorData = []
        for i in range(7):
            ColorData.append(self.__Data_buff[i + 2])
        return ColorData

    def get_track_data(self):
        """
        :return: LineData [angel,width,len]
        """
        LineData = []
        for i in range(3):
            LineData.append(self.__Data_buff[i + 1])
        return LineData

    def learn_object(self, learn_id):
        if learn_id > 5 or learn_id < 1:
            print("Learn id out of range")
        else:
            i2c.write(Camera_Add, bytearray([10, learn_id]))

    def get_learn_data(self):
        """
        :return: LearnData [ID,confidence]
        """
        LearnData = [self.__Data_buff[1], 100 - self.__Data_buff[2]]
        return LearnData


if __name__ == '__main__':
    ai = AILENS()
    ai.switch_function(Learn)
    while 0:
        ai.get_image()
        print(ai.get_ball_color())
        print(ai.get_ball_data())
    while 0:
        ai.get_image()
        print(ai.get_face)
        print(ai.get_face_data())
    while 0:
        ai.get_image()
        print(ai.get_card_content())
        print(ai.get_card_data())
    while 0:
        ai.get_image()
        print(ai.get_color_type())
        print(ai.get_color_data())
    while 0:
        ai.get_image()
        print(ai.get_track_data())
    while 1:
        ai.get_image()
        if button_a.is_pressed():
            ai.learn_object(1)
        print(ai.get_learn_data())
