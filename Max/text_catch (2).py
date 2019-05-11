# file_object = open('C:\Users\zhang\PycharmProjects\word\words.txt','r',encoding='UTF-8')
with open(r'C:\Users\zhang\PycharmProjects\five\The_Old_Man_And_the_Sea.txt', 'r', encoding='UTF-8') as file_object:
    lines = file_object.readlines()
for line in lines:
    if line != '\n':
        print(line)
        #    decode('gb2312', 'ignore'),)
