from vehicles import Vehicles
class Truck(Vehicles):
    def __init__(self,brand,color,load):
        super(Truck,self).__init__(brand,color)
        self.__load=load
        print('four ton')
    def showTrack(self):
        super(Truck,self).showInfo()
        print(self.__load)
if __name__ == '__main__':
    c = Truck('Audi', 'red', 4)
    c.showTrack()