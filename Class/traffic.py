class Vehicle(object):
    def __init__(self,speed,size):
        self.__speed =speed
        self.__size=size
    def move(self):
        print('In moving, speed ' + str(self.__speed))
    def setSpeed(self,kmph):
        self.__speed = kmph
    def speedUp(self,add):
        self.__speed = self.__speed + add
    def speedDown(self,sub):
        if(self.__speed<sub):
            self.__speed=0
        else:
            self.__speed = self.__speed - sub

if __name__ == '__main__':
    a=Vehicle(30,30)
    print(a.speed)
    print(a.size)

