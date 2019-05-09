import  requests
r = requests.get('http://www.zhidaow.com')
p=r.encoding
print(p)

s = requests.get('https://www.baidu.com')
p=s.headers
print(p)
print(s.text)