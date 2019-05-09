class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def display(self):
        print(str(self.__name)+ '的年龄是' +str(self.__age))

if __name__ == '__main__':

    bart = Person('Bart Simpson', 59)
    lisa = Person('Lisa Simpson', 87)

    lisa.display()
    bart.display()

