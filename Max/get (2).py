class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
         return self.__gender
    def set_gender(self,gender):
        if(gender=='male' or gender=='female'):
            self.__gender=gender
        else:
            raise ValueError('bad score')