with open(r'C:\Users\zhang\PycharmProjects\five\test.txt', 'r', encoding='UTF-8') as t:
    lines = t.readlines()
for line in lines:
    if line != '\n':
        print(line)