#!/usr/bin/python
class input_test(object):
    def inputing(self,x,y,z):
        print("this is a program\n")
        result = (x + y + z) / 3
        return 'the avg is '+str(result)
if __name__ == '__main__':
    x = int(input("please input the first number,then press Enter\n"))
    y = int(input("please input the second number,then press Enter\n"))
    z = int(input("please input the third number,then press Enter\n"))
    program = input_test()
    print(program.inputing(x,y,z))
