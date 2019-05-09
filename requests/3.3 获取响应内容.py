import requests
r = requests.get('https://blog.csdn.net/u011682283')
print(r.text)
s= requests.get('https://blog.csdn.net/u011682283/article/details/87023848')
print(s.text)