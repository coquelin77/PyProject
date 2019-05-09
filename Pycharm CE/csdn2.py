import time
path='C:\\Users\\zhangxiaomei\\Desktop\\Walden.txt'
with open(path,'r') as text:
    words=text.read().split()
    print(words)
    for word in words:
        time.sleep(3)
        print ('{}-{} times'.format(word,words.count(word)))