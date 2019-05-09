class Vehicles(object):
    def __init__(self,brand,color):
        self.__color = color
        self.__brand = brand
        print('我已经开动了')

    def get_color(self):
        return self.__color

    def set_color(self,color):
        self.__color = color

    def get_brand(self):
        return self.__brand

    def set_brand(self,brand):
        self.__brand = brand

    def showInfo(self):
        print('brand is '+str(self.__brand)+', color is '+str(self.__color))
if __name__ == '__main__':
    b = Vehicles('Audi','red')
    b.showInfo()
    b.set_brand('Benz')
    b.showInfo()
    b.set_color('white')
    b.showInfo()