from vehicles import Vehicles
class Car(Vehicles):
    def __init__(self, brand, color, seats):
        super(Car, self).__init__(brand, color)
        self.__seats = seats
        print('four seats')
    def showCar(self):
        super(Car, self).showInfo()
        print(self.__seats)
if __name__ == '__main__':
    a = Car('Audi','red',4)
#    a = Car('Audi', 'red')
    #print(a.showInfo())
#    a.showInfo()
    a.showCar()