import time
import string
path=(r'C:\Users\zhang\PycharmProjects\five\The_Old_Man_And_the_Sea.txt')
with open(path,'r',encoding='UTF-8') as text:
    words=text.read().split()
    #split()通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串,str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num -- 分割次数。默认为 -1, 即分隔所有。
    print(words)
    for word in words:
        time.sleep(3)
        print ('{}-{} times'.format(word,words.count(word)))