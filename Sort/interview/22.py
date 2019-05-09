from random import random as r
import pandas
df = pandas.read_excel("ss.xls")
print(df)
a = r()
print(a)
s = "ajldjlajfdljfddd"
# s1=set(s)
# s2=list(s1)
# s2.sort()
# res="".join(s2)
# print(res)                     ==》adfjl　　

s = list(set(s))
s.sort()
res = ''.join(s)
print(res)