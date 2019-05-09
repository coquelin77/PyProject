import time
path='C:\\Users\\zhangxiaomei\\Desktop\\Walden.txt'
with open(path,'r') as text:
    words=text.read().split()
    print(words)
    for word in words:
        time.sleep(3)
        print ('{}-{} times'.format(word,words.count(word)))
---------------------
作者：zhangxiaomei1952
来源：CSDN
原文：https://blog.csdn.net/zhangxiaomei1952/article/details/67654694
版权声明：本文为博主原创文章，转载请附上博文链接！