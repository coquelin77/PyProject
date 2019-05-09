import requests
payload = {'wd': '张亚楠', 'rn': '100'}
r = requests.get("http://www.baidu.com/s", params=payload)
print (r.url)
#u'http://www.baidu.com/s?rn=100&wd=%E5%BC%A0%E4%BA%9A%E6%A5%A0'