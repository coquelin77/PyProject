from Animal import  Animal
from class_cat import *
from class_dog import *


def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()


d=dir(Animal)
print(d)