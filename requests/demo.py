import requests

r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
print(r.text)  # 打印解码后的返回数据


requests.get('https://github.com/timeline.json') #GET请求
requests.post('http://httpbin.org/post') #POST请求
requests.put('http://httpbin.org/put') #PUT请求
requests.delete('http://httpbin.org/delete') #DELETE请求
requests.head('http://httpbin.org/get') #HEAD请求
requests.options('http://httpbin.org/get') #OPTIONS请求


p = requests.get('http://www.zhidaow.com')
print(p.headers)